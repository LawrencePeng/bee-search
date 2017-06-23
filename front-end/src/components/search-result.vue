<template>
  <div id="search-result">
    <div class="top-bar">
      <router-link to="/"><img src="../assets/logo.jpg" alt="Bee Search" id="logo"></router-link>
      <input type="text" v-model="this.query" @keyup.enter.prevent="search(this.query)" class="search-bar">
    </div>
    <div class="result-content">
      <article-item v-for="(article, index) in articles"
        :article="article"
        :index="index"
        :key="article.content">
      </article-item>
    </div>
    <footer>Bee Search by szu-bee</footer>
  </div>
</template>

<script>
  import articleItem from './article-item.vue'

  export default {
    name: 'searchResult',
    components: {
      articleItem
    },
    data() {
      return {
        query: '',
        articles: []
      }
    },
    created() {
      this.query = window.query
      this.search(this.query)
    },
    methods: {
      search(query) {
        window.query = this.query = query
        this.$http.get(`http://localhost:8000?search=${query}`)
          .then(res => {
            if (!query) return
            if (res.data.length === 0 && query !== '') {
              this.articles = []
              this.articles.push({
                title: '您搜的关键词在最近的文章中不存在，请移步公文通首页查询',
                url: 'http://www1.szu.edu.cn/board/',
                content: '...'
              })
              return
            } else {
              this.articles = res.data.map(item => {
                const tl = item.title
                if (tl === '') {
                  item.title = '(无标题)'
                } else {
                  if (/\s/.test(tl)) {
                    item.title = tl.slice(1)
                  }
                }
                return item
              })
            }
          })
          .catch(err => {
            console.error(err)
          })
      }
    }
  }
</script>

<style lang="less" scoped>
  #search-result {
    margin-left: 160px;

    .top-bar {
      display: inline-flex;
      background-color: #fff;
      border-bottom: 1px solid #ebebeb;

      #logo {
        width: 88px;
        margin-right: 20px;
      }

      .search-bar {
        width: 600px;
        height: 40px;
        line-height: 40px;
        padding-left: 12px;
        margin-top: 16px;
        border-radius: 4px;
        border: 1px solid #bfcbd9;
        box-shadow: 3px 4px 2px #f2f2f2;

        &:hover {
          box-shadow: 7px 6px 4px #f2f2f2;
        }

        &:focus {
          outline: none; 
          // border-color: #20a0ff;
        }
      }

      @media (max-width: 1024px) {
        #search {
          width: 520px;
        }
      }
    }

    .result-content {
      width: 660px;
    }

    footer {
      border-top: 1px solid #ebebeb;
      margin: 60px 0;
      padding-top: 20px;
      text-align: center;
      color: #545454;
    }
  }
</style>
