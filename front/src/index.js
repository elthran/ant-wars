import Vue from 'vue'
import VueKonva from 'vue-konva'

import App from './App'


Vue.use(VueKonva)

new Vue({
  el: '#app',
  components: { App },
  render (h) {
    return h('app')
  },
});
