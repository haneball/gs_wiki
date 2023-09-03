<template>
  <div ref="root" class="window-affix">
    <div :class="{'window-affix__fixed': state.fixed}" :style="affixStyle">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    offset: {
      type: Number,
      default: 0
    },
    position: {
      type: String,
      default: 'top'
    },
    start: {
      type: Number,
      default: 0
    },
    end: {
      type: Number,
      default: 0
    },
    zIndex: {
      type: Number,
      default: 100
    }
  },
  data () {
    return {
      state: {
        fixed: false,
        width: 0,
        height: 0,
        left: 0,
        scrollTop: 0,
        clientHeight: 0
      }
    }
  },
  mounted () {
    window.addEventListener('scroll', this.onScroll)
    window.addEventListener('resize', this.updateState)
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.onScroll)
    window.removeEventListener('resize', this.updateState)
  },
  computed: {
    affixStyle () {
      if (!this.state.fixed) {
        return
      }
      const offset = this.offset ? `${this.offset}px` : 0
      const left = `${this.state.left}px`

      return {
        height: `${this.state.height}px`,
        width: `${this.state.width}px`,
        top: this.position === 'top' ? offset : '',
        left: left,
        bottom: this.position === 'bottom' ? offset : '',
        zIndex: this.zIndex,
      }
    }
  },
  methods: {
    onScroll () {
      this.updateState()
      this.$emit('scroll', {
        scrollTop: this.state.scrollTop,
        fixed: this.state.fixed
      })
    },
    updateState () {
      const rootRect = this.$refs.root.getBoundingClientRect()
      this.state.width = rootRect.width
      this.state.height = rootRect.height
      this.state.left = rootRect.left
      this.state.scrollTop = document.documentElement.scrollTop
      this.state.clientHeight = document.documentElement.clientHeight

      if (this.position === 'top') {
        const flag = this.offset > rootRect.top && this.state.scrollTop > this.start
        if (!this.state.fixed || this.state.scrollTop <= this.end) {
          this.state.fixed = flag
        }
      } else {
        this.state.fixed = this.state.clientHeight - this.offset < rootRect.bottom
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/anime.scss';

.window-affix {
  .window-affix__fixed {
    position: fixed;
    @include fade-in(.2s);
  }
}
</style>
