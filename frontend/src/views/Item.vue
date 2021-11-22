<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class=" flex flex-col">
    <div class="my-10 overflow-x-auto sm:mx-12 lg:mx-16">
      <div class="align-middle inline-block min-w-full">
        <div class="shadow overflow-hidden border-2 border-gray-200 sm:rounded-lg">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Platform
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Category
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Name
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Brand
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Model
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Price
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Quantity
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="not-sr-only sm:sr-only">Actions</span>
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="item in Mock_items" :key="item.id">
                  <td class="px-6 py-4 whitespace-nowrap">
                    {{ item.platform }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    {{ item.primaryCategory }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    {{ item.attributes.name }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ item.attributes.brand }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <ul v-for="sku in item.skus" class="list-disc" :key="sku.id">
                        {{sku.sellerSku}}
                    </ul>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <ul v-for="sku in item.skus" class="list-disc" :key="sku.id">
                        {{sku.price}} ฿ 
                    </ul>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <ul v-for="sku in item.skus" class="list-disc" :key="sku.id">
                        {{sku.quantity}} Pieces
                    </ul>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <button @click="isOpen = true" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800 hover:bg-green-500  active:bg-green-800">
                      Click me
                    </button>
                  </td>
                </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <Modal :is-open='isOpen' v-on:close-modal="isOpen = false">
      <form action="#" method="POST">
        <div class="bg-white px-4 pt-5 pb-4 sm:px-6 sm:pb-4">
          <div class="sm:flex sm:items-start">
            <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
              <DialogTitle as="h3" class="text-lg leading-6 font-medium text-gray-900">
                Edit item
              </DialogTitle>
              <div class="mt-2">
                <div class="pr-4 py-5 bg-white sm:py-6">
                  <div class="grid grid-cols-6 gap-6">
                    <div class="col-span-6 sm:col-span-3">
                      <label for="first-name" class="block text-sm font-medium text-gray-700">First name</label>
                      <input type="text" name="first-name" id="first-name" autocomplete="given-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>

                    <div class="col-span-6 sm:col-span-3">
                      <label for="last-name" class="block text-sm font-medium text-gray-700">Last name</label>
                      <input type="text" name="last-name" id="last-name" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>

                    <div class="col-span-6 sm:col-span-4">
                      <label for="email-address" class="block text-sm font-medium text-gray-700">Email address</label>
                      <input type="text" name="email-address" id="email-address" autocomplete="email" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>

                    <div class="col-span-6 sm:col-span-3">
                      <label for="country" class="block text-sm font-medium text-gray-700">Country</label>
                      <select id="country" name="country" autocomplete="country-name" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                        <option>United States</option>
                        <option>Canada</option>
                        <option>Mexico</option>
                      </select>
                    </div>

                    <div class="col-span-6">
                      <label for="street-address" class="block text-sm font-medium text-gray-700">Street address</label>
                      <input type="text" name="street-address" id="street-address" autocomplete="street-address" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>

                    <div class="col-span-6 sm:col-span-6 lg:col-span-2">
                      <label for="city" class="block text-sm font-medium text-gray-700">City</label>
                      <input type="text" name="city" id="city" autocomplete="address-level2" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>

                    <div class="col-span-6 sm:col-span-3 lg:col-span-2">
                      <label for="region" class="block text-sm font-medium text-gray-700">State / Province</label>
                      <input type="text" name="region" id="region" autocomplete="address-level1" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>

                    <div class="col-span-6 sm:col-span-3 lg:col-span-2">
                      <label for="postal-code" class="block text-sm font-medium text-gray-700">ZIP / Postal code</label>
                      <input type="text" name="postal-code" id="postal-code" autocomplete="postal-code" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
          <button type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm" @click="isOpen = false">
            Save
          </button>
          <button type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm" @click="isOpen = false" ref="cancelButtonRef">
            Cancel
          </button>
        </div>
      </form>
    </Modal>
  </div>
</template>



<script>
import InventoryDataService from '../services/InventoryDataService'
import Modal from '../components/Modal'
import {
  DialogTitle,
} from '@headlessui/vue'

const Mock_items = [
  {
    id: "213133",
    platform: "lazada",
    primaryCategory: "666",
    attributes: {
      name: "atr_name",
      brand: "gucci",
    },
    skus: [
      {
        id: "01",
        sellerSku: "ssku",
        price: "100",
        quantity: "a lot"
      },
      {
        id: "02",
        sellerSku: "ssku",
        price: "100",
        quantity: "a lot"
      }
    ]
  },
  {
    id: "01",
    platform: "lazada",
    primaryCategory: "666",
    attributes: {
      name: "atr_name",
      brand: "gucci",
    },
    skus: [
      {
        id: "01",
        sellerSku: "ssku",
        price: "100",
        quantity: "a lot"
      },
      {
        id: "02",
        sellerSku: "ssku",
        price: "100",
        quantity: "a lot"
      }
    ]
  }
]

export default {
    name: 'Inventory',
    components: {
      DialogTitle,
      Modal
    },
    data() {
      return {
          items: [],
          Mock_items,
          isOpen: false
      }
    },
    methods: {
      getAllItems: async function() {
          const response = await InventoryDataService.getAllItems()
          this.items = response.data.items
      },
    },
    mounted: async function(){
        this.getAllItems()
    }
}
</script>

