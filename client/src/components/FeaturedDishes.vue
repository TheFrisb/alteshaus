<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const router = useRouter()
</script>

<template>
  <section class="relative overflow-hidden bg-gradient-to-b from-black via-gray-900 to-black">
    <!-- Enhanced Background Elements with Animation -->
    <div class="absolute inset-0 overflow-hidden">
      <!-- Animated Gradient Orbs -->
      <div class="absolute top-0 right-0 w-[600px] h-[400px] bg-gradient-radial from-gold-500/6 via-gold-500/2 to-transparent rounded-full translate-x-64 -translate-y-48 animate-pulse" style="animation-duration: 8s;"></div>
      <div class="absolute bottom-0 left-0 w-96 h-96 bg-gradient-radial from-gold-400/8 via-gold-500/3 to-transparent rounded-full -translate-x-48 translate-y-48 animate-pulse" style="animation-duration: 6s; animation-delay: 2s;"></div>
      <div class="absolute top-1/2 right-1/3 w-80 h-40 bg-gradient-radial from-gold-500/4 via-gold-500/1 to-transparent rounded-full translate-x-40 -translate-y-20 animate-pulse" style="animation-duration: 7s; animation-delay: 1s;"></div>
      
      <!-- Floating Particles -->
      <div class="absolute top-1/4 right-1/4 w-3 h-3 bg-gold-500/40 rounded-full animate-float" style="animation-delay: 0s;"></div>
      <div class="absolute top-3/4 left-1/3 w-2 h-2 bg-gold-400/50 rounded-full animate-float" style="animation-delay: 2s;"></div>
      <div class="absolute top-1/2 left-1/4 w-1.5 h-1.5 bg-gold-500/60 rounded-full animate-float" style="animation-delay: 4s;"></div>
      
      <!-- Elegant Grid Pattern -->
      <div class="absolute inset-0 opacity-3">
        <div class="w-full h-full" style="background-image: radial-gradient(circle at 2px 2px, rgba(212, 175, 55, 0.2) 1px, transparent 0); background-size: 60px 60px;"></div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto relative z-10 section-padding">
      <!-- Elegant Section Header -->
      <div class="text-center mb-32" data-aos="fade-up" data-aos-duration="1200">
        <div class="relative inline-block">
          <!-- Premium Container with Glass Effect -->
          <div class="bg-black/30 backdrop-blur-xl rounded-full px-12 py-8 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group cursor-pointer shadow-2xl hover:shadow-gold-500/10">
            <!-- Top Decorative Line -->
            <div class="absolute top-3 left-1/2 transform -translate-x-1/2 w-20 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-24 transition-all duration-500" data-aos="fade-up" data-aos-delay="200"></div>
            
            <!-- Main Title -->
            <h2 class="text-3xl md:text-4xl lg:text-5xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 mb-4 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 transition-all duration-500">
              {{ t('featuredDishes.title') }}
            </h2>
            
            <!-- Elegant Separator with Icons -->
            <div class="flex items-center justify-center space-x-3 mb-4" data-aos="fade-up" data-aos-delay="400">
              <div class="w-12 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full group-hover:w-16 transition-all duration-500"></div>
              <div class="text-gold-500 bg-gold-500/20 rounded-full p-2 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                </svg>
              </div>
              <div class="w-12 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full group-hover:w-16 transition-all duration-500"></div>
            </div>
            
            <!-- Subtitle -->
            <p class="text-base text-gray-300 font-modern group-hover:text-gold-200 transition-colors duration-500 tracking-wide max-w-2xl mx-auto leading-relaxed" data-aos="fade-up" data-aos-delay="600">
              {{ t('featuredDishes.subtitle') }}
            </p>
            
            <!-- Bottom Decorative Line -->
            <div class="absolute bottom-3 left-1/2 transform -translate-x-1/2 w-20 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-24 transition-all duration-500"></div>
          </div>
          
          <!-- Corner Decorative Elements -->
          <div class="absolute -top-1 -left-1 w-6 h-6 border-l-2 border-t-2 border-gold-500/40 rounded-tl-lg" data-aos="fade-in" data-aos-delay="800"></div>
          <div class="absolute -top-1 -right-1 w-6 h-6 border-r-2 border-t-2 border-gold-500/40 rounded-tr-lg" data-aos="fade-in" data-aos-delay="900"></div>
          <div class="absolute -bottom-1 -left-1 w-6 h-6 border-l-2 border-b-2 border-gold-500/40 rounded-bl-lg" data-aos="fade-in" data-aos-delay="1000"></div>
          <div class="absolute -bottom-1 -right-1 w-6 h-6 border-r-2 border-b-2 border-gold-500/40 rounded-br-lg" data-aos="fade-in" data-aos-delay="1100"></div>
        </div>
      </div>

      <!-- Enhanced Dishes Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-12 xl:gap-16 mb-20">
        <!-- Dish 1: Schnitzel mit Ajvar -->
        <div class="group" data-aos="fade-up" data-aos-delay="100" data-aos-duration="1000">
          <div class="relative bg-gradient-to-br from-gray-900/80 via-black/60 to-gray-800/80 backdrop-blur-xl rounded-3xl overflow-hidden shadow-2xl hover:shadow-3xl hover:shadow-gold-500/20 transition-all duration-700 transform hover:-translate-y-6 hover:scale-[1.02] border border-gray-700/50 hover:border-gold-500/40 group-hover:bg-gradient-to-br group-hover:from-gray-800/90 group-hover:via-black/70 group-hover:to-gray-700/90">
            
            <!-- Premium Corner Accents -->
            <div class="absolute top-0 right-0 w-24 h-24 bg-gradient-to-bl from-gold-500/15 to-transparent rounded-bl-full"></div>
            <div class="absolute bottom-0 left-0 w-20 h-20 bg-gradient-to-tr from-gold-500/10 to-transparent rounded-tr-full"></div>
            
            <!-- Enhanced Image Section -->
            <div class="relative overflow-hidden h-80 sm:h-96 lg:h-80 xl:h-96">
              <!-- Image with Premium Frame -->
              <div class="absolute inset-3 rounded-2xl overflow-hidden">
                <img 
                  src="https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop" 
                  alt="Schnitzel with Ajvar" 
                  class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 filter group-hover:brightness-110 group-hover:contrast-110"
                >
                <!-- Elegant Gradient Overlay -->
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent group-hover:from-black/60 transition-all duration-500"></div>
              </div>
              
              <!-- Signature Badge -->
              <div class="absolute top-8 right-8 z-10">
                <div class="bg-gradient-to-r from-gold-500 to-gold-400 text-black px-5 py-3 rounded-full font-elegant font-bold text-sm shadow-2xl shadow-gold-500/50 group-hover:scale-110 group-hover:shadow-gold-500/70 transition-all duration-300 border-2 border-gold-300/50 backdrop-blur-sm">
                  <div class="flex items-center space-x-2">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                    <span>{{ t('featuredDishes.signature') }}</span>
                  </div>
                </div>
              </div>

              <!-- Dish Name Overlay -->
              <div class="absolute bottom-8 left-8 right-8 z-10">
                <div class="bg-black/60 backdrop-blur-md rounded-2xl px-8 py-6 border border-gold-500/30 group-hover:bg-black/80 group-hover:border-gold-500/50 transition-all duration-300">
                  <h3 class="text-xl font-elegant font-bold text-white mb-3 group-hover:text-gold-300 transition-colors duration-300">
                    {{ t('featuredDishes.schnitzelAjvar') }}
                  </h3>
                  <div class="flex items-center justify-between">
                    <div class="w-20 h-0.5 bg-gold-500 rounded-full group-hover:w-28 transition-all duration-500"></div>
                    <div class="text-xl font-elegant font-bold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                      €18.50
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Enhanced Content Section -->
            <div class="p-10 space-y-8">
              <!-- Description -->
              <div class="bg-black/20 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300 group/desc">
                <p class="text-base text-gray-300 leading-relaxed font-modern group-hover/desc:text-gray-100 transition-colors duration-300 italic">
                  {{ t('featuredDishes.schnitzelAjvarDesc') }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Dish 2: Macedonian Kebapi -->
        <div class="group" data-aos="fade-up" data-aos-delay="200" data-aos-duration="1000">
          <div class="relative bg-gradient-to-br from-gray-900/80 via-black/60 to-gray-800/80 backdrop-blur-xl rounded-3xl overflow-hidden shadow-2xl hover:shadow-3xl hover:shadow-warm-800/20 transition-all duration-700 transform hover:-translate-y-6 hover:scale-[1.02] border border-gray-700/50 hover:border-warm-800/40 group-hover:bg-gradient-to-br group-hover:from-gray-800/90 group-hover:via-black/70 group-hover:to-gray-700/90">
            
            <!-- Premium Corner Accents -->
            <div class="absolute top-0 right-0 w-24 h-24 bg-gradient-to-bl from-warm-800/15 to-transparent rounded-bl-full"></div>
            <div class="absolute bottom-0 left-0 w-20 h-20 bg-gradient-to-tr from-warm-800/10 to-transparent rounded-tr-full"></div>
            
            <!-- Enhanced Image Section -->
            <div class="relative overflow-hidden h-80 sm:h-96 lg:h-80 xl:h-96">
              <!-- Image with Premium Frame -->
              <div class="absolute inset-3 rounded-2xl overflow-hidden">
                <img 
                  src="https://images.pexels.com/photos/5949888/pexels-photo-5949888.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop" 
                  alt="Macedonian Kebapi" 
                  class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 filter group-hover:brightness-110 group-hover:contrast-110"
                >
                <!-- Elegant Gradient Overlay -->
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent group-hover:from-black/60 transition-all duration-500"></div>
              </div>
              
              <!-- Spicy Badge -->
              <div class="absolute top-8 right-8 z-10">
                <div class="bg-gradient-to-r from-warm-800 to-warm-900 text-white px-5 py-3 rounded-full font-elegant font-bold text-sm shadow-2xl shadow-warm-800/50 group-hover:scale-110 group-hover:shadow-warm-800/70 transition-all duration-300 border-2 border-warm-700/50 backdrop-blur-sm">
                  <div class="flex items-center space-x-2">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2l2.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                    <span>{{ t('featuredDishes.spicy') }}</span>
                  </div>
                </div>
              </div>

              <!-- Dish Name Overlay -->
              <div class="absolute bottom-8 left-8 right-8 z-10">
                <div class="bg-black/60 backdrop-blur-md rounded-2xl px-8 py-6 border border-gold-500/30 group-hover:bg-black/80 group-hover:border-gold-500/50 transition-all duration-300">
                  <h3 class="text-xl font-elegant font-bold text-white mb-3 group-hover:text-warm-200 transition-colors duration-300">
                    {{ t('featuredDishes.macedonianKebapi') }}
                  </h3>
                  <div class="flex items-center justify-between">
                    <div class="w-20 h-0.5 bg-gold-500 rounded-full group-hover:w-28 transition-all duration-500"></div>
                    <div class="text-xl font-elegant font-bold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                      €16.00
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Enhanced Content Section -->
            <div class="p-10 space-y-8">
              <!-- Description -->
              <div class="bg-black/20 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300 group/desc">
                <p class="text-base text-gray-300 leading-relaxed font-modern group-hover/desc:text-gray-100 transition-colors duration-300 italic">
                  {{ t('featuredDishes.macedonianKebapiDesc') }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Dish 3: Balkan Sauerbraten -->
        <div class="group" data-aos="fade-up" data-aos-delay="300" data-aos-duration="1000">
          <div class="relative bg-gradient-to-br from-gray-900/80 via-black/60 to-gray-800/80 backdrop-blur-xl rounded-3xl overflow-hidden shadow-2xl hover:shadow-3xl hover:shadow-green-600/20 transition-all duration-700 transform hover:-translate-y-6 hover:scale-[1.02] border border-gray-700/50 hover:border-green-600/40 group-hover:bg-gradient-to-br group-hover:from-gray-800/90 group-hover:via-black/70 group-hover:to-gray-700/90">
            
            <!-- Premium Corner Accents -->
            <div class="absolute top-0 right-0 w-24 h-24 bg-gradient-to-bl from-green-600/15 to-transparent rounded-bl-full"></div>
            <div class="absolute bottom-0 left-0 w-20 h-20 bg-gradient-to-tr from-green-600/10 to-transparent rounded-tr-full"></div>
            
            <!-- Enhanced Image Section -->
            <div class="relative overflow-hidden h-80 sm:h-96 lg:h-80 xl:h-96">
              <!-- Image with Premium Frame -->
              <div class="absolute inset-3 rounded-2xl overflow-hidden">
                <img 
                  src="https://images.pexels.com/photos/1438672/pexels-photo-1438672.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop" 
                  alt="Balkan Sauerbraten" 
                  class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 filter group-hover:brightness-110 group-hover:contrast-110"
                >
                <!-- Elegant Gradient Overlay -->
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent group-hover:from-black/60 transition-all duration-500"></div>
              </div>
              
              <!-- Popular Badge -->
              <div class="absolute top-8 right-8 z-10">
                <div class="bg-gradient-to-r from-green-600 to-green-700 text-white px-5 py-3 rounded-full font-elegant font-bold text-sm shadow-2xl shadow-green-600/50 group-hover:scale-110 group-hover:shadow-green-600/70 transition-all duration-300 border-2 border-green-500/50 backdrop-blur-sm">
                  <div class="flex items-center space-x-2">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                    </svg>
                    <span>{{ t('featuredDishes.popular') }}</span>
                  </div>
                </div>
              </div>

              <!-- Dish Name Overlay -->
              <div class="absolute bottom-8 left-8 right-8 z-10">
                <div class="bg-black/60 backdrop-blur-md rounded-2xl px-8 py-6 border border-gold-500/30 group-hover:bg-black/80 group-hover:border-gold-500/50 transition-all duration-300">
                  <h3 class="text-xl font-elegant font-bold text-white mb-3 group-hover:text-green-300 transition-colors duration-300">
                    {{ t('featuredDishes.balkanSauerbraten') }}
                  </h3>
                  <div class="flex items-center justify-between">
                    <div class="w-20 h-0.5 bg-gold-500 rounded-full group-hover:w-28 transition-all duration-500"></div>
                    <div class="text-xl font-elegant font-bold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                      €22.00
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Enhanced Content Section -->
            <div class="p-10 space-y-8">
              <!-- Description -->
              <div class="bg-black/20 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300 group/desc">
                <p class="text-base text-gray-300 leading-relaxed font-modern group-hover/desc:text-gray-100 transition-colors duration-300 italic">
                  {{ t('featuredDishes.balkanSauerbratenDesc') }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Enhanced Call to Action -->
      <div class="text-center" data-aos="fade-up" data-aos-delay="500" data-aos-duration="1000">
        <div class="relative inline-block">
          <!-- Premium CTA Container -->
          <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 backdrop-blur-xl rounded-full px-12 py-8 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group cursor-pointer shadow-2xl hover:shadow-gold-500/10">
            
            <!-- Decorative Elements -->
            <div class="absolute top-3 left-1/2 transform -translate-x-1/2 w-20 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-24 transition-all duration-500"></div>
            <div class="absolute bottom-3 left-1/2 transform -translate-x-1/2 w-20 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-24 transition-all duration-500"></div>
            
            <!-- Content -->
            <div class="space-y-6">
              <div>
                <h3 class="text-2xl md:text-3xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 mb-3 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 transition-all duration-500">
                  {{ t('featuredDishes.exploreFullMenu') }}
                </h3>
                <p class="text-base text-gray-300 font-modern group-hover:text-gold-200 transition-colors duration-500 max-w-xl mx-auto leading-relaxed">
                  {{ t('featuredDishes.fullMenuSubtitle') }}
                </p>
              </div>
              
              <!-- Single Action Button -->
              <div class="flex justify-center">
                <button 
                  class="bg-gradient-to-r from-gold-500 to-gold-600 hover:from-gold-600 hover:to-gold-700 text-black font-bold px-8 py-4 text-sm rounded-full transition-all duration-300 transform hover:scale-105 hover:shadow-xl hover:shadow-gold-500/40 border-2 border-gold-400 hover:border-gold-300 group/btn"
                  @click="router.push('/menu')"
                >
                  <div class="flex items-center space-x-3">
                    <svg class="w-5 h-5 group-hover/btn:rotate-12 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                    </svg>
                    <span class="group-hover/btn:tracking-wider transition-all duration-300">{{ t('featuredDishes.viewFullMenu') }}</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
          
          <!-- Corner Decorative Elements -->
          <div class="absolute -top-2 -left-2 w-8 h-8 border-l-2 border-t-2 border-gold-500/40 rounded-tl-xl" data-aos="fade-in" data-aos-delay="600"></div>
          <div class="absolute -top-2 -right-2 w-8 h-8 border-r-2 border-t-2 border-gold-500/40 rounded-tr-xl" data-aos="fade-in" data-aos-delay="700"></div>
          <div class="absolute -bottom-2 -left-2 w-8 h-8 border-l-2 border-b-2 border-gold-500/40 rounded-bl-xl" data-aos="fade-in" data-aos-delay="800"></div>
          <div class="absolute -bottom-2 -right-2 w-8 h-8 border-r-2 border-b-2 border-gold-500/40 rounded-br-xl" data-aos="fade-in" data-aos-delay="900"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-30px);
  }
}

.animate-float {
  animation: float 8s ease-in-out infinite;
}

/* Custom gradient for radial backgrounds */
.bg-gradient-radial {
  background: radial-gradient(circle, var(--tw-gradient-stops));
}

/* Enhanced hover effects */
.group:hover .group-hover\:shadow-3xl {
  box-shadow: 0 35px 60px -12px rgba(0, 0, 0, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.05);
}

/* Smooth transitions for all elements */
* {
  transition-property: transform, opacity, color, background-color, border-color, box-shadow, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

/* Custom scrollbar styling */
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
</style>