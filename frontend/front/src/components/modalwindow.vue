<template>
  <div class="container">
    
    <!-- Список участников с полями для редактирования -->
    <div class="participants-list">
      <div v-if="loading" class="loading">Загрузка данных...</div>

        <div v-else v-for="person in persons" :key="person.id" class="participant-card">
          <div style=" padding-right: 20px; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
            <div class="div-player">
            <player style="position: relative; top: 10px;" :size="100" :wcard="70" :hcard="30" :fontsize="18" :topminus="-20" :fillColor="person.color" :txt="person.id"></player>
          </div>
          <button :style="'box-shadow: 0 4px 10px 0' + person.color"
            @click="updatePerson(person)" 
            class="update-btn"
            :disabled="updatingId === person.id"
          >
            <span v-if="updatingId === person.id">Сохранение...</span>
            <span v-else>Сохранить изменения</span>
          </button>
          </div>
          
          <div class="participant-fields">
            
            <div class="field">
              <label>Время реакции:</label>
              <input v-model.number="person.time_of_reaction" type="number" step="0.01" min="0.1" max="0.31">
            </div>
            
            <div class="field">
              <label>Ускорение:</label>
              <input v-model.number="person.acceleration" type="number" step="0.1" min="0.0" max="5.1">
            </div>
            
            <div class="field">
              <label>Макс. скорость:</label>
              <input v-model.number="person.max_speed" type="number" step="0.1" min="5.0" max="15.1">
            </div>
            
            <div style="margin: 0;" class="field">
              <label>Коэффициент:</label>
              <input v-model.number="person.coef" type="number" step="0.1" min="-2.1" max="0.1">
            </div>
          
          </div>
        
        </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import player from './player.vue';
export default {
  components: {
    player
  },
  data() {
    return {
      persons: [],
      loading: false,
      updatingId: null
    }
  },
  created() {
    this.fetchPersons();
  },
  methods: {
    async fetchPersons() {
      this.loading = true;
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/persons/');
        this.persons = response.data.persons;
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
    }
  }
}
</script>
 
<style scoped>
.container {
  display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    width: 100%;
}

.participants-list {
  margin-top: 30px;
  display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-evenly;
    width: 100%;
}

.participant-card {
  display: flex;
  align-items: center;
  padding: 20px;
  border-radius: 5px;
  width: 360px;
  height: 270px;
  display: grid;
  grid: 100% / 50% 50%;
  margin: 20px;
  background: #d4d4d4;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.div-player {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.participant-fields {
  flex-grow: 1;
}

.field {
  margin-bottom: 10px;
    display: flex;
    align-items: flex-start;
    flex-direction: column;
}

.field label {
  font-size: 15px;
  font-family: ubuntu-regular;
  color: #0c0c0c;
}

.field input {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 100%;
}

.field input[type="color"] {
  width: 50px;
  height: 30px;
  padding: 2px;
}

.update-btn {
  padding: 10px 20px;
  background-color: #000000;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
  transition: all 0.2s ease-in-out;
}

.update-btn:hover {
  background-color: #303030;
  transition: all 0.2s ease-in-out;
}

.update-btn:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.loading {
  text-align: center;
  padding: 30px;
  font-size: 18px;
  color: #666;
}
</style>