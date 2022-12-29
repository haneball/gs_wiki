<template>
    <div id="talent-attr">
        <el-divider></el-divider>
        <el-row type="flex" align="middle">
            <el-col :span="2">Lv.{{ level }}</el-col>
            <el-col :span="22">
                <el-slider
                    style="width: 180px"
                    v-if="attr[0].value.length > 1"
                    v-model="level"
                    :min="1"
                    :max="15"
                    :show-tooltip="false">
                </el-slider>
            </el-col>
        </el-row>
        <TabRow
            v-for="(item, index) in attr"
            :key="index"
            :label="item.label"
            :value="item.value[level - 1]"
            :is-dark="isDark(index)" />
    </div>
</template>

<script>
import TabRow from '@/components/TabRow'

export default {
  components: {
    TabRow
  },
  props: {
    attr: Array
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

<style>
#talent-attr {
  margin-top: 18px;
}

#talent-attr > .el-divider {
  margin: 0;
}

#talent-attr > .el-row {
  margin: 8px 0;
}

#talent-attr > .el-row > .el-col {
  margin: 0;
}
</style>
