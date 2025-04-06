import { createStore } from "vuex";

export default createStore({
  state: {
    globalData: {},
    arrOfRaced: [],
    arrOfRacedReverce: [],
    probOfPlayers: [],
    precentsOfWin: {"1": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "5": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "6": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "2": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "3": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "4": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}}
  },
  mutations: {
    setGlobalData(state, object){
      state.globalData = object
    },
    pushRaceToArr(state, object){
      state.arrOfRaced.push(object)
      console.log(object)
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
