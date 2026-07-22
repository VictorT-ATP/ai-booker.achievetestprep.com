import { fetchInfo } from './apiService.js'
const app = Vue.createApp({
    data() {
        return { agentId: '',
        agents: []}
    },
    methods: {
        async refresh(agentId) {
            const response = await fetchInfo('/api/v1/status-details/' + agentId)
            console.log(response)
        }
    },
    async mounted() {
        this.agents = await fetchInfo('/api/v1/agents')
        if(this.agents.length > 0) this.agentId = this.agents[0].id
    },
    template: document.getElementById('dashboard-template').innerHTML
})
app.mount('#app')
