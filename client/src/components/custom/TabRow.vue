<template>
  <div id="tab-row" :style="genStyle">
    <div class="tab-row__text">{{ label }}</div>
    <div class="tab-row__text">{{ value }}</div>
  </div>
</template>

<script>
export default {
  props: {
    label: String,
    value: String,
    isDark: Boolean
  },
  computed: {
    genStyle () {
      return this.isDark ? 'background-color: #F0F2F5;' : ''
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

#tab-row {
  width: 100%;
  display: flex;
  align-items: center;
  padding: .5rem .8rem;
  margin: 0;
  border-radius: .5rem;
  font-size: 1rem;
  color: $regular-text;
  box-sizing: border-box;
  .tab-row__text {
    &:last-child {
      flex-grow: 1;
      text-align: right;
    }
  }
}
</style>
