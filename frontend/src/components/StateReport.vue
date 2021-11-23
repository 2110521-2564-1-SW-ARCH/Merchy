<template>
    <div class="px-4 my-10">
      <div class="w-full bg-white rounded-xl overflow-hdden shadow-md p-4 undefined">
        <div class="flex flex-wrap border-b border-gray-200 undefined">
          <div v-show="isUp" class="bg-gradient-to-tr from-green-300 to-green-500 -mt-10 mb-4 rounded-xl text-white grid items-center w-24 h-24 py-4 px-4 justify-center shadow-lg mb-0">
            <TrendingUpIcon
              class="w-8 h-8 mr-2 text-green-400e"
              aria-hidden="true"
            />
          </div>
          <div v-show="!isUp" class="bg-gradient-to-tr from-pink-500 to-pink-700 -mt-10 mb-4 rounded-xl text-white grid items-center w-24 h-24 py-4 px-4 justify-center shadow-lg mb-0">
            <TrendingDownIcon
              class="w-8 h-8 mr-2 text-violet-400e"
              aria-hidden="true"
            />
          </div>
          <div class="w-full pl-4 max-w-full flex-grow flex-1 mb-2 text-right undefined">
            <h5 class="text-gray-500 font-light tracking-wide text-base mb-1">
              Traffic
            </h5>
            <span class="text-3xl text-gray-900">
              350,897
            </span>
          </div>
        </div>
        <div class="text-sm text-gray-700 pt-4 flex items-center undefined">
          <ArrowSmUpIcon v-show="isUp"
              class="w-5 h-5 text-green-500"
              aria-hidden="true"
            />
          <ArrowSmDownIcon v-show="!isUp"
            class="w-5 h-5 text-pink-500"
            aria-hidden="true"
          />
          <span v-bind:class="[isUp ? 'text-green-500 ml-1 mr-2': 'text-pink-500 ml-1 mr-2']">
            3.48
          </span>
          <span class="font-light whitespace-nowrap">
            Since last month
          </span>
        </div>
      </div>
    </div>
</template>

<script>
  import { 
    ArrowSmDownIcon,
    TrendingUpIcon,
    ArrowSmUpIcon,
    TrendingDownIcon,
  } from '@heroicons/vue/outline'

  export default {
    components: {
      ArrowSmDownIcon,
      TrendingDownIcon,
      TrendingUpIcon,
      ArrowSmUpIcon,
    },
    props: [
      'isUp'
    ]
  }
</script>
