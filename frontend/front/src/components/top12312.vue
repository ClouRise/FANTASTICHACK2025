<template>
    <div>
        <maincard
  :title="'Вероятность попадения в топ2/топ3'"
  :customHeaderHeight="70"
  style="display: flex; flex-direction: column; max-width: 160px;"
>
            <div style="display: flex; justify-content: center; align-items: center;">
                <div class="top2">
                    <top2></top2>

                    <div class="players">
                        <player fillColor="#ff0000" txt="52%"></player>
                        <player fillColor="#5C7CFA" txt="2"></player>
                        <player fillColor="#FCC419" txt="77%"></player>
                        <player fillColor="#94D82D" txt="4"></player>
                        <player fillColor="#CC5DE8" txt="5"></player>
                        <player fillColor="#FFFFFF" txt="15%"></player>
                    </div>

                </div>

                <div class="top3">
                    <top3></top3>

                    <div class="players">
                        <player fillColor="#ff0000" txt="1"></player>
                        <player fillColor="#5C7CFA" txt="2"></player>
                        <player fillColor="#FCC419" txt="3"></player>
                        <player fillColor="#94D82D" txt="4"></player>
                        <player fillColor="#CC5DE8" txt="5"></player>
                        <player fillColor="#FFFFFF" txt="6"></player>
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
    export default {
        components:{
            maincard,
            top2,
            top3,
            player,
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