<template>
    <div id="tab-row">
        <el-row :class="genClassName">
            <el-col :span="12"><span>{{ label }}</span></el-col>
            <el-col :span="12" style="text-align: right;"><span>{{ value }}</span></el-col>
        </el-row>
    </div>
</template>

<script>
export default {
  props: {
    label: String,
    value: String,
    isDark: Boolean
  },
  computed: {
    genClassName () {
      return this.isDark ? 'dark-bg' : 'bright-bg'
    }
  }
}
</script>

<style>
#tab-row > .el-row {
  padding: 10px 14px;
  margin: 0;
  border-radius: 4px;
  font-size: 14px;
}

#tab-row > .el-row > .el-col {
  margin: 0;
}

.dark-bg {
  background-color: #F2F6FC;
}
</style>
