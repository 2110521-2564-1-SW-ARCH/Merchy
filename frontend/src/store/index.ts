import {Commit, createStore} from 'vuex'

export default createStore({
    state: {
        authenticated: true,
        isOpen: false,
    },
    mutations: {
        SET_AUTH: (state, auth) => state.authenticated = auth,
        SET_MODAL: (state, isOpen) => state.isOpen = isOpen
    },
    actions: {
        setAuth: ({commit}, auth) => commit('SET_AUTH', auth),
        setModal: ({commit}, isOpen) => commit('SET_MODAL', isOpen)
    },
    modules: {}
})