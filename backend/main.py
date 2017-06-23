# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_cors import CORS
import jieba
import pickle
import pymongo
import math
import time

inverted_index = None
client = pymongo.MongoClient('mongodb://localhost/')
docs = client['test']['docs']
app = Flask(__name__)


# 使用TF-IDF作为权重的计算方式
def tf(doc, tok):
    title = doc['title']
    content = doc['content']
    return title.count(tok) + content.count(tok)


def idf(tok):
    ids = inverted_index[tok]
    return math.log(float(docs.find().count()) / float((1 + float(len(ids)))))



def euclid_dist(vec):
    return math.sqrt(sum([v ** 2 for v in vec]))

# 使用余弦相似度作为<query,doc>的相关性分值的计算方式
def cos_sim(q_words, doc):
    text = doc['title'] + doc['content']
    dot_product = 0
    vec = []
    for word in q_words:
        freq = text.count(word)
        dot_product += freq
        vec.append(freq)
    return float(dot_product) / (euclid_dist(vec) * len(q_words))


def get_score(q_words, doc):
    score = sum([tf(doc, tok) * idf(tok) for tok in q_words]) * cos_sim(q_words, doc)
    return {
        'title': doc['title'],
        'content': doc['content'][:88],
        'url': doc['url'],
        'score': score
    }


def get_doc_by_id(id):
    doc = docs.find_one({'url': 'http://www1.szu.edu.cn/board/view.asp?id=' + str(id)})
    return doc


with open('stopwords.txt') as stopwords:
    stopwords = set(stopwords.readlines())


CORS(app)


@app.route("/", methods=['GET'])
def query():
    tic = time.clock()
    ii = inverted_index
    # 对英文token的大小写转换和停用词（英文stop words）过滤
    q = request.args['search'].encode('utf8').lower()
    q_words = set(list(jieba.cut(q)))
    q_words -= stopwords
    all_docs = set()

    for tok in q_words:
        all_docs |= set(ii.get(tok, set()))

    result_list = []
    candidate = [get_doc_by_id(doc) for doc in all_docs]
    for doc in candidate:
        result_list.append(get_score(q_words, doc))
    # 根据相关性分值大小对匹配到的文档进行排序
    result_list.sort(lambda a, b: -1 if a['score'] > b['score'] else 1)
    return jsonify(result_list[:12])


app.debug = False

if __name__ == '__main__':
    with open('index.txt', 'rb') as f:
        inverted_index = pickle.load(f)
    app.run('127.0.0.1', 8000)
