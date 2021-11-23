<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class=" flex flex-col">
      <div class="my-10 sm:mx-12 lg:mx-16">
        <div class="align-middle inline-block min-w-full">
          <div class="shadow overflow-hidden border-2 border-gray-200 sm:rounded-lg">
            <Datepicker v-model="date" :enableTimePicker="false" range @update:modelValue="updateChart"></Datepicker>
            <apexchart height="350"  type="bar" :options="options" :series="series"></apexchart>
          </div>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-4 mt-6 mb-4">
          <StateReport/>
          <StateReport/>
          <StateReport/>
          <StateReport/>
        </div>
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

  export default {
    name: "getEntry",
    components: {
      Datepicker ,
      StateReport,
      apexcharts: VueApexCharts,
    },
    data() {
      return {
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
              return val + "%";
            },
            offsetY: -20,
            style: {
              fontSize: '12px',
              colors: ["#304758"]
            }
          },
          xaxis: {
            categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
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
            text: 'Monthly Accounting in 2020',
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
          data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
        }],
      };
    },
    mounted() {
        // console.log("here")
    //   this.getEntry();
    //   this.test()
    },
    methods: {
      async updateChart() {
        // console.log("hi")
        try {
          //const response = await InventoryDataService.getAllAccount()
          const response = await InventoryDataService.getAllAccount()
          if (response.status != 200) {
            alert("something wrong")
          } else {
            console.log(response.data)
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