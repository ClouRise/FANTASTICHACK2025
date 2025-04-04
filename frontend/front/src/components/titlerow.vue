<template>
    <div style="background-color: black;" class="row">
        <p>{{ num }}</p>
    </div>
</template>

<script>
    export default {
        props:{
            num:{
                type: Number
            }
        }
    }
</script>

<style scoped>
.row{
    display: flex;
    justify-content: center;
    align-items: center;
    border: solid 2px white;
    border-radius: 10px;
    text-align: center;
    font-size: 14pt;
    width: 40px;
    height: 40px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    color: white;
    margin-bottom: 15px;
}
</style>