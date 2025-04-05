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
</template>

<script>

import player from './components/player.vue';
import titlerow from './components/titlerow.vue'
import maincard from './components/maincard.vue';
import tableCard from './components/tableCard.vue';
import analys from './components/analys.vue';
import doublecard from './components/doublecard.vue';
export default {
  components: {
    player,
    titlerow,
    maincard,
    tableCard,
    analys,
    doublecard
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
