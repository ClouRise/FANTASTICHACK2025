<template>
    <div class="player">        
        <svg style="position: absolute;" :fill="fillColor" xmlns="http://www.w3.org/2000/svg" id="Layer_2" enable-background="new 0 0 32 32" viewBox="0 0 32 32"><g><path d="m26.90997.58997c-.17999-.35999-.54998-.58997-.94995-.58997h-5.12c-.59002 0-1.07.47998-1.07 1.07001l.01001.00995c-.01001 2.08001-1.70001 3.76001-3.78003 3.76001s-3.77002-1.67999-3.78003-3.76001c0-.00995.01001-.00995.01001-.00995 0-.59003-.47998-1.07001-1.07001-1.07001h-5.12c-.39996 0-.76995.22998-.94994.58997l-4.98004 9.84003c-.22998.46002-.09998 1.02002.31 1.33002l4.56 3.46997v15.70001c0 .58997.48004 1.07001 1.06 1.07001h19.92004c.57996 0 1.06-.48004 1.06-1.07001v-15.70002l4.56-3.46997c.40997-.31.53998-.87.31-1.33002z"/></g></svg>
        <div class="text"> <p style="font-size: 6pt; text-align: center;"> {{ txt }} </p></div>
    </div>

</template>

<script>
    export default {
     props: {
        fillColor :{
            type: String,
            required: true
        },
        txt:{
            type: Number
        }
     }   
    }
    
</script>

<style scoped>
.player{
    width: 30px;
    height: 30px;
    position: relative;
    display: flex;
    align-items: end;
}
.text{
    position: relative;
    top: -4px;
    width: 50px;
    height: 10px;
    background-color: black;
    border-radius: 5px;
    color: aliceblue;
}
</style>