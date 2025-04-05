<template>
        <div class="diagonal-container">
        <div class="diagonal-line"></div>
        <div class="num num-1">
            <titlerow style="width: 25px; height: 25px; border-radius: 8px; box-shadow: #EFDE22 0px 0px 3px 2px" num="1"></titlerow>
        </div>
        <div class="num num-2">
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
.diagonal-container {
  width: 60px;
  height: 60px;
  position: relative;
  overflow: hidden; /* чтобы линия не выходила за границы */
  display: absolute;
}

.diagonal-line {
  position: absolute;
  width: 140%; /* длина линии = диагональ квадрата */
  height: 1px;
  background: #353434;
  left: -20%;
  top: 50%;
  transform: 
    translateY(-50%) 
    rotate(45deg); /* поворот на 45 градусов */
  transform-origin: center;
}

.num {
  position: absolute;
  color: #333;
  z-index: 1; /* чтобы цифры были поверх линии */
}

.num-1 {
  left: 5px;
  bottom: 5px;
}

.num-2 {
  right: 5px;
  top: 5px;
}


</style>