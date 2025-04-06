<template>
    <div class="bigcontainer">

    
        <div class="container">

            <div class="num num-1">
                <titlerow style="width: 25px; height: 25px; border-radius: 8px; box-shadow: #EFDE22 0px 0px 3px 2px" num="1"></titlerow>
            </div>

            <div class="num num-2">
                <titlerow style="width: 25px; height: 25px; border-radius: 8px; box-shadow: #FF77004D 0px 0px 3px 2px" num="3"></titlerow>
        </div>

        </div>

        <div class="num num-3">
                <titlerow style="width: 25px; height: 25px; border-radius: 8px; box-shadow: #7A7A81 0px 0px 3px 2px" num="2"></titlerow>
            </div>
    </div>
</template>

<script>
import titlerow from './titlerow.vue';
export default {
    components:{
        titlerow
    }
}
</script>

<style scoped>
.bigcontainer{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 70px;
    position: relative;
    overflow: hidden; /* чтобы линия не выходила за границы */
    display: absolute;
    flex-direction: column;
}
.container{
display: flex;
justify-content: space-between;
align-items: center;
width: 70px;
height: 45px;
position: relative;
  overflow: hidden; /* чтобы линия не выходила за границы */
  display: absolute;
}
.num {
position: absolute;
color: #333;
z-index: 1; /* чтобы цифры были поверх линии */
}

.num-1 {
left: 5px;
}

.num-2 {
right: 5px;
}

.num-3 {
bottom: 4px;
}


</style>