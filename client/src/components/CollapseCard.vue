<template>
  <div id="collapse-card">
    <el-collapse>
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

<style lang="scss" scoped>
@import '../assets/scss/index.scss';

#collapse-card {
  width: 100%;
}

.el-collapse {
  padding: .25rem 1rem;
  margin-bottom: 1rem;
  border: none;
  border-radius: .5rem;
  background-color: #FFF;
  :deep(.el-collapse-item__header) {
    border: none;
    font: {
      size: 1rem;
      weight: bold;
    }
  }
  :deep(.el-collapse-item__wrap) {
    border: none;
  }
  .collapse-card-text {
    white-space: pre-wrap;
    font-size: 1rem;
    color: $regular-text;
    line-height: 1.5;
  }
}
</style>
