<template>
    <div id="page-footer">
        <el-row type="flex" align="middle">
            <el-col :span="20">
              <div>
                <i class="el-icon-warning"></i>
                本站仅作学习用途，一切数据资源归版权方所有。</div>
            </el-col>
            <el-col :span="2">
              <div class="link-tag" style="width: 100%">项目地址</div>
              <el-link href="https://gitee.com/melon-pan/gs_wiki" :underline="false">
                <el-image
                  style="width: 32px; height: 32px"
                  fit="contain"
                  :src="require('@/assets/img/ui_package/gitee_logo.png')">
                </el-image>
              </el-link>
              <el-link href="https://github.com/haneball/gs_wiki" :underline="false">
                <el-image
                  style="width: 32px; height: 32px"
                  fit="contain"
                  :src="require('@/assets/img/ui_package/github_logo.png')">
                </el-image>
              </el-link>
            </el-col>
            <el-col :span="2">
              <div class="link-tag" style="width: 100%">使用框架</div>
              <el-link href="https://cn.vuejs.org/" :underline="false">
                <el-image
                  style="width: 32px; height: 32px"
                  fit="contain"
                  :src="require('@/assets/img/ui_package/vue_logo.png')">
                </el-image>
              </el-link>
              <el-link href="https://element.eleme.io/#/zh-CN" :underline="false">
                <el-image
                  style="width: 32px; height: 32px"
                  fit="contain"
                  :src="require('@/assets/img/ui_package/elementUI_logo.png')">
                </el-image>
              </el-link>
            </el-col>
        </el-row>
    </div>
</template>

<style>
#page-footer {
  min-width: 1080px;
  height: 100%;
  padding: 0 40px;
  background-color: #F6F6F6;
  font-size: 16px;
  z-index: 1;
  overflow: inherit;
}

#page-footer .el-row {
  width: 100%;
  min-height: 60px;
  padding: 18px 0;
  margin: 0;
}

#page-footer .el-col {
  margin: 0;
}

#page-footer .el-image {
  margin-top: 4px;
}

#page-footer .link-tag {
  width: 100%;
  font-size: 14px;
  color: #606266;
}
</style>
