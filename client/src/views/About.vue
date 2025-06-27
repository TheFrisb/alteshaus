<script setup lang="ts">
import { onMounted, nextTick } from 'vue'
import { useI18n } from 'vue-i18n'
import AOS from 'aos'
import 'aos/dist/aos.css'

const { t } = useI18n()


onMounted(() => {
  nextTick(() => {
    AOS.init({
      duration: 800,
      easing: 'ease-out-cubic',
      once: true,
      offset: 100,
      delay: 0,
      disable: false,
      startEvent: 'DOMContentLoaded',
      initClassName: 'aos-init',
      animatedClassName: 'aos-animate',
    })
  })
})
</script>

<template>
  <div class="pt-20 bg-black text-white min-h-screen">
    <!-- Enhanced Hero Section -->
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
        <div class="text-center mb-20" data-aos="fade-up" data-aos-duration="1200">
          <div class="relative inline-block">
            <!-- Premium Container with Glass Effect -->
            <div class="bg-black/30 backdrop-blur-xl rounded-full px-10 py-6 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group cursor-pointer shadow-2xl hover:shadow-gold-500/10">
              <!-- Top Decorative Line -->
              <div class="absolute top-2 left-1/2 transform -translate-x-1/2 w-16 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-20 transition-all duration-500" data-aos="fade-up" data-aos-delay="200"></div>
              
              <!-- Main Title -->
              <h1 class="text-3xl md:text-4xl lg:text-5xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 mb-4 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 transition-all duration-500">
                {{ t('about.title') }}
              </h1>
              
              <!-- Elegant Separator with Icons -->
              <div class="flex items-center justify-center space-x-3 mb-4" data-aos="fade-up" data-aos-delay="400">
                <div class="w-12 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full group-hover:w-16 transition-all duration-500"></div>
                <div class="text-gold-500 bg-gold-500/20 rounded-full p-2 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                  </svg>
                </div>
                <div class="w-12 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full group-hover:w-16 transition-all duration-500"></div>
              </div>
              
              <!-- Subtitle -->
              <p class="text-base text-gray-300 font-modern group-hover:text-gold-200 transition-colors duration-500 tracking-wide max-w-2xl mx-auto leading-relaxed" data-aos="fade-up" data-aos-delay="600">
                {{ t('about.subtitle') }}
              </p>
              
              <!-- Bottom Decorative Line -->
              <div class="absolute bottom-2 left-1/2 transform -translate-x-1/2 w-16 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-20 transition-all duration-500"></div>
            </div>
            
            <!-- Corner Decorative Elements -->
            <div class="absolute -top-1 -left-1 w-6 h-6 border-l-2 border-t-2 border-gold-500/40 rounded-tl-lg" data-aos="fade-in" data-aos-delay="800"></div>
            <div class="absolute -top-1 -right-1 w-6 h-6 border-r-2 border-t-2 border-gold-500/40 rounded-tr-lg" data-aos="fade-in" data-aos-delay="900"></div>
            <div class="absolute -bottom-1 -left-1 w-6 h-6 border-l-2 border-b-2 border-gold-500/40 rounded-bl-lg" data-aos="fade-in" data-aos-delay="1000"></div>
            <div class="absolute -bottom-1 -right-1 w-6 h-6 border-r-2 border-b-2 border-gold-500/40 rounded-br-lg" data-aos="fade-in" data-aos-delay="1100"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Our Heritage Section -->
    <section class="relative overflow-hidden bg-gradient-to-b from-gray-900 via-black to-gray-900">
      <!-- Background Elements -->
      <div class="absolute inset-0 overflow-hidden">
        <div class="absolute top-1/4 left-1/4 w-40 h-20 bg-gold-500/2 rounded-full -translate-x-20 -translate-y-10 rotate-45"></div>
        <div class="absolute bottom-1/4 right-1/4 w-32 h-16 bg-gold-500/3 rounded-full translate-x-16 translate-y-8 -rotate-45"></div>
      </div>
      
      <div class="max-w-7xl mx-auto relative z-10 section-padding">
        <!-- Section Header -->
        <div class="text-center mb-20" data-aos="fade-up" data-aos-duration="800">
          <div class="inline-block bg-black/30 backdrop-blur-xl rounded-full px-8 py-5 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-500 group cursor-pointer">
            <div class="flex items-center space-x-3 mb-3">
              <div class="text-2xl">🏛️</div>
              <h2 class="text-2xl md:text-3xl font-elegant font-bold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                {{ t('about.ourHeritage') }}
              </h2>
            </div>
            <div class="w-16 h-0.5 bg-gold-500 rounded-full mx-auto group-hover:w-20 transition-all duration-300"></div>
            <p class="text-sm text-gray-300 font-modern mt-3 group-hover:text-gold-200 transition-colors duration-300">
              {{ t('about.heritageSubtitle') }}
            </p>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <!-- Text Content -->
          <div data-aos="fade-right" data-aos-duration="1000">
            <div class="space-y-8">
              <div class="bg-gradient-to-br from-black/40 via-black/20 to-transparent backdrop-blur-xl rounded-3xl px-8 py-8 border border-gold-500/10 hover:border-gold-500/30 transition-all duration-500 hover:bg-black/30 group">
                <h3 class="text-2xl font-elegant font-bold text-gold-500 mb-4 group-hover:text-gold-400 transition-colors duration-300">
                  {{ t('about.founded2009') }}
                </h3>
                <p class="text-base text-gray-300 leading-relaxed font-modern group-hover:text-gray-100 transition-colors duration-300">
                  {{ t('about.founded2009Text') }}
                </p>
              </div>

              <div class="bg-gradient-to-br from-black/40 via-black/20 to-transparent backdrop-blur-xl rounded-3xl px-8 py-8 border border-gold-500/10 hover:border-gold-500/30 transition-all duration-500 hover:bg-black/30 group">
                <h3 class="text-2xl font-elegant font-bold text-gold-500 mb-4 group-hover:text-gold-400 transition-colors duration-300">
                  {{ t('about.culturalBridge') }}
                </h3>
                <p class="text-base text-gray-300 leading-relaxed font-modern group-hover:text-gray-100 transition-colors duration-300">
                  {{ t('about.culturalBridgeText') }}
                </p>
              </div>

              <div class="bg-gradient-to-br from-black/40 via-black/20 to-transparent backdrop-blur-xl rounded-3xl px-8 py-8 border border-gold-500/10 hover:border-gold-500/30 transition-all duration-500 hover:bg-black/30 group">
                <h3 class="text-2xl font-elegant font-bold text-gold-500 mb-4 group-hover:text-gold-400 transition-colors duration-300">
                  {{ t('about.localCommitment') }}
                </h3>
                <p class="text-base text-gray-300 leading-relaxed font-modern group-hover:text-gray-100 transition-colors duration-300">
                  {{ t('about.localCommitmentText') }}
                </p>
              </div>
            </div>
          </div>

          <!-- Image Content -->
          <div data-aos="fade-left" data-aos-duration="1000" data-aos-delay="200">
            <div class="relative">
              <div class="bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-2xl rounded-3xl overflow-hidden border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group shadow-2xl hover:shadow-gold-500/20">
                <img 
                  src="https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop" 
                  alt="Restaurant Heritage" 
                  class="w-full h-96 object-cover group-hover:scale-105 transition-transform duration-700"
                >
                <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
                <div class="absolute bottom-8 left-8 right-8">
                  <div class="bg-black/60 backdrop-blur-xl rounded-2xl px-6 py-4 border border-gold-500/30">
                    <h4 class="text-lg font-elegant font-bold text-gold-400 mb-2">{{ t('story.yearsExperience') }}</h4>
                    <p class="text-sm text-gray-300 font-modern">{{ t('about.servingAuthentic') }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Our Philosophy Section -->
    <section class="relative overflow-hidden bg-gradient-to-b from-black via-gray-900 to-black">
      <div class="absolute inset-0 overflow-hidden">
        <div class="absolute top-0 left-0 w-64 h-32 bg-gold-500/5 rounded-full -translate-x-32 -translate-y-16 rotate-12"></div>
        <div class="absolute bottom-0 right-0 w-96 h-48 bg-gold-500/3 rounded-full translate-x-48 translate-y-24 -rotate-12"></div>
      </div>
      
      <div class="max-w-7xl mx-auto relative z-10 section-padding">
        <!-- Section Header -->
        <div class="text-center mb-20" data-aos="fade-up" data-aos-duration="800">
          <div class="inline-block bg-black/30 backdrop-blur-xl rounded-full px-8 py-5 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-500 group cursor-pointer">
            <div class="flex items-center space-x-3 mb-3">
              <div class="text-2xl">🎯</div>
              <h2 class="text-2xl md:text-3xl font-elegant font-bold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                {{ t('about.ourPhilosophy') }}
              </h2>
            </div>
            <div class="w-16 h-0.5 bg-gold-500 rounded-full mx-auto group-hover:w-20 transition-all duration-300"></div>
            <p class="text-sm text-gray-300 font-modern mt-3 group-hover:text-gold-200 transition-colors duration-300">
              {{ t('about.philosophySubtitle') }}
            </p>
          </div>
        </div>

        <!-- Philosophy Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          <!-- Philosophy 1 -->
          <div class="group" data-aos="fade-up" data-aos-delay="100">
            <div class="bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-xl rounded-3xl p-8 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 hover:-translate-y-4 hover:shadow-2xl hover:shadow-gold-500/20">
              <div class="text-center">
                <div class="text-4xl mb-4">🌱</div>
                <h3 class="text-xl font-elegant font-bold text-gold-500 mb-3 group-hover:text-gold-400 transition-colors duration-300">
                  {{ t('about.freshLocal') }}
                </h3>
                <p class="text-sm text-gray-300 font-modern group-hover:text-gray-200 transition-colors duration-300">
                  {{ t('about.freshLocalText') }}
                </p>
              </div>
            </div>
          </div>

          <!-- Philosophy 2 -->
          <div class="group" data-aos="fade-up" data-aos-delay="200">
            <div class="bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-xl rounded-3xl p-8 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 hover:-translate-y-4 hover:shadow-2xl hover:shadow-gold-500/20">
              <div class="text-center">
                <div class="text-4xl mb-4">🤝</div>
                <h3 class="text-xl font-elegant font-bold text-gold-500 mb-3 group-hover:text-gold-400 transition-colors duration-300">
                  {{ t('about.culturalBridgePhilosophy') }}
                </h3>
                <p class="text-sm text-gray-300 font-modern group-hover:text-gray-200 transition-colors duration-300">
                  {{ t('about.culturalBridgePhilosophyText') }}
                </p>
              </div>
            </div>
          </div>

          <!-- Philosophy 3 -->
          <div class="group" data-aos="fade-up" data-aos-delay="300">
            <div class="bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-xl rounded-3xl p-8 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 hover:-translate-y-4 hover:shadow-2xl hover:shadow-gold-500/20">
              <div class="text-center">
                <div class="text-4xl mb-4">❤️</div>
                <h3 class="text-xl font-elegant font-bold text-gold-500 mb-3 group-hover:text-gold-400 transition-colors duration-300">
                  {{ t('about.passionHeart') }}
                </h3>
                <p class="text-sm text-gray-300 font-modern group-hover:text-gray-200 transition-colors duration-300">
                  {{ t('about.passionHeartText') }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Core Values -->
        <div class="bg-gradient-to-r from-black/50 via-black/30 to-black/50 backdrop-blur-xl rounded-3xl p-8 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-500 group" data-aos="fade-up" data-aos-delay="400">
          <div class="text-center mb-8">
            <div class="inline-flex items-center space-x-3">
              <div class="w-8 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full"></div>
              <h4 class="text-lg font-elegant font-semibold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">{{ t('about.coreValues') }}</h4>
              <div class="w-8 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full"></div>
            </div>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="text-center group/value bg-black/20 rounded-2xl py-6 hover:bg-black/40 transition-all duration-300 border border-gold-500/10 hover:border-gold-500/30">
              <div class="relative mb-3">
                <div class="text-2xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-b from-gold-400 to-gold-600 group-hover/value:scale-110 transition-transform duration-300">{{ t('about.authenticity') }}</div>
              </div>
              <div class="w-12 h-0.5 bg-gradient-to-r from-gold-500/50 to-gold-400/50 rounded-full mx-auto mb-2 group-hover/value:w-16 transition-all duration-300"></div>
              <div class="text-xs text-gray-400 font-modern group-hover/value:text-gold-300 transition-colors duration-300">{{ t('about.authenticityDesc') }}</div>
            </div>
            
            <div class="text-center group/value bg-black/20 rounded-2xl py-6 hover:bg-black/40 transition-all duration-300 border border-gold-500/10 hover:border-gold-500/30">
              <div class="relative mb-3">
                <div class="text-2xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-b from-gold-400 to-gold-600 group-hover/value:scale-110 transition-transform duration-300">{{ t('about.quality') }}</div>
              </div>
              <div class="w-12 h-0.5 bg-gradient-to-r from-gold-500/50 to-gold-400/50 rounded-full mx-auto mb-2 group-hover/value:w-16 transition-all duration-300"></div>
              <div class="text-xs text-gray-400 font-modern group-hover/value:text-gold-300 transition-colors duration-300">{{ t('about.qualityDesc') }}</div>
            </div>
            
            <div class="text-center group/value bg-black/20 rounded-2xl py-6 hover:bg-black/40 transition-all duration-300 border border-gold-500/10 hover:border-gold-500/30">
              <div class="relative mb-3">
                <div class="text-2xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-b from-gold-400 to-gold-600 group-hover/value:scale-110 transition-transform duration-300">{{ t('about.hospitality') }}</div>
              </div>
              <div class="w-12 h-0.5 bg-gradient-to-r from-gold-500/50 to-gold-400/50 rounded-full mx-auto mb-2 group-hover/value:w-16 transition-all duration-300"></div>
              <div class="text-xs text-gray-400 font-modern group-hover/value:text-gold-300 transition-colors duration-300">{{ t('about.hospitalityDesc') }}</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Experience Our Story Section -->
    <section class="relative overflow-hidden bg-gradient-to-b from-black via-gray-900 to-black">
      <div class="absolute inset-0 overflow-hidden">
        <div class="absolute top-0 left-0 w-64 h-32 bg-gold-500/5 rounded-full -translate-x-32 -translate-y-16 rotate-12"></div>
        <div class="absolute bottom-0 right-0 w-96 h-48 bg-gold-500/3 rounded-full translate-x-48 translate-y-24 -rotate-12"></div>
      </div>
      
      <div class="max-w-5xl mx-auto relative z-10 section-padding text-center" data-aos="fade-up" data-aos-duration="1000">
        <div class="relative">
          <!-- Premium CTA Container -->
          <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 backdrop-blur-xl rounded-full px-10 py-6 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group cursor-pointer shadow-2xl hover:shadow-gold-500/10">
            
            <!-- Decorative Elements -->
            <div class="absolute top-2 left-1/2 transform -translate-x-1/2 w-16 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-20 transition-all duration-500"></div>
            <div class="absolute bottom-2 left-1/2 transform -translate-x-1/2 w-16 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-20 transition-all duration-500"></div>
            
            <!-- Content -->
            <div class="space-y-4">
              <div>
                <h2 class="text-2xl md:text-3xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 mb-3 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 transition-all duration-500">
                  {{ t('about.experienceStory') }}
                </h2>
                <p class="text-sm text-gray-300 font-modern group-hover:text-gold-200 transition-colors duration-500 max-w-xl mx-auto leading-relaxed">
                  {{ t('about.experienceStorySubtitle') }}
                </p>
              </div>
              
              <!-- Action Buttons -->
              <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <button class="bg-gradient-to-r from-gold-500 to-gold-600 hover:from-gold-600 hover:to-gold-700 text-black font-bold px-8 py-3 text-sm rounded-full transition-all duration-300 transform hover:scale-105 hover:shadow-xl hover:shadow-gold-500/40 border-2 border-gold-400 hover:border-gold-300 group/btn">
                  <div class="flex items-center space-x-3">
                    <svg class="w-4 h-4 group-hover/btn:rotate-12 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                    </svg>
                    <span class="group-hover/btn:tracking-wider transition-all duration-300">{{ t('contact.makeReservation') }}</span>
                  </div>
                </button>
                
                <button class="border-2 border-gold-500 text-gold-500 hover:bg-gold-500 hover:text-black font-bold px-8 py-3 text-sm rounded-full transition-all duration-300 hover:scale-105 hover:shadow-xl hover:shadow-gold-500/30 group/btn backdrop-blur-sm bg-black/10">
                  <div class="flex items-center space-x-3">
                    <svg class="w-4 h-4 group-hover/btn:scale-110 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                    </svg>
                    <span class="group-hover/btn:tracking-wider transition-all duration-300">{{ t('featuredDishes.viewFullMenu') }}</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
          
          <!-- Corner Decorative Elements -->
          <div class="absolute -top-1 -left-1 w-6 h-6 border-l-2 border-t-2 border-gold-500/40 rounded-tl-lg" data-aos="fade-in" data-aos-delay="600"></div>
          <div class="absolute -top-1 -right-1 w-6 h-6 border-r-2 border-t-2 border-gold-500/40 rounded-tr-lg" data-aos="fade-in" data-aos-delay="700"></div>
          <div class="absolute -bottom-1 -left-1 w-6 h-6 border-l-2 border-b-2 border-gold-500/40 rounded-bl-lg" data-aos="fade-in" data-aos-delay="800"></div>
          <div class="absolute -bottom-1 -right-1 w-6 h-6 border-r-2 border-b-2 border-gold-500/40 rounded-br-lg" data-aos="fade-in" data-aos-delay="900"></div>
        </div>
      </div>
    </section>

    <!-- Visit Us Today Section -->
    <section class="relative overflow-hidden bg-gradient-to-b from-gray-900 to-black">
      <div class="absolute inset-0 overflow-hidden">
        <div class="absolute top-1/4 left-1/4 w-40 h-20 bg-gold-500/2 rounded-full -translate-x-20 -translate-y-10 rotate-45"></div>
        <div class="absolute bottom-1/4 right-1/4 w-32 h-16 bg-gold-500/3 rounded-full translate-x-16 translate-y-8 -rotate-45"></div>
      </div>
      
      <div class="max-w-7xl mx-auto relative z-10 section-padding">
        <!-- Section Header -->
        <div class="text-center mb-20" data-aos="fade-up" data-aos-duration="800">
          <div class="inline-block bg-black/30 backdrop-blur-xl rounded-full px-8 py-5 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-500 group cursor-pointer">
            <div class="flex items-center space-x-3 mb-3">
              <div class="text-2xl">📍</div>
              <h2 class="text-2xl md:text-3xl font-elegant font-bold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                {{ t('about.visitUsToday') }}
              </h2>
            </div>
            <div class="w-16 h-0.5 bg-gold-500 rounded-full mx-auto group-hover:w-20 transition-all duration-300"></div>
            <p class="text-sm text-gray-300 font-modern mt-3 group-hover:text-gold-200 transition-colors duration-300">
              {{ t('about.visitUsTodaySubtitle') }}
            </p>
          </div>
        </div>

        <div class="grid grid-cols-1 xl:grid-cols-2 gap-16 xl:gap-24">
          <!-- Contact Information -->
          <div data-aos="fade-right" data-aos-duration="1200">
            <div class="relative">
              <div class="relative bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-2xl rounded-3xl p-8 lg:p-12 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group shadow-2xl hover:shadow-gold-500/20">
                
                <!-- Header Section -->
                <div class="text-center mb-12">
                  <h3 class="text-2xl lg:text-3xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 transition-all duration-500">
                    {{ t('contact.contactInformation') }}
                  </h3>
                  <div class="w-20 h-0.5 bg-gold-500 rounded-full mx-auto mt-4 group-hover:w-24 transition-all duration-300"></div>
                </div>
                
                <!-- Contact Details -->
                <div class="space-y-8">
                  <!-- Address -->
                  <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 transition-all duration-500">
                    <div class="flex items-start space-x-6">
                      <div class="text-gold-500 bg-gold-500/20 rounded-full p-4">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                        </svg>
                      </div>
                      <div>
                        <h4 class="text-xl font-elegant font-semibold text-gold-500 mb-3">Our Location</h4>
                        <p class="text-base text-white font-modern font-medium">{{ t('common.address') }}</p>
                        <p class="text-sm text-gray-300 font-modern">{{ t('common.addressDetail') }}</p>
                      </div>
                    </div>
                  </div>

                  <!-- Phone -->
                  <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 transition-all duration-500">
                    <div class="flex items-start space-x-6">
                      <div class="text-gold-500 bg-gold-500/20 rounded-full p-4">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                        </svg>
                      </div>
                      <div>
                        <h4 class="text-xl font-elegant font-semibold text-gold-500 mb-3">Phone & Reservations</h4>
                        <a href="tel:+4921611234567" class="text-base text-white font-modern font-medium hover:text-gold-300 transition-colors duration-300 block">
                          {{ t('common.phone') }}
                        </a>
                        <p class="text-sm text-gray-300 font-modern">{{ t('contact.callForReservations') }}</p>
                      </div>
                    </div>
                  </div>

                  <!-- Hours -->
                  <div class="bg-gradient-to-r from-gold-500/10 via-gold-400/5 to-gold-500/10 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/30">
                    <div class="flex items-start space-x-6">
                      <div class="text-gold-500 bg-gold-500/30 rounded-full p-4">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                        </svg>
                      </div>
                      <div>
                        <h4 class="text-xl font-elegant font-semibold text-gold-500 mb-3">Opening Hours</h4>
                        <div class="flex items-center justify-between mb-2">
                          <span class="text-base text-white font-modern font-medium">{{ t('common.daysOpen') }}</span>
                          <span class="text-lg font-elegant font-bold text-gold-400">{{ t('common.hours') }}</span>
                        </div>
                        <p class="text-sm text-gray-300 font-modern">{{ t('contact.kitchenCloses') }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Location Visual -->
          <div data-aos="fade-left" data-aos-duration="1200" data-aos-delay="200">
            <div class="relative h-full">
              <div class="relative bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-2xl rounded-3xl overflow-hidden border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group shadow-2xl hover:shadow-gold-500/20 h-full flex flex-col">
                
                <!-- Header Section -->
                <div class="p-8 text-center border-b border-gold-500/20">
                  <h3 class="text-2xl lg:text-3xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 transition-all duration-500">
                    {{ t('contact.findUs') }}
                  </h3>
                  <div class="w-16 h-0.5 bg-gold-500 rounded-full mx-auto mt-3 group-hover:w-20 transition-all duration-300"></div>
                </div>

                <!-- Location Image -->
                <div class="relative flex-1 min-h-[300px]">
                  <img 
                    src="https://images.pexels.com/photos/1267320/pexels-photo-1267320.jpeg?auto=compress&cs=tinysrgb&w=800&h=800&fit=crop" 
                    alt="Restaurant Location in Mönchengladbach" 
                    class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter group-hover:brightness-110"
                  >
                  
                  <!-- Subtle Overlay -->
                  <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-black/10 to-transparent group-hover:from-black/40 transition-all duration-500"></div>
                  
                  <!-- Premium Location Badge -->
                  <div class="absolute top-8 right-8">
                    <div class="bg-gradient-to-r from-gold-500 to-gold-600 text-black px-6 py-3 rounded-full font-elegant font-bold text-sm shadow-2xl shadow-gold-500/50 group-hover:scale-110 group-hover:shadow-gold-500/70 transition-all duration-300 border-2 border-gold-300/50 backdrop-blur-sm">
                      <div class="flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                          <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                        </svg>
                        <span>Prime Location</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Location Features -->
                <div class="p-8 space-y-6">
                  <div class="grid grid-cols-2 gap-4">
                    <div class="bg-black/30 rounded-xl px-4 py-3 border border-gold-500/20 text-center">
                      <div class="text-gold-500 mb-2">
                        <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/>
                        </svg>
                      </div>
                      <p class="text-xs text-gray-300 font-modern">Easy Access</p>
                    </div>
                    
                    <div class="bg-black/30 rounded-xl px-4 py-3 border border-gold-500/20 text-center">
                      <div class="text-gold-500 mb-2">
                        <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
                        </svg>
                      </div>
                      <p class="text-xs text-gray-300 font-modern">Historic District</p>
                    </div>
                    
                    <div class="bg-black/30 rounded-xl px-4 py-3 border border-gold-500/20 text-center">
                      <div class="text-gold-500 mb-2">
                        <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M10.5 3L12 2l1.5 1H21l-1 6H4l-1-6h7.5z"/>
                        </svg>
                      </div>
                      <p class="text-xs text-gray-300 font-modern">Cultural Quarter</p>
                    </div>
                    
                    <div class="bg-black/30 rounded-xl px-4 py-3 border border-gold-500/20 text-center">
                      <div class="text-gold-500 mb-2">
                        <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/>
                        </svg>
                      </div>
                      <p class="text-xs text-gray-300 font-modern">City Center</p>
                    </div>
                  </div>

                  <!-- Location Details -->
                  <div class="text-center bg-black/20 rounded-xl px-6 py-4 border border-gold-500/20">
                    <p class="text-lg font-elegant font-semibold text-white mb-2">Mönchengladbach</p>
                    <p class="text-sm text-gray-300 font-modern">Historic Old Town District</p>
                    <div class="flex items-center justify-center space-x-2 mt-3">
                      <div class="w-2 h-2 bg-gold-500 rounded-full animate-pulse"></div>
                      <p class="text-xs text-gold-400 font-modern font-semibold">Open Daily 17:00 - 23:00</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
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