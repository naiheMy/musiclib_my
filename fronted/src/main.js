import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';
import router from './router'
import VueParticles from 'vue-particles'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(VueParticles)
Vue.config.productionTip = false

Vue.use(ElementUI);
axios.defaults.baseURL = 'http://localhost:5000';

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
