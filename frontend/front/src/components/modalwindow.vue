<template>
   <div class="card">
            <div class="header">
            </div>
            <div class="main">
            </div>
            <div class="header">
            </div>
            <div class="main">
            </div>
            <div class="header">
            </div>
            <div class="main">
            </div>
            <div class="header">
            </div>
            <div class="main">
            </div>
            <div class="header">
            </div>
            <div class="main">
            </div>
        </div>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 20px;
}

.header {
    background-color: #2D2D2D;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: start;
    padding-inline: 35px;
}

.header h2 {
    font-family: ubuntu-bold;
    color: white;
    font-size: 17px;
}

.main {
    background-color: #1D1D1D;
    border-radius: 0 0 15px 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    padding-top: 10px;
    padding-bottom: 15px;
    box-sizing: border-box;
}
</style>