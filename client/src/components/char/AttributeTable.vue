<template>
  <div id="attr-table" v-if="$store.state.charObj !== null">
    <!-- 角色信息 -->
    <div class="info-box">
      <img
        class="char-illust"
        :src="imgURL + '/char_illust/char_illust_' + this.$route.params.id + '.png'"
        alt="Char Illust"
      />
      <div class="btn-group">
        <el-button link @click="hideInfo">
          <el-icon><Picture /></el-icon>
        </el-button>
        <el-button link @click="openIllust">
          <el-icon><ZoomIn /></el-icon>
        </el-button>
      </div>
      <transition name="el-fade-in">
        <div class="info-content" v-show="infoVisable">
          <div class="grid-content">
            <div v-for="(item, index) in genInfoList" :key="index">
              <el-tag
                effect="dark"
                :disable-transitions="true"
                round
              >{{ item.label }}
              </el-tag>
              <span class="info-value">{{ item.value }}</span>
            </div>
          </div>
          <p class="description">{{ baseInfo.description }}</p>
        </div>
      </transition>
    </div>
    <!-- 属性数值卡片 -->
    <el-card class="attr-card" shadow="never">
      <template #header>
        <div class="attr-card__header">
          <!-- 等级滑动条 -->
          <span>Lv. {{ level }}</span>
          <el-slider
            v-model="level"
            :step="10"
            :min="20"
            :max="90"
            :show-tooltip="false"
          >
          </el-slider>
          <!-- 演示弹窗按钮 -->
          <div>
            <el-button
              class="play-btn"
              type="primary"
              :disabled="baseInfo.bvid === null"
              size="small"
              @click="openDialog"
              round
            >演示
              <el-icon><Right /></el-icon>
            </el-button>
          </div>
        </div>
      </template>
      <!-- 属性数值 -->
      <div>
        <el-row class="attr-card__body">
          <el-col :span="6">
            <div>基础生命值</div>
            <div>{{ baseAttr.baseHP[genIndex] }}</div>
          </el-col>
          <el-col :span="6">
            <div>基础攻击力</div>
            <div>{{ baseAttr.baseATK[genIndex] }}</div>
          </el-col>
          <el-col :span="6">
            <div>基础防御力</div>
            <div>{{ baseAttr.baseDEF[genIndex] }}</div>
          </el-col>
          <el-col :span="6">
            <div>{{ baseAttr.ascendAttr.label }}</div>
            <div>{{ baseAttr.ascendAttr.value[genIndex] }}</div>
          </el-col>
        </el-row>
      </div>
    </el-card>
    <div class="illust-gallery" v-show="illustVisable">
      <el-button link @click="closeIllust">
        <el-icon><Close /></el-icon>
      </el-button>
      <img
        :style="illustStyle"
        :src="imgURL + '/char_illust/char_illust_' + this.$route.params.id + '.png'"
        alt="Char Illust"
      />
    </div>
    <!-- 演示弹窗 -->
    <el-dialog
      title="角色演示"
      width="50%"
      :model-value="dialogVisible"
      :append-to-body="false"
      :lock-scroll="false"
      @close="closeDialog"
    >
      <div class="video-content">
        <iframe
          :src="`//player.bilibili.com/player.html?bvid=${this.baseInfo.bvid}&page=1`"
          scrolling="no"
          border="0"
          frameborder="no"
          framespacing="0"
          allowfullscreen="true"
        >
        </iframe>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      level: 90,
      isMobile: false,
      infoVisable: true,
      illustVisable: false,
      dialogVisible: false,
      illustStyle: {
        width: '100%',
        height: '100%',
      },
      imgURL: 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com',
      videoURL: '//player.bilibili.com/player.html?bvid={bvid}&page=1'
    }
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResize)
  },
  computed: {
    baseInfo () {
      return this.$store.state.charObj.baseInfo
    },
    baseAttr () {
      return this.$store.state.charObj.baseAttr
    },
    genInfoList () {
      return [{
        label: '生日',
        value: this.baseInfo.brithday
      }, {
        label: '所属',
        value: this.baseInfo.affiliation
      }, {
        label: '神之眼',
        value: this.baseInfo.element
      }, {
        label: '命之座',
        value: this.baseInfo.constell
      }]
    },
    genIndex () {
      return this.level / 10 % 10 - 2
    }
  },
  methods: {
    onResize () {
      if (window.innerWidth > window.innerHeight) { // 是宽屏, 则 height 占满
        this.illustStyle.width = 'auto'
        this.illustStyle.height = '100%'
      } else {  // 不是宽屏, 则 width 占满
        this.illustStyle.width = '100%'
        this.illustStyle.height = 'auto'
      }
    },
    hideInfo () {
      this.infoVisable = !this.infoVisable
    },
    openIllust () {
      this.illustVisable = true
    },
    closeIllust () {
      this.illustVisable = false
    },
    openDialog () {
      if (window.innerWidth >= 992) { // PC 端在当前页面打开弹窗
        this.dialogVisible = true
      } else {  // 移动端打开新标签跳转
        window.open(`https://m.bilibili.com/video/${this.baseInfo.bvid}`)
      }
    },
    closeDialog () {
      this.dialogVisible = false
    }
  }
}
</script>

