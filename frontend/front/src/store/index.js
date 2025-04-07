import { createStore } from "vuex";

export default createStore({
  state: {
    arrOfRaced: [],
    probOfPlayers: [],
    precentsOfWin: {"1": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "5": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "6": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "2": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "3": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "4": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}}
  },
  mutations: {
    pushRaceToArr(state, object){
      state.arrOfRaced.push(object)
    },
    pushProbOfPlayers(state, object){
      state.probOfPlayers.push(object)
    },
    setPresentBase(state, obj){
      state.precentsOfWin = obj
    }
  }
});
