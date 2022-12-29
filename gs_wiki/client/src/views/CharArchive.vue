<template>
    <div id="char-archive">
        <h1>角色图鉴</h1>
        <el-row :gutter="10" justify="space-between">
          <el-col :span="3">
            <el-select v-model="areaVal" placeholder="地区">
              <el-option
                v-for="(item, index) in area"
                :key="index"
                :label="item"
                :value="item">
              </el-option>
            </el-select>
          </el-col>
          <el-col :span="3">
            <el-select v-model="starVal" placeholder="星级">
              <el-option label="不限" value="不限"></el-option>
              <el-option label="★5" value="5"></el-option>
              <el-option label="★4" value="4"></el-option>
            </el-select>
          </el-col>
          <el-col :span="3">
            <el-select v-model="elementVal" placeholder="元素">
              <el-option
                v-for="(item, index) in element"
                :key="index"
                :label="item"
                :value="item">
              </el-option>
            </el-select>
          </el-col>
          <el-col :span="3">
            <el-select v-model="typeVal" placeholder="武器">
              <el-option
                v-for="(item, index) in type"
                :key="index"
                :label="item"
                :value="item">
              </el-option>
            </el-select>
          </el-col>
          <el-col :span="12">
            <el-input
              placeholder="搜索..."
              v-model="searchVal">
              <i slot="suffix" class="el-input__icon el-icon-search"></i>
            </el-input>
          </el-col>
        </el-row>
        <el-row justify="space-between">
            <el-col :span="3" v-show="isDisplay(item)" v-for="item in dataList" :key="item">
                <ItemCell
                  :id="item.id"
                  :name="item.name"
                  :star="item.star"
                  :element="item.element"
                  :type="item.type"
                  :area="item.area"
                  :description="item.description"
                  source="/char_icon/char_icon_"
                  view="charDetail"/>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import ItemCell from '@/components/ItemCell'

export default {
  components: {
    ItemCell
  },
  beforeCreate () {
    setTimeout(() => {
      let path = '/getCharList'
      this.getData(path)
    }, 100)
  },
  data () {
    return {
      area: ['不限', '蒙德', '璃月', '稻妻', '须弥'],
      element: ['不限', '火', '水', '风', '雷', '草', '冰', '岩'],
      type: ['不限', '单手剑', '双手剑', '长柄武器', '法器', '弓'],
      dataList: [],
      areaVal: '',
      starVal: '',
      elementVal: '',
      typeVal: '',
      searchVal: ''
    }
  },
  methods: {
    getData (path) {
      this.axios.get(path).then((response) => {
        let data = []
        for (let i = 1; response.data[i]; i++) {
          data.push(response.data[i])
          data[i - 1].id = this.padID(data[i - 1].id)
        }
        this.dataList = data
      })
    },
    isDisplay (item) {
      let isArea = item.area === this.areaVal || this.areaVal === '不限' || !this.areaVal
      let isStar = item.star === this.starVal || this.starVal === '不限' || !this.starVal
      let isElement = item.element === this.elementVal || this.elementVal === '不限' || !this.elementVal
      let isType = item.type === this.typeVal || this.typeVal === '不限' || !this.typeVal
      let isSearched = item.name.search(this.searchVal) >= 0 || !this.searchVal
      return isArea && isStar && isElement && isType && isSearched
    },
    padID (id) {
      return '1' + (Array(4).join(0) + id).slice(-4)
    }
  }
}
</script>

<style>
#char-archive {
  width: 960px;
  padding-left: 12px;
  margin: auto;
}

#char-archive .el-row {
  width: 100%;
  margin-bottom: 12px;
}

#char-archive .el-col {
  margin-bottom: 12px;
}
</style>
