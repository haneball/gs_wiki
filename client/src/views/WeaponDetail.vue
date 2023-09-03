<template>
  <div id="weapon-detail">
    <el-card shadow="never">
      <template #header>
        <div class="header-box">
            <div class="info-content">
              <!-- 武器名称 -->
              <div class="weapon-name">
                <span>{{ weaponObj.name }}</span>
                <el-tag
                  class="hidden-xs-only"
                  effect="dark"
                  :disable-transitions="true"
                  round
                >{{ weaponObj.type }}
                </el-tag>
              </div>
              <!-- 武器星级 -->
              <div class="star-rate">
                <img
                  v-if="!weaponObj.star"
                  style="width: 16px; height: 16px"
                  :src="imgURL + '/ui_package/star_icon.png'"
                  alt="★"
                />
                <img
                  v-for="n in (weaponObj.star * 1)"
                  :key="n"
                  style="width: 16px; height: 16px"
                  :src="imgURL + '/ui_package/star_icon.png'"
                  alt="★"
                />
              </div>
              <!-- 属性数值 -->
              <el-row class="attr-content">
                <el-col :xl="6" :lg="6" :md="6" :sm="6" :xs="12">
                  <div class="attr-label">基础攻击力</div>
                  <div>{{ weaponObj.baseATK[genIndex] }}</div>
                </el-col>
                <el-col v-if="weaponObj.subAttr" :xl="6" :lg="6" :md="6" :sm="6" :xs="12">
                  <div class="attr-label">{{ weaponObj.subAttr.label }}</div>
                  <div>{{ weaponObj.subAttr.value[genIndex] }}</div>
                </el-col>
              </el-row>
              <!-- 等级滑动条 -->
              <div class="level-slider">
                <span>Lv.{{ level }}</span>
                  <el-slider
                    style="width: 180px;"
                    v-model="level"
                    :step="10"
                    :min="genMinLv"
                    :max="genMaxLv"
                    :show-tooltip="false"
                  >
                  </el-slider>
              </div>
            </div>
            <!-- 武器图片 -->
            <div class="weapon-img">
              <img
                :style="genStyle"
                :src="imgURL + '/weapon_icon/weapon_icon_' + $route.params.id + '.png'"
                alt="Weapon Icon"
              />
            </div>
        </div>
      </template>
      <div>
        <!-- 精炼等阶选择 -->
        <div class="refine-select">
          <el-tag
            class="refine-tag"
            effect="plain"
            :disable-transitions="true"
          >精炼等阶
          </el-tag>
          <el-tooltip effect="dark" content="该武器无法精炼" placement="bottom" :disabled="tlpDisabled">
            <el-select v-model="refineRank" size="small" :disabled="sltDisabled">
              <el-option
                v-for="num in 5"
                :key="num"
                :label="num"
                :value="num"
                >
              </el-option>
            </el-select>
          </el-tooltip>
        </div>
        <!-- 武器效果 -->
        <div class="effect-content" v-if="weaponObj.effect">
          <strong>{{ weaponObj.effect.title }}</strong>
          <div v-if="this.weaponObj.effect" v-html="weaponObj.effect.text[refineRank - 1]"></div>
        </div>
        <div class="dscp-content">{{ weaponObj.description }}</div>
      </div>
    </el-card>
    <!-- 背景故事 -->
    <CollapseCard title="背景故事" :text="weaponObj.story"/>
  </div>
</template>

<script>
import CollapseCard from '../components/CollapseCard.vue'
import { queryWeapon } from '../api/index'

