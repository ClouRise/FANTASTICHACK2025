<template>
    <div class="analys">
        <div class="titles-analys">
            <div class="row">
                <titlerow style="box-shadow: #EFDE22 0px 0px 5px 3px" num="1"></titlerow>
            </div>
            <div class="row">
                <titlerow style="box-shadow: #7A7A81 0px 0px 5px 3px" num="2"></titlerow>
            </div>
            <div class="row">
                <titlerow style="box-shadow: #FF77004D 0px 0px 5px 3px" num="3"></titlerow>
            </div>
            <div class="row">
                <titlerow num="4"></titlerow>
            </div>
            <div class="row">
                <titlerow num="5"></titlerow>
            </div>
            <div class="row">
                <titlerow num="6"></titlerow>
            </div>
        </div>
        <div class="scroll-analys">
            <div class="row">
                <div style="height: 40px; width: 40px; ">
                    <player style="margin-inline: 7px;" :size="40" :hcard="15" :wcard="25" :fontsize="12" :topminus="-10" fillColor="#ff0000" txt="1"></player>
                </div>
            </div>
            <div class="row">
                <div style="height: 40px; width: 40px; ">
                    <player style="margin-inline: 7px;" :size="40" :hcard="15" :wcard="25" :fontsize="12" :topminus="-10" fillColor="#ff0000" txt="1"></player>
                </div>
            </div>
            <div class="row">
                <div style="height: 40px; width: 40px; ">
                    <player style="margin-inline: 7px;" :size="40" :hcard="15" :wcard="25" :fontsize="12" :topminus="-10" fillColor="#ff0000" txt="1"></player>
                </div>
            </div>
            <div class="row">
                <div style="height: 40px; width: 40px; ">
                    <player style="margin-inline: 7px;" :size="40" :hcard="15" :wcard="25" :fontsize="12" :topminus="-10" fillColor="#ff0000" txt="1"></player>
                </div>
            </div>
            <div class="row">
                <div style="height: 40px; width: 40px; ">
                    <player style="margin-inline: 7px;" :size="40" :hcard="15" :wcard="25" :fontsize="12" :topminus="-10" fillColor="#ff0000" txt="1"></player>
                </div>
            </div>
            <div class="row">
                <div style="height: 40px; width: 40px; ">
                    <player style="margin-inline: 7px;" :size="40" :hcard="15" :wcard="25" :fontsize="12" :topminus="-10" fillColor="#ff0000" txt="1"></player>
                </div>
            </div>
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
.analys {
    width: 610px;
    display: flex;
    flex-direction: row;
}

.row {
    width: max-content;
    border-bottom: 1pt solid rgb(46, 46, 46);
    display: flex;
    flex-direction: row;
    justify-content: start;
    padding: 5px;
    padding-inline: 15px;
}

.scroll-analys {
    width: auto;
    overflow-x: scroll;
}
</style>