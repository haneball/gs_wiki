<template>
    <div id="collapse-card">
        <el-collapse class="collapse-card">
            <el-collapse-item :title="title">
                <div class="collapse-card-text">{{ text }}</div>
            </el-collapse-item>
        </el-collapse>
    </div>
</template>

<script>
export default {
  props: {
    title: String,
    text: String
  }
}
</script>

<style>
#collapse-card {
  width: 100%;
}

#collapse-card > .el-collapse {
  padding: 4px 20px;
  margin-bottom: 12px;
  border: 1px solid #EBEEF5;
  border-radius: 4px;
}

#collapse-card .el-collapse-item__header {
  border: none;
  font-size: 16px;
  font-weight: 666;
}

#collapse-card .el-collapse-item__wrap {
  border: none;
}

#collapse-card .collapse-card-text {
  white-space: pre-wrap;
  font-size: 14px;
}
</style>
