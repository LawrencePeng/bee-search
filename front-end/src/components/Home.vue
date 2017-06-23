<template>
  <div id="home">
    <div class="content">
      <div id="logo"><img src="../assets/logo.jpg" alt="Bee Search"></div>
      <search-form></search-form>
    </div>
  </div>
</template>

<script>
  import searchForm from './search-form.vue'

  export default {
    name: 'Home',
    components: {
      searchForm
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
  #home {
    .content {
      text-align: center;
      margin: 88px 0;

      #logo {
        img {
          width: 360px;
          height: 230px;
        }
      }
    }
  }
</style>
