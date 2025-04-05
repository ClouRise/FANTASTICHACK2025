    <template>
        <div class="card">
            <div :style="buttonRace ? 'justify-content: space-between;' : 'justify-content: start;'" class="header">
                <h2>{{ title }}</h2>
                <button v-if="buttonRace">Старт</button>
            </div>
            <div class="main">
                <slot></slot>
            </div>
        </div>
    </template>

<script>
export default {
    props: {
        title: {
            type: String,
            required: true
        },
        buttonRace: {
            type: Boolean,
            default: false
        }
    }
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
    padding: 10px;
    padding-bottom: 15px;
    box-sizing: border-box;
}

button {
    border-radius: 0px;
    border: 1px solid #8a8a8a;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    background-color: #1D1D1D;
    font-family: ubuntu-regular;
    font-size: 15px;
    padding: 5px 20px;
}
</style>