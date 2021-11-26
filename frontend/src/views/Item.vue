<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class=" flex flex-col">
    <span class="mt-7 flex flex-row-reverse sm:mx-12 lg:mx-16">
      <button @click="openCreateModal" type="button" class="inline-flex items-center px-2 py-1 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        <DocumentAddIcon class="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
        Add item
      </button>
    </span>
    <div class="mt-3 mb-10 overflow-x-auto sm:mx-12 lg:mx-16">
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
                <tr v-for="(item, index) in items" :key="item.id">
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
                  <td class="px-2 py-4 whitespace-nowrap text-sm text-gray-500">
                    <button @click="openModal(index)" class="mx-2 px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800 hover:bg-green-500  active:bg-green-800">
                      Edit
                    </button>
                    <!-- <button @click="deleteItem(index)" class="mx-2 px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800 hover:bg-red-500  active:bg-red-800">
                      Delete
                    </button> -->
                  </td>
                </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <Modal :is-open='isOpen' v-on:close-modal="isOpen = false">
      <form @submit="updateItem">
        <div class="bg-white px-4 pt-5 pb-4 sm:px-6 sm:pb-4">
          <div class="sm:flex sm:items-start">
            <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
              <DialogTitle as="h3" class="text-lg leading-6 font-medium text-gray-900">
                Edit item
              </DialogTitle>
              <div class="mt-2 pr-4 py-5 bg-white sm:py-6">
                <div class="col-span-6 mb-6">
                  <DialogTitle as="h4" class="text-lg leading-6 font-medium text-gray-900 mb-3">
                    Attribute
                  </DialogTitle>
                  <div class="grid grid-cols-6 gap-6">
                      
                      <div class="col-span-6 sm:col-span-3">
                        <label for="platform" class="block text-sm font-medium text-gray-700">Platform</label>
                        <select v-model="selectedItem.platform" id="platform" name="platform" autocomplete="platform-name" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                          <option value="lazada">Lazada</option>
                          <!-- <option>Shopee</option> -->
                        </select>
                      </div>
                      <div class="col-span-6 sm:col-span-3">
                        <label for="primaryCategory" class="block text-sm font-medium text-gray-700">Category</label>
                        <select v-model="selectedItem.primaryCategory" id="Category" name="Category" autocomplete="Category-name" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                          <option value='3602'>Pants</option>
                          <option value='3603'>Shorts</option>
                          <option value='7236'>Hoodies</option>
                          <option value='4210'>Pyjama sets</option>
                        </select>
                      </div>

                      <div class="col-span-6 sm:col-span-3">
                        <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                        <input type="text" name="name" id="name" v-model="selectedItem.attributes.name" autocomplete="given-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                      </div>

                      <div class="col-span-6 sm:col-span-3">
                        <label for="brand" class="block text-sm font-medium text-gray-700">Brand</label>
                        <input type="text" name="brand" id="brand" v-model="selectedItem.attributes.brand" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                      </div>

                      <div class="col-span-6">
                        <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                        <textarea row="2" type="text" name="description" id="description" v-model="selectedItem.attributes.description" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                      </div>
                  </div>
                </div>
                <div class="col-span-6 mb-3">
                  <DialogTitle as="h4" class="text-lg leading-6 font-medium text-gray-900 mb-3">
                    Sku
                  </DialogTitle>
                  <div v-for='(sku, index) in selectedItem.skus' :key="sku.id" class='grid grid-cols-6 gap-6'>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-sellerSku" class="block text-sm font-medium text-gray-700">Seller</label>
                      <input type="text" name="sku-sellerSku" id="sku-sellerSku" v-model="sku.sellerSku" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-price" class="block text-sm font-medium text-gray-700">Price</label>
                      <input type="number" name="sku-price" id="sku-price" v-model="sku.price" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-quantity" class="block text-sm font-medium text-gray-700">Quantity</label>
                      <input type="number" name="sku-quantity" id="sku-quantity" v-model="sku.quantity" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-packageHeight" class="block text-sm font-medium text-gray-700">PackageHeight</label>
                      <input type="number" name="sku-packageHeight" id="sku-packageHeight" v-model="sku.packageHeight" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-packageLength" class="block text-sm font-medium text-gray-700">PackageLength</label>
                      <input type="number" name="sku-packageLength" id="sku-packageLength" v-model="sku.packageLength" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-packageWidth" class="block text-sm font-medium text-gray-700">PackageWidth</label>
                      <input type="number" name="sku-packageWidth" id="sku-packageWidth" v-model="sku.packageWidth" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-packageWeight" class="block text-sm font-medium text-gray-700">PackageWeight</label>
                      <input type="number" name="sku-packageWeight" id="sku-packageWeight" v-model="sku.packageWeight" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6">
                      <label for="sku-packageWeight" class="block text-sm font-medium text-gray-700">Cover photo</label>
                      <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md">
                        <div class="space-y-1 text-center">
                          <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                            <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                          </svg>
                          <div class="flex text-sm text-gray-600">
                            <label for="file-upload" class="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500">
                              <span>Upload a file</span>
                              <input id="file-upload" name="file-upload" type="file" class="sr-only" />
                            </label>
                            <p class="pl-1">or drag and drop</p>
                          </div>
                          <p class="text-xs text-gray-500">
                            PNG, JPG, GIF up to 10MB
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div> 
              </div>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
          <button type="submit" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm" @click="isOpen = false">
            Save
          </button>
          <button type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm" @click="isOpen = false" ref="cancelButtonRef">
            Cancel
          </button>
        </div>
      </form>
    </Modal>
    <Modal :is-open='isOpenCreate' v-on:close-modal="isOpenCreate = false">
      <form @submit="createItem">
        <div class="bg-white px-4 pt-5 pb-4 sm:px-6 sm:pb-4">
          <div class="sm:flex sm:items-start">
            <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
              <DialogTitle as="h3" class="text-lg leading-6 font-medium text-gray-900">
                Create item
              </DialogTitle>
              <div class="mt-2 pr-4 py-5 bg-white sm:py-6">
                <div class="col-span-6 mb-6">
                  <DialogTitle as="h4" class="text-lg leading-6 font-medium text-gray-900 mb-3">
                    Attribute
                  </DialogTitle>
                  <div class="grid grid-cols-6 gap-6">
                      
                      <div class="col-span-6 sm:col-span-3">
                        <label for="platform" class="block text-sm font-medium text-gray-700">Platform</label>
                        <select v-model="createdItem.platform" id="platform" name="platform" autocomplete="platform-name" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                          <option value="lazada">Lazada</option>
                          <!-- <option>Shopee</option> -->
                        </select>
                      </div>
                      <div class="col-span-6 sm:col-span-3">
                        <label for="primaryCategory" class="block text-sm font-medium text-gray-700">Category</label>
                        <select v-model.number="createdItem.primaryCategory" id="Category" name="Category" autocomplete="Category-name" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                          <!-- <option value="3602">Pants</option> -->
                          <option value="3603">Shorts</option>
                          <option value="12393">Hoodies</option>
                          <!-- <option value="4210">Pyjama sets</option> -->
                        </select>
                      </div>

                      <div class="col-span-6 sm:col-span-3">
                        <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                        <input type="text" name="name" id="name" v-model="createdItem.attributes.name" autocomplete="given-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                      </div>

                      <div class="col-span-6 sm:col-span-3">
                        <label for="brand" class="block text-sm font-medium text-gray-700">Brand</label>
                        <input type="text" name="brand" id="brand" v-model="createdItem.attributes.brand" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                      </div>

                      <div class="col-span-6">
                        <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                        <textarea row="2" type="text" name="description" id="description" v-model="createdItem.attributes.description" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                      </div>
                  </div>
                </div>
                <div class="col-span-6 mb-3">
                  <DialogTitle as="h4" class="text-lg leading-6 font-medium text-gray-900 mb-3">
                    Sku
                  </DialogTitle>
                  <div v-for='(sku, index) in createdItem.skus' :key="sku.id" class='grid grid-cols-6 gap-6'>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-sellerSku" class="block text-sm font-medium text-gray-700">Seller</label>
                      <input type="text" name="sku-sellerSku" id="sku-sellerSku" v-model="sku.sellerSku" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-price" class="block text-sm font-medium text-gray-700">Price</label>
                      <input type="number" name="sku-price" id="sku-price" v-model="sku.price" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-quantity" class="block text-sm font-medium text-gray-700">Quantity</label>
                      <input type="number" name="sku-quantity" id="sku-quantity" v-model="sku.quantity" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-packageHeight" class="block text-sm font-medium text-gray-700">PackageHeight</label>
                      <input type="number" name="sku-packageHeight" id="sku-packageHeight" v-model="sku.packageHeight" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-packageLength" class="block text-sm font-medium text-gray-700">PackageLength</label>
                      <input type="number" name="sku-packageLength" id="sku-packageLength" v-model="sku.packageLength" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-packageWidth" class="block text-sm font-medium text-gray-700">PackageWidth</label>
                      <input type="number" name="sku-packageWidth" id="sku-packageWidth" v-model="sku.packageWidth" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6 sm:col-span-3">
                      <label for="sku-packageWeight" class="block text-sm font-medium text-gray-700">PackageWeight</label>
                      <input type="number" name="sku-packageWeight" id="sku-packageWeight" v-model="sku.packageWeight" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <div class="col-span-6">
                        <label for="imageURL" class="block text-sm font-medium text-gray-700">Image URL</label>
                        <input type="text" name="imageURL" id="imageURL" v-model="sku.images[0]" autocomplete="family-name" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                    </div>
                    <!-- <div class="col-span-6">
                      <label for="sku-packageWeight" class="block text-sm font-medium text-gray-700">Cover photo</label>
                      <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md">
                        <div class="space-y-1 text-center">
                          <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                            <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                          </svg>
                          <div class="flex text-sm text-gray-600">
                            <label for="file-upload" class="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500">
                              <span>Upload a file</span>
                              <input id="file-upload" name="file-upload" type="file" class="sr-only" />
                            </label>
                            <p class="pl-1">or drag and drop</p>
                          </div>
                          <p class="text-xs text-gray-500">
                            PNG, JPG, GIF up to 10MB
                          </p>
                        </div>
                      </div>
                    </div> -->
                  </div>
                </div> 
              </div>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
          <button type="submit" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm" @click="isOpenCreate = false">
            create
          </button>
          <button type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm" @click="isOpenCreate = false" ref="cancelButtonRef">
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
import { 
  DocumentAddIcon
} from '@heroicons/vue/solid'

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
      name: "atr_name2",
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

