<template>
  <div class="app">
    <header>

    </header>
    <main>
      <player fillColor="#ff0000" txt="3"></player>
    </main>
  </div>
</template>

<script>

import player from './components/player.vue';
export default {
  components: {
    player
  }
}
</script>

<style scoped>
.app{
  width: 100%;
  height: 100%;
  overflow: none;
  position: fixed;
  display: grid;
  grid: 70px auto / 100%
}
header{
  background-color: #42424A;
  box-shadow: 0px 4px 4px 0 black;
}
main{
  background-color: aqua;
  background-image: url(./assets/img/bg.jpeg);
  background-size: cover;
}
main::after {
  content: '';
  position: absolute;
  top: 0;
  background: #4E505666; 
  width: 100%;
  height: 100%;
}
</style>
