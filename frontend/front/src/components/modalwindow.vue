<template>

    <div class="bigcard">

        <div class="card">
        <button class="close-btn" @click="closeModal">×</button>
    
        <div class="row">
            <div class="header">
            <h2> Игрок </h2>
            </div>
            <div class="main">
            <player fillColor="#ff0000" txt="1"></player>
            <player fillColor="#5C7CFA" txt="2"></player>
            <player fillColor="#FCC419" txt="3"></player>
            <player fillColor="#94D82D" txt="4"></player>
            <player fillColor="#CC5DE8" txt="5"></player>
            <player fillColor="#ffffff" txt="6"></player>
            </div>
        </div>
    
        <div class="row">
            <div class="header">
            <h2> Время реакции на старте, c </h2>
            </div>
            <div class="main">
            <inputcomp v-for="(val, i) in reactionTimes" :key="i" v-model="reactionTimes[i]" />
            </div>
        </div>
    
        <div class="row">
            <div class="header">
            <h2> Ускорение, <br> м/c </h2>
            </div>
            <div class="main">
            <inputcomp v-for="(val, i) in accelerations" :key="i" v-model="accelerations[i]" />
            </div>
        </div>
    
        <div class="row">
            <div class="header">
            <h2> Макс. скорость, <br> м/c </h2>
            </div>
            <div class="main">
            <inputcomp v-for="(val, i) in maxSpeeds" :key="i" v-model="maxSpeeds[i]" />
            </div>
        </div>
    
        <div class="row">
            <div class="header">
            <h2> Коэффициент потери скорости </h2>
            </div>
            <div class="main">
            <inputcomp v-for="(val, i) in lossCoefficients" :key="i" v-model="lossCoefficients[i]" />
            </div>
        </div>
    
        
    
        </div>

        <button class="apply-btn" @click="applyChanges">Применить</button>

    </div>

  </template>
  
  <script>
  import player from './player.vue';
  import inputcomp from './inputcomp.vue';
  import axios from 'axios'
  export default {
    components: {
      player,
      inputcomp
    },
    data() {
      return {
        // Эти данные как бы "пришли с бэка"
        reactionTimes: ['0.2', '0.25', '0.22', '0.24', '0.23', '0.21'],
        accelerations: ['3.2', '3.4', '3.1', '3.0', '3.3', '3.2'],
        maxSpeeds: ['6.5', '6.4', '6.6', '6.7', '6.3', '6.2'],
        lossCoefficients: ['0.1', '0.12', '0.11', '0.09', '0.1', '0.11'],
        persons: [],
      loading: false,
      updatingId: null

      }
    },
    created(){
      this.fetchPersons();
    },
    methods: {
      async fetchPersons() {
      this.loading = true;
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/persons/');
        this.persons = response.data.persons;
        console.log(this.persons)
      } catch (error) {
        console.error('Ошибка при загрузке участников:', error);
        alert('Не удалось загрузить данные участников');
      } finally {
        this.loading = false;
      }
    },
    
    async updatePerson(person) {
      this.updatingId = person.id;
      try {
        const dataToUpdate = {
          time_of_reaction: person.time_of_reaction,
          acceleration: person.acceleration,
          max_speed: person.max_speed,
          coef: person.coef,
          color: person.color
        };
        
        await axios.put(
          `http://127.0.0.1:8000/api/persons/${person.id}/`,
          dataToUpdate
        );
        
        alert('Изменения успешно сохранены!');
      } catch (error) {
        console.error('Ошибка при обновлении:', error);
        
        // Откатываем изменения в случае ошибки
        await this.fetchPersons();
        
        alert(`Ошибка при сохранении: ${error.response?.data?.error || error.message}`);
      } finally {
        this.updatingId = null;
      }
    },

      async applyChanges() {
      try {
        console.log('Сохраняем данные на бэк:');
        console.log('reactionTimes:', this.reactionTimes);
        console.log('accelerations:', this.accelerations);
        console.log('maxSpeeds:', this.maxSpeeds);
        console.log('lossCoefficients:', this.lossCoefficients);
        this.$emit('close');
        const response = await axios.post('http://127.0.0.1:8000/api/persons', {
            email: 'penis@yadenx.ru',
            password: 'huilo228',
          }
        )
        console.log(response.data)
      } catch (e) {
        console.log(e)
        //alert("Error server");
      } finally {
        console.log('end fetch')
      }
    },
      closeModal() {
        this.$emit('close');
      }
    }
  }
  </script>
  
  <style scoped>
  .card {
    display: flex;
    flex-direction: row;
    padding: 20px;
    border-radius: 10px;
    position: relative;
    width: 590px;
  }


  .bigcard{
    display: flex;
    flex-direction: column;
    width: 550px;
  }
  
  .header {
    background-color: #2D2D2D;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 120px;
    min-width: 90px;
    padding-inline: 5px;
  }
  
  .header h2 {
    font-family: ubuntu-bold;
    color: white;
    font-size: 15px;
    text-align: center;
  }
  
  .main {
    background-color: #1D1D1D;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px 10px 15px;
    box-sizing: border-box;
    flex-direction: column;
  }
  
  .row {
    display: flex;
    flex-direction: column;
  }
  
  .apply-btn {
    align-self: flex-end;
    background-color: #202020;
    color: white;
    padding: 10px 18px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  }
  
  .close-btn {
    position: absolute;
    top: 5px;
    right: 10px;
    background: none;
    border: none;
    color: white;
    font-size: 24px;
    cursor: pointer;
  }
  </style>
  