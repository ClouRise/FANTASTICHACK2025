import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import { Store } from 'vuex'
import store from './store'
const app = createApp(App)

app.use(store)
app.mount('#app')
