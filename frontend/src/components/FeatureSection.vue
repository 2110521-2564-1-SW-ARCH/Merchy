<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="pb-40 pt-32 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="lg:text-center">
        <h2 class="text-base text-indigo-600 font-semibold tracking-wide uppercase">Features</h2>
        <p class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
          A better way to management
        </p>
        <p class="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
          Merchy allows the merchants to see all of their orders. Additionally, it provides a stock management system to allow the merchants to easily keep track of their stocks across a variety of platforms.
        </p>
      </div>

      <div class="mt-10">
        <dl class="space-y-10 md:space-y-0 md:grid md:grid-cols-2 md:gap-x-8 md:gap-y-10">
          <div v-for="feature in features" :key="feature.name" class="relative">
            <dt>
              <div class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white">
                <component :is="feature.icon" class="h-6 w-6" aria-hidden="true" />
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900">{{ feature.name }}</p>
            </dt>
            <dd class="mt-2 ml-16 text-base text-gray-500">
              {{ feature.description }}
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </div>
</template>

<script>
import { CollectionIcon, ChartBarIcon, LightningBoltIcon, SearchIcon } from '@heroicons/vue/outline'

const features = [
  {
    name: 'View business revenue',
    description:
      'This feature display incomes and expenses in the timeframe by the user.',  
    icon: ChartBarIcon,
  },
  {
    name: 'Products tracking system',
    description:
      'This feature track all orders that in the merchant’s account.',
    icon: SearchIcon,
  },
  {
    name: 'Order tracking system',
    description:
      'This feature obtain all orders’s tracking numbers from all selling platforms and display their shipping status retrieved via APIs.',
    icon: LightningBoltIcon,
  },
  {
    name: 'Stock management',
    description:
      'This feature allow a user to manually add, delete items and modify the amount of each item and display the stock of each item in the store.',
    icon: CollectionIcon,
  },
]

export default {
    name: 'FeatureSection',
    setup() {
        return {
            features,
        }
    },
}
</script>