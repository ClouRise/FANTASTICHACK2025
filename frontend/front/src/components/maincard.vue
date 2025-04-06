    <template>
        <div class="card">
            <div
                class="header"
                :style="{
                    height: customHeaderHeight ? customHeaderHeight + 'px' : '40px',
                    justifyContent: buttonRace ? 'space-between' : 'start'
                }"
                >
                <h2>{{ title }}</h2>
                <slot name="header-extension"></slot>
                <button v-if="buttonRace" @click="this.$emit('toggleRace')">Старт</button>
                
            </div>
            <div :style="id==1 ? 'padding-top: 7px; padding-bottom: 8px' : ''" class="main">
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
        },
        id: {
            type: Number,
            required: true
        },
        customHeaderHeight: {
            type: Number,
            default: null
        },
    }
}
</script>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 5px;
}

.header {
    background-color: #2D2D2D;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: start;
    padding-inline: 25px;
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
    padding-block: 5px;
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