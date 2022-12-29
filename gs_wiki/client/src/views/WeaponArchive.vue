<template>
    <div id="weapon-archive">
        <h1>武器图鉴</h1>
        <el-row :gutter="10" justify="space-between">
          <el-col :span="3">
            <el-select v-model="starVal" placeholder="星级">
                <el-option label="不限" value="不限"></el-option>
                <el-option label="★5" value="5"></el-option>
                <el-option label="★4" value="4"></el-option>
                <el-option label="★3" value="3"></el-option>
                <el-option label="★2" value="2"></el-option>
                <el-option label="★1" value="1"></el-option>
            </el-select>
          </el-col>
          <el-col :span="3">
            <el-select v-model="typeVal" placeholder="类型">
                <el-option
                    v-for="(item, index) in type"
                    :key="index"
                    :label="item"
                    :value="item">
                </el-option>
            </el-select>
          </el-col>
          <el-col :span="18">
            <el-input
              placeholder="搜索..."
              v-model="searchVal">
              <i slot="suffix" class="el-input__icon el-icon-search"></i>
            </el-input>
          </el-col>
        </el-row>
        <el-row justify="space-around">
            <el-col :span="3" v-show="isDisplay(item)" v-for="item in dataList" :key="item">
                <ItemCell
                    :id="item.id"
                    :name="item.name"
                    :star="item.star"
                    :type="item.type"
                    :description="item.description"
                    source="/weapon_icon/weapon_icon_"
                    view='weaponDetail'/>
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
      let path = '/getWeaponList'
      this.getData(path)
    }, 100)
  },
  data () {
    return {
      type: ['不限', '单手剑', '双手剑', '长柄武器', '法器', '弓'],
      dataList: [],
      starVal: '',
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
          data = this.sortData(data)
        }
        this.dataList = data
      })
    },
    isDisplay (item) {
      let isStar = item.star === this.starVal || this.starVal === '不限' || !this.starVal
      let isType = item.type === this.typeVal || this.typeVal === '不限' || !this.typeVal
      let isSearched = item.name.search(this.searchVal) >= 0 || !this.searchVal
      return isStar && isType && isSearched && isSearched
    },
    padID (id) {
      return '2' + (Array(4).join(0) + id).slice(-4)
    },
    sortData (data) {
      if (data === null || data.length < 2) {
        return data
      }
      let n = data.length
      // 第 1 级排序: 类型
      for (let i = 0; i < n; i++) {
        let flag = true
        for (let j = 0; j < n - 1; j++) {
          if (this.typeToIndex(data[j].type) > this.typeToIndex(data[j + 1].type)) {
            flag = false
            let temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp
          }
        }
        if (flag) break
      }
      // 第 2 级排序: 星级
      for (let i = 0; i < n; i++) {
        let flag = true
        for (let j = 0; j < n - 1; j++) {
          if (data[j].star > data[j + 1].star) {
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
    typeToIndex (type) {
      let index = 0
      switch (type) {
        case '单手剑':
          index = 0
          break
        case '双手剑':
          index = 1
          break
        case '长柄武器':
          index = 2
          break
        case '法器':
          index = 3
          break
        case '弓':
          index = 4
          break
      }
      return index
    }
  }
}
</script>

<style>
#weapon-archive {
  width: 960px;
  padding-left: 12px;
  margin: auto;
}

#weapon-archive .el-row {
  width: 100%;
  margin-bottom: 12px;
}

#weapon-archive .el-col {
  margin-bottom: 12px;
}
</style>
