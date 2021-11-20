<!-- This example requires Tailwind CSS v2.0+ -->
<template>
<div class=" flex flex-col">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: "getEntry",
    data() {
      return {
        entries: [],
      };
    },
    mounted() {
        console.log("here")
    //   this.getEntry();
    //   this.test()
    },
    methods: {
      async getEntry() {
        console.log("hahah2")
        await axios
          .get(`http://localhost:3000/api/entry`)
          .then(res => {
              console.log(res.data)
              this.entries = res.entries
              console.log("All entries", res.entries)
          })
          .catch(error => {
              console.log(error)
          })
      },
      async test(){
          console.log("")
      }
    },
    beforeMount(){
        this.getEntry()
    },
  };
</script>