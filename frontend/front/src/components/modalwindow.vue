<template>
   <div class="card">

            <div class="row">
                <div class="header">
                    <h2> Игрок </h2>
                </div>


                <div class="main">
                    <player fillColor="#ff0000" txt="1" ></player>
                    <player fillColor="#5C7CFA" txt="2" ></player>
                    <player fillColor="#FCC419" txt="3" ></player>
                    <player fillColor="#94D82D" txt="4" ></player>
                    <player fillColor="#CC5DE8" txt="5" ></player>
                    <player fillColor="#ffffff" txt="6" ></player>
                </div>

            </div>

            <div class="row">
                <div class="header">
                    <h2> Время реакции на старте, c </h2>
                </div>


                <div class="main">
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                </div>

            </div>

            <div class="row">
                <div class="header">
                    <h2> Ускорение, <br> м/c </h2>
                </div>


                <div class="main">
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                </div>

            </div>

            <div class="row">
                <div class="header">
                    <h2> Макс. скорость, <br> м/c </h2>
                </div>


                <div class="main">
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                </div>

            </div>

            <div class="row">
                <div class="header">
                    <h2> Коэффициент потери скорости </h2>
                </div>


                <div class="main">
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                    <inputcomp></inputcomp>
                </div>

            </div>  

        
        </div>
</template>

<script>
import player from './player.vue';
import inputcomp from './inputcomp.vue';
    export default {
        components:{
            player,
            inputcomp
        }
    }
</script>

<style scoped>
.card {
    display: flex;
    flex-direction: row;
    padding: 20px;
}

.header {
    background-color: #2D2D2D;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 120px;
    min-width: 90px;
    padding-inline: 5px;
}

.header h2 {
    font-family: ubuntu-bold;
    color: white;
    font-size: 15px;
    text-align: center;
}

.main {
    background-color: #1D1D1D;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    padding-top: 10px;
    padding-bottom: 15px;
    box-sizing: border-box;
    flex-direction: column;
}
.row{
    display: flex;
    flex-direction:column;
}
</style>