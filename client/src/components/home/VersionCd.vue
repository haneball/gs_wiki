<template>
  <div id="version-cd">
    <div class="version-box">
      <el-row type="flex">
        <el-col :span="5">
          <div class="info-label">当前版本</div>
          <div class="main-text">
            <span>{{ number }}</span>
          </div>
        </el-col>
        <el-col :span="5">
          <div class="info-label">剩余</div>
          <el-progress
            type="circle"
            :width="48"
            :height="48"
            :percentage="percent"
            :format="format"
          >
          </el-progress>
        </el-col>
        <el-col class="logo" :span="14">
          <img
            :src="imgURL + '/ui_package/gs_wiki_logo_dark.png'"
          />
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { getVersion } from '../../api'

let number = ref('')
let name = ref('')
let days = ref(0)
let hours = ref(0)
let percent = ref(0)

let now = null
const imgURL = 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'


const getData = () => {
  getVersion().then(response => {
    number.value = response.data.number
    name.value = response.data.name
    now = response.data.now
    calcDate(response.data.start, response.data.end)
  }).catch(error => {
    console.log(error)
  })
}
getData()

// 日期字符串转数组
const resolveDate = (dateString) => {
  let arr = dateString.replace(/\+.*/g, '').split(' ')
  let date = arr[0].split('-')
  let time = arr[1].split(':')
  // 拼合日期和时间
  return date.concat(time)
}

// 计算版本剩余天数
const calcDate = (start, end) => {
  const startArr = resolveDate(start)
  const endArr = resolveDate(end)
  const nowArr = resolveDate(now)

  const startDate = new Date(startArr[0], startArr[1] - 1, startArr[2], startArr[3], startArr[4], startArr[5])  // 起始时间
  const endDate = new Date(endArr[0], endArr[1] - 1, endArr[2], endArr[3], endArr[4], endArr[5])  // 结束时间
  const nowDate = new Date(nowArr[0], nowArr[1] - 1, nowArr[2], nowArr[3], nowArr[4], nowArr[5])  // 当前时间
  const surplus = (Date.parse(endDate) - Date.parse(nowDate)) / 1000  // 已过时间
  const len = (Date.parse(endDate) - Date.parse(startDate)) / 1000    // 版本总时长

  days.value = Math.floor(surplus / 60 / 60 / 24)
  hours.value = Math.floor(surplus / 60 / 60) - days.value * 24
  percent.value = Math.round(surplus / len * 100)
}

// el-progress 的 format 属性
const format = () => {
  return (days.value + '天')
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

#version-cd {
  width: 100%;
}

.version-box {
  padding: .5rem;
  border-radius: .5rem;
  background-color: #FFF;
}

.el-row {
  justify-content: center;
  align-items: center;
  margin: 0;
  :deep(.el-col) {
    height: 100%;
    text-align: center;
    &:nth-child(2) {
      border-left: 2px solid $light-border;
      border-right: 2px solid $light-border;
    }
  }
}

.el-progress {
  :deep(.el-progress__text) > span {
    font-size: .75rem;
  }
}

.info-label {
  margin-bottom: .25rem;
  color: $regular-text;
  font-size: $base-font-size;
}

.main-text {
  display: flex;
  height: 48px;
  justify-content: center;
  align-items: center;
  font: {
    size: 2rem;
    weight: bold;
  }
}

.logo {
  padding: .5rem;
  img {
    width: 100%;
    max-width: 210px;
    aspect-ratio: 3/1;
  }
}
</style>
