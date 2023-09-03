<template>
  <div id="gacha-timer">
    <el-row type="flex">
      <el-col :offset="offset" :span="24 - offset * 2">
        <div class="header-box">
          <h1>祈愿计时</h1>
          <el-select v-model="star">
            <el-option label="★5" :value="5"></el-option>
            <el-option label="★4" :value="4"></el-option>
          </el-select>
        </div>
      </el-col>
      <el-col :offset="offset" :xl="12 - offset" :lg="12 - offset" :md="12" :sm="12" :xs="24">
        <TimerProgress category="char" :star="star" />
      </el-col>
      <el-col :xl="12 - offset" :lg="12 - offset" :md="12" :sm="12" :xs="24">
        <TimerProgress category="weapon" :star="star" />
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import TimerProgress from '../components/timer/TimerProgress.vue'

let star = ref(5)
let offset = ref(0)

onMounted (() => {
  onResize()
  window.addEventListener('resize', onResize)
})

onUnmounted (() => {
  window.removeEventListener('resize', onResize)
})

const onResize = () => {
  if (window.innerWidth >= 1200) {
    offset.value = 1
  } else {
    offset.value = 0
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/scss/index.scss';

.el-row {
  flex-wrap: wrap;
}

.el-select {
  width: 96px;
  float: right;
  :deep(.el-input__wrapper) {
    border-radius: .5rem;
  }
}

.header-box {
  display: flex;
  align-items: center;
  overflow: hidden;
  h1 {
    flex-grow: 1;
    float: left;
    color: $primary-text;
  }
}

.progress-box {
  display: flex;
  justify-content: space-between;
  clear: both;
}

@media (min-width: $sm-width) {
  .el-row {
    :deep(.el-col:nth-child(2)) {
      padding-right: 2rem;
    }
  }
}
</style>
