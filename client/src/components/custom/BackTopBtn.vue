<template>
  <div id="back-top-btn">
    <div v-show="showBtn" class="back-top-outer">
      <div class="back-top-inner">
        <div class="back-top-wrap">
          <div class="back-top-btn" @click="backTop">
            <svg width="12" height="12">
              <polygon points="0,12 12,12 6,6" fill="#FFF" stroke="none"></polygon>
            </svg>
            <span>{{ text }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      default: '顶部'
    }
  },
  data () {
    return {
      showBtn: false
    }
  },
  mounted () {
    window.addEventListener('scroll', this.handleScroll)
  },
  methods: {
    handleScroll () {
      let scrollTop = document.documentElement.scrollTop
      if (scrollTop >= 400) {
        this.showBtn = true
      } else {
        this.showBtn = false
      }
    },
    backTop () {
      let timer = null
      cancelAnimationFrame(timer)
      timer = requestAnimationFrame(function scrollAnime () {
        let distance = document.body.scrollTop || document.documentElement.scrollTop
        if (distance > 0) {
          scrollTo(0, distance - 100)
          timer = requestAnimationFrame(scrollAnime)
        } else {
          cancelAnimationFrame(timer)
        }
      })
    }
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';
@import '../../assets/scss/anime.scss';

.back-top-outer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 0 96px;
  background-color: transparent;
  z-index: 1999;
  pointer-events: none;
}

.back-top-inner {
  position: relative;
  width: 100%;
  height: 100%;
}

.back-top-wrap {
  position: absolute;
  bottom: 120px;
  left: 100%;
}

.back-top-btn {
  width: 48px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 8px 0;
  font-size: $xsmall-font-size;
  color: #FFF;
  background-color: $brand-color;
  pointer-events: auto;
  box-shadow: 0 2px 2px rgba(0, 0, 0, .08);
  border: none;
  border-radius: .5rem;
  user-select: none;
  @include fade-in(.2s);
  &:hover {
    background-color: #66b1ff;
  }
  &:active {
    background-color: #3a8ee6;
    transform: scale(0.95);
  }
}
</style>
