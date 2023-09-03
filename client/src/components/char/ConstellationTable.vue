<template>
  <div id="constellation-table" v-if="$store.state.charObj !== null">
    <el-card shadow="never" v-for="(item, index) in constellation" :key="index">
      <template #header>
        <div class="constell-header">
          <!-- 命之座图标 -->
          <img
            :src="imgURL + '/constellation_icon/constellation_icon_' + $route.params.id + '_' + (index + 1) + '.png'"
            alt="Constellation Icon"
          />
          <!-- 命之座名称 -->
          <strong>{{ `第${index + 1}层 ${item.title}` }}</strong>
        </div>
      </template>
      <!-- 命之座文本 -->
      <div class="constell-text" v-html="item.text"></div>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      imgURL: 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'
    }
  },
  computed: {
    constellation () {
      return this.$store.state.charObj.constellation
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

#constellation-table {
  width: 100%;
}

.constell-header {
  display: flex;
  align-items: center;
  img {
    width: 2.75rem;
    margin-right: .8rem;
    aspect-ratio: 1/1;
  }
}

.constell-text {
  margin-bottom: 1rem;
  white-space: pre-wrap;
  font-size: 1rem;
  color: $regular-text;
  line-height: 1.5;
  :deep(.font-bold) {
    font-weight: bold;
  }
}

.el-card {
  border: none;
  border-radius: .5rem;
  &:not(:last-child) {
    margin-bottom: 1rem;
  }
  :deep(.el-card__header) {
    padding: .5rem 1rem;
    border-bottom: 2px solid $light-border;
  }
  :deep(.el-card__body) {
    padding: .5rem 1rem;
  }
}
</style>
