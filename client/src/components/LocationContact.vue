<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
  <section class="relative overflow-hidden bg-gradient-to-b from-black via-gray-900 to-black">
    <!-- Enhanced Background Elements with Animation -->
    <div class="absolute inset-0 overflow-hidden">
      <!-- Animated Gradient Orbs -->
      <div class="absolute top-0 right-0 w-[500px] h-[300px] bg-gradient-radial from-gold-500/8 via-gold-500/3 to-transparent rounded-full translate-x-64 -translate-y-32 animate-pulse" style="animation-duration: 6s;"></div>
      <div class="absolute bottom-0 left-0 w-96 h-96 bg-gradient-radial from-gold-400/6 via-gold-500/2 to-transparent rounded-full -translate-x-48 translate-y-48 animate-pulse" style="animation-duration: 8s; animation-delay: 1s;"></div>
      <div class="absolute top-1/2 left-1/4 w-80 h-40 bg-gradient-radial from-gold-500/4 via-gold-500/1 to-transparent rounded-full -translate-x-40 -translate-y-20 animate-pulse" style="animation-duration: 7s; animation-delay: 2s;"></div>
      
      <!-- Floating Particles -->
      <div class="absolute top-1/4 right-1/4 w-2 h-2 bg-gold-500/40 rounded-full animate-float" style="animation-delay: 0s;"></div>
      <div class="absolute top-3/4 left-1/3 w-1.5 h-1.5 bg-gold-400/50 rounded-full animate-float" style="animation-delay: 2s;"></div>
      <div class="absolute top-1/2 right-1/3 w-1 h-1 bg-gold-500/60 rounded-full animate-float" style="animation-delay: 4s;"></div>
      
      <!-- Elegant Grid Pattern -->
      <div class="absolute inset-0 opacity-3">
        <div class="w-full h-full" style="background-image: radial-gradient(circle at 2px 2px, rgba(212, 175, 55, 0.2) 1px, transparent 0); background-size: 50px 50px;"></div>
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
              {{ t('contact.title') }}
            </h2>
            
            <!-- Elegant Separator with Icons -->
            <div class="flex items-center justify-center space-x-3 mb-4" data-aos="fade-up" data-aos-delay="400">
              <div class="w-12 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full group-hover:w-16 transition-all duration-500"></div>
              <div class="text-gold-500 bg-gold-500/20 rounded-full p-2 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </div>
              <div class="w-12 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full group-hover:w-16 transition-all duration-500"></div>
            </div>
            
            <!-- Subtitle -->
            <p class="text-base text-gray-300 font-modern group-hover:text-gold-200 transition-colors duration-500 tracking-wide max-w-xl mx-auto leading-relaxed" data-aos="fade-up" data-aos-delay="600">
              {{ t('contact.subtitle') }}
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

      <div class="grid grid-cols-1 xl:grid-cols-2 gap-16 xl:gap-24">
        <!-- Enhanced Contact Information -->
        <div data-aos="fade-right" data-aos-duration="1200">
          <div class="relative">
            <!-- Premium Background Frame -->
            <div class="absolute inset-0 bg-gradient-to-br from-gold-500/5 via-transparent to-gold-400/3 rounded-3xl transform rotate-1 scale-105"></div>
            <div class="absolute inset-0 bg-gradient-to-tl from-gold-400/4 via-transparent to-gold-500/4 rounded-3xl transform -rotate-1 scale-105"></div>
            
            <!-- Main Content Container -->
            <div class="relative bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-2xl rounded-3xl p-8 lg:p-12 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group shadow-2xl hover:shadow-gold-500/20">
              
              <!-- Header Section -->
              <div class="text-center mb-12">
                <div class="inline-flex items-center space-x-3 mb-6">
                  <div class="w-12 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full group-hover:w-16 transition-all duration-500"></div>
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-3 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
                    </svg>
                  </div>
                  <div class="w-12 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full group-hover:w-16 transition-all duration-500"></div>
                </div>
                <h3 class="text-2xl lg:text-3xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 transition-all duration-500">
                  {{ t('contact.contactInformation') }}
                </h3>
                <div class="w-20 h-0.5 bg-gold-500 rounded-full mx-auto mt-4 group-hover:w-24 transition-all duration-300"></div>
              </div>
              
              <!-- Contact Details Grid -->
              <div class="space-y-8">
                <!-- Address -->
                <div class="group/item">
                  <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 hover:from-black/50 hover:via-black/30 hover:to-black/50 transition-all duration-500 cursor-pointer">
                    <div class="flex items-start space-x-6">
                      <div class="flex-shrink-0">
                        <div class="text-gold-500 bg-gold-500/20 rounded-full p-4 group-hover/item:bg-gold-500/30 group-hover/item:scale-110 transition-all duration-300 shadow-lg shadow-gold-500/20">
                          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                          </svg>
                        </div>
                      </div>
                      <div class="flex-1">
                        <h4 class="text-xl font-elegant font-semibold text-gold-500 mb-3 group-hover/item:text-gold-400 transition-colors duration-300">
                          {{ t('contact.ourLocation') }}
                        </h4>
                        <div class="space-y-2">
                          <p class="text-base text-white font-modern font-medium group-hover/item:text-gold-200 transition-colors duration-300">
                            {{ t('common.address') }}
                          </p>
                          <p class="text-sm text-gray-300 font-modern group-hover/item:text-gray-200 transition-colors duration-300">
                            {{ t('common.addressDetail') }}
                          </p>
                          <p class="text-xs text-gray-400 font-modern italic group-hover/item:text-gray-300 transition-colors duration-300">
                            {{ t('contact.culturalQuarter') }}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Phone -->
                <div class="group/item">
                  <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 hover:from-black/50 hover:via-black/30 hover:to-black/50 transition-all duration-500 cursor-pointer">
                    <div class="flex items-start space-x-6">
                      <div class="flex-shrink-0">
                        <div class="text-gold-500 bg-gold-500/20 rounded-full p-4 group-hover/item:bg-gold-500/30 group-hover/item:scale-110 transition-all duration-300 shadow-lg shadow-gold-500/20">
                          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                          </svg>
                        </div>
                      </div>
                      <div class="flex-1">
                        <h4 class="text-xl font-elegant font-semibold text-gold-500 mb-3 group-hover/item:text-gold-400 transition-colors duration-300">
                          {{ t('contact.phoneReservations') }}
                        </h4>
                        <div class="space-y-2">
                          <a href="tel:+4921611234567" class="text-base text-white font-modern font-medium hover:text-gold-300 transition-colors duration-300 block">
                            {{ t('common.phone') }}
                          </a>
                          <p class="text-sm text-gray-300 font-modern group-hover/item:text-gray-200 transition-colors duration-300">
                            {{ t('contact.callForReservations') }}
                          </p>
                          <p class="text-xs text-gray-400 font-modern italic group-hover/item:text-gray-300 transition-colors duration-300">
                            {{ t('common.availableDaily') }}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Email -->
                <div class="group/item">
                  <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/10 hover:border-gold-500/30 hover:from-black/50 hover:via-black/30 hover:to-black/50 transition-all duration-500 cursor-pointer">
                    <div class="flex items-start space-x-6">
                      <div class="flex-shrink-0">
                        <div class="text-gold-500 bg-gold-500/20 rounded-full p-4 group-hover/item:bg-gold-500/30 group-hover/item:scale-110 transition-all duration-300 shadow-lg shadow-gold-500/20">
                          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                          </svg>
                        </div>
                      </div>
                      <div class="flex-1">
                        <h4 class="text-xl font-elegant font-semibold text-gold-500 mb-3 group-hover/item:text-gold-400 transition-colors duration-300">
                          {{ t('contact.emailContact') }}
                        </h4>
                        <div class="space-y-2">
                          <a href="mailto:info@alteshaus.de" class="text-base text-white font-modern font-medium hover:text-gold-300 transition-colors duration-300 block">
                            {{ t('common.email') }}
                          </a>
                          <p class="text-sm text-gray-300 font-modern group-hover/item:text-gray-200 transition-colors duration-300">
                            {{ t('contact.loveToHear') }}
                          </p>
                          <p class="text-xs text-gray-400 font-modern italic group-hover/item:text-gray-300 transition-colors duration-300">
                            {{ t('contact.responseTime') }}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Opening Hours -->
                <div class="group/item">
                  <div class="bg-gradient-to-r from-gold-500/10 via-gold-400/5 to-gold-500/10 backdrop-blur-sm rounded-2xl px-8 py-6 border border-gold-500/30 hover:border-gold-500/50 hover:from-gold-500/15 hover:via-gold-400/10 hover:to-gold-500/15 transition-all duration-500 cursor-pointer">
                    <div class="flex items-start space-x-6">
                      <div class="flex-shrink-0">
                        <div class="text-gold-500 bg-gold-500/30 rounded-full p-4 group-hover/item:bg-gold-500/40 group-hover/item:scale-110 transition-all duration-300 shadow-lg shadow-gold-500/30">
                          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                          </svg>
                        </div>
                      </div>
                      <div class="flex-1">
                        <h4 class="text-xl font-elegant font-semibold text-gold-500 mb-3 group-hover/item:text-gold-400 transition-colors duration-300">
                          {{ t('contact.openingHours') }}
                        </h4>
                        <div class="space-y-3">
                          <div class="flex items-center justify-between">
                            <span class="text-base text-white font-modern font-medium group-hover/item:text-gold-200 transition-colors duration-300">
                              {{ t('common.daysOpen') }}
                            </span>
                            <span class="text-lg font-elegant font-bold text-gold-400 group-hover/item:text-gold-300 transition-colors duration-300">
                              {{ t('common.hours') }}
                            </span>
                          </div>
                          <div class="w-full h-0.5 bg-gold-500/30 rounded-full group-hover/item:bg-gold-500/50 transition-all duration-300"></div>
                          <p class="text-sm text-gray-300 font-modern group-hover/item:text-gray-200 transition-colors duration-300">
                            {{ t('contact.kitchenCloses') }}
                          </p>
                          <p class="text-xs text-gold-400 font-modern italic group-hover/item:text-gold-300 transition-colors duration-300">
                            {{ t('contact.reservationsRecommended') }}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Call to Action Button -->
              <div class="mt-12 text-center">
                <button class="bg-gradient-to-r from-gold-500 to-gold-600 hover:from-gold-600 hover:to-gold-700 text-black font-bold px-10 py-4 text-base rounded-full transition-all duration-300 transform hover:scale-105 hover:shadow-xl hover:shadow-gold-500/40 border-2 border-gold-400 hover:border-gold-300 group/btn w-full sm:w-auto">
                  <div class="flex items-center justify-center space-x-3">
                    <svg class="w-5 h-5 group-hover/btn:rotate-12 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                    </svg>
                    <span class="group-hover/btn:tracking-wider transition-all duration-300">{{ t('contact.makeReservation') }}</span>
                  </div>
                </button>
              </div>

              <!-- Bottom Decorative Element -->
              <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-1">
                <div class="w-2 h-2 bg-gold-500/30 rounded-full animate-pulse"></div>
                <div class="w-2 h-2 bg-gold-500/50 rounded-full animate-pulse" style="animation-delay: 0.2s;"></div>
                <div class="w-2 h-2 bg-gold-500/30 rounded-full animate-pulse" style="animation-delay: 0.4s;"></div>
              </div>
            </div>

            <!-- Elegant Corner Accents -->
            <div class="absolute -top-3 -left-3 w-8 h-8 border-l-2 border-t-2 border-gold-500/30 rounded-tl-2xl group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1200"></div>
            <div class="absolute -top-3 -right-3 w-8 h-8 border-r-2 border-t-2 border-gold-500/30 rounded-tr-2xl group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1300"></div>
            <div class="absolute -bottom-3 -left-3 w-8 h-8 border-l-2 border-b-2 border-gold-500/30 rounded-bl-2xl group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1400"></div>
            <div class="absolute -bottom-3 -right-3 w-8 h-8 border-r-2 border-b-2 border-gold-500/30 rounded-br-2xl group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1500"></div>
          </div>
        </div>

        <!-- Enhanced Location Visual -->
        <div data-aos="fade-left" data-aos-duration="1200" data-aos-delay="200">
          <div class="relative h-full">
            <!-- Premium Background Frame -->
            <div class="absolute inset-0 bg-gradient-to-br from-gold-500/5 via-transparent to-gold-400/3 rounded-3xl transform -rotate-1 scale-105"></div>
            <div class="absolute inset-0 bg-gradient-to-tl from-gold-400/4 via-transparent to-gold-500/4 rounded-3xl transform rotate-1 scale-105"></div>
            
            <!-- Main Visual Container -->
            <div class="relative bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-2xl rounded-3xl overflow-hidden border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group shadow-2xl hover:shadow-gold-500/20 h-full flex flex-col">
              
              <!-- Header Section -->
              <div class="p-8 text-center border-b border-gold-500/20">
                <div class="inline-flex items-center space-x-3 mb-4">
                  <div class="w-8 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full group-hover:w-12 transition-all duration-500"></div>
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-2 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                    </svg>
                  </div>
                  <div class="w-8 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full group-hover:w-12 transition-all duration-500"></div>
                </div>
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
                      <span>{{ t('contact.primeLocation') }}</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Location Features Grid -->
              <div class="p-8 space-y-6">
                <div class="grid grid-cols-2 gap-4">
                  <div class="bg-black/30 rounded-xl px-4 py-3 border border-gold-500/20 hover:border-gold-500/40 hover:bg-black/40 transition-all duration-300 group/feature text-center">
                    <div class="text-gold-500 mb-2 group-hover/feature:text-gold-400 transition-colors duration-300">
                      <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/>
                      </svg>
                    </div>
                    <p class="text-xs text-gray-300 font-modern group-hover/feature:text-gray-200 transition-colors duration-300">{{ t('contact.easyAccess') }}</p>
                  </div>
                  
                  <div class="bg-black/30 rounded-xl px-4 py-3 border border-gold-500/20 hover:border-gold-500/40 hover:bg-black/40 transition-all duration-300 group/feature text-center">
                    <div class="text-gold-500 mb-2 group-hover/feature:text-gold-400 transition-colors duration-300">
                      <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
                      </svg>
                    </div>
                    <p class="text-xs text-gray-300 font-modern group-hover/feature:text-gray-200 transition-colors duration-300">{{ t('contact.historicDistrict') }}</p>
                  </div>
                  
                  <div class="bg-black/30 rounded-xl px-4 py-3 border border-gold-500/20 hover:border-gold-500/40 hover:bg-black/40 transition-all duration-300 group/feature text-center">
                    <div class="text-gold-500 mb-2 group-hover/feature:text-gold-400 transition-colors duration-300">
                      <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M10.5 3L12 2l1.5 1H21l-1 6H4l-1-6h7.5z"/>
                      </svg>
                    </div>
                    <p class="text-xs text-gray-300 font-modern group-hover/feature:text-gray-200 transition-colors duration-300">{{ t('contact.culturalQuarter') }}</p>
                  </div>
                  
                  <div class="bg-black/30 rounded-xl px-4 py-3 border border-gold-500/20 hover:border-gold-500/40 hover:bg-black/40 transition-all duration-300 group/feature text-center">
                    <div class="text-gold-500 mb-2 group-hover/feature:text-gold-400 transition-colors duration-300">
                      <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/>
                      </svg>
                    </div>
                    <p class="text-xs text-gray-300 font-modern group-hover/feature:text-gray-200 transition-colors duration-300">{{ t('contact.cityCenter') }}</p>
                  </div>
                </div>

                <!-- Location Details -->
                <div class="text-center bg-black/20 rounded-xl px-6 py-4 border border-gold-500/20">
                  <p class="text-lg font-elegant font-semibold text-white group-hover:text-gold-200 transition-colors duration-300 mb-2">
                    {{ t('common.address').split(',')[0] }}
                  </p>
                  <p class="text-sm text-gray-300 font-modern group-hover:text-white transition-colors duration-300">
                    {{ t('common.addressDetail') }}
                  </p>
                  <div class="flex items-center justify-center space-x-2 mt-3">
                    <div class="w-2 h-2 bg-gold-500 rounded-full animate-pulse"></div>
                    <p class="text-xs text-gold-400 font-modern font-semibold">
                      {{ t('contact.openDaily') }}
                    </p>
                  </div>
                </div>
              </div>

              <!-- Bottom Decorative Element -->
              <div class="absolute bottom-2 left-1/2 transform -translate-x-1/2 flex space-x-1">
                <div class="w-1.5 h-1.5 bg-gold-500/40 rounded-full animate-pulse"></div>
                <div class="w-1.5 h-1.5 bg-gold-500/60 rounded-full animate-pulse" style="animation-delay: 0.3s;"></div>
                <div class="w-1.5 h-1.5 bg-gold-500/40 rounded-full animate-pulse" style="animation-delay: 0.6s;"></div>
              </div>
            </div>

            <!-- Elegant Corner Accents -->
            <div class="absolute -top-1 -left-1 w-6 h-6 border-l-2 border-t-2 border-gold-500/30 rounded-tl-lg group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1600"></div>
            <div class="absolute -top-1 -right-1 w-6 h-6 border-r-2 border-t-2 border-gold-500/30 rounded-tr-lg group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1700"></div>
            <div class="absolute -bottom-1 -left-1 w-6 h-6 border-l-2 border-b-2 border-gold-500/30 rounded-bl-lg group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1800"></div>
            <div class="absolute -bottom-1 -right-1 w-6 h-6 border-r-2 border-b-2 border-gold-500/30 rounded-tr-lg group-hover:border-gold-500/50 transition-all duration-500" data-aos="fade-in" data-aos-delay="1900"></div>
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