const default_item = {
            platform: "lazada",
            primaryCategory: 12393,
            attributes: {
                name: "",
                description: "",
                brand: "" 
            },
            skus: [{
                    sellerSku: "",
                    price: "",
                    quantity: "",
                    packageHeight: null,
                    packageLength: null,
                    packageWidth:null,
                    packageWeight: null,
                    images: [
                        "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png",
                        "https://d17fnq9dkz9hgj.cloudfront.net/uploads/2018/01/shelter-dog-cropped-1.jpeg"
                    ]
                  }]
          }


export default {
    name: 'Inventory',
    components: {
      DocumentAddIcon,
      DialogTitle,
      Modal
    },
    data() {
      return {
          items: [],
          Mock_items,
          isOpen: false,
          isOpenCreate: false,
          selectedItem: {},
          createdItem: default_item
      }
    },
    methods: {
      getAllItems: async function() {
        const response = await InventoryDataService.getAllItems()
        this.items = response.data.items
      },
      openModal: function(index) {
        this.selectedItem = this.items[index]
        this.isOpen = true
      },
      openCreateModal: function() {
        this.isOpenCreate = true
      },
      createItem: async function(e) {
        e.preventDefault()
        this.createdItem.skus[0].price = this.createdItem.skus[0].price.toString()
        this.createdItem.primaryCategory = parseInt(this.createdItem.primaryCategory)
        this.createdItem.skus[0].quantity = this.createdItem.skus[0].quantity.toString()
        // this.createdItem.skus[0].images[0]
        try {
          const response = await InventoryDataService.createItem(this.createdItem)
          this.createdItem = default_item
          console.log("response", response)
          this.getAllItems()
        } catch(e) {
          console.log(e)
        }
      },
      updateItem: async function(e) {
        e.preventDefault()
        const { id, ...updatedItem } = this.selectedItem
        updatedItem.skus[0].price = updatedItem.skus[0].price.toString()
        updatedItem.primaryCategory = parseInt(updatedItem.primaryCategory)
        updatedItem.skus[0].quantity = updatedItem.skus[0].quantity.toString()  
        try {
          const response = await InventoryDataService.updateItem(id, updatedItem)
          // console.log("response", response)
        } catch(e) {
          console.log(e)
        }
      },
      deleteItem: async function(index) {
        try {
          const response = await InventoryDataService.deleteItem(this.items[index].id)
          this.items = this.items.filter( (currentValue, i, arr) => i != index )
          // console.log("response", response)
        } catch(e) {
          console.log(e)
        }
      }
    },
    mounted: async function(){
        this.getAllItems()
    }
}
</script>

