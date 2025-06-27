<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
  <section id="story" class="relative overflow-hidden bg-gradient-to-b from-gray-900 via-black to-gray-900">
    <!-- Enhanced Background Elements with Animation -->
    <div class="absolute inset-0 overflow-hidden">
      <!-- Animated Gradient Orbs -->
      <div class="absolute top-0 left-0 w-96 h-96 bg-gradient-radial from-gold-500/8 via-gold-500/3 to-transparent rounded-full -translate-x-48 -translate-y-48 animate-pulse" style="animation-duration: 4s;"></div>
      <div class="absolute bottom-0 right-0 w-[500px] h-[300px] bg-gradient-radial from-gold-400/6 via-gold-500/2 to-transparent rounded-full translate-x-64 translate-y-32 animate-pulse" style="animation-duration: 6s; animation-delay: 1s;"></div>
      <div class="absolute top-1/2 left-1/3 w-64 h-32 bg-gradient-radial from-gold-500/4 via-gold-500/1 to-transparent rounded-full -translate-x-32 -translate-y-16 animate-pulse" style="animation-duration: 5s; animation-delay: 2s;"></div>
      
      <!-- Floating Particles -->
      <div class="absolute top-1/4 left-1/4 w-2 h-2 bg-gold-500/30 rounded-full animate-float" style="animation-delay: 0s;"></div>
      <div class="absolute top-3/4 right-1/3 w-1.5 h-1.5 bg-gold-400/40 rounded-full animate-float" style="animation-delay: 1s;"></div>
      <div class="absolute top-1/2 right-1/4 w-1 h-1 bg-gold-500/50 rounded-full animate-float" style="animation-delay: 2s;"></div>
      
      <!-- Elegant Grid Pattern -->
      <div class="absolute inset-0 opacity-5">
        <div class="w-full h-full" style="background-image: radial-gradient(circle at 1px 1px, rgba(212, 175, 55, 0.3) 1px, transparent 0); background-size: 40px 40px;"></div>
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
              {{ t('story.title') }}
            </h2>
            
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
            <p class="text-base text-gray-300 font-modern italic group-hover:text-gold-200 transition-colors duration-500 tracking-wide" data-aos="fade-up" data-aos-delay="600">
              {{ t('story.subtitle') }}
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

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-24 items-center">
        <!-- Enhanced Text Content -->
        <div data-aos="fade-right" data-aos-duration="1400" data-aos-delay="200">
          <div class="space-y-12">
            <!-- Story Paragraphs with Enhanced Design -->
            <div class="relative group">
              <div class="absolute -left-6 top-0 w-1 h-full bg-gradient-to-b from-gold-500/60 via-gold-500/30 to-transparent rounded-full group-hover:w-1.5 transition-all duration-500"></div>
              <div class="bg-gradient-to-br from-black/40 via-black/20 to-transparent backdrop-blur-xl rounded-3xl px-8 py-8 border border-gold-500/10 hover:border-gold-500/30 transition-all duration-500 hover:bg-black/30 group cursor-pointer">
                <div class="flex items-start space-x-4">
                  <div class="flex-shrink-0 w-3 h-3 bg-gradient-to-r from-gold-500 to-gold-400 rounded-full mt-2 group-hover:scale-150 transition-transform duration-300 shadow-lg shadow-gold-500/50"></div>
                  <div>
                    <h3 class="text-xl font-elegant font-semibold text-gold-500 mb-4 group-hover:text-gold-400 transition-colors duration-300">
                      {{ t('story.culinaryBridge') }}
                    </h3>
                    <p class="text-base text-gray-300 leading-relaxed font-modern group-hover:text-gray-100 transition-colors duration-300">
                      {{ t('story.culinaryBridgeText') }}
                    </p>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="relative group">
              <div class="absolute -left-6 top-0 w-1 h-full bg-gradient-to-b from-gold-500/30 via-gold-500/60 to-transparent rounded-full group-hover:w-1.5 transition-all duration-500"></div>
              <div class="bg-gradient-to-br from-black/40 via-black/20 to-transparent backdrop-blur-xl rounded-3xl px-8 py-8 border border-gold-500/10 hover:border-gold-500/30 transition-all duration-500 hover:bg-black/30 group cursor-pointer">
                <div class="flex items-start space-x-4">
                  <div class="flex-shrink-0 w-3 h-3 bg-gradient-to-r from-gold-400 to-gold-500 rounded-full mt-2 group-hover:scale-150 transition-transform duration-300 shadow-lg shadow-gold-500/50"></div>
                  <div>
                    <h3 class="text-xl font-elegant font-semibold text-gold-500 mb-4 group-hover:text-gold-400 transition-colors duration-300">
                      {{ t('story.passionArtistry') }}
                    </h3>
                    <p class="text-base text-gray-300 leading-relaxed font-modern group-hover:text-gray-100 transition-colors duration-300">
                      {{ t('story.passionArtistryText') }}
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Enhanced Stats Section -->
            <div class="relative" data-aos="fade-up" data-aos-delay="800">
              <div class="bg-gradient-to-r from-black/50 via-black/30 to-black/50 backdrop-blur-xl rounded-3xl p-8 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-500 group">
                <!-- Decorative Header -->
                <div class="text-center mb-8">
                  <div class="inline-flex items-center space-x-3">
                    <div class="w-8 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full"></div>
                    <h4 class="text-lg font-elegant font-semibold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">{{ t('story.ourLegacy') }}</h4>
                    <div class="w-8 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full"></div>
                  </div>
                </div>
                
                <div class="grid grid-cols-3 gap-6">
                  <div class="text-center group/stat bg-black/20 rounded-2xl py-6 hover:bg-black/40 transition-all duration-300 border border-gold-500/10 hover:border-gold-500/30">
                    <div class="relative mb-3">
                      <div class="text-3xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-b from-gold-400 to-gold-600 group-hover/stat:scale-110 transition-transform duration-300">15+</div>
                      <div class="absolute -top-1 left-1/2 transform -translate-x-1/2 w-8 h-8 bg-gold-500/10 rounded-full group-hover/stat:scale-150 transition-transform duration-300"></div>
                    </div>
                    <div class="w-12 h-0.5 bg-gradient-to-r from-gold-500/50 to-gold-400/50 rounded-full mx-auto mb-2 group-hover/stat:w-16 transition-all duration-300"></div>
                    <div class="text-xs text-gray-400 font-modern uppercase tracking-wider group-hover/stat:text-gold-300 transition-colors duration-300">{{ t('story.yearsExperience') }}</div>
                  </div>
                  
                  <div class="text-center group/stat bg-black/20 rounded-2xl py-6 hover:bg-black/40 transition-all duration-300 border border-gold-500/10 hover:border-gold-500/30">
                    <div class="relative mb-3">
                      <div class="text-3xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-b from-gold-400 to-gold-600 group-hover/stat:scale-110 transition-transform duration-300">50+</div>
                      <div class="absolute -top-1 left-1/2 transform -translate-x-1/2 w-8 h-8 bg-gold-500/10 rounded-full group-hover/stat:scale-150 transition-transform duration-300"></div>
                    </div>
                    <div class="w-12 h-0.5 bg-gradient-to-r from-gold-500/50 to-gold-400/50 rounded-full mx-auto mb-2 group-hover/stat:w-16 transition-all duration-300"></div>
                    <div class="text-xs text-gray-400 font-modern uppercase tracking-wider group-hover/stat:text-gold-300 transition-colors duration-300">{{ t('story.signatureDishes') }}</div>
                  </div>
                  
                  <div class="text-center group/stat bg-black/20 rounded-2xl py-6 hover:bg-black/40 transition-all duration-300 border border-gold-500/10 hover:border-gold-500/30">
                    <div class="relative mb-3">
                      <div class="text-3xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-b from-gold-400 to-gold-600 group-hover/stat:scale-110 transition-transform duration-300">2</div>
                      <div class="absolute -top-1 left-1/2 transform -translate-x-1/2 w-8 h-8 bg-gold-500/10 rounded-full group-hover/stat:scale-150 transition-transform duration-300"></div>
                    </div>
                    <div class="w-12 h-0.5 bg-gradient-to-r from-gold-500/50 to-gold-400/50 rounded-full mx-auto mb-2 group-hover/stat:w-16 transition-all duration-300"></div>
                    <div class="text-xs text-gray-400 font-modern uppercase tracking-wider group-hover/stat:text-gold-300 transition-colors duration-300">{{ t('story.culinaryTraditions') }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Enhanced Call to Action -->
            <div class="pt-8" data-aos="fade-up" data-aos-delay="1000">
              <div class="flex flex-col sm:flex-row gap-4">
                <button class="bg-gradient-to-r from-gold-500 to-gold-600 hover:from-gold-600 hover:to-gold-700 text-black font-semibold px-8 py-4 text-sm rounded-full transition-all duration-300 group hover:scale-105 hover:shadow-xl hover:shadow-gold-500/40 border-2 border-gold-400 hover:border-gold-300">
                  <div class="flex items-center justify-center space-x-2">
                    <svg class="w-4 h-4 group-hover:rotate-12 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                    </svg>
                    <span class="group-hover:tracking-wider transition-all duration-300">{{ t('story.discoverHeritage') }}</span>
                  </div>
                </button>
                
                <button class="border-2 border-gold-500 text-gold-500 hover:bg-gold-500 hover:text-black font-semibold px-8 py-4 text-sm rounded-full transition-all duration-300 group hover:scale-105 hover:shadow-xl hover:shadow-gold-500/30 backdrop-blur-sm bg-black/10">
                  <div class="flex items-center justify-center space-x-2">
                    <svg class="w-4 h-4 group-hover:scale-110 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                    </svg>
                    <span class="group-hover:tracking-wider transition-all duration-300">{{ t('story.visitToday') }}</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Enhanced Image Content -->
        <div data-aos="fade-left" data-aos-duration="1400" data-aos-delay="400">
          <div class="relative">
            <!-- Professional Master Chef Showcase -->
            <div class="relative max-w-lg mx-auto">
              <!-- Premium Background Frame -->
              <div class="absolute inset-0 bg-gradient-to-br from-gold-500/10 via-transparent to-gold-400/5 rounded-3xl transform rotate-1 scale-105"></div>
              <div class="absolute inset-0 bg-gradient-to-tl from-gold-400/8 via-transparent to-gold-500/8 rounded-3xl transform -rotate-1 scale-105"></div>
              
              <!-- Main Content Container -->
              <div class="relative bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-2xl rounded-3xl p-6 sm:p-8 lg:p-10 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group cursor-pointer shadow-2xl hover:shadow-gold-500/20">
                
                <!-- Header Section -->
                <div class="text-center mb-8">
                  <div class="inline-flex items-center space-x-3 mb-4">
                    <div class="w-8 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full group-hover:w-12 transition-all duration-500"></div>
                    <div class="text-gold-500 bg-gold-500/20 rounded-full p-2 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                      </svg>
                    </div>
                    <div class="w-8 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full group-hover:w-12 transition-all duration-500"></div>
                  </div>
                  <h3 class="text-2xl sm:text-3xl lg:text-4xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 transition-all duration-500">
                    {{ t('story.masterChef') }}
                  </h3>
                  <p class="text-sm text-gray-300 font-modern italic mt-2 group-hover:text-gold-200 transition-colors duration-300">
                    {{ t('story.culinaryExcellence') }}
                  </p>
                </div>

                <!-- Chef Image with Elegant Frame -->
                <div class="relative mb-8">
                  <!-- Outer Glow Effect -->
                  <div class="absolute -inset-3 bg-gradient-to-r from-gold-500/20 via-gold-400/10 to-gold-500/20 rounded-full blur-xl group-hover:blur-2xl transition-all duration-700"></div>
                  
                  <!-- Image Container -->
                  <div class="relative w-48 h-48 sm:w-56 sm:h-56 lg:w-64 lg:h-64 mx-auto">
                    <!-- Premium Border Frame -->
                    <div class="absolute inset-0 rounded-full bg-gradient-to-br from-gold-500/30 via-gold-400/20 to-gold-500/30 p-1 group-hover:from-gold-500/50 group-hover:via-gold-400/30 group-hover:to-gold-500/50 transition-all duration-500">
                      <div class="w-full h-full rounded-full bg-gradient-to-br from-black/80 to-black/60 p-1">
                        <div class="relative w-full h-full rounded-full overflow-hidden bg-gradient-to-br from-gold-500/10 to-transparent">
                          <img 
                            src="https://images.pexels.com/photos/1367269/pexels-photo-1367269.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop" 
                            alt="Master Chef Marcus Weber" 
                            class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700 filter group-hover:brightness-110"
                          >
                          <!-- Subtle Overlay -->
                          <div class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent group-hover:from-black/20 transition-all duration-500"></div>
                        </div>
                      </div>
                    </div>
                    
                    <!-- Floating Achievement Badge -->
                    <div class="absolute -top-2 -right-2 sm:-top-3 sm:-right-3 bg-gradient-to-r from-gold-500 to-gold-600 rounded-full p-2 sm:p-3 shadow-xl shadow-gold-500/50 group-hover:scale-110 group-hover:shadow-gold-500/70 transition-all duration-300 border-2 border-gold-300/50">
                      <svg class="w-4 h-4 sm:w-5 sm:h-5 text-black" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                      </svg>
                    </div>
                  </div>
                </div>

                <!-- Chef Information -->
                <div class="text-center space-y-6">
                  <!-- Name and Title -->
                  <div class="bg-black/30 backdrop-blur-sm rounded-2xl px-6 py-4 border border-gold-500/20 group-hover:border-gold-500/40 group-hover:bg-black/40 transition-all duration-300">
                    <h4 class="text-xl sm:text-2xl font-elegant font-bold text-gold-500 mb-2 group-hover:text-gold-400 transition-colors duration-300">
                      Marcus Weber
                    </h4>
                    <div class="w-16 h-0.5 bg-gold-500 rounded-full mx-auto mb-3 group-hover:w-20 transition-all duration-300"></div>
                    <p class="text-sm text-gray-300 font-modern group-hover:text-gray-200 transition-colors duration-300">
                      {{ t('story.executiveChef') }}
                    </p>
                    <p class="text-xs text-gold-400 font-modern italic mt-1 group-hover:text-gold-300 transition-colors duration-300">
                      {{ t('story.germanMacedonianSpecialist') }}
                    </p>
                  </div>

                  <!-- Expertise Grid -->
                  <div class="grid grid-cols-2 gap-4">
                    <div class="bg-black/20 rounded-xl px-4 py-3 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300 group/skill text-center">
                      <div class="text-gold-500 mb-2 group-hover/skill:text-gold-400 transition-colors duration-300">
                        <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                        </svg>
                      </div>
                      <p class="text-xs text-gray-300 font-modern group-hover/skill:text-gray-200 transition-colors duration-300">15+</p>
                      <p class="text-xs text-gold-400 font-elegant group-hover/skill:text-gold-300 transition-colors duration-300">{{ t('story.experience') }}</p>
                    </div>
                    
                    <div class="bg-black/20 rounded-xl px-4 py-3 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300 group/skill text-center">
                      <div class="text-gold-500 mb-2 group-hover/skill:text-gold-400 transition-colors duration-300">
                        <svg class="w-5 h-5 mx-auto" fill="currentColor" viewBox="0 0 24 24">
                          <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                        </svg>
                      </div>
                      <p class="text-xs text-gray-300 font-modern group-hover/skill:text-gray-200 transition-colors duration-300">{{ t('story.awardWinning').split(' ')[0] }}</p>
                      <p class="text-xs text-gold-400 font-elegant group-hover/skill:text-gold-300 transition-colors duration-300">{{ t('story.awardWinning').split(' ')[1] }}</p>
                    </div>
                    
                    <div class="bg-black/20 rounded-xl px-4 py-3 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300 group/skill text-center">
                      <div class="text-gold-500 mb-2 group-hover/skill:text-gold-400 transition-colors duration-300">
                        <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                        </svg>
                      </div>
                      <p class="text-xs text-gray-300 font-modern group-hover/skill:text-gray-200 transition-colors duration-300">{{ t('story.passionDriven').split(' ')[0] }}</p>
                      <p class="text-xs text-gold-400 font-elegant group-hover/skill:text-gold-300 transition-colors duration-300">{{ t('story.passionDriven').split(' ')[1] }}</p>
                    </div>
                    
                    <div class="bg-black/20 rounded-xl px-4 py-3 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300 group/skill text-center">
                      <div class="text-gold-500 mb-2 group-hover/skill:text-gold-400 transition-colors duration-300">
                        <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                        </svg>
                      </div>
                      <p class="text-xs text-gray-300 font-modern group-hover/skill:text-gray-200 transition-colors duration-300">{{ t('story.globalCuisine').split(' ')[0] }}</p>
                      <p class="text-xs text-gold-400 font-elegant group-hover/skill:text-gold-300 transition-colors duration-300">{{ t('story.globalCuisine').split(' ')[1] }}</p>
                    </div>
                  </div>

                  <!-- Signature Quote -->
                  <div class="bg-gradient-to-r from-gold-500/10 via-gold-400/5 to-gold-500/10 rounded-2xl px-6 py-4 border border-gold-500/20 hover:border-gold-500/40 hover:from-gold-500/15 hover:via-gold-400/10 hover:to-gold-500/15 transition-all duration-300">
                    <div class="text-gold-500 mb-3">
                      <svg class="w-6 h-6 mx-auto" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h4v10h-10z"/>
                      </svg>
                    </div>
                    <p class="text-sm text-gray-300 font-modern italic leading-relaxed mb-3 group-hover:text-white transition-colors duration-300">
                      "{{ t('story.quote') }}"
                    </p>
                    <div class="flex items-center justify-center space-x-2">
                      <div class="w-8 h-0.5 bg-gold-500 rounded-full"></div>
                      <p class="text-xs text-gold-400 font-elegant font-semibold">Chef Marcus</p>
                      <div class="w-8 h-0.5 bg-gold-500 rounded-full"></div>
                    </div>
                  </div>
                </div>

                <!-- Bottom Decorative Element -->
                <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-1">
                  <div class="w-2 h-2 bg-gold-500/30 rounded-full animate-pulse"></div>
                  <div class="w-2 h-2 bg-gold-500/50 rounded-full animate-pulse" style="animation-delay: 0.2s;"></div>
                  <div class="w-2 h-2 bg-gold-500/30 rounded-full animate-pulse" style="animation-delay: 0.4s;"></div>
                </div>
              </div>

              <!-- Elegant Corner Accents -->
              <div class="absolute -top-4 -left-4 w-8 h-8 border-l-2 border-t-2 border-gold-500/30 rounded-tl-2xl group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1200"></div>
              <div class="absolute -top-4 -right-4 w-8 h-8 border-r-2 border-t-2 border-gold-500/30 rounded-tr-2xl group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1300"></div>
              <div class="absolute -bottom-4 -left-4 w-8 h-8 border-l-2 border-b-2 border-gold-500/30 rounded-bl-2xl group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1400"></div>
              <div class="absolute -bottom-4 -right-4 w-8 h-8 border-r-2 border-b-2 border-gold-500/30 rounded-tr-2xl group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1500"></div>
            </div>
          </div>
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
    transform: translateY(-20px);
  }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

/* Custom gradient for radial backgrounds */
.bg-gradient-radial {
  background: radial-gradient(circle, var(--tw-gradient-stops));
}

/* Enhanced pulse animation */
@keyframes enhanced-pulse {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.7;
    transform: scale(1.05);
  }
}

.animate-enhanced-pulse {
  animation: enhanced-pulse 3s ease-in-out infinite;
}
</style>