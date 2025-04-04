<template>
  <div class="app">
    <header>

    </header>
    <main>
      <player fillColor="#ff0000" txt="3"></player>
      <titlerow style="box-shadow: #EFDE22 0px 0px 5px 3px" num="1"></titlerow>
      <titlerow style="box-shadow: #7A7A81 0px 0px 5px 3px" num="2"></titlerow>
      <titlerow style="box-shadow: #FF77004D 0px 0px 5px 3px" num="3"></titlerow>
      <titlerow num="4"></titlerow>
      <titlerow num="5"></titlerow>
      <titlerow num="6"></titlerow>
    </main>
  </div>
</template>

<script>

import player from './components/player.vue';
import titlerow from './components/titlerow.vue'
export default {
  components: {
    player,
    titlerow
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
