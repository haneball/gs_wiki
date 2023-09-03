<template>
  <div id="today-material">
    <div class="space-header">
      <h2>每日素材</h2>
      <el-select v-model="weekday" placeholder="请选择" @change="handleSelect">
        <el-option
          v-for="(item, index) in week"
          :key="index"
          :label="item"
          :value="index < 6 ? index + 1 : 0"
        >
        </el-option>
      </el-select>
    </div>
    <div class="material-box">
      <div v-show="!weekday" class="info-content">
        <el-result title="温馨提示" subTitle="今日所有素材均可获取">
          <template #icon>
            <img
              style="width: 96px; height: 96px;"
              :src="imgURL + '/ui_package/info_icon.png'"
            />
          </template>
        </el-result>
      </div>
      <div v-show="weekday" class="item-content">
        <div v-for="(item, index) in dataList" :key="index">
          <div class="area-banner">
            <img
              :src="imgURL + '/ui_package/area_' + (index * 1 + 1) + '.png'"
            />
            <span>{{ item.area }}</span>
          </div>
          <el-row type="flex">
            <el-col
              v-for="(cItem, cIndex) in item.char"
              :key="cIndex"
              :xl="4" :lg="4" :md="4" :sm="4" :xs="4"
            >
              <div class="col-item">
                <router-link :to="`/char/${cItem.id}`">
                  <img
                    :style="genStyle(cItem.star)"
                    :src="imgURL + '/char_icon/char_icon_' + cItem.id + '.png'"
                  />
                </router-link>
              </div>
            </el-col>
          </el-row>
          <el-divider></el-divider>
          <el-row type="flex">
            <el-col
              v-for="(wItem, wIndex) in item.weapon"
              :key="wIndex"
              :xl="4" :lg="4" :md="4" :sm="4" :xs="4"
            >
              <div class="col-item">
                <router-link :to="`/weapon/${wItem.id}`">
                  <img
                    :style="genStyle(wItem.star)"
                    :src="imgURL + '/weapon_icon/weapon_icon_' + wItem.id + '.png'"
                  />
                </router-link>
              </div>
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { queryMaterial } from '../../api'

let weekday = ref(1)
let dataList = ref({})

let severDay = 0
const week = ref(['周一', '周二', '周三', '周四', '周五', '周六', '周日'])
const imgURL = 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'
// 背景数值
const bgImage = [{
  top: '#72767D',
  bottom: '#A3A9B2'
}, {
  top: '#1B6B59',
  bottom: '#27997F'
}, {
  top: '#206993',
  bottom: '#2F96D1'
}, {
  top: '#71419A',
  bottom: '#A25DDB'
}, {
  top: '#9C6721',
  bottom: '#E0932F'
}]

// 请求数据
const getData = (day) => {
  if (!weekday.value) return
  queryMaterial(day).then(response => {
    let sd = response.data.day
    if (severDay === 0) {
      severDay = sd
      weekday.value = severDay
    }
    if (response.data.status === 200) {
      // 处理数据
      response.data.data = resolveData(response.data.data)
      // 拷贝到 dataList
      dataList.value = Object.assign({}, response.data.data)
    }
    // 缓存结果
    sessionStorage.setItem(`material_data_${weekday.value}`, JSON.stringify(response.data.data))
  }).catch((error) => {
    console.log(error)
  })
}
getData()

// 处理数据
const resolveData = (data) => {
  if (data && data.length > 0) {
    data.forEach(item => {
      item.weapon = bubbleSort(item.weapon, 'type');  // 按类型 type 排序
      item.weapon = bubbleSort(item.weapon, 'star');  // 按星级 star 排序
    });
  }
  return data
}

// 排序
const bubbleSort = (data, condition) => {
  if (data && data.length) {
    for (let i = 0; i < data.length; i++) {
      let flag = true
      for (let j = 0; j < data.length - 1; j++) {
        // 调用 judgeFunc() 方法判断
        let res = judgeFunc(data[j], data[j + 1], condition)
        if (res === 'err') break
        if (res) {
          flag = false
          let temp = data[j]
          data[j] = data[j + 1]
          data[j + 1] = temp
        }
      }
      if (flag) break
    }
  }
  return data
}

// 排序条件判断
const judgeFunc = (a, b, condition) => {
  if (condition === 'type' && a.type && b.type) {
    return typeToIndex(a.type) > typeToIndex(b.type)
  }
  if (condition === 'star' && a.star && b.star) {
    return a.star > b.star
  }
  return 'err'
}

// 类型权重
const typeToIndex = (type) => {
  const typeList = ['单手剑', '双手剑', '长柄武器', '法器', '弓']
  return typeList.indexOf(type)
}

// 处理星期 Select 操作
const handleSelect = () => {
  const storage = JSON.parse(sessionStorage.getItem(`material_data_${weekday.value}`))
  if (storage) {  // 查询是否有缓存
    dataList.value = Object.assign({}, storage)
  } else {
    getData(weekday.value)
  }
}

// 生成背景
const genStyle = (star) => {
  let index = star * 1 - 1
  if (isNaN(star * 1) || !bgImage[index]) return
  return `background-image: linear-gradient(${bgImage[index].top}, ${bgImage[index].bottom});`
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

#today-material {
  width: 100%;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  margin-top: 1rem;
  border-radius: .5rem;
  background-color: #FFF;
  h2 {
    margin: 0;
  }
}

.el-select {
  width: 7rem;
  :deep(.el-input__wrapper) {
    border: {
      color: $base-border;
      radius: .5rem;
    };
  }
}

.el-row {
  flex-wrap: wrap;
  :deep(.el-col) {
    margin: 0;
  }
}

.el-divider {
  width: 96%;
  margin: 1rem auto;
}

.material-box {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  padding: 1rem;
  border-top: 2px solid $light-border;
  overflow-y: auto;
  &::-webkit-scrollbar{
    width: 4px;
  }
  &::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background: rgba(0,0,0,0.2);
  }
  &::-webkit-scrollbar-track {
    border-radius: 0;
    background: transparent;
  }
}

.space-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  & > span {
    font: {
      size: $medium-font-size;
      weight: bold;
    }
  }
}

.area-banner {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: .5rem 0;
  margin: .25rem 0;
  border-radius: .5rem;
  background-color: $info-color;
  img {
    width: 2rem;
    height: 2rem;
  }
  span {
    color: #FFF;
    line-height: 1.5;
  }
}

.col-item {
  margin: .25rem;
  img {
    width: 100%;
    display: block;
    border-radius: .5rem;
    aspect-ratio: 1/1;
  }
}

@media (min-width: $sm-width) {
  .material-box {
    height: 80vh;
  }

  .info-content {
    height: 100%;
  }

  .item-content {
    height: auto;
  }
}
</style>
