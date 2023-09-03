<template>
  <div id="talent-table" v-if="$store.state.charObj !== null">
    <!-- 战斗天赋 -->
    <el-card shadow="never" v-for="(item, index) in combatTalent" :key="index">
      <template #header>
        <div class="talent-header">
          <!-- 天赋图标 -->
          <img
            :src="imgURL + '/talent_icon/' + genImgName(index)"
            alt="Talent Icon"
          />
          <!-- 天赋名称 -->
          <strong>{{ item.title }}</strong>
          <!-- 显示属性开关 -->
          <div>
            <el-switch
              v-model="showAttr[index]"
              active-text="更多"
              active-color="#13ce66"
            >
            </el-switch>
          </div>
        </div>
      </template>
      <!-- 天赋文本 -->
      <div class="talent-text" v-html="item.text"></div>
      <!-- 天赋属性 -->
      <el-collapse-transition v-show="showAttr[index] == true">
        <TalentAttr v-show="showAttr[index] == true" :attr="item.attr" />
      </el-collapse-transition>
    </el-card>
    <!-- 固有天赋 -->
    <el-card shadow="never" v-for="(item, index) in passiveTalent" :key="index">
      <template #header>
        <div class="talent-header">
          <!-- 天赋图标 -->
          <img
            :src="imgURL + '/talent_icon/' + genImgName(index + combatTalent.length)"
            alt="Talent Icon"
          />
          <!-- 天赋名称 -->
          <strong>{{ item.title }}</strong>
        </div>
      </template>
      <!-- 天赋文本 -->
      <div class="talent-text" v-html="item.text"></div>
    </el-card>
  </div>
</template>

<script>
import TalentAttr from './TalentAttr.vue'

export default {
  components: {
    TalentAttr
  },
  data () {
    return {
      showAttr: [false, false, false],
      imgURL: 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'
    }
  },
  computed: {
    weaponType () {
      return this.$store.state.charObj.baseInfo.type
    },
    combatTalent () {
      return this.$store.state.charObj.combatTalent
    },
    passiveTalent () {
      return this.$store.state.charObj.passiveTalent
    }
  },
  methods: {
    genImgName (index) {
      if (index === 0) {
        const translateMap = {
          '单手剑': 'sword',
          '双手剑': 'claymore',
          '长柄武器': 'polearm',
          '法器': 'catalyst',
          '弓': 'bow',
        }
        let enType = translateMap[this.weaponType]
        return enType ? `attack_icon_${enType}.png` : 'attack_icon_sword.png'
      }
      return `talent_icon_${this.$route.params.id}_${index}.png`
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

#talent-table {
  width: 100%;
}

.el-card {
  border: none;
  border-radius: .5rem;
  &:not(:last-child) {
    margin-bottom: 1rem;
  }
  :deep(.el-card__header) {
    padding: .5rem 1rem;
    border-bottom: 2px solid $light-border;
  }
  :deep(.el-card__body) {
    padding: .5rem 1rem;
  }
}

.el-switch {
  :deep(.el-switch__label) {
    span {
      color: $regular-text;
      font-size: 1rem;
    }
  }
}

.talent-header {
  display: flex;
  align-items: center;
  & > div:last-child {
    flex-grow: 1;
    text-align: right;
  }
  img {
    width: 2.75rem;
    margin-right: .8rem;
    aspect-ratio: 1/1;
  }
}

.talent-text {
  margin-bottom: 1rem;
  white-space: pre-wrap;
  font-size: 1rem;
  color: $regular-text;
  line-height: 1.5;
  :deep(.font-bold) {
    font-weight: bold;
  }
  :deep(i) {
    color: $secondary-text;
  }
}
</style>
