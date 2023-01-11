<template>
  <div id="item-cell" @click="jmpToDetail">
    <el-popover
      placement="top"
      width="160"
      trigger="hover"
      open-delay="200">
      <div style="font-size: 12px; color: #909399;">{{ description }}</div>
      <div style="margin-top: 2px;">
        <el-tag v-if="area" effect="plain" size="mini">{{ area }}</el-tag>
        <el-tag effect="plain" size="mini">{{ type }}</el-tag>
      </div>
      <el-card :body-style="{ padding: '0px' }" shadow="hover" slot="reference">
        <div class="item-header">
          <img
            v-if="element"
            style="width: 24px; height: 24px"
            class="item-badge"
            :src="require('@/assets/img/ui_package/' + genImgName + '.png')"
            loading="lazy"
            alt="Item Badge"
            >
          <img
            style="width: 108px; height: 108px"
            class="item-icon"
            :class="genClassName"
            :src="require('@/assets/img' + source + id + '.png')"
            loading="lazy"
            alt="Item Icon"
            >
        </div>
        <div style="padding: 4px; text-align: center;">{{ name }}</div>
      </el-card>
    </el-popover>
  </div>
</template>

<script>
export default {
  props: {
    id: String,
    name: String,
    star: String,
    element: String,
    type: String,
    area: String,
    description: String,
    source: String,
    view: String
  },
  computed: {
    genImgName () {
      let imgName = ''
      switch (this.element) {
        case '火':
          imgName = 'element_badge_1'
          break
        case '水':
          imgName = 'element_badge_2'
          break
        case '风':
          imgName = 'element_badge_3'
          break
        case '雷':
          imgName = 'element_badge_4'
          break
        case '草':
          imgName = 'element_badge_5'
          break
        case '冰':
          imgName = 'element_badge_6'
          break
        case '岩':
          imgName = 'element_badge_7'
          break
      }
      return imgName
    },
    genClassName () {
      let className = ''
      switch (this.star) {
        case '5':
          className = 'orange-bg'
          break
        case '4':
          className = 'purple-bg'
          break
        case '3':
          className = 'blue-bg'
          break
        case '2':
          className = 'green-bg'
          break
        case '1':
          className = 'grey-bg'
          break
      }
      return className
    }
  },
  methods: {
    jmpToDetail () {
      this.$router.push({
        name: this.view,
        params: {id: this.id}
      })
    }
  }
}
</script>

<style>
#item-cell {
  width: 108px;
  font-size: 14px;
}

#item-cell > .el-card > .el-image {
  padding: 0;
}

#item-cell .item-header {
  position: relative;
  width: 108px;
  height: 108px;
}

#item-cell .item-badge {
  position: absolute;
  left: 2px;
  top: 2px;
  z-index: 5;
}

#item-cell .item-icon {
  position: absolute;
  left: 0;
  top: 0;
  z-index: 4;
}

#item-cell .orange-bg {
  background-image: url(../assets/img/ui_package/item_bg_5.png);
}

#item-cell .purple-bg {
  background-image: url(../assets/img/ui_package/item_bg_4.png);
}

#item-cell .blue-bg {
  background-image: url(../assets/img/ui_package/item_bg_3.png);
}

#item-cell .green-bg {
  background-image: url(../assets/img/ui_package/item_bg_2.png);
}

#item-cell .grey-bg {
  background-image: url(../assets/img/ui_package/item_bg_1.png);
}
</style>
