<template>
  <div class="common-layout">
    <div class="notice">注意：本网站已暂停更新</div>
    <el-container>
      <el-header>
        <HeadNavMenu />
      </el-header>
      <el-main>
        <router-view v-wechat-title="$route.meta.title"></router-view>
        <BackTopBtn class="hidden-xs-only"/>
      </el-main>
      <el-footer>
        <PageFooter />
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import HeadNavMenu from './components/HeadNavMenu.vue'
import PageFooter from './components/PageFooter.vue'
import BackTopBtn from './components/custom/BackTopBtn.vue'

export default {
  name: 'App',
  components: {
    HeadNavMenu,
    PageFooter,
    BackTopBtn
  }
}
</script>

<style lang="scss">
@import 'element-plus/theme-chalk/display.css';
@import './assets/scss/index.scss';
$element-height: 100%;


html, body {
  height: $element-height;
  padding: 0;
  margin: 0;
}

html {
  overflow-y: scroll;
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
  'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}

body {
  background-color: #F2F3F5;
}

h1 {
  font-size: 2rem;
  margin: 1.5rem 0;
}

h2 {
  font-size: 1.25rem;
  margin: 1rem 0;
}

#app {
  width: 100%;
  max-width: 2160px;
  height: 100%;
  padding: 0;
  text-align: left;
}

.el-container {
  height: $element-height;
  .el-header {
    width: 100%;
    height: 60px;
    padding: 0;
  }
  .el-main {
    min-height: calc(100vh - 150px);
    color: $primary-text;
    background-color: #F2F3F5;
    z-index: 1;
  }
  .el-footer {
    min-height: 90px;
    padding: 0;
  }
}

.el-button:active {
  transform: scale(0.95);
}

.notice {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: .5rem 0;
  color: #E6A23C;
  background-color: #FDF6EC;
}

@media (min-width: $xs-width) {
  html {
    font-size: $xsmall-font-size;
  }
  .el-container {
    .el-main {
      padding: 1rem;
    }
  }
}

@media (min-width: $sm-width) {
  html {
    font-size: $small-font-size;
  }
  .el-container {
    .el-main {
      padding: 1.5rem;
    }
  }
}

@media (min-width: $md-width) {
  html {
    font-size: $base-font-size;
  }
  .el-container {
    .el-main {
      padding: 2rem;
    }
  }
}

@media (min-width: $lg-width) {
  html {
    font-size: $base-font-size;
  }
  .el-container {
    .el-main {
      padding: 2rem 10rem;
    }
  }
}
</style>
