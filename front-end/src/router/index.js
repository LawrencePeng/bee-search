import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import searchResult from '@/components/search-result'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/search-result',
      name: 'searchResult',
      component: searchResult
    }
  ]
})
