<template>
  <div id="page-footer">
    <!-- 声明 -->
    <div class="disclaimer">
      <el-icon><InfoFilled /></el-icon>
      本站仅作学习用途，一切数据资源归版权方所有。
    </div>
    <!-- 相关链接 -->
    <div class="link-content" v-for="(item, index) in linkList" :key="index">
      <div class="link-tag">{{ item.title }}</div>
      <a
        v-for="(subItem, subIndex) in item.content"
        :key="subIndex"
        :href="subItem.link"
        target="_blank"
      >
        <img
          style="width: 28px; height:28px;"
          :src="imgURL + '/ui_package/' + subItem.img"
        />
      </a>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      linkList: [{
        title: '项目地址',
        content: [{
          img: 'gitee_logo.png',
          link: 'https://gitee.com/haneball/gs_wiki'
        }, {
          img: 'github_logo.png',
          link: 'https://github.com/haneball/gs_wiki'
        }]
      }, {
        title: '使用框架',
        content: [{
          img: 'vue_logo.png',
          link: 'https://cn.vuejs.org'
        }, {
          img: 'elementUI_logo.png',
          link: 'https://element.eleme.cn/#/zh-CN'
        }]
      }],
      imgURL: 'https://proj-gswiki-1316988911.cos.ap-shanghai.myqcloud.com'
    }
  }
}
</script>

<style lang="scss" scoped>
@import 'element-plus/theme-chalk/display.css';
@import '../assets/scss/index.scss';

#page-footer {
  min-height: 90px;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  padding: .5rem 2.5rem;
  background-color: #3F3F3F;
  font-size: 1.25rem;
  color: $disabled-text;
  .disclaimer {
    flex-grow: 1;
    padding: .5rem;
  }
}

.link-content {
  width: 80px;
  border-left: 2px solid #898989;
  padding-left: 6px;
}

a > img {
  margin: 4px 6px 0 0;
}

.link-tag {
  width: 100%;
  font-size: 1rem;
  color: $placeholder-text;
}

@media (min-width: $xs-width) {
  .disclaimer {
    flex-basis: 100%;
  }
  .link-content:last-child {
    border-right: 2px solid #898989;
  }
}

@media (min-width: $sm-width) {
  .disclaimer {
    display: flex;
    flex-basis: auto;
    justify-content: start;
    align-items: center;
  }
  .link-content:last-child {
    border-right: none;
  }
}
</style>
