<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const router = useRouter()

const scrollToNextSection = () => {
  const nextSection = document.querySelector('#story')
  if (nextSection) {
    nextSection.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<template>
  <section class="relative min-h-screen flex items-center justify-center overflow-hidden pt-28 pb-12">
    <!-- Enhanced Background with Multiple Layers -->
    <div class="absolute inset-0 z-0">
      <!-- Main Background Image -->
      <img 
        src="https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&w=1920&h=1080&fit=crop"
        alt="Restaurant Interior" 
        class="w-full h-full object-cover"
      >
      <!-- Gradient Overlays for Better Text Readability -->
      <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-black/70"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-black/30 via-transparent to-black/30"></div>
      
      <!-- Animated Background Elements -->
      <div class="absolute top-1/4 left-1/4 w-96 h-48 bg-gold-500/5 rounded-full animate-pulse"></div>
      <div class="absolute bottom-1/3 right-1/4 w-64 h-32 bg-gold-500/3 rounded-full animate-pulse" style="animation-delay: 1s;"></div>
    </div>

    <!-- Decorative Frame Elements -->
    <div class="absolute inset-0 z-5 pointer-events-none">
      <!-- Top Border -->
      <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-gold-500/50 to-transparent"></div>
      <!-- Bottom Border -->
      <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-gold-500/50 to-transparent"></div>
      <!-- Side Accents -->
      <div class="absolute top-1/4 left-0 w-1 h-32 bg-gradient-to-b from-transparent via-gold-500/40 to-transparent"></div>
      <div class="absolute top-1/4 right-0 w-1 h-32 bg-gradient-to-b from-transparent via-gold-500/40 to-transparent"></div>
    </div>

    <!-- Main Content Container -->
    <div class="relative z-10 w-full max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8 items-center">
        
        <!-- Left Content Section -->
        <div class="lg:col-span-7 text-center lg:text-left space-y-6">
          <!-- Restaurant Branding -->
          <div data-aos="fade-right" data-aos-duration="1200">
            <!-- Premium Logo Container -->
            <div class="inline-block bg-black/20 backdrop-blur-md rounded-full px-10 py-6 hover:bg-black/30 transition-all duration-500 group cursor-pointer border border-gold-500/20 hover:border-gold-500/40">
              <h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-elegant font-bold mb-2 group-hover:scale-105 transition-transform duration-500">
                <span class="text-gold-500 group-hover:text-gold-400 transition-colors duration-300">{{ t('hero.title').split('Haus')[0] }}</span><span class="text-white group-hover:text-gold-200 transition-colors duration-300">Haus</span>
              </h1>
              
              <!-- Elegant Separator -->
              <div class="flex items-center justify-center lg:justify-start space-x-2 mb-2">
                <div class="w-8 h-0.5 bg-gold-500 rounded-full group-hover:w-12 transition-all duration-500"></div>
                <div class="text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                  <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                  </svg>
                </div>
                <div class="w-8 h-0.5 bg-gold-500 rounded-full group-hover:w-12 transition-all duration-500"></div>
              </div>
              
              <!-- Tagline -->
              <p class="text-xs md:text-sm text-gray-200 font-modern font-light tracking-wider group-hover:text-gold-200 transition-colors duration-300">
                {{ t('hero.subtitle') }}
              </p>
              <p class="text-xs text-gold-400 font-elegant italic mt-1 group-hover:text-gold-300 transition-colors duration-300">
                {{ t('hero.tagline') }}
              </p>
            </div>
          </div>

          <!-- Description -->
          <div data-aos="fade-right" data-aos-delay="400" data-aos-duration="1000">
            <div class="bg-black/15 backdrop-blur-sm rounded-full px-4 py-3 hover:bg-black/25 transition-all duration-300 border border-gold-500/10 hover:border-gold-500/30">
              <p class="text-xs md:text-sm text-gray-200 font-modern leading-relaxed max-w-xl mx-auto lg:mx-0">
                {{ t('hero.description') }}
              </p>
            </div>
          </div>

          <!-- Action Buttons -->
          <div data-aos="fade-right" data-aos-delay="600" data-aos-duration="1000">
            <div class="flex flex-col sm:flex-row gap-3 justify-center lg:justify-start items-center">
              <button 
                class="bg-gradient-to-r from-gold-500 to-gold-600 hover:from-gold-600 hover:to-gold-700 text-black font-semibold px-5 py-2.5 text-xs rounded-full transition-all duration-300 transform hover:scale-105 hover:shadow-xl hover:shadow-gold-500/40 group border-2 border-gold-400 hover:border-gold-300"
                @click="router.push('/menu')"
              >
                <div class="flex items-center space-x-2">
                  <svg class="w-3 h-3 group-hover:rotate-12 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                  </svg>
                  <span class="group-hover:tracking-wider transition-all duration-300">{{ t('hero.exploreMenu') }}</span>
                </div>
              </button>
              
              <button class="border-2 border-gold-500 text-gold-500 hover:bg-gold-500 hover:text-black font-semibold px-5 py-2.5 text-xs rounded-full transition-all duration-300 hover:scale-105 hover:shadow-xl hover:shadow-gold-500/30 group backdrop-blur-sm bg-black/10 hover:bg-gold-500">
                <div class="flex items-center space-x-2">
                  <svg class="w-3 h-3 group-hover:scale-110 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                  </svg>
                  <span class="group-hover:tracking-wider transition-all duration-300">{{ t('hero.reserveTable') }}</span>
                </div>
              </button>
            </div>
          </div>

          <!-- Contact Information -->
          <div data-aos="fade-right" data-aos-delay="800" data-aos-duration="1000">
            <div class="bg-black/15 backdrop-blur-sm rounded-full px-3 py-2 hover:bg-black/25 transition-all duration-300 inline-block border border-gold-500/10 hover:border-gold-500/30">
              <div class="flex items-center space-x-3 text-center lg:text-left">
                <div class="text-gold-500 bg-gold-500/20 rounded-full p-1.5">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                  </svg>
                </div>
                <div>
                  <p class="text-xs text-gray-400 font-modern">{{ t('hero.forReservations') }}</p>
                  <a 
                    href="tel:+4921611234567" 
                    class="text-gold-500 hover:text-gold-400 transition-all duration-300 font-modern text-xs font-semibold hover:tracking-wider"
                  >
                    {{ t('common.phone') }}
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Info Panel -->
        <div class="lg:col-span-5" data-aos="fade-left" data-aos-delay="400" data-aos-duration="1200">
          <div class="bg-black/20 backdrop-blur-md rounded-3xl p-4 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-500 hover:bg-black/30">
            
            <!-- Info Header -->
            <div class="text-center mb-4">
              <div class="w-6 h-0.5 bg-gold-500 rounded-full mx-auto mb-2"></div>
              <h3 class="text-lg font-elegant font-bold text-gold-500 mb-1">{{ t('hero.visitUs') }}</h3>
              <div class="w-6 h-0.5 bg-gold-500 rounded-full mx-auto"></div>
            </div>

            <!-- Location & Hours Grid -->
            <div class="space-y-3">
              <!-- Location -->
              <div class="bg-black/20 rounded-full px-3 py-2 hover:bg-black/30 transition-all duration-300 group cursor-pointer">
                <div class="flex items-center space-x-3">
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-1.5 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="text-white font-semibold font-modern text-xs group-hover:text-gold-400 transition-colors duration-300">{{ t('hero.location') }}</h4>
                    <p class="text-gray-300 font-modern text-xs group-hover:text-gray-200 transition-colors duration-300">{{ t('common.address') }}</p>
                    <p class="text-gray-400 font-modern text-xs group-hover:text-gray-300 transition-colors duration-300">{{ t('common.addressDetail') }}</p>
                  </div>
                </div>
              </div>

              <!-- Hours -->
              <div class="bg-black/20 rounded-full px-3 py-2 hover:bg-black/30 transition-all duration-300 group cursor-pointer">
                <div class="flex items-center space-x-3">
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-1.5 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="text-white font-semibold font-modern text-xs group-hover:text-gold-400 transition-colors duration-300">{{ t('hero.openingHours') }}</h4>
                    <p class="text-gold-400 font-modern text-xs font-semibold group-hover:text-gold-300 transition-colors duration-300">{{ t('common.hours') }}</p>
                    <p class="text-gray-400 font-modern text-xs group-hover:text-gray-300 transition-colors duration-300">{{ t('common.daysOpen') }}</p>
                  </div>
                </div>
              </div>

              <!-- Special Notice -->
              <div class="bg-gradient-to-r from-gold-500/10 to-gold-400/10 rounded-full px-3 py-2 border border-gold-500/30 hover:from-gold-500/20 hover:to-gold-400/20 hover:border-gold-500/50 transition-all duration-300 group cursor-pointer">
                <div class="flex items-center space-x-3">
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-1.5 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                    <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="text-gold-500 font-semibold font-modern text-xs group-hover:text-gold-400 transition-colors duration-300">{{ t('nav.reservations') }}</h4>
                    <p class="text-gray-300 font-modern text-xs group-hover:text-white transition-colors duration-300">{{ t('contact.reservationsRecommended').split(',')[0] }}</p>
                    <p class="text-gray-400 font-modern text-xs group-hover:text-gray-300 transition-colors duration-300">{{ t('contact.reservationsRecommended').split(',')[1] }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Awards Section -->
            <div class="mt-4 pt-3 border-t border-gold-500/20">
              <div class="text-center">
                <div class="flex justify-center space-x-1 mb-1">
                  <div class="text-gold-500">
                    <svg class="w-2 h-2" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                  </div>
                  <div class="text-gold-500">
                    <svg class="w-2 h-2" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                  </div>
                  <div class="text-gold-500">
                    <svg class="w-2 h-2" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                  </div>
                </div>
                <p class="text-gold-400 font-elegant text-xs font-semibold">{{ t('hero.awardWinning') }}</p>
                <p class="text-gray-400 font-modern text-xs">{{ t('hero.since2009') }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Enhanced Scroll Indicator -->
    <div 
      class="absolute bottom-4 left-1/2 transform -translate-x-1/2 z-20"
      data-aos="fade-in"
      data-aos-delay="1400"
    >
      <div class="bg-black/30 backdrop-blur-sm rounded-full p-2 hover:bg-black/50 transition-all duration-300 border border-gold-500/20 hover:border-gold-500/40">
        <button 
          @click="scrollToNextSection"
          class="text-gold-500 hover:text-gold-400 transition-all duration-300 animate-bounce hover:scale-110 group"
        >
          <svg class="w-4 h-4 group-hover:translate-y-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Decorative Corner Elements -->
    <div class="absolute top-32 left-2 opacity-30 z-5" data-aos="fade-right" data-aos-delay="1600">
      <div class="w-8 h-8 border-l-2 border-t-2 border-gold-500/40 rounded-tl-lg"></div>
    </div>
    <div class="absolute top-32 right-2 opacity-30 z-5" data-aos="fade-left" data-aos-delay="1600">
      <div class="w-8 h-8 border-r-2 border-t-2 border-gold-500/40 rounded-tr-lg"></div>
    </div>
    <div class="absolute bottom-12 left-2 opacity-30 z-5" data-aos="fade-right" data-aos-delay="1800">
      <div class="w-8 h-8 border-l-2 border-b-2 border-gold-500/40 rounded-bl-lg"></div>
    </div>
    <div class="absolute bottom-12 right-2 opacity-30 z-5" data-aos="fade-left" data-aos-delay="1800">
      <div class="w-8 h-8 border-r-2 border-b-2 border-gold-500/40 rounded-br-lg"></div>
    </div>
  </section>
</template>

<style scoped>
@keyframes bounce {
  0%, 20%, 53%, 80%, 100% {
    transform: translate3d(0,0,0);
  }
  40%, 43% {
    transform: translate3d(0, -8px, 0);
  }
  70% {
    transform: translate3d(0, -4px, 0);
  }
  90% {
    transform: translate3d(0, -2px, 0);
  }
}

.animate-bounce {
  animation: bounce 2s infinite;
}
</style>