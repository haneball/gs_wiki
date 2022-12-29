<template>
    <div id="weapon-detail">
      <el-card shadow="never">
        <div slot="header">
          <el-row>
            <el-col :span="18">
              <div class="weapon-name">{{ weaponObj.name }}</div>
              <div>
                <el-image
                  v-for="n in (weaponObj.star * 1)"
                  :key="n"
                  style="width: 14px; height: 14px"
                  fit="contain"
                  :src="require('@/assets/img/ui_package/star_icon.png')">
                </el-image>
              </div>
              <div class="attr-content">
                <div v-if="weaponObj.subAttr">
                  <div class="attr-label">{{ weaponObj.subAttr.label }}</div>
                  <div>{{ weaponObj.subAttr.value[genIndex] }}</div>
                </div>
                <div>
                  <div class="attr-label">基础攻击力</div>
                  <div>{{ weaponObj.baseATK[genIndex] }}</div>
                </div>
              </div>
              <el-row type="flex" align="middle">
                <el-col :span="3"><span>Lv.{{ level }}</span></el-col>
                <el-col :span="21">
                  <el-slider
                    style="width: 180px;"
                    v-model="level"
                    :step="10"
                    :min="20"
                    :max="maxLv"
                    :show-tooltip="false">
                  </el-slider>
                </el-col>
              </el-row>
            </el-col>
            <el-col style="text-align: right;" :span="6">
              <el-image
                style="width: 168px; height: 168px"
                fit="contain"
                :class="genClassName"
                :src="require('@/assets/img/weapon_icon/weapon_icon_' + $route.params.id + '.png')">
              </el-image>
            </el-col>
          </el-row>
        </div>
        <div>
          <el-tag effect="plain" size="medium">精炼等阶</el-tag>
          <el-select v-model="refineRank" size="mini" :disabled="sltState">
              <el-option v-for="num in 5" :key="num" :label="num" :value="num"></el-option>
          </el-select>
          <div class="effect-content" v-if="weaponObj.effect">
              <div>{{ weaponObj.effect.title }}</div>
              <div v-if="this.weaponObj.effect" v-html="weaponObj.effect.text[refineRank - 1]"></div>
          </div>
          <div class="dscp-content">{{ weaponObj.description }}</div>
        </div>
      </el-card>
      <CollapseCard title="背景故事" :text="weaponObj.story"/>
    </div>
</template>

<script>
import CollapseCard from '@/components/CollapseCard'

export default {
  components: {
    CollapseCard
  },
  beforeCreate () {
    setTimeout(() => {
      let path = '/getWeaponDetail/id=' + this.$route.params.id
      this.getData(path)
    }, 100)
  },
  data () {
    return {
      weaponObj: {
        name: '',
        star: '',
        type: '',
        story: '',
        description: '',
        baseATK: [],
        subAttr: {
          label: '',
          value: []
        },
        effect: {
          title: '',
          text: '',
          value: ''
        }
      },
      level: 90,
      maxLv: 90,
      maxRank: 5,
      refineRank: 1,
      sltState: false
    }
  },
  computed: {
    genIndex () {
      return this.level / 10 % 10 - 2
    },
    genClassName () {
      let className = ''
      switch (this.weaponObj.star) {
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
    getData (path) {
      this.axios.get(path).then((response) => {
        this.weaponObj = response.data
        this.level = this.maxLv = (response.data.baseATK.length + 1) * 10
        if (response.data.effect.text.length) {
          for (let i = 0; i < response.data.effect.text.length; i++) {
            this.weaponObj.effect.text[i] = this.toHtml(this.weaponObj.effect.text[i])
          }
        }
        if (!response.data.effect || response.data.effect.text.length <= 1) {
          this.sltState = true
        }
      })
    },
    toHtml (str) {
      if (!str) return
      let color = str.match(/(#\w+)/g)
      let html = str.replace(/(<color=#.*?>)/g, '<span style="color: ' + color[0] + '">')
      return html.replace(/(<\/color>)/g, '</span>')
    }
  }
}
</script>

<style>
#weapon-detail {
  width: 723px;
  padding-top: 24.8px;
  margin: auto;
}

#weapon-detail > .el-card {
  margin-bottom: 12px;
}

#weapon-detail .el-row {
  margin: 0;
}

#weapon-detail .el-row .el-col {
  margin: 0;
}

#weapon-detail .el-select {
  width: 60px;
}

#weapon-detail .weapon-name {
  margin-bottom: 4px;
  font-size: 32px;
  font-weight: 666;
}

#weapon-detail .attr-content {
  margin: 12px 0;
}

#weapon-detail .attr-content > .attr-label {
  margin: 4px 0;
  font-size: 16px;
  font-weight: 555;
}

#weapon-detail .attr-content > div:last-child {
  font-size: 20px;
}

#weapon-detail .effect-content {
  margin: 12px 0;
}

#weapon-detail .effect-content > div:first-child {
  font-size: 16px;
  font-weight: 555;
}

#weapon-detail .effect-content .effect-value {
  color: #409EFF;
}

#weapon-detail .dscp-content {
  margin-top: 6px;
  font-size: 13px;
  color: #909399;
}

#weapon-detail .orange-bg {
  margin: auto;
  border-radius: 4px;
  background-image: url(../assets/img/ui_package/item_bg_5.png);
  background-size: 100% 100%;
}

#weapon-detail .purple-bg {
  margin: auto;
  border-radius: 4px;
  background-image: url(../assets/img/ui_package/item_bg_4.png);
  background-size: 100% 100%;
}

#weapon-detail .blue-bg {
  margin: auto;
  border-radius: 4px;
  background-image: url(../assets/img/ui_package/item_bg_3.png);
  background-size: 100% 100%;
}

#weapon-detail .green-bg {
  margin: auto;
  border-radius: 4px;
  background-image: url(../assets/img/ui_package/item_bg_2.png);
  background-size: 100% 100%;
}

#weapon-detail .grey-bg {
  margin: auto;
  border-radius: 4px;
  background-image: url(../assets/img/ui_package/item_bg_1.png);
  background-size: 100% 100%;
}
</style>
