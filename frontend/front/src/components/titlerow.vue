<template>
    <div style="background-color: black;" class="titlerow">
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
.titlerow{
    display: flex;
    justify-content: center;
    align-items: center;
    border: solid 2px white;
    border-radius: 10px;
    font-size: 14pt;
    width: 40px;
    height: 40px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    color: white;
}
</style>