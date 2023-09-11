/**
 * 中间件 防抖函数
 * @param {Function} callbackFn 回调函数
 * @param {number} delay 延时毫秒数
 * @param {boolean} immediate 是否立即执行
 * @returns
 */
export function debounce (callbackFn, delay, immediate = false) {
  let timer = null
  let done = false

  return function _debounce (...args) {
    if (timer) {
      clearTimeout(timer)
    }

    if (immediate && !done) {
      callbackFn.apply(this, args)
      done = true
    } else {
      timer = setTimeout(() => {
        callbackFn.apply(this, args)
      }, delay)
      done = false
    }
  }
}
