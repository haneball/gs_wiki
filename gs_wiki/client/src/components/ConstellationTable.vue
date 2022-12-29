<template>
    <div id="constellation-table">
        <el-card shadow="never" v-for="(item, index) in constellation" :key="index">
            <div slot="header">
                <el-row type="flex" align="middle">
                    <el-col :span="2">
                        <el-image
                            style="width: 44px; height: 44px"
                            fit="contain"
                            :src="require('@/assets/img/constellation_icon/constellation_icon_' + $route.params.id + '_' + (index + 1) + '.png')">
                        </el-image>
                    </el-col>
                    <el-col class="constell-title" :span="22">
                        <span>第{{ index + 1 }}层  </span>
                        <span>{{ item.title }}</span>
                    </el-col>
                </el-row>
            </div>
            <div class="constell-text" v-html="item.text"></div>
        </el-card>
    </div>
</template>

<script>
export default {
  props: {
    constellation: Array
  }
}
</script>

<style>
#constellation-table {
  width: 100%;
}

#constellation-table > .el-card {
  margin-bottom: 12px;
}

#constellation-table > .el-card > .el-card__header {
  padding: 6px 18px;
}

#constellation-table > .el-card > .el-card__header .el-row {
  margin-bottom: 0;
}

#constellation-table > .el-card > .el-card__header .el-row .el-col {
  margin: 4px 0 0 0;
}

#constellation-table > .el-card > .el-card__body {
  padding: 10px 18px;
}

#constellation-table .constell-title {
  font-weight: 666;
}

#constellation-table .constell-text {
  margin-bottom: 12px;
  white-space: pre-wrap;
  font-size: 14px;
}

#constellation-table .constell-text > .font-bold {
  font-weight: 555;
}
</style>
