<template>
    <div :style="'width: ' + size + 'px!important; height: ' + size + 'px!important'" class="player">        
<svg style="position: absolute;" :fill="fillColor" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg"><g id="Layer_1" data-name="Layer 1"><path d="m38.055 9.906c-.014.069-.028.138-.045.206-.03.127-.065.253-.1.378q-.027.09-.057.18c-.044.127-.093.252-.146.376-.023.055-.045.109-.07.163-.056.123-.118.244-.183.363-.027.051-.054.1-.084.153-.067.117-.14.23-.216.342-.033.048-.064.1-.1.146-.078.108-.16.211-.244.314-.039.047-.076.1-.117.142-.084.1-.174.19-.265.283-.045.046-.089.093-.136.138-.091.086-.186.168-.282.249-.053.044-.1.09-.158.133-.1.075-.2.145-.3.215-.059.041-.117.085-.178.125-.1.064-.2.123-.308.182-.066.037-.13.077-.2.113-.105.054-.213.1-.32.15-.072.032-.141.068-.214.1-.11.045-.224.082-.337.121-.074.025-.146.054-.221.077-.118.035-.239.062-.36.09-.074.018-.146.04-.22.054-.135.027-.273.044-.41.062-.064.008-.126.021-.19.027-.2.02-.408.031-.616.031s-.413-.011-.615-.031c-.066-.006-.128-.019-.193-.028-.136-.017-.272-.034-.406-.06-.078-.016-.153-.038-.23-.057-.117-.027-.234-.053-.348-.087-.081-.025-.159-.056-.239-.083-.107-.037-.214-.071-.317-.114-.081-.032-.159-.071-.238-.107-.1-.045-.2-.089-.293-.138-.079-.041-.154-.087-.23-.131-.092-.053-.184-.1-.272-.162s-.147-.1-.22-.153-.17-.119-.251-.183-.138-.114-.206-.173-.156-.133-.23-.2-.128-.128-.191-.193-.141-.145-.208-.221-.117-.14-.174-.212-.126-.156-.185-.238-.1-.15-.154-.227-.11-.168-.161-.254-.09-.161-.133-.242-.093-.178-.136-.269-.074-.168-.11-.254-.076-.188-.11-.284-.058-.176-.085-.264-.057-.2-.082-.3-.042-.182-.06-.274-.037-.2-.052-.308-.024-.187-.033-.282c0-.051-.014-.1-.017-.152l-8.429 3.916v41.962h29.259v-41.962l-8.465-3.934c0 .059-.015.116-.02.175-.008.082-.016.164-.028.245-.016.124-.037.245-.061.366z"/><path d="m26.529 10.283c.011.038.019.077.031.115a5.494 5.494 0 0 0 .217.56c.053.118.112.232.172.346s.137.242.212.359q.129.2.275.4c.1.128.2.253.308.372.066.073.132.146.2.216a5.576 5.576 0 0 0 .516.455c.06.047.124.091.186.136a5.891 5.891 0 0 0 .608.386l.078.042a5.635 5.635 0 0 0 .708.3c.051.019.1.039.155.056a5.705 5.705 0 0 0 .775.2c.051.009.1.015.155.023a5.2 5.2 0 0 0 1.712 0c.052-.007.1-.014.154-.023a5.6 5.6 0 0 0 .78-.2c.049-.016.1-.034.144-.051a5.737 5.737 0 0 0 1.442-.763c.039-.028.078-.055.116-.084a5.656 5.656 0 0 0 .586-.517c.034-.034.066-.07.1-.105a5.6 5.6 0 0 0 .925-1.319c.022-.044.045-.086.066-.13a5.538 5.538 0 0 0 .283-.732c.005-.017.009-.034.014-.051a8.1 8.1 0 0 1 -5.465 1.705 8.114 8.114 0 0 1 -5.453-1.696z"/><path d="m30.2 14.027c-.053-.017-.1-.037-.155-.056.049.019.099.039.155.056z"/><path d="m29.334 13.666-.078-.042z"/><path d="m33.917 13.975c-.048.017-.095.035-.144.051.049-.016.096-.034.144-.051z"/><path d="m35.475 13.128c-.038.029-.077.056-.116.084.041-.028.078-.055.116-.084z"/><path d="m26.51 10.267c.013.045.036.086.05.131-.012-.038-.02-.077-.031-.115z"/><path d="m31.127 14.245c-.051-.008-.1-.014-.155-.023.052.009.103.015.155.023z"/><path d="m27.436 12.059q-.146-.192-.275-.4c.087.141.177.272.275.4z"/><path d="m32.993 14.222c-.051.009-.1.016-.154.023.052-.008.103-.014.154-.023z"/><path d="m37.151 11.057c-.021.044-.044.086-.066.13.022-.044.045-.087.066-.13z"/><path d="m27.946 12.647c-.07-.07-.136-.143-.2-.216.064.069.129.146.2.216z"/><path d="m37.456 10.267-.008.007c-.005.017-.009.034-.014.051.006-.02.016-.038.022-.058z"/><path d="m28.648 13.238c-.062-.045-.126-.089-.186-.136.061.047.123.091.186.136z"/><path d="m36.16 12.506c-.033.035-.065.071-.1.105.04-.034.067-.07.1-.105z"/><path d="m26.949 11.3c-.06-.114-.119-.228-.172-.346.053.122.111.236.172.346z"/><path d="m13.641 16.505-6.29 12.115 9.519 3.68v-19a7.525 7.525 0 0 0 -3.229 3.205z"/><path d="m50.359 16.505a7.525 7.525 0 0 0 -3.229-3.213v19l9.519-3.677z"/></g></svg>       
<div class="bg" :style="'box-shadow: 1px 1px 8px 1px '+ fillColor + '; width: ' + wcard + 'px; height:' + hcard + 'px; top: ' + topminus + 'px'"> <slot><p :style="'font-size: ' + fontsize + 'px'" class="txt"> {{ txt }} </p></slot></div>

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
        },
        size: {
            type: Number,
            default: () => 40
        },
        wcard: {
            type: Number,
            default: () => 20
        },
        hcard: {
            type: Number,
            default: () => 15
        },
        fontsize: {
            type: Number,
            default: () => 12
        },
        topminus: {
            type: Number,
            default: () => -6
        }
     }   
    }
    
</script>

<style scoped>
.player{
    position: relative;
    display: flex;
    align-items: end;
    justify-content: center;
    box-sizing: border-box;
}
.bg{
    position: relative;
    top: -15px;
    background-color: rgb(0, 0, 0);
    border-radius: 5px;
    color: aliceblue;
    display: flex;
    justify-content: center;
    align-items: center;

}
.txt{
    text-align: center;
    font-family: ubuntu-medium;
}
</style>