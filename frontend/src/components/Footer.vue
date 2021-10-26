<template>
    <div>
        <footer id="footer" class="relative z-50 dark:bg-gray-900">
            <div class="py-12 flex flex-col justify-center items-center">
                <a href="javascript:void(0)">
                    <img class="h-8 w-auto sm:h-10" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="" />
                </a>
                <p class="mt-6 text-xs lg:text-sm leading-none text-gray-900 dark:text-gray-50">2021 Tailwind UI Kit. All Rights Reserved.</p>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    name: "Footer",
    data() {
        return {
            auto: true,
            light: false,
            dark: false,
        };
    },
    mounted() {},
    methods: {
        toggle(event) {
            if (event.target.value === "auto") {
                this.auto = true;
                this.light = false;
                this.dark = false;
            }
            if (event.target.value === "light") {
                this.auto = false;
                this.light = true;
                this.dark = false;
            }
            if (event.target.value === "dark") {
                this.auto = false;
                this.light = false;
                this.dark = true;
            }
        },
    },
};
</script>

<style scoped>
@import url("https://cdn.tuk.dev/dist/css/tailwind-v2.2.11.min.css");
</style>
