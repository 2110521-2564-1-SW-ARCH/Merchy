<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class=" flex flex-col">
      <div class="my-10 sm:mx-12 lg:mx-16">
        <div class="align-middle inline-block min-w-full">
          <div class="shadow overflow-hidden border-2 border-gray-200 sm:rounded-lg">
              <div class="grid grid-cols-10">
                <Datepicker class="col-span-9" v-model="date" :enableTimePicker="false" range @update:modelValue="updateChart"></Datepicker>
                  <div class="col-span-1">
                      <select v-model="type" @change="updateChart" id="country" class="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                        <option value="day">Day</option>
                        <option value="month">Month</option>
                        <option value="year">Year</option>
                      </select>
                    </div>  
                </div>
            <apexchart height="350"  type="bar" :options="options" :series="series"></apexchart>
          </div>
        </div>
        <!--<div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-4 mt-6 mb-4">
          <StateReport :is-up='true'/>
          <StateReport :is-up='false'/>
          <StateReport :is-up='true'/>
          <StateReport :is-up='false'/>
        </div> -->
      </div>
  </div>
</template>

<script>
  import axios from "axios";
  import VueApexCharts from 'vue-apexcharts'
  import StateReport from '../components/StateReport.vue'
  import Datepicker from 'vue3-date-time-picker';
  import 'vue3-date-time-picker/dist/main.css'
  import InventoryDataService from '../services/InventoryDataService'
  import dayjs from "dayjs" 

  export default {
    name: "Accounting",
    components: {
      Datepicker ,
      StateReport,
      apexcharts: VueApexCharts,
    },
    data() {
      return {
        type: '',
        date: null,
        entries: [],
        options: {
          chart: {
            id: 'vuechart-example'
          },
          plotOptions: {
          bar: {
            borderRadius: 10,
            dataLabels: {
              position: 'top', // top, center, bottom
            },
          }
          },
          dataLabels: {
            enabled: true,
            formatter: function (val) {
              return val + "฿";
            },
            offsetY: -20,
            style: {
              fontSize: '12px',
              colors: ["#304758"]
            }
          },
          xaxis: {
            categories: [],
            position: 'top',
            axisBorder: {
              show: false
            },
            axisTicks: {
              show: false
            },
            crosshairs: {
              fill: {
                type: 'gradient',
                gradient: {
                  colorFrom: '#D8E3F0',
                  colorTo: '#BED1E6',
                  stops: [0, 100],
                  opacityFrom: 0.4,
                  opacityTo: 0.5,
                }
              }
            },
            tooltip: {
              enabled: true,
            }
          },
          yaxis: {
            axisBorder: {
              show: false
            },
            axisTicks: {
              show: false,
            },
            labels: {
              show: false,
              formatter: function (val) {
                return val + "฿";
              }
            }
          
          },
          title: {
            text: 'business revenue',
            floating: true,
            offsetY: 330,
            align: 'center',
            style: {
              color: '#444'
            }
          }
        },
        series: [{
          name: 'Income',
          data: []
        }],
      };
    },
    async beforeMount() {
        this.type = 'day'
        try {
          const response = await InventoryDataService.getAllAccount('2021-11-02', '2021-11-30', 'day')
          if (response.status != 200) {
            alert("something wrong")
          } else {
                console.log("response ",response.data)
                let categories = []
                let data = []
                for (let [key, value] of Object.entries(response.data)) {
                  categories.push(key) 
                  data.push(value)
                }
              console.log(typeof this.options.xaxis.categories)
              console.log(this.options.xaxis.categories)
              console.log(data)
              this.options = {
                              xaxis: {
                                categories: categories,
                              },
                            }
              this.series = [{
                data: data
               }]
          }
        } catch (e) {
          console.log(e)
        }
    },
    methods: {   
      async updateChart() {
        const start = dayjs(this.date[0]).format("YYYY-MM-DD")
        const end = dayjs(this.date[1]).format("YYYY-MM-DD")
        console.log(start, end)
        try {
          const response = await InventoryDataService.getAllAccount(start, end, this.type)
          if (response.status != 200) {
            alert("something wrong")
          } else {
                console.log("response ",response.data)
                let categories = []
                let data = []
                for (let [key, value] of Object.entries(response.data)) {
                  categories.push(key) 
                  data.push(value)
                }
              console.log(typeof this.options.xaxis.categories)
              console.log(this.options.xaxis.categories)
              console.log(data)
              this.options = {
                              xaxis: {
                                categories: categories,
                              },
                            }
              this.series = [{
                data: data
               }]
          }
        } catch (e) {
          console.log(e)
        }
      },
      // async getEntry() {
      //   console.log("hahah2")
      //   await axios
      //     .get(`http://localhost:3000/api/entry`)
      //     .then(res => {
      //         console.log(res.data)
      //         this.entries = res.entries
      //         console.log("All entries", res.entries)
      //     })
      //     .catch(error => {
      //         console.log(error)
      //     })
      // },
      // async test(){
      //     console.log("")
      // }
    },

  };
</script>