<!-- This example requires Tailwind CSS v2.0+ -->
<template>
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
        <!--<th scope="col" class="relative px-6 py-3">
          <span class="sr-only">Actions</span>
        </th> -->
      </tr>
    </thead>
    <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="item in items">
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
            <ul v-for="sku in item.skus" class="list-disc">
                 {{sku.sellerSku}}
            </ul>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            <ul v-for="sku in item.skus" class="list-disc">
                 {{sku.price}} ฿ 
            </ul>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            <ul v-for="sku in item.skus" class="list-disc">
                 {{sku.quantity}} Pieces
            </ul>
          </td>
          <!--<td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
            <a href="#" class="text-indigo-600 hover:text-indigo-900">Details</a>
          </td> -->
        </tr>
    </tbody>
  </table>
</template>



<script>
import InventoryDataService from '../services/InventoryDataService'

export default {
    name: 'Inventory',
    data() {
        return {
            items: [],
        }
    },
    methods: {
        getAllItems: async function() {
            const response = await InventoryDataService.getAllItems()
            this.items = response.data.items
        }
    },
    mounted: async function(){
        this.getAllItems()
    }
}
</script>

