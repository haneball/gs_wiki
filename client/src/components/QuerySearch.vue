<template>
  <div id="query-search">
    <el-autocomplete
      v-model="inputVal"
      :fetch-suggestions="querySearchAsync"
      placeholder="搜索..."
      :trigger-on-focus="false"
      @select="jmpToDetail"
    >
      <template #suffix>
        <el-icon><Search /></el-icon>
      </template>
      <template #default="{ item }">
        <div style="padding: 4px 0; line-height: 1.3;">
          <div v-html="toHtml(item.value)"></div>
          <span class="category-label">{{ item.categoryCN }}</span>
        </div>
      </template>
    </el-autocomplete>
    </div>
</template>

<script>
import { querySearch } from '../api'

export default {
  data () {
    return {
      inputVal: '',
      dataList: [],
      queryURL: '/querySearch',
      timeout: null
    }
  },
  watch: {
    inputVal: {
      handler (newVal) {
        if (newVal !== '') {
          this.getData(newVal)
        }
      }
    }
  },
  methods: {
    getData (kw) {
      querySearch(kw).then(response => {
        if (response.data.status === 200) {
          this.dataList.length = 0
          response.data.data.forEach(item => {
            this.dataList.push(item)
          }) 
        } else if (response.data.status === 404) {  // 构造空结果
            this.dataList = [{
              id: null,
              value: '',
              categoryCN: '',
              categoryEN: ''
            }]
        }
      }).catch((error) => {
        console.log(error)
      })
    },
    querySearchAsync (queryString, cb) {
      let result = []
      if (queryString === '') { // 返回空数组
        cb(result)
      } else {
        result = this.dataList
        cb(result)
      }
    },
    toHtml (str) {
      let p = ''
      if (str === '') {
        p = '暂无结果'
      } else {
        p = this.inputVal.length ?
          str.replace(new RegExp(this.inputVal, 'g'), `<span style="color: #409EFF">${this.inputVal}</span>`) : str
      }
      return p
    },
    jmpToDetail (item) {
      if (item.id === null) return
      this.$router.push({
        name: item.categoryEN + 'Detail',
        params: {id: item.id}
      })
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/scss/index.scss';

:deep(.el-input__wrapper) {
  border: none;
  border-radius: .5rem;
  background-color: #3D3F43;
  box-shadow: none;
  box-sizing: border-box;
  .el-input__inner {
    width: 120px;
    color: #FFF;
    // transition: width .3s ease;
    // &:focus {
    //   width: 180px;
    // }
  }
  &:hover {
    box-shadow: none;
  }
  &:focus {
    box-shadow: none;
  }
}

:deep(.el-input__wrapper.is-focus) {
    box-shadow: none;
  }

.el-autocomplete {
  :deep(el-input > .el-input__wrapper) {
    width: 160px;
    color: #FFF;
    border: none;
    border-radius: .5rem;
    background-color: #3D3F43;
  }
}

:deep(.el-autocomplete-suggestion) {
  border-radius: .5rem;
}

.category-label {
  font-size: $xsmall-font-size;
  color: $placeholder-text;
}
</style>
