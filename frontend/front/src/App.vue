<script>
</script>

<template>
  <div class="app">
    <header>

    </header>
    <main>

    </main>
  </div>
</template>

<style scoped>
.app{
  width: 100%;
  height: 100%;
  overflow: none;
  position: fixed;
  display: grid;
  grid: 70px auto / 100%
}
header{
  background-color: #42424A;
  box-shadow: 0px 4px 4px 0 black;
}
main{
  background-color: aqua;
  background-image: url(./assets/img/bg.jpeg);
  background-size: cover;
}
main::after {
  content: '';
  position: absolute;
  top: 0;
  background: #4E505666; 
  width: 100%;
  height: 100%;
}
</style>
