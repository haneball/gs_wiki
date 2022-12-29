<template>
    <div id="profile-table">
        <div class="btn-group">
            <el-button
                :style="{background: [btnVal ? '#409EFF' : '#fff'], color: [btnVal ? '#fff' : '#606266']}"
                round
                @click="handleClick(0)">故事
            </el-button>
            <el-button
                :style="{background: [!btnVal ? '#409EFF' : '#fff'], color: [!btnVal ? '#fff' : '#606266']}"
                round
                @click="handleClick(1)">语音
            </el-button>
        </div>
        <Story v-show="btnVal" :story="story" />
        <VoiceOver v-show="!btnVal" :voice="voice" />
    </div>
</template>

<script>
import Story from '@/components/Story'
import VoiceOver from '@/components/VoiceOver'

export default {
  components: {
    Story,
    VoiceOver
  },
  props: {
    story: Array,
    voice: Array
  },
  data () {
    return {
      btnVal: true
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

<style>
#profile-table {
  width: 100%;
}

#profile-table .btn-group {
  margin-bottom: 12px;
  text-align: center;
}

#profile-table .btn-group > .el-button {
  width: 154px;
}
</style>
