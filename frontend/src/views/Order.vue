<!-- This example requires Tailwind CSS v2.0+ -->
<template>

          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Platform
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Order ID
                </th>
                 <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Date
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Items
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Buyer name
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Address
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Payment Method
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Price
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="sr-only">Actions</span>
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="order in orders">
                  <td class="whitespace-nowrap">
                      {{ order.platform }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    {{ order.orderId }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    {{ dayjs(order.createdAt).format("DD MMM YYYY HH:mm:ss") }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap ">
                      <ul v-for="orderItem in order.orderItems" class="list-disc">
                        <li> {{orderItem.item.attributes.name}} </li>
                      </ul>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ order.addressShipping.firstName }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ order.addressShipping.country }} - {{order.addressShipping.city}}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ order.paymentMethod }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ order.price }} ฿
                  </td>
                  <!-- <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                    <a href="#" class="text-indigo-600 hover:text-indigo-900">Details</a>
                  </td> -->
                </tr>
            </tbody>
          </table>
 
</template>



<script>
import InventoryDataService from '../services/InventoryDataService'
import * as dayjs from "dayjs"

export default {
    name: 'Inventory',
    data() {
        return {
            orders: [],
            dayjs
        }
    },
    methods: {
        getAllOrders: async function() {
            const response = await InventoryDataService.getAllEntries()
            console.log(response)
            this.orders = response.data.orders
        }
    },
    mounted: async function(){
        this.getAllOrders()
    }
}
</script>

