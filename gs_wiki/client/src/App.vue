<template>
  <div id="app">
    <el-container>
      <el-aside style="width: 200px">
        <AsideNavMenu />
      </el-aside>
      <el-container>
        <el-main>
          <router-view v-wechat-title="$route.meta.title"></router-view>
        </el-main>
        <el-footer>
          <PageFooter />
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AsideNavMenu from '@/components/AsideNavMenu'
import PageFooter from '@/components/PageFooter'

export default {
  name: 'App',
  components: {
    AsideNavMenu,
    PageFooter
  }
}
</script>

<style>
body {
  padding: 0;
  margin: 0;
}

#app .el-container .el-container {
  min-height: 100vh;
}

#app .el-aside {
  z-index: 2;
  overflow-x: hidden;
}

#app .el-main {
  /* min-height: 100vh; */
  padding: 40px 220px 40px 20px;
  z-index: 1;
  overflow: inherit;
}

#app .el-footer {
  min-height: 96px;
  padding: 0;
}
</style>
