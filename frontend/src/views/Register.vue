<template>
    <div class="hidden sm:block" aria-hidden="true">
        <div class="py-5">
            <div class="border-t border-gray-200" />
        </div>
    </div>

    <div class="mt-10 sm:mt-0">
        <div class="md:grid md:grid-cols-3 md:gap-6">
            <div class="ml-16 md:col-span-1">
                <div class="px-4 sm:px-0">
                    <h1 class="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
                        <p class="block text-indigo-400 xl:inline">Personal Information</p>
                    </h1>
                    <p class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                        Enter your personal details <br> and start journey with us!
                    </p>
                    
                </div>
            </div>
            <div class="mt-5 mr-16 md:mt-0 md:col-span-2">
                <form @submit="RegisterUser">
                    <div class="shadow overflow-hidden sm:rounded-md">
                        <div class="px-4 py-5 bg-white sm:p-6">
                            <div class="grid grid-cols-6 gap-6">
                                <div class="col-span-6 sm:col-span-3">
                                    <label for="first-name" class="block text-sm font-medium text-gray-700">First name</label>
                                    <input type="text" v-model="fname" name="first-name" id="first-name" autocomplete="given-name" required="" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                                </div>

                                <div class="col-span-6 sm:col-span-3">
                                    <label for="last-name" class="block text-sm font-medium text-gray-700">Last name</label>
                                    <input type="text" v-model="lname" name="last-name" id="last-name" autocomplete="family-name" required="" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                                </div>

                                <div class="col-span-6 sm:col-span-4">
                                    <label for="email-address" class="block text-sm font-medium text-gray-700">Email address</label>
                                    <input type="text" v-model="email" name="email-address" id="email-address" autocomplete="email" required="" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                                </div>

                                <div class="col-span-6 sm:col-span-4">
                                    <label for="password" class="block text-sm font-medium text-gray-700">password</label>
                                    <input type="password" v-model="password" name="password" id="password" autocomplete="current-password" required="" class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                                </div>

                            </div>
                        </div>
                        <div class="px-4 py-3 bg-gray-50 text-right sm:px-6">
                            <button type="submit" class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                            sign up
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div> 

</template>

// userexample = {
//   fname: garky,
//   lname: garky,
//   email: gark@gark.com,
//   password: garkgark
// }
<script>
import AuthDataService from "../services/AuthDataService"

export default {
    data() {
        return {
            fname: '',
            lname: '',
            email: '',
            password: ''
        }
    },
    methods: {
        async RegisterUser(e) {
            e.preventDefault()
            const response = await AuthDataService.create({
                fname: this.fname,
                lname: this.lname,
                email: this.email,
                password: this.password
            })
            .then((res) => {
                console.log(res)
                this.$router.push('/login');
            }).catch((error) => {
                this.message = "Error!" + error
            })

        }
    },
}
</script>
