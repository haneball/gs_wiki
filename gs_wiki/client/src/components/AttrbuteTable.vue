<template>
    <div id="attrbute-table">
        <el-card shadow="never">
            <div slot="header">
                <el-row type="flex" align="middle">
                    <el-col :span="3">等级 {{ level }}</el-col>
                    <el-col :span="21">
                        <el-slider
                            style="width: 180px"
                            v-model="level"
                            :step="10"
                            :min="20"
                            :max="90"
                            :show-tooltip="false">
                        </el-slider>
                    </el-col>
                </el-row>
            </div>
            <TabRow label="基础生命值" :value="attrbute.baseHP[genIndex]" :is-dark="true" />
            <TabRow label="基础攻击力" :value="attrbute.baseATK[genIndex]" />
            <TabRow label="基础防御力" :value="attrbute.baseDEF[genIndex]" :is-dark="true" />
            <TabRow :label="attrbute.ascendAttr.label" :value="attrbute.ascendAttr.value[genIndex]" />
        </el-card>
        <el-card shadow="never">
            <div slot="header">
              <el-row type="flex" align="middle">
                <el-col :span="12">
                  <span>基本信息</span>
                </el-col>
                <el-col :span="12" style="text-align: right">
                  <el-button v-if="bvid" type="primary" @click="dialogVisible = true" size="mini" round>
                    演示
                    <i class="el-icon-right"></i>
                  </el-button>
                </el-col>
              </el-row>
            </div>
            <TabRow label="生日" :value="baseInfo.brithday" :is-dark="true" />
            <TabRow label="所属" :value="baseInfo.affiliation" />
            <TabRow label="神之眼" :value="baseInfo.element" :is-dark="true" />
            <TabRow label="命之座" :value="baseInfo.constell" />
            <div class="dscp-content">{{ baseInfo.description }}</div>
        </el-card>
        <el-dialog
          width="40%"
          title="角色演示"
          :visible.sync="dialogVisible"
          append-to-body="true">
          <div class="video-contain">
            <iframe
              :src="genVideoSrc"
              scrolling="no"
              border="0"
              frameborder="no"
              framespacing="0"
              allowfullscreen="true">
            </iframe>
          </div>
        </el-dialog>
    </div>
</template>

<script>
import TabRow from '@/components/TabRow'

export default {
  components: {
    TabRow
  },
  props: {
    attrbute: Object,
    baseInfo: Object,
    bvid: String
  },
  data () {
    return {
      level: 90,
      dialogVisible: false,
      vdsrc: '//player.bilibili.com/player.html?bvid={bvid}&page=1'
    }
  },
  computed: {
    genIndex () {
      return this.level / 10 % 10 - 2
    },
    genVideoSrc () {
      return this.vdsrc.replace('{bvid}', this.bvid)
    }
  }
}
</script>

<style>
#attrbute-table {
  width: 100%;
}

#attrbute-table .el-card {
  margin-bottom: 12px;
}

#attrbute-table .el-card .el-card__header {
  padding: 16px 18px;
  font-weight: 666;
}

#attrbute-table .el-card .el-card__body {
  padding: 18px;
}

#attrbute-table .el-card .el-row {
    margin: 0;
}

#attrbute-table .el-card .el-row .el-col {
    margin: 0;
}

#attrbute-table .dscp-content {
  margin: 6px 0 0 14px;
  font-size: 13px;
  color: #909399;
}

.el-dialog .video-contain {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 75%;;
}

.el-dialog .video-contain iframe {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
}
</style>
