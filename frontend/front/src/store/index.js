import { createStore } from "vuex";

export default createStore({
  state: {
    globalData: {},
    arrOfRaced: [],
    arrOfRacedReverce: [],
    probOfPlayers: [],
    precentsOfWin: {"1": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}, "5": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}, "6": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}, "2": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}, "3": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}, "4": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}}
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
    },
    setPresentBase(state, obj){
      state.precentsOfWin = obj
    }
  },
  getters: {
    pushToLocaleStoarge(){

    }
  }
});
