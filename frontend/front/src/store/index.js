import { createStore } from "vuex";

export default createStore({
  state: {
    globalData: {},
    arrOfRaced: [],
    arrOfRacedReverce: [],
    probOfPlayers: []
  },
  mutations: {
    setGlobalData(state, object){
      state.globalData = object
    },
    pushRaceToArr(state, object){
      state.arrOfRaced.push(object)
    },
    pushRaceToArrReverce(state, object){
      state.arrOfRacedReverce.push(object)
    },
    pushProbOfPlayers(state, object){
      state.probOfPlayers.push(object)
    }
  },
  getters: {
    pushToLocaleStoarge(){

    }
  }
});
