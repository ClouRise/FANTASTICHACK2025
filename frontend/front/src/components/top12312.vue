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
                        <player wcard="40" hcard="18" fillColor="#ff0000" :txt="`${(precentBase['1']['1'] + precentBase['1']['2']) * 100}%`"></player>
                        <player wcard="40" hcard="18" fillColor="#5C7CFA" :txt="`${(precentBase['2']['1'] + precentBase['2']['2']) * 100}%`"></player>
                        <player wcard="40" hcard="18" fillColor="#FCC419" :txt="`${(precentBase['3']['1'] + precentBase['3']['2']) * 100}%`"></player>
                        <player wcard="40" hcard="18" fillColor="#94D82D" :txt="`${(precentBase['4']['1'] + precentBase['4']['2']) * 100}%`"></player>
                        <player wcard="40" hcard="18" fillColor="#CC5DE8" :txt="`${(precentBase['5']['1'] + precentBase['5']['2']) * 100}%`"></player>
                        <player wcard="40" hcard="18" fillColor="#FFFFFF" :txt="`${(precentBase['6']['1'] + precentBase['6']['2']) * 100}%`"></player>
                    </div>

                </div>

                <div class="top3">
                    <top3></top3>

                    <div class="players">
                        <player wcard="40" hcard="18" fillColor="#ff0000" txt="52%"></player>
                        <player wcard="40" hcard="18" fillColor="#5C7CFA" txt="2"></player>
                        <player wcard="40" hcard="18" fillColor="#FCC419" txt="77%"></player>
                        <player wcard="40" hcard="18" fillColor="#94D82D" txt="4"></player>
                        <player wcard="40" hcard="18" fillColor="#CC5DE8" txt="5"></player>
                        <player wcard="40" hcard="18" fillColor="#FFFFFF" txt="15%"></player>
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