<!-- <template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style> -->

<template>
  <Navbar v-show='notRegisterPageOrLoginPage'/>
  <router-view/>
  <Footer v-show='notRegisterPageOrLoginPage'/>

</template>

<script>
import Footer from './components/Footer'
import Navbar from './components/Navbar'
import AuthDataService from './services/AuthDataService'
import store from './store/index.ts'

export default {
  components: {
    Navbar,
    Footer,
  },
  computed: {
    notRegisterPageOrLoginPage() {
      if(this.$route.path !== '/login' && this.$route.path !== '/register') {
        return true
      } else {
        return false
      }
    },
  },
  beforeMount: async function() {
    try {
      const response = await AuthDataService.get()
      console.log("response", response)
      if (response.status != 200) {
        this.$router.push('/');
      } if (response.data.message == "Unauthorized") {
        this.$router.push('/');
      }else {
        store.dispatch('setAuth', true)
      }
    } catch (e) {
      console.log(e)
    }
  }
}
</script>

