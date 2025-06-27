<script setup lang="ts">
interface MenuItem {
  id: number
  name: string
  price: string
  image: string
  story: string
  ingredients: string[]
  badge?: {
    text: string
    color: string
  }
}

defineProps<{
  item: MenuItem
  index: number
}>()
</script>

<template>
  <div 
    class="group" 
    :data-aos="index % 2 === 0 ? 'fade-right' : 'fade-left'" 
    :data-aos-duration="1000" 
    :data-aos-delay="index * 100"
  >
    <div class="relative bg-gradient-to-br from-gray-900/80 via-black/60 to-gray-800/80 backdrop-blur-xl rounded-3xl overflow-hidden shadow-2xl hover:shadow-3xl hover:shadow-gold-500/20 transition-all duration-700 transform hover:-translate-y-6 hover:scale-[1.02] border border-gray-700/50 hover:border-gold-500/40 group-hover:bg-gradient-to-br group-hover:from-gray-800/90 group-hover:via-black/70 group-hover:to-gray-700/90">
      
      <!-- Premium Corner Accents -->
      <div class="absolute top-0 right-0 w-24 h-24 bg-gradient-to-bl from-gold-500/15 to-transparent rounded-bl-full"></div>
      <div class="absolute bottom-0 left-0 w-20 h-20 bg-gradient-to-tr from-gold-500/10 to-transparent rounded-tr-full"></div>
      
      <!-- Enhanced Image Section -->
      <div class="relative overflow-hidden h-80 sm:h-96 lg:h-80 xl:h-96">
        <!-- Image with Premium Frame -->
        <div class="absolute inset-3 rounded-2xl overflow-hidden">
          <img 
            :src="item.image" 
            :alt="item.name" 
            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 filter group-hover:brightness-110 group-hover:contrast-110"
          >
          <!-- Elegant Gradient Overlay -->
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent group-hover:from-black/60 transition-all duration-500"></div>
        </div>
        
        <!-- Dynamic Badge -->
        <div v-if="item.badge" class="absolute top-8 right-8 z-10">
          <div 
            :class="[
              'px-5 py-3 rounded-full font-elegant font-bold text-sm shadow-2xl group-hover:scale-110 transition-all duration-300 border-2 backdrop-blur-sm',
              item.badge.color === 'gold' ? 'bg-gradient-to-r from-gold-500 to-gold-400 text-black border-gold-300/50 shadow-gold-500/50 group-hover:shadow-gold-500/70' :
              item.badge.color === 'red' ? 'bg-gradient-to-r from-red-600 to-red-700 text-white border-red-500/50 shadow-red-600/50 group-hover:shadow-red-600/70' :
              item.badge.color === 'green' ? 'bg-gradient-to-r from-green-600 to-green-700 text-white border-green-500/50 shadow-green-600/50 group-hover:shadow-green-600/70' :
              'bg-gradient-to-r from-blue-600 to-blue-700 text-white border-blue-500/50 shadow-blue-600/50 group-hover:shadow-blue-600/70'
            ]"
          >
            <div class="flex items-center space-x-2">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
              </svg>
              <span>{{ item.badge.text }}</span>
            </div>
          </div>
        </div>

        <!-- Dish Name Overlay -->
        <div class="absolute bottom-8 left-8 right-8 z-10">
          <div class="bg-black/60 backdrop-blur-md rounded-2xl px-8 py-6 border border-gold-500/30 group-hover:bg-black/80 group-hover:border-gold-500/50 transition-all duration-300">
            <h3 class="text-xl font-elegant font-bold text-white mb-3 group-hover:text-gold-300 transition-colors duration-300">
              {{ item.name }}
            </h3>
            <div class="flex items-center justify-between">
              <div class="w-20 h-0.5 bg-gold-500 rounded-full group-hover:w-28 transition-all duration-300 ease-in-out"></div>
              <div class="text-xl font-elegant font-bold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                {{ item.price }}
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Enhanced Content Section -->
      <div class="p-10 space-y-8">
        <!-- Story Section -->
        <div class="bg-black/20 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300 group/story">
          <div class="flex items-start space-x-4 mb-4">
            <div class="flex-shrink-0 w-3 h-3 bg-gradient-to-r from-gold-500 to-gold-400 rounded-full mt-2 group-hover/story:scale-150 transition-transform duration-300 shadow-lg shadow-gold-500/50"></div>
            <div>
              <h4 class="text-sm font-elegant font-semibold text-gold-500 mb-3 group-hover/story:text-gold-400 transition-colors duration-300 tracking-wider uppercase">
                The Story
              </h4>
              <p class="text-base text-gray-300 leading-relaxed font-modern group-hover/story:text-gray-100 transition-colors duration-300 italic">
                {{ item.story }}
              </p>
            </div>
          </div>
        </div>

        <!-- Ingredients Section -->
        <div class="bg-black/20 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300 group/ingredients">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2 h-2 bg-gold-500 rounded-full group-hover/ingredients:scale-150 transition-transform duration-300"></div>
            <h4 class="text-sm font-elegant font-semibold text-gold-500 group-hover/ingredients:text-gold-400 transition-colors duration-300 tracking-wider uppercase">
              Premium Ingredients
            </h4>
          </div>
          <div class="flex flex-wrap gap-2.5">
            <span
              v-for="ingredient in item.ingredients"
              :key="ingredient"
              class="bg-black/40 text-gray-300 px-4 py-2 rounded-full text-xs font-modern hover:bg-gold-500/20 hover:text-gold-300 transition-all duration-300 cursor-pointer hover:scale-105 border border-gray-600/30 hover:border-gold-500/40 backdrop-blur-sm"
            >
              {{ ingredient }}
            </span>
          </div>
        </div>

        <!-- Action Section -->
        <div class="flex justify-center items-center pt-4 border-t border-gold-500/20">
          <!-- Price Display -->
          <div class="bg-gradient-to-r from-gold-500/10 to-gold-400/10 rounded-full px-8 py-4 border border-gold-500/30 backdrop-blur-sm group-hover:from-gold-500/20 group-hover:to-gold-400/20 group-hover:border-gold-500/50 transition-all duration-300">
            <div class="text-2xl font-elegant font-bold text-gold-500 group-hover:text-gold-400 transition-colors duration-300 flex items-center space-x-2">
              <svg class="w-5 h-5 opacity-70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              {{ item.price }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Enhanced hover effects */
.group:hover .group-hover\:shadow-3xl {
  box-shadow: 0 35px 60px -12px rgba(0, 0, 0, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.05);
}

/* Smooth transitions for all elements */
* {
  transition-property: transform, opacity, color, background-color, border-color, box-shadow, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}
</style>