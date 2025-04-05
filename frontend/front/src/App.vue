<template>
  <div class="app">
    <header>
      <a href="">Характеристики</a>
    </header>
    <main>
      <!-- <player fillColor="#ff0000" txt="3"></player>
      <titlerow style="box-shadow: #EFDE22 0px 0px 5px 3px" num="1"></titlerow>
      <titlerow style="box-shadow: #7A7A81 0px 0px 5px 3px" num="2"></titlerow>
      <titlerow style="box-shadow: #FF77004D 0px 0px 5px 3px" num="3"></titlerow>
      <titlerow num="4"></titlerow>
      <titlerow num="5"></titlerow>
      <titlerow num="6"></titlerow> -->
      <div class="row">
        <maincard :title="'Номер игрока и вероятность по местам'">
          <tableCard></tableCard>
        </maincard>
      </div>
      <div class="row">
        <maincard :title="'Статистика'">
          <analys></analys>
        </maincard>
      </div>
    </main>
  </div>
  <button @click="toggleRace">sdhsdhs</button>
  <p>{{ racers }}</p>
</template>

<script>

import player from './components/player.vue';
import titlerow from './components/titlerow.vue'
import maincard from './components/maincard.vue';
import tableCard from './components/tableCard.vue';
import analys from './components/analys.vue';
import doublecard from './components/doublecard.vue';
import axios from 'axios';
export default {
  data(){
    return {
      isRacing: false,
      loading: false,
      error: null,
      currentTime: 0,
      racers: {},
      winner: null,
      cancelTokenSource: null,
      eventSource: null
    }
  },
  components: {
    player,
    titlerow,
    maincard,
    tableCard,
    analys,
    doublecard
  },
  methods: {
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
        this.eventSource = new EventSource(`http://localhost:8000/api/race/?t=${Date.now()}`);
        
        this.eventSource.onmessage = (event) => {
          try {
            const data = JSON.parse(event.data);
            this.currentTime = data.time;
            this.racers = data.racers;
            
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
  }
}
</script>

<style scoped>
.app{
  width: 100%;
  height: 100%;
}
header{
  background-color: #1F1F1F;
  height: 70px;
  padding-inline: 70px;
  display: flex;
  justify-content: start;
  align-items: center;
  background-image: url(./assets/img/doritos-bg.svg);
  background-repeat: no-repeat;
  background-position-x: right;
}
main{
  background-image: url(./assets/img/bg-top.svg);
  background-position-y: -60px;
  background-repeat: no-repeat;
  background-position-x: right;
  padding: 50px;
}
header a{
  font-family: ubuntu-bold;
  color: white;
  font-size: 20px;
  text-decoration: none;
}
.row{
  width: 100%;
  display: flex;
  flex-direction: row;
  margin-bottom: 30px;
}
</style>
