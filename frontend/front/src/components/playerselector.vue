<template>
        <div class="player-selector">
      <!-- Выбранный игрок -->
      <div class="current-player" @click="togglePicker">
        <player 
          :fillColor="selectedPlayer.color" 
          :txt="selectedPlayer.number"
          class="selected"
        />
      </div>
  
      <!-- Список игроков -->
      <div v-if="showPicker" class="players-list">
        <div 
          v-for="(player,index) in players" 
          :key="index"
          class="player-item"
          @click="selectPlayer(player)"
        >
          <player 
            :fillColor="player.color" 
            :txt="player.number"
            :class="{ 'active': player.id === selectedPlayer.id }"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import player from './player.vue'
  
  export default {
    components: { player },
    props: {
      players: {
        type: Array,
        required: true,
        validator: value => value.length === 6
      }
    },
    data() {
      return {
        showPicker: false,
        selectedPlayer: this.players[0]
      }
    },
    methods: {
      togglePicker() {
        this.showPicker = !this.showPicker
      },
      selectPlayer(player) {
        this.selectedPlayer = player
        this.showPicker = false
        this.$emit('selected', player)
      },
      handleClickOutside(e) {
        if (!this.$el.contains(e.target)) {
          this.showPicker = false
        }
      }
    },
    mounted() {
      document.addEventListener('click', this.handleClickOutside)
    },
    beforeDestroy() {
      document.removeEventListener('click', this.handleClickOutside)
    }
  }
  </script>
  
  <style scoped>
  .player-selector {
    position: relative;
    display: inline-block;
    margin: 10px;
  }
  
  .current-player {
    cursor: pointer;
    transition: transform 0.2s;
  }
  
  .current-player:hover {
    transform: scale(1.05);
  }
  
  .players-list {
    position: absolute;
    top: 100%;
    left: 0;
    z-index: 1000;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    background: rgba(40, 40, 40, 0.95);
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    margin-top: 10px;
  }
  
  .player-item {
    cursor: pointer;
    transition: all 0.2s;
  }
  
  .player-item:hover {
    transform: scale(1.1);
    filter: brightness(1.2);
  }
  
  .selected {
    border: 2px solid #ffffff;
    border-radius: 8px;
  }
  
  .active {
    border: 2px solid #ff0000;
    border-radius: 5px;
  }
  </style>