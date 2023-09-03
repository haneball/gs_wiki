import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import CharArchive from '../views/CharArchive.vue'
import WeaponArchive from '../views/WeaponArchive.vue'
import CharDetail from '../views/CharDetail.vue'
import WeaponDetail from '../views/WeaponDetail.vue'
import GachaTimer from '../views/GachaTimer.vue'
import AttributeTable from '../components/char/AttributeTable.vue'
import TalentTable from '../components/char/TalentTable.vue'
import ConstellationTable from '../components/char/ConstellationTable.vue'
import ProfileTable from '../components/char/ProfileTable.vue'
import NotFound from '../views/NotFound.vue'

const routes = [
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
    path: '/char/:id(\\d+)',
    name: 'charDetail',
    component: CharDetail,
    redirect: { name: 'attribute' },
    meta: {
      title: '角色详情 | gs_wiki'
    },
    children: [{
      path: 'attribute',
      name: 'attribute',
      component: AttributeTable
    }, {
      path: 'talent',
      name: 'talent',
      component: TalentTable
    }, {
      path: 'constellation',
      name: 'constellation',
      component: ConstellationTable
    }, {
      path: 'profile',
      name: 'profile',
      component: ProfileTable
    }]
  }, {
    path: '/weapon/:id(\\d+)',
    name: 'weaponDetail',
    component: WeaponDetail,
    meta: {
      title: '武器详情 | gs_wiki'
    }
  }, {
    path: '/timer',
    name: GachaTimer,
    component: GachaTimer,
    meta: {
      title: '祈愿计时 | gs_wiki'
    }
  }, {
    hide: true,
    path: '/:pathMatch(.*)*',
    component: NotFound,
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes: routes
})

export default router
