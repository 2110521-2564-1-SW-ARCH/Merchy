<template>

  <Popover class="relative bg-white z-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div class="flex justify-between items-center border-b-2 border-gray-100 py-6 md:justify-start md:space-x-10">
        <div class="flex justify-start lg:w-0 lg:flex-1">
          <router-link to="/">
            <span class="sr-only">Workflow</span>
            <img class="h-8 w-auto sm:h-10" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="" />
          </router-link>
        </div>
        <div class="-mr-2 -my-2 md:hidden">
          <PopoverButton class="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
            <span class="sr-only">Open menu</span>
            <MenuIcon class="h-6 w-6" aria-hidden="true" />
          </PopoverButton>
        </div>
        <PopoverGroup as="nav" class="hidden md:flex space-x-10">

          <a href="#" class="text-base font-medium text-gray-500 hover:text-gray-900">
            Pricing
          </a>
          <a href="#" class="text-base font-medium text-gray-500 hover:text-gray-900">
            Docs
          </a>
        </PopoverGroup>
        <div class="hidden md:flex items-center justify-end md:flex-1 lg:w-0">
          <router-link v-show="!isLogin" to="/login" class="whitespace-nowrap text-base font-medium text-gray-500 hover:text-gray-900">
            Sign in
          </router-link>
          <router-link v-show="!isLogin" to="/register" class="ml-8 whitespace-nowrap inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700">
            Sign up
          </router-link>
          <button v-show="isLogin" @click="logoutUser" class="ml-8 whitespace-nowrap inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700">
            Sign out
          </button>
        </div>
      </div>
    </div>

    <transition enter-active-class="duration-200 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="duration-100 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
      <PopoverPanel focus class="absolute top-0 inset-x-0 p-2 transition transform origin-top-right md:hidden">
        <div class="rounded-lg shadow-lg ring-1 ring-black ring-opacity-5 bg-white divide-y-2 divide-gray-50">
          <div class="flex items-center justify-between pt-5 pb-6 px-5">
            <div>
              <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="Workflow" />
            </div>
            <div class="-mr-2">
              <PopoverButton class="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
                <span class="sr-only">Close menu</span>
                <XIcon class="h-6 w-6" aria-hidden="true" />
              </PopoverButton>
            </div>
          </div>
          <div class="py-6 px-5 space-y-6">
            <router-link v-show="!isLogin" to="/register" class="w-full flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700">
              Sign up
            </router-link>
            <p v-show="!isLogin" class="mt-6 text-center text-base font-medium text-gray-500">
              Existing customer?
              {{ ' ' }}
              <router-link to="/login" class="text-indigo-600 hover:text-indigo-500">
                Sign in
              </router-link>
            </p>
            <button v-show="isLogin" @click="logoutUser" class="w-full flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700">
              Sign Out
            </button>
          </div>
        </div>
      </PopoverPanel>
    </transition>
  </Popover>

</template>

<script>
import { useStore } from "vuex";
import axios from 'axios';
import {
  MenuIcon,
  XIcon,
} from '@heroicons/vue/outline'
import { Popover, PopoverButton, PopoverGroup, PopoverPanel } from '@headlessui/vue'

export default {
    name: "Navbar",
    components: {
      Popover,
      PopoverButton,
      PopoverGroup,
      PopoverPanel,
      MenuIcon,
      XIcon,
    },
    computed: {
      isLogin() {
        const store = useStore()
        return store.state.authenticated
      }
    },
    methods: {
      async logoutUser(e){
        const store = useStore()
        e.preventDefault()
        try {
          await axios.post('http://localhost:3000/api/user/logout',
            {email: this.email, password: this.password},
            {withCredentials: true}
          ).then((res) => {
              console.log(res)
          })

          await store.dispatch('setAuth', false)
          this.$router.push('/');

        } catch (e) {
            this.message = "e" + error
        }
      }
    }
};
</script>