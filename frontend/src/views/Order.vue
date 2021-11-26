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
                  Order Status
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Order ID
                </th>
                
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Platform
                </th>
                              
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Date
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Item
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Category
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Buyer name
                </th>
               <!-- <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Address
                </th> -->
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Payment Method
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Price
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="order in orders">
                  
                  <td class="flex justify-center px-2 py-4 whitespace-nowrap text-sm text-gray-500">
                    <span v-if="order.status == 'unpaid'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800"> 
                      {{ order.status }}
                    </span>
                     <span  v-else-if="order.status == 'pending'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800"> 
                      {{ order.status }}
                    </span>
                     <span  v-else-if="order.status == 'canceled'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800"> 
                      {{ order.status }}
                    </span>
                      <span  v-else class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800"> 
                      error status
                    </span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    {{ order.orderId }}
                  </td>
                  
                  <td class="px-6 py-4 whitespace-nowrap">
                      {{ order.platform }}
                  </td>
                  
                  <td class="px-6 py-4 whitespace-nowrap">
                    {{ dayjs(order.createdAt).add(0, 'hour').format("DD MMM YYYY HH:mm:ss") }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <ul v-for="orderItem in order.orderItems">
                        <li>{{ orderItem.item.attributes.name}}</li>
                    </ul>
                    <!-- {{ order.orderItems[0].item.attributes.name}} - {{ order.itemsCount }} Pieces -->
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <ul v-for="orderItem in order.orderItems">
                        
                        <li>{{ categoryList.filter( 
(currentValue, index, arr) => currentValue.value == orderItem.item.primaryCategory)[0].text }}</li>

                    </ul>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ order.addressShipping.firstName }}
                  </td>
                 <!-- <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 truncate">
                    {{ order.addressShipping.country }} - {{order.addressShipping.city}}
                  </td> -->
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
        </div>
      </div>
    </div>
  </div>

</template>



<script>
import InventoryDataService from '../services/InventoryDataService'
import * as dayjs from "dayjs"
import axios from "axios"

export default {
    name: 'Inventory',
    data() {
        return {
            orders: [],
            categoryList:[{
                    value:"12393", 
                    text: "Hoodies"
                    },
                    {
                    value:"3603", 
                    text: "Shorts"
                    }
            ],
            dayjs
        }
    },
    methods: {
        getAllOrders: async function() {
            const response = await InventoryDataService.getAllEntries()
            this.orders = response.data.orders
        }
    },
    mounted: async function(){
        this.getAllOrders()
    }
}
</script>

