<template>
    <div style="display: flex; flex-direction: row; justify-content: start; width: 100%; height: 100%;">
        <article>
            <div style="height: 25px;" class="cell-table"></div>
            <div class="cell-table"><titlerow style="box-shadow: #EFDE22 0px 0px 5px 3px" num="1"></titlerow></div>
            <div class="cell-table"><titlerow style="box-shadow: #7A7A81 0px 0px 5px 3px" num="2"></titlerow></div>
            <div class="cell-table"><titlerow style="box-shadow: #FF77004D 0px 0px 5px 3px" num="3"></titlerow></div>
            <div class="cell-table"><titlerow num="4"></titlerow></div>
            <div class="cell-table"><titlerow num="5"></titlerow></div>
            <div style="border: none;" class="cell-table"><titlerow num="6"е5></titlerow></div>
        </article>
        <div class="scroll-container" style="overflow-x: scroll; display: flex; flex-direction: row;">
            <section v-for="(sect, id) in arr" :key="id">
                <div style="height: 25px;" class="cell-table"><h4>№{{id + 1}}</h4></div>
                <div v-for="(elem, ind) in sect" :key="ind" :style="id == 6 ? 'border: none' : ''" style="padding-block: 15px; width: 60px; height: 45px;" class="cell-table"><player :fillColor="returnColor(elem[0])" :txt="elem[0]"></player></div>
            </section>
        </div>
    </div>
</template>

<script>
import titlerow from './titlerow.vue';
import player from './player.vue';
import store from '@/store';
import { ref } from 'vue';
export default {
    components: {
        titlerow,
        player
    },
    data(){
        return{
            arr: store.state.arrOfRaced
        }
    },
    watch: {
        arr(){
            console.log('2345')
        }
    },
    methods: {
        returnColor(id){
            if(id == 1){
                return "#ff0000"
            }
            if(id == 2){
                return "#5C7CFA"
            }
            if(id == 3){
                return "#FCC419"
            }
            if(id == 4){
                return "#94D82D"
            }
            if(id == 5){
                return "#CC5DE8"
            }
            if(id == 6){
                return "#FFFFFF"
            }
        }
    }
}
</script>

<style scoped>
h4{
    font-family: ubuntu-medium;
    color: white;
}
article{
    display: flex;
    flex-direction: column;
    margin-left: 15px;
}
.cell-table{
    padding-block: 22px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 1pt solid rgb(46, 46, 46);
    height: 40px;
}
section{
    display: flex;
    flex-direction: column;
}
.scroll-container {
    overflow-x: auto;
    display: flex;
    flex-direction: row;
}
.scroll-container::-webkit-scrollbar {
    height: 0px;
}

.scroll-container::-webkit-scrollbar-track {
    background: #2e2e2e; /* Цвет фона дорожки */
    border-radius: 4px;
}

.scroll-container::-webkit-scrollbar-thumb {
    background-color: #888; /* Цвет ползунка */
    border-radius: 4px;
}

.scroll-container::-webkit-scrollbar-thumb:hover {
    background-color: #aaa; /* Цвет при наведении */
}
</style>