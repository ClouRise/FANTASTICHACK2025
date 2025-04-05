import { createStore } from "vuex";

export default createStore({
  state: {
    globalData: {}
  },
  mutations: {
    setGlobalData(state, object){
      state.globalData = object
    }
  },
  getters: {
    pushToLocaleStoarge(){
      
    }
  }
});
