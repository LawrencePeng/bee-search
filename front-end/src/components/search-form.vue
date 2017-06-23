<template>
  <div id="search-form">
    <input type="text" v-model="this.query" @keyup.enter.prevent="search(this.query)" class="search-bar">
    <div class="submit-buttons" style="text-align: center;">
      <input value="Search Now" type="submit" @click="search(this.query)">
      <input value="I'm Feeling Lucky" type="submit" @click="optimum(this.query)">
    </div>
  </div>
</template>

<script>
  export default {
    name: 'searchForm',
    data() {
      return {
        query: ''
      }
    },
    created() {
      this.query = window.query = ''
    },
    methods: {
      search(query) {
        // window.query = query
        if (query !== '') {
          this.$router.push('/search-result')
        }
      },
      optimum(query) {
        this.$http.get(`http://localhost:8000?search=${query}`)
          .then(res => {
            window.location = res.data[0].url
          })
          .catch(err => {
            console.error(err)
          })
      }
    }
  }
</script>

<style lang="less" scoped>
  #search-form {
    .search-bar {
      width: 600px;
      height: 40px;
      line-height: 40px;
      padding-left: 12px;
      border-radius: 4px;
      border: 1px solid #bfcbd9;
      box-shadow: 3px 4px 2px #f2f2f2;

      &:hover {
        box-shadow: 7px 6px 4px #f2f2f2;
      }

      &:focus {
        outline: none;
      }
    }

    @media (max-width: 1024px) {
      #search {
        width: 520px;
      }
    }

    .microphone-icon {
      a {
        width: 18px;
        background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAACrElEQ…2iTnbwNT+gBX54H+IaXAtxJzE3ycSAFqSAFJACUkAikXD+AHj5/wx2o5osAAAAAElFTkSuQmCC) no-repeat -3px 0;
        background-size: 24px 24px;
        display: inline-block;
        height: 23px;
        vertical-align: middle;
      }
    }

    .submit-buttons {
      padding-top: 20px;

      input {
        height: 36px;
        line-height: 27px;
        background-color: #f2f2f2;
        border: 1px solid #f2f2f2;
        border-radius: 2px;
        color: #757575;
        cursor: default;
        font-family: arial, sans-serif;
        font-size: 13px;
        font-weight: bold;
        margin: 11px 4px;
        min-width: 54px;
        padding: 0 16px;
        text-align: center;

        &:hover {
          border: 1px solid #c6c6c6;
          box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
          color: #222;
        }

        &:focus {
          border: 1px solid #4d90fe;
          outline: none;
        }
      }
    }
  }
</style>
