import { createStore } from "vuex";

export default createStore({
  state: {
    globalData: {},
    arrOfRaced: []
  },
  mutations: {
    setGlobalData(state, object){
      state.globalData = object
    },
    pushRaceToArr(state, object){
      state.arrOfRaced.push(object)
    }
  },
  getters: {
    pushToLocaleStoarge(){

    }
  }
});
