<template>
    <div>
        <maincard
  :title="'Вероятность попадения в топ2/топ3'"
  :customHeaderHeight="70"
  style="display: flex; justify-content: center; flex-direction: column; max-width: 100%;"
>
            <div style="display: flex; justify-content: space-around; width: 100%; align-items: center;">
                <div class="top2">
                    <top2></top2>

                    <div class="players">
                        <player wcard="40" hcard="18" fillColor="#ff0000" :txt="`${( Math.floor(($store.state.precentsOfWin['1']['1'] +  $store.state.precentsOfWin['1']['2']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#5C7CFA" :txt="`${( Math.floor(($store.state.precentsOfWin['2']['1'] +  $store.state.precentsOfWin['2']['2']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#FCC419" :txt="`${( Math.floor(($store.state.precentsOfWin['3']['1'] +  $store.state.precentsOfWin['3']['2']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#94D82D" :txt="`${( Math.floor(($store.state.precentsOfWin['4']['1'] +  $store.state.precentsOfWin['4']['2']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#CC5DE8" :txt="`${( Math.floor(($store.state.precentsOfWin['5']['1'] +  $store.state.precentsOfWin['5']['2']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#FFFFFF" :txt="`${( Math.floor(($store.state.precentsOfWin['6']['1'] +  $store.state.precentsOfWin['6']['2']) * 100) * 100) / 100 }%`"></player>
                    </div>

                </div>

                <div class="top3">
                    <top3></top3>

                    <div class="players">
                        <player wcard="40" hcard="18" fillColor="#ff0000" :txt="`${( Math.floor(($store.state.precentsOfWin['1']['1'] +  $store.state.precentsOfWin['1']['2'] + $store.state.precentsOfWin['1']['3']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#5C7CFA" :txt="`${( Math.floor(($store.state.precentsOfWin['2']['1'] +  $store.state.precentsOfWin['2']['2'] + $store.state.precentsOfWin['2']['3']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#FCC419" :txt="`${( Math.floor(($store.state.precentsOfWin['3']['1'] +  $store.state.precentsOfWin['3']['2'] + $store.state.precentsOfWin['3']['3']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#94D82D" :txt="`${( Math.floor(($store.state.precentsOfWin['4']['1'] +  $store.state.precentsOfWin['4']['2'] + $store.state.precentsOfWin['4']['3']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#CC5DE8" :txt="`${( Math.floor(($store.state.precentsOfWin['5']['1'] +  $store.state.precentsOfWin['5']['2'] + $store.state.precentsOfWin['5']['3']) * 100) * 100) / 100 }%`"></player>
                        <player wcard="40" hcard="18" fillColor="#FFFFFF" :txt="`${( Math.floor(($store.state.precentsOfWin['6']['1'] +  $store.state.precentsOfWin['6']['2'] + $store.state.precentsOfWin['6']['3']) * 100) * 100) / 100 }%`"></player>
                    </div>

                </div>

            </div>
        </maincard>
    </div>
</template>

<script>
import maincard from './maincard.vue';
import top2 from './top2.vue';
import top3 from './top3.vue';
import player from './player.vue';
import store from '@/store';
    export default {
        components:{
            maincard,
            top2,
            top3,
            player,
        },
        data(){
            return{
                precentBase: store.state.precentsOfWin
            }
        }
        
    }
</script>

<style scoped>
.top2{
 display: flex;
 flex-direction: column;
}
.top3{
display: flex;
flex-direction: column;
}
.players{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
</style>