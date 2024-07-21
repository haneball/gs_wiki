<template>
  <div id="char-archive">
    <el-row type="flex">
      <el-col :span="24">
        <h1>角色图鉴</h1>
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
                  :key="subIndex"
                >{{ subItem }}
                </PickBar>
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
            <ItemCell v-bind="item" category="char" />
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ItemCell from '../components/ItemCell.vue'
import PickBar from '../components/custom/PickBar.vue'
import { getCharList } from '../api/index'

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
        title: '地区',
        options: ['不限', '蒙德', '璃月', '稻妻', '须弥', '枫丹', '纳塔','至冬', '其他']
      }, {
        title: '星级',
        options: ['不限', '★5', '★4']
      }, {
        title: '元素',
        options: ['不限', '火', '水', '风', '雷', '草', '冰', '岩']
      }, {
        title: '类型',
        options: ['不限', '单手剑', '双手剑', '长柄武器', '法器', '弓']
      }],
      sltVal: ['不限', '不限', '不限', '不限']
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
      getCharList().then(response => {
        if (response.data.status === 200) {
          this.dataList.length = 0
          response.data.data.forEach(item => {
            this.dataList.push(item)
          })
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
      let isArea = item.area === this.sltVal[0] || this.sltVal[0] === '不限' || !this.sltVal[0]
      let isStar = item.star === this.sltVal[1].replace('★', '') || this.sltVal[1] === '不限' || !this.sltVal[1]
      let isElement = item.element === this.sltVal[2] || this.sltVal[2] === '不限' || !this.sltVal[2]
      let isType = item.type === this.sltVal[3] || this.sltVal[3] === '不限' || !this.sltVal[3]
      let isSearched = item.name.search(this.searchVal) >= 0 || !this.searchVal
      return isArea && isStar && isElement && isType && isSearched
    }
  }
}
</script>

<style lang="scss" scoped>
@import 'element-plus/theme-chalk/display.css';
@import '../assets/scss/index.scss';

#char-archive {
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
