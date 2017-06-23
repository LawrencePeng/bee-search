# coding:utf-8
import pymongo
import pickle
import jieba

client = pymongo.MongoClient('mongodb://localhost')
db = client['test']
docs = db['docs']
real_docs = docs.find()

inverted_index = {}


def get_id(doc):
    """
    get id by doc.url
    :param doc: input doc
    :return: doc id in doc.url
    """
    url = doc['url']
    begin = url.find('?') + 4
    return int(url[begin:])


for r_doc in real_docs:
    # 使用jieba分词算法对中文文档进行分词
    doc_title = set(list(jieba.cut(r_doc['title'])))
    doc_content = set(list(jieba.cut(r_doc['content'])))
    identify = get_id(r_doc)

    for word in doc_title | doc_content:
        w_list = inverted_index.get(word, list())
        w_list.append(identify)
        w_list.sort()
        inverted_index[word] = w_list


with open('../index.txt', 'wb') as f:
    # 使用pickle模块将对象转化为文件保存在磁盘上
    pickle.dump(inverted_index, f)
