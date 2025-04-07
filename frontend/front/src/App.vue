<template>
  <div class="app">
    <header>
      <a href="#" @click.prevent="isModalOpen = true">Характеристики</a>
    </header>

    <main>
      <div class="row">
        <maincard :id="1" :title="'Номер игрока и вероятность по местам'">
          <tableCard :prob="probabilitiesFinal"></tableCard>
        </maincard>

        <maincard style="width: 300px;" :id="2" :title="'Статистика'">
          <div v-if="!showInfoAnalys" style="width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; padding: 50px;">
            <p style="font-family: ubuntu-regular; color: rgb(95, 95, 95); text-align: center; font-size: 15px;">Статистика без первого забега недоступна.</p>
          </div>
          <analys v-if="showInfoAnalys" style="width: 100%;"></analys>
        </maincard>

        <maincard :id="4" :title="'Вероятность занять 1ое и 2ое места'">
          <doublecard></doublecard>
        </maincard>
        <top12312></top12312>
      </div>
      <div class="row">

        <maincard :id="3" v-on:toggle-race="toggleRace" style="width: 100%;" :buttonRace="true"
          :title="'Симуляция забега'">
          <raceMap :racers="racers"></raceMap>
        </maincard>
      </div>
      <div v-if="isModalOpen">
        <div class="overlay" @click="closeModal"></div>
        <div class="modal-container">
          <modalwindow @close="closeModal" />
        </div>
      </div>
    </main>
  </div>
</template>

<script>

import player from './components/player.vue';
import titlerow from './components/titlerow.vue'
import maincard from './components/maincard.vue';
import tableCard from './components/tableCard.vue';
import analys from './components/analys.vue';
import doublecard from './components/doublecard.vue';
import raceMap from './components/raceMap.vue';
import modalwindow from './components/modalwindow.vue';
import axios from 'axios';
import store from './store';
import top12312 from './components/top12312.vue';
export default {
  data() {
    return {
      isRacing: false,
      loading: false,
      error: null,
      isModalOpen: false,
      currentTime: 0,
      racers: {
        "1": { "distance": 100, "speed": 0, "finished": true, "color": "#ff0000" },
        "2": { "distance": 100, "speed": 0, "finished": true, "color": "#5c7cfa" },
        "3": { "distance": 100, "speed": 0, "finished": true, "color": "#fcc419" },
        "4": { "distance": 100, "speed": 0, "finished": true, "color": "#94d82d" },
        "5": { "distance": 100, "speed": 0, "finished": true, "color": "#cc5de8" },
        "6": { "distance": 100, "speed": 0, "finished": true, "color": "#ffffff" }
      },
      winner: null,
      cancelTokenSource: null,
      eventSource: null,
      finalRes: {},
      showInfoAnalys: false,
      probabilities: {},
      probabilitiesFinal: {"1": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "5": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "6": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "2": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "3": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}, "4": {"1": 0.16, "2": 0.16, "3": 0.16, "4": 0.16, "5": 0.16, "6": 0.16}}
    }
  },
  components: {
    player,
    titlerow,
    maincard,
    tableCard,
    analys,
    doublecard,
    raceMap,
    modalwindow,
    top12312
  },
  methods: {
    closeModal() {
      this.isModalOpen = false;
    },
    async toggleRace() {
      if (this.isRacing) {
        await this.stopRace();
      } else {
        await this.startRace();
      }
    },

    async startRace() {
      try {
        this.loading = true;
        this.resetRace();

        // Создаем новый источник для отмены запроса
        this.cancelTokenSource = axios.CancelToken.source();

        // Используем EventSource для получения потоковых данных
        this.eventSource = new EventSource(`http://localhost/api/race/?t=${Date.now()}`);  //исправил путь, потом поменять

        this.eventSource.onmessage = (event) => {
          try {
            const data = JSON.parse(event.data);
            this.currentTime = data.time;
            this.racers = data.racers;
            this.probabilities = data.probabilities
            this.finalRes = data.final_results;

            store.commit('setGlobalData', data);
            if (data.winner && !this.winner) {
              this.winner = data.winner;
            }

            if (Object.values(data.racers).every(r => r.finished)) {
              setTimeout(() => this.stopRace(), 1000);
            }
          } catch (e) {
            console.error('Ошибка обработки данных:', e);
            this.error = 'Ошибка обработки данных с сервера';
            this.stopRace();
          }
        };

        this.eventSource.onerror = (e) => {
          console.error('Ошибка соединения:', e);
          if (this.isRacing) {
            this.error = 'Ошибка соединения с сервером';
            this.stopRace();
          }
        };

        this.isRacing = true;
        this.loading = false;

      } catch (e) {
        console.error('Ошибка запуска:', e);
        this.error = 'Не удалось начать забег';
        this.loading = false;
      }
    },

    async stopRace() {
      try {
        if (this.cancelTokenSource) {
          this.cancelTokenSource.cancel('Забег остановлен пользователем');
        }

        if (this.eventSource) {
          this.eventSource.close();
          this.eventSource = null;
        }

        this.isRacing = false;
        this.loading = false;

      } catch (e) {
        console.error('Ошибка остановки:', e);
      }
    },

    resetRace() {
      this.error = null;
      this.currentTime = 0;
      this.racers = {};
      this.winner = null;
    }
  },
  async beforeUnmount() {
    await this.stopRace();
  },
  watch: {
    finalRes() {
      if (this.finalRes != null) {

        this.showInfoAnalys = true;
        this.probabilitiesFinal = this.probabilities

        var finres = {}
        Object.entries(this.finalRes).forEach(([key, value]) => {
          finres[value] = key
        })
        console.log(this.probabilities)
        console.log(this.probabilitiesFinal)

        store.commit('pushRaceToArr', finres);
        store.commit('pushRaceToArrReverce', this.finalRes);
        store.commit('setPresentBase', this.probabilitiesFinal);

      }
    }
  }
}
</script>

<style scoped>
.app {
  width: 100%;
  height: 100%;
  background-image: url(./assets/img/bg.jpg);
  background-attachment: fixed;
  background-size: 110%;
  position: fixed;
}

body {
  background-image: url(./assets/img/bg.jpeg);
  filter: brightness(60%);
}
header a{
  text-decoration: underline solid;
  text-decoration-color: rgba(255, 255, 255, 0);
    text-underline-offset: 10px;
    transition: all 0.25s ease-in-out;
}
header a:hover{
  text-decoration: underline solid;
  text-decoration-color: rgba(255, 255, 255, 1);
    text-underline-offset: 3px;
    transition: all 0.25s ease-in-out;
}
header {
  background-color: #1F1F1F;
  height: 60px;
  padding-inline: 60px;
  display: flex;
  justify-content: start;
  align-items: center;
  background-image: url(./assets/img/doritos-bg.svg);
  background-repeat: no-repeat;
  background-position-x: right;
}

main {
  background-image: url(./assets/img/bg-top.svg);
  background-position-y: -60px;
  background-repeat: no-repeat;
  background-position-x: right;
  padding: 5px;
}

header a {
  font-family: ubuntu-bold;
  color: white;
  font-size: 20px;
  text-decoration: none;
}

.row {
  width: 100%;
  display: flex;
  flex-direction: row;
  margin-bottom: 30px;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 10;
}

.modal-container {
  position: fixed;
  width: 100%;
  display: flex;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 11;
  max-height: 90vh;
}
</style>
