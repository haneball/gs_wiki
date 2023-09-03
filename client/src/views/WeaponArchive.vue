<template>
  <div id="weapon-archive">
    <el-row type="flex">
      <el-col :span="24">
        <h1>武器图鉴</h1>
      </el-col>
      <el-col :xl="7" :lg="7" :md="6" :sm="24" :xs="24">
        <div class="pick-box">
          <div class="operate-bar">
            <el-button plain @click="dataList.reverse()">
              <el-icon><Sort /></el-icon>
            </el-button>
            <el-input v-model="searchVal" placeholder="从图鉴搜索...">
              <template #suffix>
                <el-icon><Search /></el-icon>
              </template>
            </el-input>
            <el-button class="hidden-sm-and-up" plain @click="handleClick">
              <el-icon><Filter /></el-icon>
            </el-button>
          </div>
          <el-collapse-transition>
            <div class="pick-content" v-show="isVisable">
              <div v-for="(item, index) in sltList" :key="index">
                <span>{{ item.title }}</span>
                <PickBar
                  v-for="(subItem, subIndex) in item.options"
                  v-model="sltVal[index]"
                  :label="subItem"
                  :key="subIndex">{{ subItem }}</PickBar>
              </div>
            </div>
          </el-collapse-transition>
        </div>
      </el-col>
      <el-col :xl="17" :lg="17" :md="18" :sm="24" :xs="24">
        <el-row class="item-box" type="flex">
          <el-col
            v-for="(item, index) in dataList"
            :key="index"
            v-show="isDisplay(item)"
            :xl="3" :lg="3" :md="4" :sm="4" :xs="6"
          >
            <ItemCell v-bind="item" category="weapon" />
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ItemCell from '../components/ItemCell.vue'
import PickBar from '../components/custom/PickBar.vue'
import { getWeaponList } from '../api/index'

export default {
  components: {
    ItemCell,
    PickBar
  },
  data () {
    return {
      dataList: [],
      isVisable: false,
      searchVal: '',
      sltList: [{
        title: '星级',
        options: ['不限', '★5', '★4', '★3', '★2', '★1']
      }, {
        title: '类型',
        options: ['不限', '单手剑', '双手剑', '长柄武器', '法器', '弓']
      }],
      sltVal: ['不限', '不限']
    }
  },
  created () {
    this.getData()
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResize)
  },
  methods: {
    getData () {
      getWeaponList().then(response => {
        if (response.status === 200) {
          this.dataList.length = 0
          response.data.data.forEach(item => {
            this.dataList.push(item)
          })
          this.dataList = this.bubbleSort(this.dataList, 'type')
          this.dataList = this.bubbleSort(this.dataList, 'star')
        }
      }).catch(error => {
        console.log(error)
      })
    },
    onResize () {
      if (window.innerWidth >= 768) {
        this.isVisable = true
      } else {
        this.isVisable = false
      }
    },
    handleClick () {
      this.isVisable = !this.isVisable
    },
    isDisplay (item) {
      let isStar = item.star === this.sltVal[0].replace('★', '') || this.sltVal[0] === '不限' || !this.sltVal[0]
      let isType = item.type === this.sltVal[1] || this.sltVal[1] === '不限' || !this.sltVal[1]
      let isSearched = item.name.search(this.searchVal) >= 0 || !this.searchVal
      return isStar && isType && isSearched && isSearched
    },
    bubbleSort (data, condition) {
      for (let i = 0; i < data.length; i++) {
        let flag = true
        for (let j = 0; j < data.length - 1; j++) {
          let res = this.judgeFunc(data[j], data[j + 1], condition)
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
      return data
    },
    judgeFunc (a, b, condition) {
      if (condition === 'type' && a.type && b.type) {
        return this.typeToIndex(a.type) > this.typeToIndex(b.type)
      }
      if (condition === 'star' && a.star && b.star) {
        return a.star > b.star
      }
      return 'err'
    },
    typeToIndex (type) {
      const typeList = ['单手剑', '双手剑', '长柄武器', '法器', '弓']
      return typeList.indexOf(type)
    }
  }
}
</script>

<style lang="scss" scoped>
@import 'element-plus/theme-chalk/display.css';
@import '../assets/scss/index.scss';

#weapon-archive {
  margin: auto;
  h1 {
    margin: 20px auto;
    color: $primary-text;
  }
}

.el-row {
  flex-wrap: wrap;
}

.el-button {
  padding: 9px;
  border-radius: .5rem;
}

.el-input {
  margin-left: .4rem;
  :deep(.el-input__wrapper) {
    border-radius: .5rem;
    background-color: #F0F2F5;
    box-shadow: none;
  }
}

.pick-box {
  padding: 1rem;
  margin: .4rem;
  border-radius: .5rem;
  background-color: #FFF;
  .operate-bar, .pick-content > div {
    display: flex;
  }
  .pick-content > div {
    flex-wrap: wrap;
    margin-bottom: .4rem;
    span {
      font-size: 1rem;
      flex-basis: 100%;
    }
    &:first-child {
      margin-top: .4rem;
    }
  }
}

@media (min-width: $xs-width) {
  .el-input {
    margin-right: .4rem;
  }
}
</style>
