<template>
    <div style="display: flex; flex-direction: row; justify-content: start; width: 100%; height: 100%;">
        <article>
            <div style="height: 25px;" class="cell-table"></div>
            <div class="cell-table"><titlerow style="box-shadow: #EFDE22 0px 0px 5px 3px" num="1"></titlerow></div>
            <div class="cell-table"><titlerow style="box-shadow: #7A7A81 0px 0px 5px 3px" num="2"></titlerow></div>
            <div class="cell-table"><titlerow style="box-shadow: #FF77004D 0px 0px 5px 3px" num="3"></titlerow></div>
            <div class="cell-table"><titlerow num="4"></titlerow></div>
            <div class="cell-table"><titlerow num="5"></titlerow></div>
            <div style="border: none; padding-bottom: 0;" class="cell-table"><titlerow num="6"е5></titlerow></div>
        </article>
        <div style="overflow-x: scroll; display: flex; flex-direction: row;">
            <section>
                <div style="height: 25px;" class="cell-table"><h4>№1</h4></div>
                <div style="padding-block: 15px; width: 70px; height: 55px;" class="cell-table"><player fillColor="#ff0000" txt="1"></player></div>
                <div style="padding-block: 15px; width: 70px; height: 55px;" class="cell-table"><player fillColor="#ff0000" txt="1"></player></div>
                <div style="padding-block: 15px; width: 70px; height: 55px;" class="cell-table"><player fillColor="#ff0000" txt="1"></player></div>
                <div style="padding-block: 15px; width: 70px; height: 55px;" class="cell-table"><player fillColor="#ff0000" txt="1"></player></div>
                <div style="padding-block: 15px; width: 70px; height: 55px;" class="cell-table"><player fillColor="#ff0000" txt="1"></player></div>
                <div style="padding-block: 15px; width: 70px; height: 55px; border: none;" class="cell-table"><player fillColor="#ff0000" txt="1"></player></div>
            </section>
        </div>
    </div>
</template>

<script>
import titlerow from './titlerow.vue';
import player from './player.vue';
export default {
    components: {
        titlerow,
        player
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
    padding-block: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 1pt solid rgb(46, 46, 46);
}
section{
    display: flex;
    flex-direction: column;
}
</style>