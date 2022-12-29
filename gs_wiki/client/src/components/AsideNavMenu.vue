<template>
    <div id="aside-nav-bar">
        <el-menu router>
          <el-image
            style="width: 160px; height: 42.1px"
            fit="contain"
            :src="require('@/assets/img/ui_package/gs_wiki.png')">
          </el-image>
          <el-divider></el-divider>
          <!-- <el-menu-item @click="toggleCollapse">
            <i class="el-icon-s-help"></i>
            <span>收起</span>
          </el-menu-item> -->
          <el-menu-item
            v-for="item in menuItem"
            :key="item"
            :index="item.path">
            <i :class="item.icon"></i>
            <span slot="title">{{ item.name }}</span>
          </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
export default {
  data () {
    return {
      isCollapse: false,
      menuItem: [{
        name: '主页',
        path: '/',
        icon: 'el-icon-s-home'
      }, {
        name: '角色',
        path: '/char',
        icon: 'el-icon-user-solid'
      }, {
        name: '武器',
        path: '/weapon',
        icon: 'el-icon-s-cooperation'
      }]
    }
  },
  methods: {
    toggleCollapse () {
      this.isCollapse = !this.isCollapse
    }
  }
}
</script>

<style>
#aside-nav-bar > .el-menu {
  position: fixed;
  height: 100vh;
}

#aside-nav-bar > .el-menu:not(.el-menu--collapse) {
  width: 200px;
  height: 100vh;
}

#aside-nav-bar .el-image {
  margin: 20px;
}

#aside-nav-bar .el-divider {
  margin: 0;
}
</style>
