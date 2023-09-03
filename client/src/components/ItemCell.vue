<template>
  <div id="item-cell">
    <router-link :to="`/${category}/${id}`">
      <el-popover
        placement="top"
        trigger="hover"
        :width="180"
        :show-after="160"
        :hide-after="0"
        :disabled="isDiabled"
      >
        <!-- 简介浮框 -->
        <template #default>
          <div style="font-size: .8rem; color: #909399;">{{ description }}</div>
          <div style="margin-top: .25rem">
            <el-tag
              v-if="area"
              effect="plain"
              :disable-transitions="true"
              size="small"
            >{{ area }}
            </el-tag>
            <el-tag
              effect="plain"
              size="small"
              :disable-transitions="true"
            >{{ type }}
            </el-tag>
          </div>
        </template>
        <!-- 单元卡片 -->
        <template #reference>
          <el-card shadow="hover">
            <template #header>
              <div>
                <img
                  v-if="element"
                  class="item-badge"
                  :src="imgURL + '/ui_package/' + genImgName + '.png'"
                  loading="lazy"
                  alt="Item Badge"
                />
                <img
                  class="item-icon"
                  :style="genStyle"
                  :src="imgURL + genPath + id + '.png'"
                  loading="lazy"
                  alt="Item Icon"
                />
              </div>
            </template>
            <div>{{ name }}</div>
          </el-card>
        </template>
      </el-popover>
    </router-link>
  </div>
</template>

<script>
export default {
  props: {
    id: Number,
    name: String,
    star: String,
    element: String,
    type: String,
    area: String,
    description: String,
    category: String
  },
  data () {
    return {
      isDiabled: false,
      bgImage: [{
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
      }],
      imgURL: 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'
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
    genImgName () {
      const elementList = ['火', '水', '风', '雷', '草', '冰', '岩']
      return 'element_badge_' + (elementList.indexOf(this.element) + 1)
    },
    genPath () {
      return `/${this.category}_icon/${this.category}_icon_`
    },
    genStyle () {
      let index = this.star * 1 - 1
      if (isNaN(this.star * 1) || !this.bgImage[index]) return
      return `background-image: linear-gradient(${this.bgImage[index].top}, ${this.bgImage[index].bottom});`
    }
  },
  methods: {
    onResize () {
      if (window.innerWidth >= 1200) {
        this.isDiabled = false
      } else {
        this.isDiabled = true
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/scss/index.scss';

#item-cell {
  height: 100%;
  margin: .4rem;
  font-size: 1rem;
  a {
    text-decoration: none;
  }
}

.el-tag {
  margin-right: .25rem;
}

.el-card {
  border: {
    style: solid;
    width: 1px;
    color: $base-border;
    radius: .5rem;
  };
  box-shadow: 0 2px 2px rgba(0, 0, 0, .08);
  :deep(.el-card__header) {
    position: relative;
    width: 100%;
    aspect-ratio: 1/1;
    border-color: $base-border;
    .item-badge {
      position: absolute;
      left: 3px;
      top: 3px;
      width: 25%;
      aspect-ratio: 1/1;
      z-index: 5;
    }
    .item-icon {
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      aspect-ratio: 1/1;
      z-index: 4;
    }
  }
  :deep(.el-card__body) {
    width: 100%;
    padding: 0;
    color: $regular-text;
    div {
      padding: .25rem;
      line-height: 1.5;
      white-space: nowrap;
      text-align: center;
      text-overflow: ellipsis;
      overflow: hidden;
    }
  }
}

@media (min-width: $md-width) {
  .el-card {
    &:hover {
      transform: scale(1.1, 1.1);
    }
  }
}
</style>
