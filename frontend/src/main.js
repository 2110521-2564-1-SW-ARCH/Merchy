import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index.ts'
import VueApexCharts from "vue3-apexcharts";
import './index.css'

createApp(App).use(store).use(VueApexCharts).use(router).mount('#app')
