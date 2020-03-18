# bee-search
A simple search engine for school's news board.


# Instructions for use
> Local installation:
- node
- npm
- [mongodb](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
- python
- [pip](https://pip.pypa.io/en/stable/installing/)
- pymongo
- [Flask](http://docs.jinkan.org/docs/flask/installation.html#installation)
- [“结巴”中文分词](https://github.com/fxsjy/jieba)

## front-end
### install dependencies
npm install
### serve with hot reload at localhost:8080
npm run dev

## backend
### install dependencies
npm install
### start up mongodb
sudo mongod
### run spider
node spider.js
### build inverted index
python inverted_index_build.py
### run server
python main.py


当时我们一起完成的搜索引擎网站，功能是爬取深大通的文章，然后可以搜索。我还记得那个时候在信工楼，我们一起搞定爬虫，你看到快速闪烁的日志时的兴奋感。
python inverted_index_build.py我们
python inverted_index_build.py
