<template>
  <div id="home-page">
    <el-row type="flex">
      <el-col class="main-col" :xl="14" :lg="14" :md="12" :sm="12" :sx="24">
        <el-carousel>
          <el-carousel-item v-for="(item, index) in dataList" :key="index">
            <img
              :src="imgURL + '/gacha_banner/' + item.img + '.jpg'"
              @click="jmpToOuter(item.link)"
            />
          </el-carousel-item>
        </el-carousel>
        <div class="btn-group">
          <h2>快捷入口</h2>
          <div>
            <el-button
              v-for="(item, index) in btnAttr"
              :key="index"
              type="primary"
              size="large"
              :icon="item.icon"
              round
              @click="jmpToView(item.path)"
            >
              {{ item.text }}
            </el-button>
          </div>
        </div>
        <ComingBrith />
      </el-col>
      <el-col class="aside-col" :xl="10" :lg="10" :md="12" :sm="12" :sx="24">
        <VersionCd class="hidden-xs-only" />
        <TodayMaterial />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import TodayMaterial from '../components/home/TodayMaterial.vue'
import ComingBrith from '../components/home/CommingBrith.vue'
import VersionCd from '../components/home/VersionCd.vue'
import { getGachaPool } from '../api/index'

export default {
  components: {
    TodayMaterial,
    ComingBrith,
    VersionCd
  },
  data () {
    return {
      dataList: [],
      btnAttr: [{
        icon: 'User',
        path: '/char',
        text: '角色'
      }, {
        icon: 'KnifeFork',
        path: '/weapon',
        text: '武器'
      }, {
        icon: 'Timer',
        path: '/timer',
        text: '祈愿计时'
      }],
      imgURL: 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com',
      jmpURL: 'https://www.miyoushe.com/ys/article/'
    }
  },
  created () {
    this.getData()
  },
  methods: {
    getData () {
      getGachaPool().then(response => {
        if (response.data.status === 200) {
          this.dataList.length = 0
          response.data.data.forEach(element => {
            this.dataList.push(element)
          })
        }
      }).catch((error) => {
        console.log(error)
      })
    },
    jmpToView (path) {
      this.$router.push(path)
    },
    jmpToOuter (n) {
      window.open(this.jmpURL + n)
    }
  }
}
</script>

<style lang="scss" scoped>
@import 'element-plus/theme-chalk/display.css';
@import '../assets/scss/index.scss';

@mixin flex-col {
  display: flex;
  flex-direction: column;
}

#home-page {
  width: 100%;
}

.el-row {
  flex-wrap: wrap;
}

.el-carousel {
  width: 100%;
  height: auto;
  margin-bottom: 1rem;
  aspect-ratio: 69/32;
  border-radius: .5rem;
  :deep(.el-carousel__container) {
    width: 100%;
    height: 100%;
  }
  :deep(.el-carousel__item) {
    height: auto;
    aspect-ratio: 69/32;
  }
  img {
    width: 100%;
    aspect-ratio: 69/32;
    border-radius: .5rem;
  }
}

.btn-group {
  & > div:first-child {
    margin: 1rem 0;
  }
  h2 {
    margin: 1rem 0 0 1rem;
    font: {
      size: 1.25rem;
      weight: bold;
    }
  }
  .el-button.is-round {
    margin-top: 1rem;
  }
}

@media (min-width: $sm-width) {
  .main-col, .aside-col {
    @include flex-col;
  }

  .main-col {
    padding-right: 1rem;
  }
}
</style>
