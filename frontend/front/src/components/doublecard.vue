<template>
  <table>
      <thead>
          <tr>
              <th><top12></top12></th>
              <th><player  fillColor="#ff0000" txt="1"></player></th>
              <th><player  fillColor="#5C7CFA" txt="2"></player></th>
              <th><player  fillColor="#FCC419" txt="3"></player></th>
              <th><player  fillColor="#94D82D" txt="4"></player></th>
              <th><player  fillColor="#CC5DE8" txt="5"></player></th>
              <th><player  fillColor="#FFFFFF" txt="6"></player></th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td style="display: flex; justify-content: center;" ><player  fillColor="#ff0000" txt="1"></player></td>
              <td v-for="n in 6" :key="n"><p>{{ ( Math.floor(($store.state.precentsOfWin['1']['1'] * $store.state.precentsOfWin[`${n}`]['2']) * 100) * 100) / 100 }}%</p></td>
          </tr>
          <tr>
              <td style="display: flex; justify-content: center;"><player  fillColor="#5C7CFA" txt="2"></player></td>
              <td v-for="n in 6" :key="n"><p>{{ ( Math.floor(($store.state.precentsOfWin['2']['1'] * $store.state.precentsOfWin[`${n}`]['2']) * 100) * 100) / 100 }}%</p></td>
          </tr>
          <tr>
              <td style="display: flex; justify-content: center;"><player  fillColor="#FCC419" txt="3"></player></td>
              <td v-for="n in 6" :key="n"><p>{{ ( Math.floor(($store.state.precentsOfWin['3']['1'] * $store.state.precentsOfWin[`${n}`]['2']) * 100) * 100) / 100 }}%</p></td>
          </tr>
          <tr>
              <td style="display: flex; justify-content: center;"><player  fillColor="#94D82D" txt="4"></player></td>
              <td v-for="n in 6" :key="n"><p>{{ ( Math.floor(($store.state.precentsOfWin['4']['1'] * $store.state.precentsOfWin[`${n}`]['2']) * 100) * 100) / 100 }}%</p></td>
          </tr>
          <tr>
              <td style="display: flex; justify-content: center;"><player  fillColor="#CC5DE8" txt="5"></player></td>
              <td v-for="n in 6" :key="n"><p>{{ ( Math.floor(($store.state.precentsOfWin['5']['1'] * $store.state.precentsOfWin[`${n}`]['2']) * 100) * 100) / 100 }}%</p></td>
          </tr>
          <tr style="border: none;">
              <td style="display: flex; justify-content: center;"><player  fillColor="#FFFFFF" txt="6"></player></td>
              <td v-for="n in 6" :key="n"><p>{{ ( Math.floor(($store.state.precentsOfWin['6']['1'] * $store.state.precentsOfWin[`${n}`]['2']) * 100) * 100) / 100 }}%</p></td>
          </tr>
      </tbody>
  </table>
</template>

<script>
import titlerow from './titlerow.vue';
import player from './player.vue';
import top12 from './top12.vue';
export default {
  components: {
      titlerow,
      player,
      top12
  }
}
</script>

<style scoped>
table{
  width: auto;
  height: auto;
  border-collapse: collapse;
} 
tr{
  border-bottom: 1pt solid rgb(46, 46, 46);
}
td{
  padding-inline: 8px;

  font-family: ubuntu-regular;
  color: white;
}
th{
  padding-inline: 5.5px;
  padding-block: 4.5px;
  font-family: ubuntu-regular;
  color: white;
}
p{
  text-align: center;
}
</style>