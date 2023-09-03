<template>
  <div id="head-nav-menu" :class="navClass">
    <div class="head-nav-menu__inner">
      <div class="left-content">
        <a href="/">
          <img
            style="width: 150px; height: 50px"
            :src="imgURL + '/ui_package/gs_wiki_logo_light.png'"
          />
        </a>
        <el-menu
          :default-active="setActiveIndex"
          class="hidden-xs-only"
          mode="horizontal"
          :ellipsis="false"
          :text-color="textColor"
          :active-text-color="activeColor"
          router
        >
          <el-menu-item
            v-for="(item, index) in menuItem"
            :key="index"
            :index="item.path"
            style="border-bottom-width: 0;"
          >
            <template #title>
              <span>{{ item.name }}</span>
            </template>
          </el-menu-item>
        </el-menu>
      </div>
      <div class="right-content hidden-xs-only"><QuerySearch /></div>
      <el-dropdown class="hidden-sm-and-up" trigger="click" placement="bottom-start">
        <div class="menu-btn">
          <el-icon><Menu /></el-icon>
        </div>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item
              class="hidden-sm-and-up"
              v-for="(item, index) in menuItem"
              :key="index"
              :icon="item.icon"
              @click.native="jmpToPage(item.path)"
            >{{ item.name }}
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
import QuerySearch from './QuerySearch.vue'

export default {
  components: {
    QuerySearch
  },
  data () {
    return {
      isVisable: false,
      activeIndex: '',
      menuItem: [{
        name: '主页',
        path: '/',
        icon: 'House'
      }, {
        name: '角色',
        path: '/char',
        icon: 'User'
      }, {
        name: '武器',
        path: '/weapon',
        icon: 'KnifeFork'
      }, {
        name: '祈愿计时',
        path: '/timer',
        icon: 'Timer'
      }],
      navClass: 'nav-bar__top',
      textColor: '#FFF',
      activeColor: '#FFF',
      imgURL: 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'
    }
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize)
    window.addEventListener('scroll', this.onScroll)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResize)
    window.removeEventListener('scroll', this.onScroll)
  },
  computed: {
    setActiveIndex () {
      if (this.$route.path.match('char')) {
        return '/char'
      } else if (this.$route.path.match('weapon')) {
        return '/weapon'
      } else if (this.$route.path.match('timer')) {
        return '/timer'
      }
      return '/'
    }
  },
  methods: {
    onResize () {
      if (window.innerWidth >= 768) {
        this.isVisable = false
      } 
    },
    onScroll () {
      let scrollTop = document.documentElement.scrollTop
      if (scrollTop >= 240) { // 滚动高度大于 240, 导航栏为 fixed 定位
        this.navClass = 'nav-bar__fixed'
      } else if (scrollTop <= 60) {
        this.navClass = 'nav-bar__top'
      }
    },
    handleClick () {
      this.isVisable = !this.isVisable
    },
    jmpToPage (index) {
      this.$router.push(index)
    }
  }
}
</script>

<style lang="scss" scoped>
@import 'element-plus/theme-chalk/display.css';
@import '../assets/scss/index.scss';
@import '../assets/scss/anime.scss';
$element-height: 60px;

#head-nav-menu {
  width: 100%;
  height: $element-height;
  padding: 0 1rem;
  box-sizing: border-box;
  z-index: 1999;
}

:deep(.el-menu--horizontal.el-menu) {
  border: none;
}

.el-menu {
  background-color: transparent;
  :deep(.el-menu-item) {
    font-size: $medium-font-size;
    font-weight: 520;
    &:not(.is-disabled):hover, &:not(.is-disabled):focus {
      background-color: #3D3F43;
    }
    &.is-active {
      font-weight: 555;
      background-color: #3D3F43;
    }
  }
}

.el-dropdown {
  color: #FFF;
}

.head-nav-menu__inner {
  height: $element-height;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 auto;
  .left-content {
    display: flex;
    align-items: center;
    a > img {
      padding: 0 12px;
    }
  }
  .right-content {
    display: flex;
    flex-grow: 1;
    justify-content: end;
    margin-right: 12px;
  }
}

.nav-bar__top {
  // position: absolute;
  // top: 0;
  background-color: #272727;
}

.nav-bar__fixed {
  position: fixed;
  top: 0;
  background-color: #272727;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
  @include slide-in(.2s);
}

.menu-btn {
  width: 60px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5rem;
  box-sizing: border-box;
  i {
    font-size: 24px;
  }
}
</style>
