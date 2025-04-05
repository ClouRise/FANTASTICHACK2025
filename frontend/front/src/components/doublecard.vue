<template>
  <table>
      <thead>
          <tr>
              <th><top12></top12></th>
              <th><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#ff0000" txt="1"></player></th>
              <th><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#5C7CFA" txt="2"></player></th>
              <th><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#FCC419" txt="3"></player></th>
              <th><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#94D82D" txt="4"></player></th>
              <th><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#CC5DE8" txt="5"></player></th>
              <th><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#FFFFFF" txt="6"></player></th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#ff0000" txt="1"></player></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
          </tr>
          <tr>
              <td><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#5C7CFA" txt="2"></player></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
          </tr>
          <tr>
              <td><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#FCC419" txt="3"></player></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
          </tr>
          <tr>
              <td><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#94D82D" txt="4"></player></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
          </tr>
          <tr>
              <td><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#CC5DE8" txt="5"></player></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
          </tr>
          <tr style="border: none;">
              <td><player :size="50" :wcard="30" :hcard="18" :fontsize="15" :topminus="-10" fillColor="#FFFFFF" txt="6"></player></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
              <td><p>15%</p></td>
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
  padding-inline: 5px;
  padding-block: 5px;
  font-family: ubuntu-regular;
  color: white;
}
th{
  padding-inline: 5px;
  padding-block: 5px;
  font-family: ubuntu-regular;
  color: white;
}
p{
  text-align: center;
}
</style>