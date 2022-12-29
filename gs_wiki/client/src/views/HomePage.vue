<template>
    <div id="home-page">
        <div>
            <el-image
                style="width:380px; height:100px"
                fit="contain"
                :src="require('@/assets/img/ui_package/gs_wiki.png')">
            </el-image>
        </div>
        <div>
            <el-autocomplete
                class="inline-input"
                v-model="inputVal"
                :fetch-suggestions="querySearchAsync"
                placeholder="搜索..."
                :trigger-on-focus="false"
                @input="getData"
                @select="jmpToDetail">
                <el-select v-model="select" slot="prepend" placeholder="请选择" @change="handleChange">
                    <el-option label="角色" value="char"></el-option>
                    <el-option label="武器" value="weapon"></el-option>
                </el-select>
                <i class="el-icon-search el-input__icon" slot="suffix"></i>
            </el-autocomplete>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      select: 'char',
      inputVal: '',
      dataList: [],
      queryPath: '/queryChar/kw=',
      timeout: null
    }
  },
  methods: {
    getData () {
      if (!this.inputVal) return
      this.axios.get(this.genPath()).then((response) => {
        let data = []
        for (let i = 1; response.data[i]; i++) {
          data.push(response.data[i])
        }
        this.dataList = data
      })
    },
    querySearchAsync (queryString, cb) {
      var item = this.dataList
      var results = queryString ? item.filter(this.createFilter(queryString)) : item
      clearTimeout(this.timeout)
      this.timeout = setTimeout(() => {
        cb(results)
      }, 300)
    },
    createFilter (queryString) {
      return (item) => {
        return (item.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0)
      }
    },
    handleChange () {
      if (this.select === 'char') {
        this.queryPath = '/queryChar/kw='
      }
      if (this.select === 'weapon') {
        this.queryPath = '/queryWeapon/kw='
      }
      this.dataList.length = 0
      this.inputVal = ''
    },
    genPath () {
      let kw = encodeURI(this.inputVal)
      return this.queryPath + kw
    },
    jmpToDetail (item) {
      this.$router.push({
        name: this.select + 'Detail',
        params: {id: this.padID(item.id)}
      })
    },
    padID (id) {
      return this.select === 'char' ? id + 10000 : id + 20000
    }
  }
}
</script>

<style>
#home-page {
  width: 988px;
  padding-top: 100px;
  margin: auto;
}

#home-page > div {
    width: 100%;
    text-align: center;
}

#home-page > div:last-child {
    margin: 24px 0;
}

#home-page .el-select .el-input {
    width: 80px;
}

#home-page .el-autocomplete {
    width: 600px;
}

#home-page .el-autocomplete .el-input-group__prepend {
    background-color: #fff;
}
</style>
