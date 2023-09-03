<template>
  <div id="char-detail">
    <el-row type="flex">
      <el-col :offset="offset" :xl="8 - offset" :lg="8 - offset" :md="7" :sm="24" :xs="24">
        <div class="name-card">
          <div class="color-label" :style="genStyle"></div>
          <div class="char-icon">
            <img
              :src="imgURL + '/char_icon/char_icon_' + this.$route.params.id + '.png'"
              alt="Avatar Icon"
            />
          </div>
          <div>
            <h2>{{ hasOwn('name') }}</h2>
            <div class="char-tag">{{ hasOwn('title') }}</div>
            <div class="star-rate">
              <img
                v-for="n in (hasOwn('star') * 1)"
                :key="n"
                :src="imgURL + '/ui_package/star_icon.png'"
                alt="★"
              />
            </div>
          </div>
        </div>
        <!-- 页面子菜单 -->
        <div class="sub-menu">
          <router-link
            v-for="(item, index) in menuItem"
            :key="index"
            :to="item.path"
            replace
          >{{ item.title }}
          </router-link>
        </div>
      </el-col>
      <el-col :xl="16 - offset" :lg="16 - offset" :md="17" :sm="24" :xs="24">
        <router-view></router-view>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { queryChar } from '../api/index'

export default {
  data () {
    return {
      charObj: {},
      offset: 0,
      tab: 0,
      color: ['#C47DFF', '#FFCC68'],
      menuItem: [{
        path: 'attribute',
        title: '属性'
      }, {
        path: 'talent',
        title: '天赋'
      }, {
        path: 'constellation',
        title: '命之座'
      }, {
        path: 'profile',
        title: '资料'
      }],
      subMenuItem: ['属性', '天赋', '命之座', '资料'],
      imgURL: 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'
    }
  },
  beforeCreate () {
    // 清空 state
    this.$store.commit('setCharObj', null)
  },
  created () {
    const storage = JSON.parse(sessionStorage.getItem(`charDetail_${this.$route.params.id}`))
    if (storage) {  // 查询是否有缓存
      this.charObj = storage
      this.$store.commit('setCharObj', storage)
    } else {
      this.getData(this.$route.params.id)
    }
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize)
    document.documentElement.scrollTop = 0
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResize)
  },
  computed: {
    genStyle () {
      return 'background-color: ' + this.color[this.hasOwn('star') - 4]
    }
  },
  methods: {
    getData (id) {
      queryChar(id).then(response => {
        this.charObj = response.data.data
        // 处理数据
        this.resolveData()
        // 提交到 VueX
        this.$store.commit('setCharObj', response.data.data)
        // 缓存结果
        sessionStorage.setItem(`charDetail_${this.charObj.baseInfo.id}`, JSON.stringify(this.charObj))
      }).catch((error) => {
        console.log(error)
      })
    },
    resolveData () {
      for (let i = 0; i < this.charObj.combatTalent.length; i++) {
        this.charObj.combatTalent[i].text = this.toHtml(this.charObj.combatTalent[i].text)
      }
      for (let i = 0; i < this.charObj.passiveTalent.length; i++) {
        this.charObj.passiveTalent[i].text = this.toHtml(this.charObj.passiveTalent[i].text)
      }
      for (let i = 0; i < this.charObj.constellation.length; i++) {
        this.charObj.constellation[i].text = this.toHtml(this.charObj.constellation[i].text)
      }
    },
    onResize () {
      if (window.innerWidth >= 1200) {
        this.offset = 2
      } else {
        this.offset = 0
      }
    },
    handleClick (index) {
      this.tab = index
    },
    hasOwn (key) {
      return this.charObj.baseInfo ? this.charObj.baseInfo[key] : ''
    },
    toHtml (str) {
      str = str.replace(/<color=/g, '<span class="font-bold" style="color: ')
      str = str.replace(/(?<=#[a-fA-F0-9]{6}|[a-fA-F]{3})>/g, '">')
      str = str.replace(/<\/color>/g, '</span>')
      return str
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/scss/index.scss';

.el-row {
  flex-wrap: wrap;
}

.el-card {
  border-color: $base-border;
  :deep(.el-card__body) {
    padding: 0;
  }
}

.name-card {
  display: flex;
  padding: 0;
  margin-bottom: 1rem;
  border-radius: .5rem;
  background-color: #FFF;
  overflow: hidden;
  .color-label {
    width: .5rem;
    height: auto;
  }
  .char-icon {
    width: 4.75rem;
    height: 4.75rem;
    margin: .8rem;
    border-radius: 50%;
    background-color: #CF9E7D;
    overflow: hidden;
    img {
      width: 4.75rem;
      height: 4.75rem;
      transform: scale(1.25, 1.25);
    }
  }
  h2 {
    margin: .8rem 0 0 0;
  }
  .char-tag {
    margin-bottom: .15rem;
    font-size: 1rem;
    color: $secondary-text;
  }
  .star-rate > img {
    width: 1rem;
    height: 1rem;
    padding-right: .125rem;
  }
}

.sub-menu {
  display: flex;
  padding: .25rem;
  margin: 1rem 0;
  border-radius: .5rem;
  background-color: #FFF;
  overflow: hidden;
  a {
    display: block;
    margin: .25rem .25rem;
    padding: .75rem;
    color: $primary-text;
    text-decoration: none;
    border-radius: .5rem;
    background-color: transparent;
    &:hover {
      color: $brand-color;
      background-color: #F5F7FA;
    }
    &.router-link-active {
      color: $brand-color;
      font-weight: bold;
      background-color: #ECF5FF;
    }
  }
}

@media (min-width: $md-width) {
  .sub-menu {
    flex-direction: column;
  }
}

@media (min-width: $md-width) {
  .el-row {
    .el-col:first-child {
      padding-right: 1rem;
    }
  }
}
</style>
