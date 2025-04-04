<template>
  <div class="app">
    <header>
      <a href="">Характеристики</a>
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
}
header{
  background-color: #1F1F1F;
  height: 70px;
  padding-inline: 70px;
  display: flex;
  justify-content: start;
  align-items: center;
}
main{

}
header a{
  font-family: ubuntu-bold;
  color: white;
  font-size: 18px;
  text-decoration: none;
}

</style>
