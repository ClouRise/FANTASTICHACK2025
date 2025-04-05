<template>
      <maincard title="Вероятность занятия 1го и 2го места">
        <div class="selectors-wrapper">
          <div class="cont">
            <p>Топ 1</p>
            <playerselector 
            :players="players"
            @selected="handleFirstPlayerSelect"
            class="selector"
          />
        </div>

        
          <div class="cont">
            <p>Топ 2</p>
            <playerselector 
            :players="players"
            @selected="handleSecondPlayerSelect"
            class="selector"
          />
        </div>
        </div>
      </maincard>
  </template>
  
  <script>
  import maincard from './maincard.vue'
  import playerselector from './playerselector.vue'
  
  export default {
    components: {
      maincard,
      playerselector
    },
    data() {
      return {
        players: [
          { id: 1, number: 1, color: '#ff0000' },
          { id: 2, number: 2, color: '#5C7CFA' },
          { id: 3, number: 3, color: '#FCC419' },
          { id: 4, number: 4, color: '#94D82D' },
          { id: 5, number: 5, color: '#CC5DE8' },
          { id: 6, number: 6, color: '#FFFFFF' }
        ]
      }
    },
    methods: {
      handleFirstPlayerSelect(player) {
        console.log('Первый игрок:', player)
      },
      handleSecondPlayerSelect(player) {
        console.log('Второй игрок:', player)
      }
    }
  }
  </script>
  
  <style>
  .double-card-container {
    padding: 20px;
    background: #1a1a1a;
  }
  
  .selectors-wrapper {
    display: flex;
    gap: 40px;
    justify-content: center;
    padding: 20px;
  }
  
  .selector {
    transform: scale(0.9);
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }
  
  .selector:hover {
    transform: scale(1);
  }
  .cont{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    font-size: 12pt;
    color: white;
  }
  </style>