import { fetchInfo } from './apiService.js'
const app = Vue.createApp({
    data() {
        return { count: 0 }
    },
    methods: {
        refresh() {
            console.log(fetchInfo('/api/v1/status-details'))
        }
    },
    template: document.getElementById('dashboard-template').innerHTML
})
app.mount('#app')