<style lang="scss" scoped>
@import 'element-plus/theme-chalk/display.css';
@import '../../assets/scss/index.scss';

#baseAttr-table {
  width: 100%;
}

.el-card {
  border: none;
  border-radius: .5rem;
  :deep(.el-card__header) {
    padding: 1.25rem;
    border-bottom: 2px solid $light-border;
  }
  :deep(.el-card__body) {
    padding: 1.25rem;
  }
}

.el-tag {
  font-size: .8rem;
}

.el-slider {
  width: 11rem;
  margin-left: 1rem;
}

.el-dialog {
  .video-content {
    position: relative;
    width: 100%;
    // height: 0;
    // padding-bottom: 75%;
    aspect-ratio: 16/9;
    iframe {
      position: absolute;
      width: 100%;
      height: 100%;
      left: 0;
      top: 0;
    }
  }
}

:deep(.el-dialog ) {
  border-radius: .5rem;
  overflow: hidden;
}

:deep(.el-dialog__body) {
  padding: 0;
}

.info-box {
  position: relative;
  padding: 0;
  margin-bottom: 1rem;
  border-radius: .5rem;
  background-color: #FFF;
  overflow: hidden;
  .char-illust {
    width: 100%;
    display: block;
    aspect-ratio: 3/2;
  }
  .btn-group {
    position: absolute;
    top: 1rem;
    right: 1rem;
    .el-button {
      padding: 0;
      color: $secondary-text;
      font-size: 1.5rem;
      &:last-child {
        margin-left: .5rem;
      }
    }
  }
  .info-content {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    padding: 1rem 0;
    border-top: 2px solid $light-border;
    background-color: rgba($color: #FFF, $alpha: .85);
    backdrop-filter: blur(6px);
    .description {
      margin: 1rem auto 0;
      color: $secondary-text;
      font-size: 1rem;
    }
  }
}

.grid-content {
  display: grid;
  grid-template-columns: repeat(2, .5fr);
  gap: .5rem 2rem;
  margin: 0 auto;
  div {
    display: flex;
    align-items: center;
    .info-value {
      flex-grow: 1;
      display: block;
      text-align: right;
      font-weight: 520;
    }
  }
}

.attr-card {
  :deep(.el-card__header) {
    padding: 1rem;
  }
}

.attr-card__header {
  display: flex;
  align-items: center;
  & > span {
    width: 3rem;
    display: block;
  }
  & > div:last-child {
    flex-grow: 1;
    text-align: right;
    .play-btn {
      padding: 1rem;
    }
  }
}

.attr-card__body {
  :deep(.el-col) {
    border-left: 2px solid $light-border;
    &:first-child {
      border-left: none;
    }
    & > div {
      text-align: center;
      color: $regular-text;
      &:last-child {
        color: $primary-text;
        font-weight: 555;
      }
    }
  }
}

.illust-gallery {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000;
  z-index: 9999;
  .el-button {
    position: fixed;
    top: 1rem;
    right: 1rem;
    color: #FFF;
    font-size: 2rem;
    background-color: transparent;
    z-index: 10000;
  }
}

@media (min-width: $xs-width) {
  .info-box {
    padding: 1rem 1rem 4rem;
  }

  .grid-content, .description {
    width: 90%;
  }

  .info-value {
    font-size: 1rem;
  }

  .attr-card__body {
    :deep(.el-col > div) {
      font-size: .8rem;
      &:last-child {
        font-size: 1.25rem;
      }
    }
  }
}

@media (min-width: $sm-width) {
  .info-box {
    padding: 1rem;
  }

  .grid-content, .description {
    width: 75%;
  }

  .info-value {
    font-size: 1.25rem;
  }
}

@media (min-width: $md-width) {
  .grid-content, .description {
    width: 60%;
  }

  .attr-card__body {
    :deep(.el-col > div) {
      font-size: 1rem;
      &:last-child {
        font-size: 1.5rem;
      }
    }
  }
}
</style>
