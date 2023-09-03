<template>
  <div :class="{'is-active' : isActive}" @click="handleClick">
    <slot></slot>
  </div>
</template>

<script>
export default {
  props: ['modelValue', 'label'],
  data () {
    return {
      isActive: false
    }
  },
  watch: {
    modelValue: {
      handler (newVal) {
        if (newVal === this.label) {
          this.isActive = true
        } else {
            this.isActive = false
        }
      },
      immediate: true
    }
  },
  computed: {
    value: {
      get () {
        return this.modelValue
      },
      set (value) {
        this.$emit('update:modelValue', value)
      }
    }
  },
  methods: {
    handleClick () {
      if (this.value === this.label) {
        this.$emit('update:modelValue', '不限')
      } else {
        this.$emit('update:modelValue', this.label)
      }
    }
  } 
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/index.scss';

div {
  height: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 12px;
  margin: 6px;
  color: $regular-text;
  font-size: .8rem;
  border-radius: .5rem;
  background-color: $lighter-border;
  box-sizing: border-box;
}

div:hover {
  color: $brand-color;
  background-color: #ECF5FF;
}

div.is-active {
  color: #FFF;
  background-color: $brand-color;
}
</style>
