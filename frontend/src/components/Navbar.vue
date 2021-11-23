<template>

  <Popover class="relative bg-white z-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div class="flex justify-between items-center border-b-2 border-gray-100 py-3 md:justify-start md:space-x-10">
        <div class="flex justify-start lg:w-0 lg:flex-1">
          <router-link to="/">
            <span class="sr-only">Workflow</span>
            <img class="h-10 w-auto sm:h-10" src="../assets/Merchy.png" alt="" />
          </router-link>
        </div>
        <div class="-mr-2 -my-2 md:hidden">
          <PopoverButton class="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
            <span class="sr-only">Open menu</span>
            <MenuIcon class="h-6 w-6" aria-hidden="true" />
          </PopoverButton>
        </div>
        <PopoverGroup v-show="!isLogin" as="nav" class="hidden md:flex space-x-10">

          <router-link to="/" class="text-base font-medium text-gray-500 hover:text-gray-900">
            Pricing
          </router-link>
          <router-link to="/" class="text-base font-medium text-gray-500 hover:text-gray-900">
            Docs
          </router-link>
        </PopoverGroup>
        <PopoverGroup v-show="isLogin" as="nav" class="hidden md:flex space-x-10">
          <router-link to="/item" class="text-base font-medium text-gray-500 hover:text-gray-900">
            Stock
          </router-link>
          <router-link to="/order" class="text-base font-medium text-gray-500 hover:text-gray-900">
            Order
          </router-link>
          <router-link to="/status" class="text-base font-medium text-gray-500 hover:text-gray-900">
            Accounting
          </router-link>
        </PopoverGroup>
        <div class="hidden md:flex items-center justify-end md:flex-1 lg:w-0">
          <router-link v-show="!isLogin" to="/login" class="whitespace-nowrap text-base font-medium text-gray-500 hover:text-gray-900">
            Sign in
          </router-link>
          <router-link v-show="!isLogin" to="/register" class="ml-8 whitespace-nowrap inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700">
            Sign up
          </router-link>
          <!-- <button v-show="isLogin" @click="logoutUser" class="ml-8 whitespace-nowrap inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700">
            Sign out
          </button> -->
          <Menu v-show="isLogin" as="div" class="h-full relative">
            <div>
              <MenuButton class="bg-gray-800 flex text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
                <span class="sr-only">Open user menu</span>
                <img class="h-8 w-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
              </MenuButton>
            </div>
            <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
              <MenuItems class="origin-top-right absolute right-0 mt-2 w-40 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
                <MenuItem v-slot="{ active }">
                  <button @click='openSlide = true' :class="[active ? 'bg-gray-100' : '', 'group flex rounded-md items-center w-full px-4 py-2 text-sm text-gray-700']">
                    <PencilIcon
                        :active="active"
                        class="w-5 h-5 mr-2 text-violet-400"
                        aria-hidden="true"
                    />
                    My Profile
                  </button>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <button @click='logoutUser' :class="[active ? 'bg-gray-100' : '', 'group flex rounded-md items-center w-full px-4 py-2 text-sm text-gray-700']">
                    <LogoutIcon
                        :active="active"
                        class="w-5 h-5 mr-2 text-violet-400"
                        aria-hidden="true"
                    />
                    Sign Out
                  </button>
                </MenuItem>
              </MenuItems>
            </transition>
          </Menu>
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
    <SlideOver :is-open='openSlide' v-on:close-slide="openSlide = false"/>
  </Popover>

</template>

<script>
import store from '../store/index.ts'
import axios from 'axios';
import {
  MenuIcon,
  XIcon,
} from '@heroicons/vue/outline'
import { 
  Popover, 
  PopoverPanel,
  PopoverButton, 
  PopoverGroup, 
  PopoverPanelDisclosure, 
  Menu, 
  MenuButton, 
  MenuItem, 
  MenuItems,
} from '@headlessui/vue'
import SlideOver from '../components/SlideOver'
import { 
  ChevronDownIcon,
  TrashIcon,
  PencilIcon,
} from '@heroicons/vue/solid'
import { 
  LogoutIcon,
} from '@heroicons/vue/outline'
import AuthDataService from "../services/AuthDataService"

export default {
    components: {
      TrashIcon,
      ChevronDownIcon,
      PencilIcon,
      LogoutIcon,

      Menu,
      MenuButton,
      MenuItem,
      MenuItems,

      SlideOver,
      Popover,
      PopoverButton,
      PopoverGroup,
      PopoverPanel,
      MenuIcon,
      XIcon,
    },
    data() {
      return {
        openSlide: false,
      }
    },
    computed: {
      isLogin () {
        return store.state.authenticated
      }
    },
    methods: {
      async logoutUser(e){
        e.preventDefault()
        try {
          const response = await AuthDataService.logout()
          if (response.status != 200) {
            alert("something wrong")
          } else {
            store.dispatch('setAuth', false)
            this.$router.push('/');
          }

        } catch (e) {
          this.message = "e" + error
        }
      }
    }
};
</script>