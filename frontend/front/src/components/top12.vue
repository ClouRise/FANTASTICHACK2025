<template>
    <div class="diagonal-container">
        <div class="diagonal-line"></div>
        <div class="num num-1">
            <titlerow style="width: 30px; height: 30px; box-shadow: #EFDE22 0px 0px 5px 3px" num="1"></titlerow>
        </div>
        <div class="num num-2">
            <titlerow style="width: 30px; height: 30px; box-shadow: #7A7A81 0px 0px 5px 3px" num="2"></titlerow>
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
  width: 80px;
  height: 80px;
  position: relative;
  overflow: hidden; /* чтобы линия не выходила за границы */
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
  left: 8px;
  bottom: 8px;
}

.num-2 {
  right: 8px;
  top: 8px;
}

</style>