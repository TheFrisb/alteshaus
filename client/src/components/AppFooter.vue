<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
  <footer class="bg-gradient-to-b from-gray-900 to-black border-t border-gold-500/20 relative overflow-hidden">
    <!-- Decorative background elements -->
    <div class="absolute top-0 left-0 w-96 h-48 bg-gold-500/3 rounded-full -translate-x-48 -translate-y-24 rotate-12"></div>
    <div class="absolute bottom-0 right-0 w-64 h-32 bg-gold-500/5 rounded-full translate-x-32 translate-y-16 -rotate-12"></div>
    <div class="absolute top-1/2 left-1/3 w-40 h-20 bg-gold-500/2 rounded-full -translate-x-20 -translate-y-10 rotate-45"></div>
    
    <div class="max-w-7xl mx-auto relative z-10">
      <!-- Main Footer Content -->
      <div class="px-6 lg:px-8 py-20">
        <!-- Top Section - Restaurant Branding -->
        <div class="text-center mb-20" data-aos="fade-up" data-aos-duration="1000">
          <div class="inline-block bg-black/20 backdrop-blur-sm rounded-full px-12 py-8 hover:bg-black/30 transition-all duration-500 group cursor-pointer">
            <h2 class="text-4xl md:text-5xl font-elegant font-bold text-gold-500 mb-3 group-hover:text-gold-400 transition-all duration-300">
              <span class="group-hover:tracking-wider transition-all duration-300">Altes</span><span class="group-hover:text-gold-300 transition-colors duration-300">Haus</span>
            </h2>
            <div class="w-20 h-0.5 bg-gold-500 rounded-full mx-auto mb-4 group-hover:w-24 transition-all duration-300"></div>
            <p class="text-sm text-gray-300 font-modern italic group-hover:text-gold-200 transition-colors duration-300">
              {{ t('footer.tagline') }}
            </p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
          <!-- Restaurant Info -->
          <div class="text-center lg:text-left" data-aos="fade-up" data-aos-delay="100">
            <div class="bg-black/10 backdrop-blur-sm rounded-full px-6 py-6 hover:bg-black/20 transition-all duration-300 group">
              <h3 class="text-xl font-elegant font-bold text-gold-500 mb-6 group-hover:text-gold-400 transition-colors duration-300">
                {{ t('footer.aboutUs') }}
              </h3>
              <p class="text-sm text-gray-300 mb-6 font-modern leading-relaxed group-hover:text-gray-200 transition-colors duration-300">
                {{ t('footer.aboutUsText') }}
              </p>
              <div class="flex justify-center lg:justify-start space-x-4">
                <a href="#" class="text-gold-500 hover:text-gold-400 transition-all duration-300 bg-gold-500/10 rounded-full p-3 hover:bg-gold-500/20 hover:scale-110 hover:rotate-12 group">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
                  </svg>
                </a>
                <a href="#" class="text-gold-500 hover:text-gold-400 transition-all duration-300 bg-gold-500/10 rounded-full p-3 hover:bg-gold-500/20 hover:scale-110 hover:rotate-12 group">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M22.46 6c-.77.35-1.6.58-2.46.69.88-.53 1.56-1.37 1.88-2.38-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29 0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15 0 1.49.75 2.81 1.91 3.56-.71 0-1.37-.2-1.95-.5v.03c0 2.08 1.48 3.82 3.44 4.21a4.22 4.22 0 0 1-1.93.07 4.28 4.28 0 0 0 4 2.98 8.521 8.521 0 0 1-5.33 1.84c-.34 0-.68-.02-1.02-.06C3.44 20.29 5.7 21 8.12 21 16 21 20.33 14.46 20.33 8.79c0-.19 0-.37-.01-.56.84-.6 1.56-1.36 2.14-2.23z"/>
                  </svg>
                </a>
                <a href="#" class="text-gold-500 hover:text-gold-400 transition-all duration-300 bg-gold-500/10 rounded-full p-3 hover:bg-gold-500/20 hover:scale-110 hover:rotate-12 group">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.174-.105-.949-.199-2.403.041-3.439.219-.937 1.406-5.957 1.406-5.957s-.359-.72-.359-1.781c0-1.663.967-2.911 2.168-2.911 1.024 0 1.518.769 1.518 1.688 0 1.029-.653 2.567-.992 3.992-.285 1.193.6 2.165 1.775 2.165 2.128 0 3.768-2.245 3.768-5.487 0-2.861-2.063-4.869-5.008-4.869-3.41 0-5.409 2.562-5.409 5.199 0 1.033.394 2.143.889 2.74.099.12.112.225.085.345-.09.375-.293 1.199-.334 1.363-.053.225-.172.271-.402.165-1.495-.69-2.433-2.878-2.433-4.646 0-3.776 2.748-7.252 7.92-7.252 4.158 0 7.392 2.967 7.392 6.923 0 4.135-2.607 7.462-6.233 7.462-1.214 0-2.357-.629-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24.009 12.017 24.009c6.624 0 11.99-5.367 11.99-11.988C24.007 5.367 18.641.001 12.017.001z"/>
                  </svg>
                </a>
              </div>
            </div>
          </div>

          <!-- Contact Info -->
          <div class="text-center" data-aos="fade-up" data-aos-delay="200">
            <div class="bg-black/10 backdrop-blur-sm rounded-full px-6 py-6 hover:bg-black/20 transition-all duration-300 group">
              <h4 class="text-xl font-elegant font-bold text-gold-500 mb-6 group-hover:text-gold-400 transition-colors duration-300">
                {{ t('footer.contact') }}
              </h4>
              <div class="space-y-4 text-gray-300 font-modern">
                <div class="flex items-center justify-center space-x-3 bg-black/20 rounded-full px-4 py-3 hover:bg-black/30 transition-all duration-300 cursor-pointer hover:scale-105">
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                    </svg>
                  </div>
                  <div class="text-left">
                    <p class="text-sm font-medium">{{ t('common.address').split(',')[0] }}</p>
                    <p class="text-xs text-gray-400">{{ t('common.addressDetail') }}</p>
                  </div>
                </div>

                <div class="flex items-center justify-center space-x-3 bg-black/20 rounded-full px-4 py-3 hover:bg-black/30 transition-all duration-300 cursor-pointer hover:scale-105">
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                    </svg>
                  </div>
                  <div class="text-left">
                    <p class="text-sm font-medium">{{ t('common.phone') }}</p>
                    <p class="text-xs text-gray-400">{{ t('contact.callForReservations') }}</p>
                  </div>
                </div>

                <div class="flex items-center justify-center space-x-3 bg-black/20 rounded-full px-4 py-3 hover:bg-black/30 transition-all duration-300 cursor-pointer hover:scale-105">
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                    </svg>
                  </div>
                  <div class="text-left">
                    <p class="text-sm font-medium">{{ t('common.email') }}</p>
                    <p class="text-xs text-gray-400">{{ t('contact.loveToHear') }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Opening Hours -->
          <div class="text-center" data-aos="fade-up" data-aos-delay="300">
            <div class="bg-black/10 backdrop-blur-sm rounded-full px-6 py-6 hover:bg-black/20 transition-all duration-300 group">
              <h4 class="text-xl font-elegant font-bold text-gold-500 mb-6 group-hover:text-gold-400 transition-colors duration-300">
                {{ t('contact.openingHours') }}
              </h4>
              <div class="space-y-4 text-gray-300 font-modern">
                <div class="bg-black/20 rounded-full px-4 py-3 hover:bg-black/30 transition-all duration-300 cursor-pointer hover:scale-105">
                  <div class="flex items-center justify-center space-x-2 mb-2">
                    <div class="text-gold-500 bg-gold-500/20 rounded-full p-1.5">
                      <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                      </svg>
                    </div>
                    <p class="text-sm font-medium">{{ t('common.daysOpen') }}</p>
                  </div>
                  <p class="text-lg font-elegant font-bold text-gold-400">{{ t('common.hours') }}</p>
                  <p class="text-xs text-gray-400 mt-1">{{ t('contact.kitchenCloses') }}</p>
                </div>

                <div class="bg-black/20 rounded-full px-4 py-3 hover:bg-black/30 transition-all duration-300 cursor-pointer hover:scale-105">
                  <p class="text-xs text-gray-400 mb-1">{{ t('contact.reservationsRecommended').split(',')[0] }}</p>
                  <p class="text-sm font-medium text-gold-400">{{ t('contact.reservationsRecommended').split(',')[1] }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Newsletter -->
          <div class="text-center" data-aos="fade-up" data-aos-delay="400">
            <div class="bg-black/10 backdrop-blur-sm rounded-full px-6 py-6 hover:bg-black/20 transition-all duration-300 group">
              <h4 class="text-xl font-elegant font-bold text-gold-500 mb-6 group-hover:text-gold-400 transition-colors duration-300">
                {{ t('footer.stayConnected') }}
              </h4>
              <p class="text-sm text-gray-300 mb-6 font-modern leading-relaxed group-hover:text-gray-200 transition-colors duration-300">
                {{ t('footer.stayConnectedText') }}
              </p>
              <div class="space-y-3">
                <input 
                  type="email" 
                  :placeholder="t('footer.enterEmail')" 
                  class="w-full px-4 py-3 bg-black/30 border border-gold-500/30 rounded-full focus:outline-none focus:border-gold-500 text-white font-modern text-sm hover:bg-black/40 transition-all duration-300 focus:scale-105 placeholder-gray-400"
                >
                <button class="w-full bg-gold-500 hover:bg-gold-600 text-black font-medium py-3 px-6 text-sm rounded-full transition-all duration-300 transform hover:scale-105 hover:shadow-lg hover:shadow-gold-500/30 group">
                  <span class="group-hover:tracking-wider transition-all duration-300">{{ t('footer.subscribeNewsletter') }}</span>
                </button>
              </div>
              <p class="text-xs text-gray-500 mt-3 font-modern">
                {{ t('footer.privacyRespect') }}
              </p>
            </div>
          </div>
        </div>

        <!-- Quick Links Section -->
        <div class="text-center mb-16" data-aos="fade-up" data-aos-delay="500">
          <div class="bg-black/10 backdrop-blur-sm rounded-full px-8 py-6 hover:bg-black/20 transition-all duration-300 inline-block">
            <h4 class="text-lg font-elegant font-bold text-gold-500 mb-4">
              {{ t('footer.quickLinks') }}
            </h4>
            <div class="flex flex-wrap justify-center gap-4">
              <router-link 
                to="/" 
                class="text-sm text-gray-300 hover:text-gold-400 transition-all duration-300 font-modern bg-black/20 rounded-full px-4 py-2 hover:bg-black/30 hover:scale-105"
              >
                {{ t('nav.home') }}
              </router-link>
              <router-link 
                to="/about" 
                class="text-sm text-gray-300 hover:text-gold-400 transition-all duration-300 font-modern bg-black/20 rounded-full px-4 py-2 hover:bg-black/30 hover:scale-105"
              >
                {{ t('nav.about') }}
              </router-link>
              <router-link 
                to="/menu" 
                class="text-sm text-gray-300 hover:text-gold-400 transition-all duration-300 font-modern bg-black/20 rounded-full px-4 py-2 hover:bg-black/30 hover:scale-105"
              >
                {{ t('nav.menu') }}
              </router-link>
              <a 
                href="#" 
                class="text-sm text-gray-300 hover:text-gold-400 transition-all duration-300 font-modern bg-black/20 rounded-full px-4 py-2 hover:bg-black/30 hover:scale-105"
              >
                {{ t('nav.reservations') }}
              </a>
              <a 
                href="#" 
                class="text-sm text-gray-300 hover:text-gold-400 transition-all duration-300 font-modern bg-black/20 rounded-full px-4 py-2 hover:bg-black/30 hover:scale-105"
              >
                {{ t('footer.events') }}
              </a>
              <a 
                href="#" 
                class="text-sm text-gray-300 hover:text-gold-400 transition-all duration-300 font-modern bg-black/20 rounded-full px-4 py-2 hover:bg-black/30 hover:scale-105"
              >
                {{ t('footer.contact') }}
              </a>
            </div>
          </div>
        </div>

        <!-- Bottom Section -->
        <div class="border-t border-gold-500/20 pt-12">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-center">
            <!-- Copyright -->
            <div class="text-center md:text-left" data-aos="fade-up" data-aos-delay="600">
              <div class="bg-black/10 backdrop-blur-sm rounded-full px-6 py-4 hover:bg-black/20 transition-all duration-300 group cursor-pointer inline-block">
                <p class="text-sm text-gray-400 font-modern group-hover:text-gold-500 transition-colors duration-300">
                  &copy; 2024 AltesHaus Restaurant
                </p>
                <p class="text-xs text-gray-500 font-modern group-hover:text-gray-400 transition-colors duration-300">
                  {{ t('footer.allRightsReserved') }}
                </p>
              </div>
            </div>

            <!-- Center Logo -->
            <div class="text-center" data-aos="fade-up" data-aos-delay="700">
              <div class="bg-black/10 backdrop-blur-sm rounded-full px-6 py-4 hover:bg-black/20 transition-all duration-300 group cursor-pointer inline-block">
                <div class="text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                  <svg class="w-8 h-8 mx-auto" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                  </svg>
                </div>
                <p class="text-xs text-gray-400 font-modern mt-1 group-hover:text-gray-300 transition-colors duration-300">
                  {{ t('footer.qualityAssured') }}
                </p>
              </div>
            </div>

            <!-- Legal Links -->
            <div class="text-center md:text-right" data-aos="fade-up" data-aos-delay="800">
              <div class="bg-black/10 backdrop-blur-sm rounded-full px-6 py-4 hover:bg-black/20 transition-all duration-300 group inline-block">
                <div class="flex flex-wrap justify-center md:justify-end gap-4">
                  <a href="#" class="text-xs text-gray-400 hover:text-gold-400 transition-colors duration-300 font-modern group-hover:text-gray-300">
                    {{ t('footer.privacyPolicy') }}
                  </a>
                  <span class="text-gray-600">•</span>
                  <a href="#" class="text-xs text-gray-400 hover:text-gold-400 transition-colors duration-300 font-modern group-hover:text-gray-300">
                    {{ t('footer.termsOfService') }}
                  </a>
                  <span class="text-gray-600">•</span>
                  <a href="#" class="text-xs text-gray-400 hover:text-gold-400 transition-colors duration-300 font-modern group-hover:text-gray-300">
                    {{ t('footer.impressum') }}
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>