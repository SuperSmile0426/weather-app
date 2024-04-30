<template>
    <header class="bg-black-100 dark:bg-black-800 py-4">
        <div class="container mx-auto flex justify-between items-center">
            <a href="/" class="text-gray-800 dark:text-gray-200 font-bold text-xl">
                <div class="flex flex-row flex justify-content gap-6">
                    <div class="row-span-3 flex justify-center">
                        <img src="/5.svg" class="w-14" alt="SVG" />
                    </div>
                    <div class="items-center justify-center flex text-gray-800 dark:text-gray-200 font-bold text-3xl">
                        Weather App
                    </div>
                </div>

            </a>
            <div class="flex items-center space-x-4">
                <nav>
                    <ul class="flex space-x-4">
                        <li>
                            <a href="#"
                                class="text-gray-800 dark:text-gray-200 hover:text-gray-600 dark:hover:text-gray-400">
                                New York, US
                            </a>
                        </li>
                    </ul>
                </nav>
                <button type="button" class="text-gray-800 dark:text-gray-200 focus:outline-none"
                    @click="toggleDarkMode">
                    <svg v-if="isDarkMode" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z">
                        </path>
                    </svg>
                    <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z">
                        </path>
                    </svg>
                </button>
            </div>
        </div>
    </header>
    <Weather />
</template>

<script>
export default {
    
    data() {
        return {
            isDarkMode: false
        };
    },
    mounted() {
        this.checkDarkMode();
    },
    methods: {
        toggleDarkMode() {
            this.isDarkMode = !this.isDarkMode;
            if (this.isDarkMode) {
                document.documentElement.classList.add('dark');
                localStorage.setItem('theme', true);
            } else {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('theme', false);
            }
        },
        checkDarkMode() {
            const storedTheme = localStorage.getItem('theme');
            if (storedTheme === 'true') {
                this.isDarkMode = true;
                document.documentElement.classList.add('dark');
            } else {
                this.isDarkMode = false;
                document.documentElement.classList.remove('dark');
            }
        },
    },
};
</script>