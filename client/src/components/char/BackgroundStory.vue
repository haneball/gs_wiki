<template>
  <div id="story">
    <CollapseCard
      v-for="item in story"
      :key="item"
      :title="item.title"
      :text="item.text"
    />
  </div>
</template>

<script>
import CollapseCard from '../../components/CollapseCard.vue'

export default {
  components: {
    CollapseCard
  },
  props: {
    story: {
      type: Array,
      default () {
        return [{title: '', text: ''}]
      }
    }
  }
}
</script>

<style lang="scss" scoped>
#story {
  width: 100%;
}
</style>
