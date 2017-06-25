# coding:utf-8
import pymongo
import pickle
import jieba

client = pymongo.MongoClient('mongodb://localhost')
db = client['test']
docs = db['docs']
real_docs = docs.find()

inverted_index = {}


# 从文档对应的url中提取其id值
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
    # 使用结巴分词算法对中文文档进行分词
    # jieba.cut返回的结构是一个可迭代的generator，需要list接收，再用set去重
    doc_title = set(list(jieba.cut(r_doc['title'])))
    doc_content = set(list(jieba.cut(r_doc['content'])))
    identify = get_id(r_doc)

    for word in doc_title | doc_content:
        # 查询是否含有对应的词项，如果没有，返回一个空的list
        w_list = inverted_index.get(word, list())
        w_list.append(identify)
        inverted_index[word] = w_list


with open('../index.txt', 'wb') as f:
    # 使用pickle模块将对象转化为文件保存在磁盘上
    pickle.dump(inverted_index, f)
