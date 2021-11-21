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
                    <button @click="openModal" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800 hover:bg-green-500  active:bg-green-800">
                      Click me
                    </button>
                  </td>
                  <!--<td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                    <a href="#" class="text-indigo-600 hover:text-indigo-900">Details</a>
                  </td> -->
                </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  <Modal/>
</template>



<script>
import InventoryDataService from '../services/InventoryDataService'
import Modal from '../components/Modal'
import { useStore } from "vuex";

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
      Modal
    },
    data() {
      return {
          items: [],
      }
    },
    setup() {
      return {
        Mock_items
      }
    },
    methods: {
        getAllItems: async function() {
            const response = await InventoryDataService.getAllItems()
            this.items = response.data.items
        },
        async openModal() {
          const store = useStore()
          await store.dispatch('setModal', true)
        },
    },
    mounted: async function(){
        this.getAllItems()
    }
}
</script>

