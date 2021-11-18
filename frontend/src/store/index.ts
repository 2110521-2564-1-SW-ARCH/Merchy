import {Commit, createStore} from 'vuex'

export default createStore({
    state: {
        authenticated: true,
    },
    mutations: {
        SET_AUTH: (state, auth) => state.authenticated = auth
    },
    actions: {
        setAuth: ({commit}, auth) => commit('SET_AUTH', auth)
    },
    modules: {}
})