import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/views/HomePage'
import CharArchive from '@/views/CharArchive'
import WeaponArchive from '@/views/WeaponArchive'
import CharDetail from '@/views/CharDetail'
import WeaponDetail from '@/views/WeaponDetail'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'homePage',
      component: HomePage,
      meta: {
        title: 'gs_wiki'
      }
    }, {
      path: '/char',
      name: 'charArchive',
      component: CharArchive,
      meta: {
        title: '角色图鉴 | gs_wiki'
      }
    }, {
      path: '/weapon',
      name: 'weaponArchive',
      component: WeaponArchive,
      meta: {
        title: '武器图鉴 | gs_wiki'
      }
    }, {
      path: '/char/:id',
      name: 'charDetail',
      component: CharDetail,
      meta: {
        title: '角色详情 | gs_wiki'
      }
    }, {
      path: '/weapon/:id',
      name: 'weaponDetail',
      component: WeaponDetail,
      meta: {
        title: '武器详情 | gs_wiki'
      }
    }
  ]
})
