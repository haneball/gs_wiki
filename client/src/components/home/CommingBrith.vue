<template>
  <div id="coming-brith">
    <div class="header">即将到来的生日</div>
    <div class="body">
      <el-row type="flex">
        <el-col
          v-for="(item, index) in dataList"
          :key="index"
          :xl="4" :lg="4" :md="4" :sm="6" :xs="6"
        >
          <div class="col-item">
            <router-link :to="`/char/${item.id}`">
              <img
                :style="genStyle(item.star)"
                :src="imgURL + '/char_icon/char_icon_' + item.id + '.png'"
              />
            </router-link>
            <span>{{ item.brithday }}</span>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { getComingBrith } from '../../api'

let dataList = ref([])

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

// 获取数据
const getData = () => {
  getComingBrith().then(response => {
    if (response.data.status === 200) {
      dataList.value.length = 0
      response.data.data.forEach(item => {
        dataList.value.push(item)
      })
    }
  }).catch((error) => {
    console.log(error)
  })
}
getData()

// 生成背景属性
const genStyle = (star) => {
  let index = star * 1 - 1
  if (isNaN(star * 1) || !bgImage[index]) return
  return `background-image: linear-gradient(${bgImage[index].top}, ${bgImage[index].bottom});`
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

#coming-brith {
  width: 100%;
  margin-top: 1rem;
  border-radius: .5rem;
  background-color: #FFF;
}

.el-row {
  flex-wrap: wrap;
}

.header {
  padding: 1rem;
  color: $primary-text;
  font: {
    size: 1.25rem;
    weight: bold;
  }
}

.body {
  padding: 1rem;
  border-top: 2px solid $light-border;
}

.space-header {
  margin: 1rem 0;
  font: {
    size: $medium-font-size;
    weight: bold;
  }
}

.col-item {
  margin: .4rem;
  font-size: $base-font-size;
  text-align: center;
  img {
    width: 100%;
    display: block;
    margin-bottom: .25rem;
    aspect-ratio: 1/1;
    border-radius: .5rem;
  }
  span {
    line-height: 1.5;
  }
}
</style>
