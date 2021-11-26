<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <TransitionRoot as="template" :show="isOpen">
    <Dialog as="div" class="fixed z-50 inset-0 overflow-hidden" @close="$emit('closeSlide')">
      <div class="absolute inset-0 overflow-hidden">
        <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in-out duration-500" leave-from="opacity-100" leave-to="opacity-0">
          <DialogOverlay class="absolute inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
        <div class="fixed inset-y-0 right-0 pl-10 max-w-full flex">
          <TransitionChild as="template" enter="transform transition ease-in-out duration-500 sm:duration-700" enter-from="translate-x-full" enter-to="translate-x-0" leave="transform transition ease-in-out duration-500 sm:duration-700" leave-from="translate-x-0" leave-to="translate-x-full">
            <div class="relative w-screen max-w-md">
              <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in-out duration-500" leave-from="opacity-100" leave-to="opacity-0">
                <div class="absolute top-0 left-0 -ml-8 pt-4 pr-2 flex sm:-ml-10 sm:pr-4">
                  <button type="button" class="rounded-md text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white" @click="$emit('closeSlide')">
                    <span class="sr-only">Close panel</span>
                    <XIcon class="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>
              </TransitionChild>
              <div class="h-full flex flex-col py-6 bg-white shadow-xl overflow-y-scroll">
                <div class="px-4 sm:px-6">
                  <DialogTitle class="text-lg font-medium text-gray-900">
                    My Profile
                  </DialogTitle>
                </div>
                <div class="mt-6 relative flex-1 px-4 sm:px-6">
                  <!-- Replace with your content -->
                  <div class="absolute inset-0 px-4 sm:px-6">
                    <div class="border-2 border-dashed border-gray-200" aria-hidden="true">
                      <form action="#" method="POST">
                        <div class="bg-white px-4 pb-4 sm:px-6 sm:pb-4">
                          <div class="sm:flex sm:items-start">
                            <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                              <div class="pr-4 py-5 bg-white sm:py-6">
                                <h5 class="mb-3">Personal Info:</h5>
                                <div class="grid grid-cols-6 gap-4">
                                  <div class="col-span-6 sm:col-span-3">
                                    <label for="first-name" class="block text-sm font-medium text-gray-700">First Name : {{ this.user.fname }}</label>
                                  </div>

                                  <div class="col-span-6 sm:col-span-3">
                                    <label for="last-name" class="block text-sm font-medium text-gray-700">Last Name : {{ this.user.lname }}</label>
                                  </div>

                                  <div class="col-span-6">
                                    <label for="email-address" class="block text-sm font-medium text-gray-700">Email Address : {{ this.user.email }}</label>
                                  </div>
                                  <div class="col-span-6">
                                        <h5 class="mt-6 mb-3">Connected Platforms:</h5>
                                        <div v-if="user.platforms.length==0">
                                            <span class="text-sm font-medium text-gray-700">None</span>
                                        </div>
                                        <div v-else>
                                            <ul v-for="platform in user.platforms">
                                               <li class="text-sm font-medium text-gray-700">{{platform.charAt(0).toUpperCase() + platform.slice(1)}}: connected</li> 
                                            </ul>
                                        </div>
                                  </div>

                                </div>
                              </div>
                            </div>
                            
                          </div>
                          
                        </div>
                      </form>
                    </div>
                    <div v-if="!user.platforms.some(x => x=='lazada')" class="pb-4 py-8 sm:px-6 sm:flex sm:justify-center">
                      <button type="button" @click="getLazadaLink()" class="w-full rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:w-auto sm:text-sm">
                        Login to LAZADA
                      </button>
                    </div>
                  </div>
                  <!-- /End replace -->
                </div>
              </div>
            </div>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot >
</template>

<script>
import { Dialog, DialogOverlay, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XIcon } from '@heroicons/vue/outline'
import AuthDataService from '../services/AuthDataService'

export default {
  components: {
    Dialog,
    DialogOverlay,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
    XIcon,
  },
  props: [
    'isOpen',
  ],
  data() {
    return {
      user: null,
      lazadaUrl: null,
      name: 'UserDetail',
    } 
  },
  methods: {
      getUser: async function(){
        const response = await AuthDataService.get()
        this.user = response.data
      },
      getLazadaLink: async function(){
        const response = await AuthDataService.loginLazada()
        this.lazadaUrl = response.data
        window.location.href = this.lazadaUrl.url
      },
  },
  mounted: async function(){
      this.getUser()
      // this.getLazadaLink()
      // console.log(user)
  },
}

</script>