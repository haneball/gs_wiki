<template>
  <div id="talent-attr">
    <!-- 分割线 -->
    <el-divider></el-divider>
    <!-- 等级滑动条 -->
    <div class="slider-box">
      <span>Lv. {{ level }}</span>
      <el-slider
        v-if="attr[0].value.length > 1"
        v-model="level"
        :min="1"
        :max="15"
        :show-tooltip="false"
      >
      </el-slider>
    </div>
    <!-- 天赋数值 -->
    <TabRow
      v-for="(item, index) in attr"
      :key="index"
      :label="item.label"
      :value="item.value[level - 1]"
      :is-dark="isDark(index)"
    />
  </div>
</template>

<script>
import TabRow from '../custom/TabRow.vue'

export default {
  components: {
    TabRow
  },
  props: {
    attr: {
      type: Array,
      default () {
        return [{label: '', value: ''}]
      }
    }
  },
  data () {
    return {
      level: 1
    }
  },
  methods: {
    isDark (index) {
      return !(index % 2)
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

#talent-attr {
  margin-top: 1rem;
}

.el-slider {
  width: 11rem;
  margin-left: 1rem;
}

.slider-box {
  display: flex;
  align-items: center;
  margin: .5rem 0;
  font-size: 1rem;
  color: $primary-text;
  span {
    width: 3rem;
    display: block;
  }
}

.el-divider {
  margin: 0;
}
</style>
