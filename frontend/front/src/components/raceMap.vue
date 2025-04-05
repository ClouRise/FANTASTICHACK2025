<template>
    <div class="map">
        <section class="road">
            <player :style="'position: absolute;'" fillColor="#ff0000" txt="1"></player>
            <p>1</p>
        </section>
        <section class="road">
            <p>2</p>
        </section>
        <section class="road">
            <p>3</p>
        </section>
        <section class="road">
            <p>4</p>
        </section>
        <section class="road">
            <p>5</p>
        </section>
        <section class="road">
            <p>6</p>
        </section>
        <div class="finish"></div>
    </div>
</template>

<script>
import player from './player.vue';
export default {
    components: {
        player
    },
    props: {
        racers: {
            type: Object,
            required: true
        }
    }
}
</script>

<style scoped>
.map {
    width: 100%;
    height: 500px;
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
    width: 100%;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: start;
    position: relative;
}

.road p {
    margin-left: 30px;
    font-size: 40px;
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