export default {
  components: {
    CollapseCard
  },
  data () {
    return {
      weaponObj: {
        name: '',
        star: '',
        type: '',
        story: '',
        description: '',
        baseATK: [],
        subAttr: {label: '', value: []},
        effect: {title: '', text: '', value: ''}
      },
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
      level: 90,
      maxRank: 5,
      refineRank: 1,
      tlpDisabled: true,
      sltDisabled: false,
      imgURL: 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'
    }
  },
  created () {
    const storage = JSON.parse(sessionStorage.getItem(`weaponDetail_${this.$route.params.id}`))
    if (storage) {  // 查询是否有缓存
      this.weaponObj = storage
    } else {
      this.getData(this.$route.params.id)
    }
  },
  mounted () {
    document.documentElement.scrollTop = 0
  },
  computed: {
    genIndex () {
      return this.level / 10 % 10 - 2
    },
    genMinLv () {
      return this.weaponObj.baseATK.length > 0 ? 20 : 0
    },
    genMaxLv () {
      return (this.weaponObj.baseATK.length + 1) * 10
    },
    genStyle () {
      let index = this.weaponObj.star * 1 - 1
      if (isNaN(this.weaponObj.star * 1) || !this.bgImage[index]) return
      return `background-image: linear-gradient(${this.bgImage[index].top}, ${this.bgImage[index].bottom});`
    }
  },
  methods: {
    getData (id) {
      queryWeapon(id).then(response => {
        this.weaponObj = response.data.data
        // 处理数据
        this.resolveData()
        // 缓存结果
        sessionStorage.setItem(`weaponDetail_${this.weaponObj.id}`, JSON.stringify(this.weaponObj))
      }).catch((error) => {
        console.log(error)
      })
    },
    resolveData () {
      this.level = this.maxLv = (this.weaponObj.baseATK.length + 1) * 10
      if (this.weaponObj.effect) {
        for (let i = 0; i < this.weaponObj.effect.text.length; i++) {
          this.weaponObj.effect.text[i] = this.toHtml(this.weaponObj.effect.text[i])
        }
      }
      if (!this.weaponObj.effect || this.weaponObj.effect.text.length <= 1) {
        this.tlpDisabled = false
        this.sltDisabled = true
      }
    },
    toHtml (str) {
      let color = str.match(/#[a-fA-F0-9]{6}|[a-fA-F]{3}/g)
      if (color) {
        str = str.replace(/<color=#([a-fA-F0-9]{6}|[a-fA-F]{3})>/g, `<span style="color: ${color[0]}">`)
        str = str.replace(/(<\/color>)/g, '</span>')
      }
      return str
    }
  }
}
</script>

<style lang="scss" scoped>
@import 'element-plus/theme-chalk/display.css';
@import '../assets/scss/index.scss';

#weapon-detail {
  max-width: 730px;
  margin: auto;
}

.header-box {
  display: flex;
  .info-content {
    min-width: 70%;
    flex-grow: 1;
  }
  .weapon-img > img {
    width: 100%;
    display: block;
    max-width: 168px;
    border-radius: .5rem;
    aspect-ratio: 1/1;
  }
}

.level-slider {
  display: flex;
  align-items: center;
  .el-slider {
    margin-left: 1rem;
  }
}

.weapon-name {
  display: flex;
  align-items: center;
  & > span:first-child {
    margin-right: .5rem;
    font: {
      size: 2rem;
      weight: bold;
    }
  }
}

.star-rate {
  margin: .25rem 0;
  img {
    padding-right: .2rem;
  }
}

.attr-content {
  margin: .8rem 0;
  font: {
    size: 1.5rem;
    weight: 555;
  };
  .attr-label {
    color: $regular-text;
    font: {
      size: 1rem;
      weight: 500;
    };
  }
}

.refine-select {
  display: flex;
  align-items: center;
  .refine-tag {
    border-radius: .5rem;
  }
}

.effect-content {
  margin: .8rem 0;
  color: $regular-text;
  .effect-value {
    color: $brand-color;
  }
  strong {
    margin-bottom: .25rem;
    color: $primary-text;
  }
}

.dscp-content {
  margin-top: .5rem;
  font-size: 1rem;
  color: $secondary-text;
}

.el-card {
  margin-bottom: 1rem;
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

.el-select {
  width: 4.5rem;
  margin-left: .5rem;
  box-sizing: border-box;
  :deep(.el-input__wrapper) {
    border-radius: .5rem;
  }
  :deep(.el-input__inner) {
    font-size: .8rem;
    text-align: center;
  }
}
</style>
