
<template>
    <div class="container mx-auto py-8 transition-all duration-500">
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-2xl font-bold">Locations</h1>
            <button class="bg-black-500 hover:bg-gray-600 text-blue px-4 py-2 rounded"
                @click="showAddLocationModal = true">
                + Add Location
            </button>
        </div>
        <!-- Weather Table -->
        <div class="overflow-x-auto bg-gray-100 dark:bg-gray-800 rounded-lg">
            <table class="w-full table-auto  table-fixed p-8">
                <thead>
                    <tr class="bg-gray-200 dark:bg-gray-700 border-bottom-white-300">
                        <th class="px-4 py-2 pr-8 pl-8 text-left">Location</th>
                        <th class="px-4 py-2 pr-8 pl-8 text-left">Temperature</th>
                        <th class="px-4 py-2 pr-8 pl-8 text-left">Rainfall</th>
                        <th class="px-4 py-2"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="border-b-0" v-for="location in locations" :key="location.id"
                        @click="showForecastSidebar(location.name)">
                        <td class="border-b-2 pr-8 pl-8">
                            <div class="flex flex-row flex justify-content gap-6">
                                <div class="row-span-3">
                                    <img :src="`${classifyWeather(location.current_weather_condition.current.weather_code)}.svg`" alt="SVG 1" />
                                </div>
                                <div class="font-bold col-span-4 text-right">
                                    {{ location.name }}
                                </div>
                            </div>
                        </td>
                        <td class="border-b-2 p-8 border-100">{{ location.current_weather_condition.current.temperature_2m }}°C</td>
                        <td class="border-b-2 p-8 border-100">{{ location.current_weather_condition.current.rain }}mm</td>
                        <td class="border-b-2 p-8 py-2 text-right">
                            <button class="text-blue px-2 py-1 rounded" @click.stop="confirmDelete(location)">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
                                </svg>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Sidebar -->
        <transition name="fade">
            <div v-if="selectedLocation"
                class="fixed top-0 right-0 w-full md:w-1/3 h-full bg-gray-100 dark:bg-gray-800 p-8 overflow-y-auto">
                <button class="absolute top-4 right-4 text-gray-800 dark:text-gray-200"
                    @click="selectedLocation = null">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12">
                        </path>
                    </svg>
                </button>
                <h2 class="text-2xl font-bold mb-4">{{ selectedLocation }} </h2>
                <div class="grid grid-cols-1 md:grid-cols-1 gap-4 rounded-20">
                    <h3 class="text-lg">This Week</h3>
                    <div v-for="(date, index) in selectedLocationForecast.daily.time" :key="index"
                        class="bg-white dark:bg-gray-700 p-6 rounded-2xl shadow">
                        <div class="flex flex-row flex justify-between">
                            <div class="flex flex-row flex justify-content gap-6">
                                <div class="row-span-3 flex justify-center">
                                    <img :src="`${classifyWeather(selectedLocationForecast.daily.weather_code[index])}.svg`" class="w-12" alt="SVG" />
                                </div>
                                <div
                                    class="items-center flex justify-center text-gray-800 dark:text-gray-200 font-bold text-3xl">
                                    {{ getDayFromDate(date) }}
                                </div>
                            </div>
                            <div class="col-span-4 text-right">
                                <div class="text-gray-800 dark:text-gray-200 flex items-center">Min . &nbsp {{ selectedLocationForecast.daily.temperature_2m_max[index] }}°C</div>
                                <div class="text-gray-800 dark:text-gray-200 flex items-center">Max . &nbsp {{ selectedLocationForecast.daily.temperature_2m_min[index] }}°C</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </transition>

        <!-- Add Location Modal -->
        <transition name="fade">
            <div v-if="showAddLocationModal"
                class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-75 transition-all duration-500">
                <div class="bg-white dark:bg-gray-800 p-8 rounded shadow  w-96">
                    <div class="flex justify-between">
                        <div class="text-white-800">
                            <h2 class="text-2xl font-bold mb-4">Add Location</h2>
                        </div>
                        <div class="text-white-800">                            
                            <button class="dark:text-gray-200" @click="showAddLocationModal = false">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M6 18L18 6M6 6l12 12">
                                    </path>
                                </svg>
                            </button>
                        </div>
                    </div>
                    <form @submit.prevent="addLocation">
                        <div class="gap-6 mb-4">
                            <input class="border rounded px-3 py-2 w-full rounded-lg" type="text" id="location"
                                v-model="newLocationName" placeholder="Enter a location" required>
                        </div>
                        <button class="bg-gray-600 hover:bg-blue-600 text-white px-4 py-2 w-full rounded-lg"
                            type="submit">
                            Add Location
                        </button>
                    </form>
                </div>
            </div>
        </transition>
    </div>
</template>
<script setup lang="ts">

import { ref, watchEffect } from 'vue';
import axios from 'axios';

const locations = ref([]);

const getData = async () => {
    try {
        const response = await axios.get("http://localhost:8000/locations/");
        locations.value = response.data;
        console.log(locations.value)
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

watchEffect(() => {
    getData();
});

const selectedLocation = ref(null);
const selectedLocationForecast = ref([]);
const showAddLocationModal = ref(false);
const newLocationName = ref('');

const getDataForecast = async(location) => {
    try {
        const response = await axios.get(`http://localhost:8000/forecast/${location}`);
        selectedLocationForecast.value = response.data;
        console.log(selectedLocationForecast.value)
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

const showForecastSidebar = (location) => {
    selectedLocation.value = location;
    getDataForecast(location);
    
};
const confirmDelete = (location) => {
    if (confirm(`Are you sure you want to remove ${location.name}?`)) {
        deleteLocation(location);
    }
};
const getDayFromDate = (dateString) => {
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const date = new Date(dateString);
    const dayIndex = date.getDay();
    return days[dayIndex];
};
const deleteLocation = (location) => {
    axios.delete(`http://localhost:8000/locations/${location.name}`);
    locations.value = locations.value.filter((l) => l.name !== location.name);
};

const addLocation = () => {
    if (newLocationName.value.trim() !== '') {
        const postData = {
            "name" : newLocationName.value
        }
        axios.post(`http://localhost:8000/locations`, postData);
        newLocationName.value = '';
        // location.current_weather_condition.current.push({
        //     id: locations.value.length + 1,
        //     name: newLocationName.value,
        //     temperature: Math.floor(Math.random() * 20) + 10,
        //     rainfall: Math.floor(Math.random() * 20),
        //     weather_code: ['1', '2', '3', '4'][Math.floor(Math.random() * 4)],
        // });
        showAddLocationModal.value = false;
    }
};
const weatherConditions = {
      0: "1",
      "1, 2, 3": "3",
      "45, 48": "4",
      "51, 53, 55, 56, 57, 61, 63, 65, 66, 67": "2",
      "71, 73, 75, 77, 80, 81, 82, 85, 86": "5",
    };


function classifyWeather(code) {
  for (let key in weatherConditions) {
    if (key.includes(",")) {
      const codeList = key.split(", ").map(Number);
      if (codeList.includes(code)) {
        return weatherConditions[key];
      }
    } else if (code === parseInt(key)) {
      return weatherConditions[key];
    }
  }
  return "5";
}
</script>


<style>
.dark {
    color: white;
    background-color: #333;
}

.transition-all {
    transition: all 0.5s;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}

table tr:last-child td {
    @apply border-b-0;
}
</style>

                            