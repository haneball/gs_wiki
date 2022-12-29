<template>
    <div id="story">
        <CollapseCard v-for="item in story" :key="item" :title="item.title" :text="item.text"/>
    </div>
</template>

<script>
import CollapseCard from '@/components/CollapseCard'

export default {
  components: {
    CollapseCard
  },
  props: {
    story: Array
  }
}
</script>

<style>
#story {
  width: 100%;
}
</style>
