<template>
    <div id="voice-over">
        <el-card
            v-for="item in voice"
            :key="item"
            shadow="never">
            <div slot="header">
                <span>{{ item.title }}</span>
                <el-button style="float: right; padding: 3px 0" type="text" disabled>播放</el-button>
            </div>
            <div class="voice-text">{{ item.text }}</div>
        </el-card>
    </div>
</template>

<script>
export default {
  props: {
    voice: Array
  }
}
</script>

<style>
#voice-over > .el-card {
  margin-bottom: 12px;
}

#voice-over > .el-card > .el-card__header {
  padding: 16px 18px;
  font-weight: 666;
}

#voice-over > .el-card > .el-card__body {
  padding: 10px 18px;
}

#voice-over .voice-text {
  margin-bottom: 12px;
  white-space: pre-wrap;
  font-size: 14px;
}
</style>
