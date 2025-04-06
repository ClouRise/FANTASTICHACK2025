<template>
    <div class="map">
        <section id="widthTrack" class="road">
            <div class="roadroad">
                <player id="player1" :style="'position: absolute; z-index: 3; transition: left 0.1s linear; left: '+ (100-racers['1']['distance'])+'%'" :fillColor="racers['1']['color']"
                    txt="1"></player>
                <p>1</p>
            </div>
        </section>
        <section class="road">
            <div class="roadroad">
                <player id="player2" :style="'position: absolute; z-index: 3; transition: left 0.1s linear; left: '+ (100-racers['2']['distance'])+'%'" :fillColor="racers['2']['color']"
                    txt="2"></player>
                <p>2</p>
            </div>
        </section>
        <section class="road">
            <div class="roadroad">
                <player id="player3" :style="'position: absolute; z-index: 3; transition: left 0.1s linear; left: '+ (100-racers['3']['distance'])+'%'" :fillColor="racers['3']['color']"
                    txt="3"></player>
                <p>3</p>
            </div>
        </section>
        <section class="road">
            <div class="roadroad">
                <player id="player1" :style="'position: absolute; z-index: 3; transition: left 0.1s linear; left: '+ (100-racers['4']['distance'])+'%'" :fillColor="racers['4']['color']"
                    txt="4"></player>
                <p>4</p>
            </div>
        </section>
        <section class="road">
            <div class="roadroad">
                <player id="player1" :style="'position: absolute; z-index: 3; transition: left 0.1s linear; left: '+ (100-racers['5']['distance'])+'%'" :fillColor="racers['5']['color']"
                    txt="5"></player>
                <p>5</p>
            </div>
        </section>
        <section class="road">
            <div class="roadroad">
                <player id="player1" :style="'position: absolute; z-index: 3; transition: left 0.1s linear; left: '+ (100-racers['6']['distance'])+'%'" :fillColor="racers['6']['color']"
                    txt="6"></player>
                <p>6</p>
            </div>
        </section>
        <div class="finish"></div>
    </div>
</template>

<script>
import player from './player.vue';
export default {
    data() {
        return {
            widthTrack: 0,
        }
    },
    components: {
        player
    },
    props: {
        racers: {
            type: Object,
            required: true
        }
    },
    mounted() {
        this.widthTrack = document.getElementById('widthTrack').clientWidth
    },
    methods: {
        movePlayer() {
            const player1 = document.getElementById('player1')
            const player2 = document.getElementById('player2')
            const player3 = document.getElementById('player3')
            const player4 = document.getElementById('player4')
            const player5 = document.getElementById('player5')
            const player6 = document.getElementById('player6')
        }
    },
    watch: {
        racers() {
            this.movePlayer()
        }
    }
}
</script>

<style scoped>
.map {
    width: 100%;
    height: 265px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    position: relative;
}

.road {
    background-color: rgb(108, 45, 45);
    border-top: 1px solid white;
    border-bottom: 1px solid white;
    border-left: 5px solid rgb(221, 221, 221);
    width: 95%;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: start;
}
.roadroad{
    width: 92%;
    height: 40px;
    display: flex;
    position: absolute;
    align-items: center;
}
.road p {
    margin-left: 10px;
    font-size: 30px;
    color: rgb(224, 224, 224);
    font-family: rubicDirt;
}

.finish {
    background-image: url(../assets/img/title-finish.svg);
    background-size: 28px;
    width: 70px;
    height: 100%;
    position: absolute;
    right: 0;
}
</style>