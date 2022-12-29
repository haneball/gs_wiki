<template>
    <div id="char-detail">
        <el-row :gutter="18">
            <el-col :span="18">
                <el-collapse class="char-illust">
                    <el-collapse-item title="查看立绘">
                        <el-image
                            style="width: 600px; height: 400px"
                            fit="contain"
                            :src="require('@/assets/img/char_illust/char_illust_' + this.$route.params.id + '.png')">
                        </el-image>
                    </el-collapse-item>
                </el-collapse>
                <AttrbuteTable
                    v-show="table == '1'"
                    :attrbute="charObj.baseAttr"
                    :base-info="charObj.baseInfo"
                    :bvid="charObj.baseInfo.bvid" />
                <TalentTable
                    v-show="table == '2'"
                    :weapon-type="charObj.baseInfo.type"
                    :combat-talent="charObj.combatTalent"
                    :passive-talent="charObj.passiveTalent" />
                <ConstellationTable
                    v-show="table == '3'"
                    :constellation="charObj.constellation" />
                <ProfileTable
                    v-show="table == '4'"
                    :story="charObj.story"
                    :voice="charObj.voice" />
            </el-col>
            <el-col :span="6">
                <el-card class="char-card" :body-style="{ padding: '0px' }" shadow="never">
                    <el-row justify="space-around">
                        <el-col :span="8">
                            <el-image
                                class="avatar-icon"
                                style="width: 64px; height: 64px"
                                fit="contain"
                                :src="require('@/assets/img/char_round_icon/char_round_icon_' + this.$route.params.id + '.png')">
                            </el-image>
                        </el-col>
                        <el-col :span="16">
                            <div class="char-name">{{ charObj.baseInfo.name }}</div>
                            <div class="char-tag">{{ charObj.baseInfo.title }}</div>
                            <div class="star-rare">
                                <el-image
                                    v-for="n in (charObj.baseInfo.star * 1)"
                                    :key="n"
                                    style="width: 14px; height: 14px"
                                    fit="contain"
                                    :src="require('@/assets/img/ui_package/star_icon.png')">
                                </el-image>
                            </div>
                        </el-col>
                    </el-row>
                </el-card>
                <el-card :body-style="{ padding: '0px' }" shadow="never">
                    <el-menu
                        class="sub-menu"
                        default-active="1"
                        @select="handleSelect">
                        <el-menu-item index="1">
                            <span slot="title">属性</span>
                        </el-menu-item>
                        <el-menu-item index="2">
                            <span slot="title">天赋</span>
                        </el-menu-item>
                        <el-menu-item index="3">
                            <span slot="title">命之座</span>
                        </el-menu-item>
                        <el-menu-item index="4">
                            <span slot="title">资料</span>
                        </el-menu-item>
                    </el-menu>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import AttrbuteTable from '@/components/AttrbuteTable'
import TalentTable from '@/components/TalentTable'
import ConstellationTable from '@/components/ConstellationTable'
import ProfileTable from '@/components/ProfileTable'

export default {
  components: {
    AttrbuteTable,
    TalentTable,
    ConstellationTable,
    ProfileTable
  },
  beforeCreate () {
    setTimeout(() => {
      let path = '/getCharDetail/id=' + this.$route.params.id
      this.getData(path)
    }, 100)
  },
  data () {
    return {
      charObj: {
        baseInfo: {
          id: '',
          name: '',
          title: '',
          star: '',
          element: '',
          type: '',
          area: '',
          brithday: '',
          affiliation: '',
          constell: '',
          description: '',
          bvid: ''
        },
        baseAttr: {
          baseHP: [],
          baseATK: [],
          baseDEF: [],
          ascendAttr: {
            label: '',
            value: []
          }
        },
        combatTalent: [{
          title: '',
          text: '',
          attr: [{
            label: '',
            value: ''
          }]
        }],
        passiveTalent: [{
          title: '',
          text: ''
        }],
        constellation: [{
          title: '',
          text: ''
        }],
        story: [{
          title: '',
          text: ''
        }],
        voice: [{
          title: '',
          text: ''
        }]
      },
      table: '1'
    }
  },
  methods: {
    getData (path) {
      this.axios.get(path).then((response) => {
        this.charObj = response.data
        for (let i = 0; i < this.charObj.combatTalent.length; i++) {
          this.charObj.combatTalent[i].text = this.toHtml(this.charObj.combatTalent[i].text)
        }
        for (let i = 0; i < this.charObj.passiveTalent.length; i++) {
          this.charObj.passiveTalent[i].text = this.toHtml(this.charObj.passiveTalent[i].text)
        }
        for (let i = 0; i < this.charObj.constellation.length; i++) {
          this.charObj.constellation[i].text = this.toHtml(this.charObj.constellation[i].text)
        }
      })
    },
    handleSelect (index) {
      this.table = index
    },
    toHtml (str) {
      str = str.replace(/<color=/g, '<span class="font-bold" style="color: ')
      str = str.replace(/>/g, '">')
      str = str.replace(/<\/color">/g, '</span>')
      str = str.replace(/i">/g, 'i>')
      return str
    }
  }
}
</script>

<style>
#char-detail {
  width: 988px;
  padding-top: 24.8px;
  margin: auto;
}

#char-detail .sub-menu {
  height: 224px;
}

#char-detail .sub-menu:not(.el-menu--collapse) {
  width: 100%;
  height: 224px;
  border: none;
}

#char-detail .avatar-icon {
  margin: 12px;
}

#char-detail .char-card {
  height: 88px;
  margin-bottom: 12px;
}

#char-detail .char-name {
  margin: 12px 0 0 12px;
  font-size: 16px;
  font-weight: 600;
}

#char-detail .char-tag {
  margin: 2px 0 0 12px;
  font-size: 14px;
  color: #909399;
}

#char-detail .star-rare {
  margin: 2px 0 0 12px;
}

#char-detail .star-rare > .el-image{
  margin-right: 2px;
}

#char-detail .char-illust {
  padding: 4px 20px;
  margin-bottom: 12px;
  border: 1px solid #EBEEF5;
  border-radius: 4px;
}

#char-detail .char-illust > .el-collapse-item {
  text-align: center;
}

#char-detail .char-illust .el-collapse-item__header {
  border: none;
  font-size: 14px;
}

#char-detail .char-illust .el-collapse-item__wrap {
  border: none;
}
</style>
