<template>
  <div id="timer-progress">
    <div class="timer-title">{{ timerTitle }}</div>
    <div class="item-content" v-for="(item, index) in dataList" :key="index">
      <router-link :to="`/${category}/${item.id}`">
        <div class="item-icon">
          <span v-if="item.days < 1">UP</span>
          <img
            :style="genStyle"
            :src="imgURL + '/' + props.category + '_icon/' + props.category + '_icon_' + item.id + '.png'"
            alt="Item Icon"
          />
        </div>
      </router-link>
      <div>
        <div class="text-content">
          <span class="item-name">{{ item.name }}</span>
          <el-tag
            effect="plain"
            size="small"
            :disable-transitions="true"
            round
          >{{ item.debut }}
          </el-tag>
          <span class="item-days">{{ item.format }}</span>
        </div>
        <el-progress
          :show-text="false"
          :stroke-width="12"
          :percentage="percent(item.days)"
          :status="status(item.days)"
        >
        </el-progress>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { queryTimer } from '../../api'

let dataList = ref([])
const props = defineProps({
  category: String,
  star: Number
})

let todayArr
const imgURL = 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'
// 背景数值
const bgImage = [{
  top: '#71419A',
  bottom: '#A25DDB'
}, {
  top: '#9C6721',
  bottom: '#E0932F'
}]

watch (
  () => props.star,
  (newVal) => {
    const storage = JSON.parse(sessionStorage.getItem(props.category + props.star))
    if (storage) {  // 查询是否有缓存
      dataList.value.length = 0
      storage.forEach(element => {
        dataList.value.push(element)
      })
    } else {
      getData(props.category, newVal)
    }
  }
)

// 请求数据
const getData = (category, star) => {
  queryTimer(category, star).then(response => {
    if (response.data.status === 200) { // 校准客户端日期
      dataList.value.length = 0
      todayArr = response.data.today.split('-')

      response.data.data.forEach(item => {
        // 计算日期
        const tmp = resolveData(item)
        item.format = tmp.format
        item.days = tmp.days
        dataList.value.push(item)
      })
    }
    // 排序
    dataList.value = bubbleSort(dataList.value)
    // 缓存结果
    sessionStorage.setItem(props.category + props.star, JSON.stringify(dataList.value))
  }).catch((error) => {
    console.log(error)
  })
}
getData(props.category, props.star)

// 日期计算
const resolveData = (data) => {
  const startArr = data.start.split('-')
  const endArr = data.end.split('-')
  const nowDate = new Date(todayArr[0], todayArr[1] - 1, todayArr[2])   // 当前日期对象
  const startDate = new Date(startArr[0], startArr[1] - 1, startArr[2]) // 起始日期对象
  const endDate = new Date(endArr[0], endArr[1] - 1, endArr[2])         // 结束日期对象
  // 当前日期与开始日期的相对值
  const startDays = Math.round((Date.parse(nowDate) - Date.parse(startDate)) / 1000 / 86400)
  // 当前日期与结束日期的相对值
  const endDays = Math.round((Date.parse(nowDate) - Date.parse(endDate)) / 1000 / 86400)

  let result = {format: '', days: 0}
  if (startDays > 0) {  // 祈愿已经开始
    if (endDays > 0) {  // 祈愿已经结束
      result.format = `${endDays}天`
      result.days = endDays
    } else {  // 祈愿尚未结束
      result.format = `距结束 ${-endDays}天`
    }
  } else {  // 祈愿尚未开始
    result.format = `距开始 ${-startDays}天`
    result.days = -1
  }
  return result
}

// 排序
function bubbleSort (data) {
  for (let i = 0; i < data.length; i++) {
    let flag = true
    for (let j = 0; j < data.length - 1; j++) {
      if (data[j].days < data[j + 1].days) {
        let temp = data[j]
        data[j] = data[j + 1]
        data[j + 1] = temp
        flag = false
      }
    }
    if (flag) break
  }
  return data
}

// el-progress 的 percent 属性
const percent = (days) => {
  if (dataList.value.length > 0) {
    return parseInt(days / dataList.value[0].days * 100)
  }
  return 0
}

// el-progress 的 status 属性
const status = (days) => {
  let per = 0
  if (dataList.value.length > 0) {
    per = parseInt(days / dataList.value[0].days * 100)
  }
  let s = ''
  if (per >= 80) {
    s = 'exception'
  } else if (per >= 60) {
    s = 'warning'
  } else if (per <= 20) {
    s = 'success' 
  }
  return s
}

// 组件标题
const timerTitle = computed(() => {
  const translateMap = {'char': '角色', 'weapon': '武器'}
  return translateMap[props.category]
})

// 生成背景属性
const genStyle = computed(() => {
  let index = props.star - 4
  return `background-image: linear-gradient(${bgImage[index].top}, ${bgImage[index].bottom});`
})

const genURL = computed(() => {
    const path = `/${props.category}/${props.id}`
    return this.category === 'char' ? path + '/attribute' : path
})
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

#timer-progress {
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: .5rem;
  background-color: #FFF;
}

.timer-title {
  width: 100%;
  padding: .5rem 0;
  margin: 0 auto;
  color: #FFF;
  font-size: 1rem;
  text-align: center;
  border-radius: .5rem;
  background-color: $info-color;
}

.item-content {
  width: 100%;
  display: flex;
  margin: .8rem 0;
  &:last-child {
    margin-bottom: 0;
  }
  & > div {
    flex-grow: 1;
    margin-left: .8rem;
  }
}

.item-icon {
  position: relative;
  width: 4.5rem;
  height: 4.5rem;
  border-radius: .5rem;
  overflow: hidden;
  span {
    position: absolute;
    top: 0;
    left: 0;
    padding: .125rem .25rem;
    color: #FFF;
    font: {
      size: .8rem;
      weight: bold;
    };
    border-bottom-right-radius: .5rem;
    background-color: #F00;
  }
  img {
    width: 4.5rem;
    height: 4.5rem;
    display: block;
  }
}

.text-content {
  display: flex;
  align-items: center;
  margin-bottom: .5rem;
  .item-name {
    margin-right: .25rem;
    font: {
      size: 1rem;
      weight: bold;
    };
  }
  .item-days {
    flex-grow: 1;
    color: $secondary-text;
    font-size: 1rem;
    text-align: right;
  }
}
</style>
