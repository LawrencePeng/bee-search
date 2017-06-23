<template>
  <div id="article-item">
    <h3 :title="article.title">
      <a :href="article.url">{{ article.title }}</a>
    </h3>
    <div>
      <cite :url="article.url">{{ article.url }}</cite>
      <div><span :content="article.content">{{ article.content }} ...</span></div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'articleItem',
    props: {
      article: Object
    }
  }
</script>

<style lang="less" scoped>
  #article-item {
    h3 {
      display: block;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      line-height: 1.2;
      margin-bottom: 0;
      font-size: 18px;
      font-weight: normal;

      a {
        text-decoration: none;
        color: #1a0dab;

        &:hover {
          cursor: pointer;
          text-decoration: underline;
        }

        &:visited {
          color: #609;
        }
      }
    }

    div {
      cite {
        font-size: 14px;
        color: #006621;
        font-style: normal;
        white-space: nowrap;
        line-height: 16px;
      }

      div {
        span {
          line-height: 1.6;
          font-size: small;
          font-family: arial, sans-serif;
          word-wrap: break-word;
          color: #545454;
        }
      }
    }
  }
</style>
