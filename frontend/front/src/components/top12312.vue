<template>
    <div>
        <maincard :title="'Вероятность попадения в топ2 или топ3'" style="display: flex; flex-direction: column;">
            <div style="display: flex; justify-content: center; align-items: center;">
                <div class="top2">
                    <top2></top2>

                    <div class="players">
                        <player></player>
                    </div>

                </div>

                <div class="top3">
                    <top3></top3>

                    <div class="players">
                        <player></player>
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
            player
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