import { createStore } from 'vuex'

const store = createStore({
  state () {
    return {
      charObj: null
    }
  },
  getters: {
    getCharObj () {
      return state.charObj
    }
  },
  mutations: {
    setCharObj (state, data) {
      state.charObj = data
    }
  }
})

export default store
