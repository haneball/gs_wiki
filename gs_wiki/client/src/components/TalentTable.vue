<template>
    <div id="talent-table">
        <el-card shadow="never" v-for="(item, index) in combatTalent" :key="index">
            <div slot="header">
                <el-row type="flex" align="middle">
                    <el-col :span="2">
                        <el-image
                            style="width: 44px; height: 44px"
                            fit="contain"
                            :src="require('@/assets/img/talent_icon/' + genImgName(index))">
                        </el-image>
                    </el-col>
                    <el-col class="talent-title" :span="10">{{ item.title }}</el-col>
                    <el-col :span="12" style="text-align: right">
                        <el-switch
                            v-model="showAttr[index]"
                            active-text="显示属性"
                            active-color="#13ce66">
                        </el-switch>
                    </el-col>
                </el-row>
            </div>
            <div class="talent-text" v-html="item.text"></div>
            <el-collapse-transition v-show="showAttr[index] == true">
                <TalentAttr v-show="showAttr[index] == true" :attr="item.attr" />
            </el-collapse-transition>
        </el-card>
        <el-card shadow="never" v-for="(item, index) in passiveTalent" :key="index">
            <div slot="header">
                <el-row type="flex" align="middle">
                    <el-col :span="2">
                        <el-image
                            style="width: 44px; height: 44px"
                            fit="contain"
                            :src="require('@/assets/img/talent_icon/' + genImgName(index + combatTalent.length))">
                        </el-image>
                    </el-col>
                    <el-col class="talent-title" :span="22">{{ item.title }}</el-col>
                </el-row>
            </div>
            <div class="talent-text" v-html="item.text"></div>
        </el-card>
    </div>
</template>

<script>
import TalentAttr from '@/components/TalentAttr'

export default {
  components: {
    TalentAttr
  },
  props: {
    weaponType: String,
    combatTalent: Array,
    passiveTalent: Array
  },
  data () {
    return {
      showAttr: [false, false, false]
    }
  },
  methods: {
    genImgName (index) {
      let imgName = ''
      if (index === 0) {
        switch (this.weaponType) {
          case '单手剑':
            imgName = 'attack_icon_sword.png'
            break
          case '双手剑':
            imgName = 'attack_icon_claymore.png'
            break
          case '长柄武器':
            imgName = 'attack_icon_polearm.png'
            break
          case '法器':
            imgName = 'attack_icon_catalyst.png'
            break
          case '弓':
            imgName = 'attack_icon_bow.png'
            break
          default:
            imgName = 'attack_icon_sword.png'
        }
        return imgName
      }
      return 'talent_icon_' + this.$route.params.id + '_' + index + '.png'
    }
  }
}
</script>

<style>
#talent-table {
  width: 100%;
}

#talent-table > .el-card {
  margin-bottom: 12px;
}

#talent-table > .el-card > .el-card__header {
  padding: 6px 18px;
}

#talent-table > .el-card > .el-card__body {
  padding: 10px 18px;
}

#talent-table > .el-card > .el-card__header .el-row {
  margin-bottom: 0;
}

#talent-table > .el-card > .el-card__header .el-row .el-col {
  margin: 4px 0 0 0;
}

#talent-table .talent-title {
  font-size: 16px;
  font-weight: 666;
}

#talent-table .talent-text {
  margin-bottom: 12px;
  white-space: pre-wrap;
  font-size: 14px;
}

#talent-table .talent-text > .font-bold {
  font-weight: 555;
}
</style>
