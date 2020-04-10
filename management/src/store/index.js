import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        menuItems: [
            {
                name: "user",
            }
        ]
    },
    mutations: {
        setMenu(state, items) {
            state.menuItems = [...items]
        }
    }

})
export default store
