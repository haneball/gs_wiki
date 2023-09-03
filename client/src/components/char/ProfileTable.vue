<template>
  <div id="profile-table" v-if="$store.state.charObj !== null">
    <!-- 单选按钮组 -->
    <div class="btn-group">
      <el-button
        :type="btnVal ? 'primary' : ''"
        :plain="!btnVal"
        @click="handleClick(0)"
        round
      >
        故事
      </el-button>
      <el-button
        :type="!btnVal ? 'primary' : ''"
        :plain="btnVal"
        @click="handleClick(1)"
        round
      >
        语音
      </el-button>
    </div>
    <!-- 角色故事 -->
    <BackgroundStory v-show="btnVal" :story="story" />
    <!-- 角色语音 -->
    <VoiceOver v-show="!btnVal" :voice="voice" />
  </div>
</template>

<script>
import BackgroundStory from './BackgroundStory.vue'
import VoiceOver from './VoiceOver.vue'

export default {
  components: {
    BackgroundStory,
    VoiceOver
  },
  data () {
    return {
      btnVal: true
    }
  },
  computed: {
    story () {
      return this.$store.state.charObj.story
    },
    voice () {
      return this.$store.state.charObj.voice
    }
  },
  methods: {
    handleClick (index) {
      if ((index === 0 && this.btnVal) || (index === 1 && !this.btnVal)) return
      this.btnVal = !this.btnVal
    }
  }
}
</script>

<style lang="scss" scoped>
#profile-table {
  width: 100%;
}

.btn-group {
  margin-bottom: 12px;
  text-align: center;
  .el-button {
    width: 160px;
    padding: 1.2rem;
  }
}
</style>
