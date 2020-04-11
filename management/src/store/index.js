import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        menuList: []
    },
    mutations: {
        setMenu(state, item) {
            state.menuList = item
        }
    }

})
export default store
