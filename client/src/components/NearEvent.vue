<template>
  <div id="near-event">
    <div
      class="event-item"
      v-for="(item, index) in dataList"
      :key="index"
      @click="handleClick(index)"
    >{{ item.title }}
    </div>
    <el-dialog
      custom-class="event-dialog"
      :title="dialogTitle"
      :visible.sync="dialogVisible"
      :width="dialogWidth"
      :append-to-body="true"
      :lock-scroll="false"
    >
      <div class="event-content" v-html="dialogContent"></div>
    </el-dialog>
  </div>
</template>

<script>
import { getEvent } from '../api'

export default {
  data () {
    return {
      dialogVisible: false,
      dialogWidth: '0%',
      dialogTitle: '',
      dialogContent: '',
      dataList: []
    }
  },
  created () {
    const storage = JSON.parse(sessionStorage.getItem('event'))
    if (storage) {
      this.dataList = storage
    } else {
      this.getData()
    }
    this.getData()
  },
  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResize)
  },
  methods: {
    getData () {
      getEvent().then(response => {
        if (response.data.status === 200) {
          this.dataList.length = 0
          response.data.data.forEach(item => {
            this.dataList.push(item)
          })
          sessionStorage.setItem('event', JSON.stringify(this.dataList))
        }
      }).catch(error => {
        console.log(error)
      })
    },
    onResize () {
      const width = window.innerWidth 
      if (width >= 1200) {
        this.dialogWidth = '50%'
      } else if (width >= 992) {
        this.dialogWidth = '80%'
      } else {
        this.dialogWidth = '100%'
      }
    },
    handleClick (index) {
      this.dialogTitle = this.dataList[index].title
      console.log(this.dialogTitle)
      this.dialogContent = this.dataList[index].content
      console.log(this.dialogContent)
      this.dialogVisible = true
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/scss/index.scss';

#near-event {
  margin-bottom: 1rem;
  border: {
    style: solid;
    width: 1px;
    color: $base-border;
    radius: .5rem;
  };
}

.event-item {
  width: 100%;
  display: flex;
  align-items: center;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  border-bottom: 1px solid $base-border;
  &:last-child {
    border-bottom: none;
  }
}

.el-dialog {
  .event-content {
    height: 60vh;
    padding: 1rem;
    overflow-y: auto;
    box-sizing: border-box;
    /deep/ img {
      width: 75%;
      height: 100%;
      object-fit: contain;
    }
    // 容器滚动条样式
    &::-webkit-scrollbar{
      width: 4px;
    }
    &::-webkit-scrollbar-thumb {
      border-radius: 10px;
      background: rgba(0,0,0,0.2);
    }
    &::-webkit-scrollbar-track {
      border-radius: 0;
      background: transparent;
    }
  }
}

/deep/ .event-dialog {
  .el-dialog__body {
    height: 60vh;
    padding: 0;
    overflow: hidden;
  }
}
</style>
