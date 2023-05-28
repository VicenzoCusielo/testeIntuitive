import {createRouter, createWebHistory} from 'vue-router'
import HomeTeste from './components/HomeTeste.vue'; 
import OperadorasResultado from './components/OperadorasResultado.vue'; 


const routes = [
    {
        path:'/',
        name:'HomeTeste',
        component: HomeTeste
    },
    {
        path:'/pesquisar_operadoras/:campo/:valor_parecido',
        name:'OperadorasResultado',
        component:OperadorasResultado
    }
]
const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;