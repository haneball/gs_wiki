<template>
  <div id="voice-over">
    <el-card
      v-for="item in voice"
      :key="item"
      shadow="never"
    >
      <template #header>
        <div class="voice-title">
          <strong>{{ item.title }}</strong>
          <!-- <el-button
            style="float: right; padding: 3px 0"
            type="text"
            disabled
          >
            播放
          </el-button> -->
        </div>
      </template>
      <div class="voice-text">{{ item.text }}</div>
    </el-card>
  </div>
</template>

<script>
export default {
  props: {
    voice: {
      type: Array,
      default () {
        return [{title: '', text: ''}]
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

.el-card {
  border: none;
  border-radius: .5rem;
  &:not(:last-child) {
    margin-bottom: 1rem;
  }
  :deep(.el-card__header) {
    padding: 1rem;
    border-bottom: 2px solid $light-border;
  }
  :deep(.el-card__body) {
    padding: .8rem 1rem;
  }
}

.voice-text {
  margin-bottom: 1rem;
  white-space: pre-wrap;
  font-size: 1rem;
  color: $regular-text;
  line-height: 1.5;
}
</style>
