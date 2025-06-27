<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import LanguageSwitcher from './LanguageSwitcher.vue'

const { t } = useI18n()
const router = useRouter()
const isScrolled = ref(false)
const isMenuOpen = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const navigateTo = (path: string) => {
  router.push(path)
  isMenuOpen.value = false
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <header 
    class="fixed top-0 left-0 right-0 z-50 transition-all duration-500"
    :class="isScrolled ? 'bg-black/95 backdrop-blur-xl shadow-2xl shadow-black/50 border-b border-gold-500/20' : 'bg-gradient-to-b from-black/80 via-black/40 to-transparent backdrop-blur-md'"
  >
    <!-- Elegant Top Border -->
    <div class="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-gold-500/60 to-transparent"></div>
    
    <!-- Premium Background Pattern -->
    <div class="absolute inset-0 opacity-5">
      <div class="w-full h-full" style="background-image: radial-gradient(circle at 2px 2px, rgba(212, 175, 55, 0.3) 1px, transparent 0); background-size: 40px 40px;"></div>
    </div>
    
    <div class="max-w-7xl mx-auto relative z-10">
      <div class="flex justify-between items-center h-20 px-4 sm:px-6 lg:px-8">
        
        <!-- Enhanced Logo Section -->
        <div class="flex-shrink-0 cursor-pointer group" @click="navigateTo('/')">
          <div class="relative">
            <!-- Main Logo Container -->
            <div class="relative bg-gradient-to-br from-black/50 via-black/30 to-black/50 backdrop-blur-xl rounded-full px-6 py-3 border border-gold-500/30 hover:border-gold-500/50 transition-all duration-300 hover:bg-black/60 shadow-lg hover:shadow-xl hover:shadow-gold-500/20">
              
              <!-- Logo Content -->
              <div class="text-center">
                <h1 class="text-lg sm:text-xl lg:text-2xl font-elegant font-bold mb-1">
                  <span class="text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 hover:from-gold-300 hover:via-gold-400 hover:to-gold-500 transition-all duration-300">Altes</span><span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-gray-100 to-white hover:from-gold-200 hover:via-gold-100 hover:to-gold-200 transition-all duration-300">Haus</span>
                </h1>
              </div>
            </div>
          </div>
        </div>

        <!-- Enhanced Desktop Navigation -->
        <nav class="hidden lg:flex items-center space-x-8">
          <router-link 
            v-for="(link, index) in [
              { to: '/', label: t('nav.home'), icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
              { to: '/about', label: t('nav.about'), icon: 'M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z' },
              { to: '/menu', label: t('nav.menu'), icon: 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253' }
            ]"
            :key="link.to"
            :to="link.to" 
            class="relative group/nav"
          >
            <!-- Navigation Item Container -->
            <div :class="[
              'relative backdrop-blur-sm rounded-full px-5 py-2.5 border transition-all duration-300',
              $route.path === link.to 
                ? 'bg-gradient-to-br from-gold-500/20 via-gold-400/10 to-gold-500/20 border-gold-500/40' 
                : 'bg-gradient-to-br from-black/30 via-black/20 to-black/30 border-transparent hover:border-gold-500/30 hover:bg-gradient-to-br hover:from-gold-500/10 hover:via-black/30 hover:to-gold-500/10'
            ]">
              
              <!-- Link Content -->
              <div class="relative flex items-center space-x-2">
                <!-- Icon -->
                <div :class="[
                  'transition-colors duration-300',
                  $route.path === link.to 
                    ? 'text-gold-400' 
                    : 'text-gold-500/60 group-hover/nav:text-gold-400'
                ]">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="link.icon"/>
                  </svg>
                </div>
                
                <!-- Text -->
                <span :class="[
                  'transition-all duration-300 font-medium text-sm font-modern',
                  $route.path === link.to 
                    ? 'text-gold-400' 
                    : 'text-white group-hover/nav:text-gold-400'
                ]">
                  {{ link.label }}
                </span>
              </div>
            </div>
          </router-link>
        </nav>

        <!-- Enhanced Contact Info & Language Switcher (Desktop) -->
        <div class="hidden xl:flex items-center space-x-4">
          <!-- Language Switcher -->
          <LanguageSwitcher />
          
          <!-- Phone Contact -->
          <div class="relative group/contact">
            <!-- Contact Container -->
            <div class="relative bg-gradient-to-br from-black/40 via-black/30 to-black/40 backdrop-blur-xl rounded-full px-5 py-2.5 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-300 cursor-pointer hover:bg-black/60 shadow-lg hover:shadow-xl hover:shadow-gold-500/20">
              <div class="flex items-center space-x-3">
                <!-- Phone Icon -->
                <div class="text-gold-500 bg-gold-500/20 rounded-full p-2 group-hover/contact:bg-gold-500/30 transition-all duration-300">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                  </svg>
                </div>
                
                <!-- Contact Info -->
                <div class="text-left">
                  <p class="text-sm font-medium text-white group-hover/contact:text-gold-400 transition-colors duration-300 font-modern">
                    {{ t('common.phone') }}
                  </p>
                  <p class="text-xs text-gray-400 font-modern group-hover/contact:text-gold-300 transition-colors duration-300">
                    {{ t('nav.reservations') }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Mobile Actions Container -->
        <div class="lg:hidden flex items-center space-x-3">
          <!-- Mobile Language Switcher -->
          <LanguageSwitcher />
          
          <!-- Enhanced Mobile Menu Button -->
          <button 
            class="relative group/menu"
            @click="toggleMenu"
          >
            <!-- Button Container -->
            <div class="relative bg-gradient-to-br from-black/40 via-black/30 to-black/40 backdrop-blur-xl rounded-full p-3 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-300 hover:bg-black/60 shadow-lg hover:shadow-xl hover:shadow-gold-500/20">
              <!-- Hamburger Icon -->
              <div class="relative w-6 h-6">
                <span 
                  class="absolute left-0 w-full h-0.5 bg-gold-500 rounded-full transition-all duration-300 group-hover/menu:bg-gold-400"
                  :class="isMenuOpen ? 'rotate-45 top-3' : 'top-1'"
                ></span>
                <span 
                  class="absolute top-3 left-0 w-full h-0.5 bg-gold-500 rounded-full transition-all duration-300 group-hover/menu:bg-gold-400"
                  :class="isMenuOpen ? 'opacity-0' : ''"
                ></span>
                <span 
                  class="absolute left-0 w-full h-0.5 bg-gold-500 rounded-full transition-all duration-300 group-hover/menu:bg-gold-400"
                  :class="isMenuOpen ? '-rotate-45 top-3' : 'top-5'"
                ></span>
              </div>
            </div>
          </button>
        </div>
      </div>

      <!-- Enhanced Mobile Menu -->
      <div 
        class="lg:hidden transition-all duration-500 overflow-hidden"
        :class="isMenuOpen ? 'max-h-[500px] opacity-100 pb-6' : 'max-h-0 opacity-0'"
      >
        <!-- Mobile Menu Container -->
        <div class="relative mx-4 mt-4 overflow-hidden rounded-2xl">
          <!-- Background Effects -->
          <div class="absolute inset-0 bg-gradient-to-br from-black/95 via-black/85 to-black/95 backdrop-blur-2xl"></div>
          <div class="absolute inset-0 bg-gradient-to-r from-gold-500/5 via-transparent to-gold-500/5"></div>
          
          <!-- Border -->
          <div class="absolute inset-0 rounded-2xl border border-gold-500/30"></div>
          
          <!-- Content -->
          <div class="relative z-10 p-6">
            <!-- Mobile Navigation Links -->
            <nav class="space-y-2 mb-6">
              <router-link 
                v-for="(link, index) in [
                  { to: '/', label: t('nav.home'), icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
                  { to: '/about', label: t('nav.about'), icon: 'M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z' },
                  { to: '/menu', label: t('nav.menu'), icon: 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253' }
                ]"
                :key="link.to"
                :to="link.to" 
                class="block group/mobile"
                @click="isMenuOpen = false"
              >
                <!-- Mobile Link Container -->
                <div :class="[
                  'rounded-xl px-4 py-3 transition-all duration-300 border',
                  $route.path === link.to 
                    ? 'bg-gradient-to-r from-gold-500/20 via-gold-400/10 to-gold-500/20 border-gold-500/40' 
                    : 'bg-gradient-to-r from-black/30 via-black/20 to-black/30 border-transparent hover:bg-black/50 hover:border-gold-500/30'
                ]">
                  <div class="flex items-center space-x-3">
                    <!-- Icon -->
                    <div :class="[
                      'rounded-full p-2 transition-all duration-300',
                      $route.path === link.to 
                        ? 'text-gold-400 bg-gold-500/30' 
                        : 'text-gold-500 bg-gold-500/20 group-hover/mobile:bg-gold-500/30'
                    ]">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="link.icon"/>
                      </svg>
                    </div>
                    
                    <!-- Text -->
                    <span :class="[
                      'transition-all duration-300 font-medium text-base font-modern flex-1',
                      $route.path === link.to 
                        ? 'text-gold-400' 
                        : 'text-white group-hover/mobile:text-gold-400'
                    ]">
                      {{ link.label }}
                    </span>
                    
                    <!-- Arrow -->
                    <div :class="[
                      'transition-all duration-300',
                      $route.path === link.to 
                        ? 'text-gold-400' 
                        : 'text-gold-500/50 group-hover/mobile:text-gold-400'
                    ]">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                      </svg>
                    </div>
                  </div>
                </div>
              </router-link>
            </nav>

            <!-- Mobile Contact Section -->
            <div class="border-t border-gold-500/20 pt-6">
              <!-- Contact Info -->
              <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 rounded-xl p-4 border border-gold-500/20 hover:border-gold-500/40 hover:bg-black/60 transition-all duration-300 group/mobile-contact mb-3">
                <div class="flex items-center space-x-3">
                  <!-- Phone Icon -->
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-2 group-hover/mobile-contact:bg-gold-500/30 transition-all duration-300">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                    </svg>
                  </div>
                  
                  <!-- Contact Details -->
                  <div class="flex-1">
                    <p class="text-sm font-medium text-white group-hover/mobile-contact:text-gold-400 transition-colors duration-300 font-modern">
                      {{ t('common.phone') }}
                    </p>
                    <p class="text-xs text-gray-400 font-modern group-hover/mobile-contact:text-gold-300 transition-colors duration-300">
                      {{ t('contact.callForReservations') }}
                    </p>
                  </div>
                </div>
              </div>

              <!-- Hours Info -->
              <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 rounded-xl p-4 border border-gold-500/20 hover:border-gold-500/40 hover:bg-black/60 transition-all duration-300 group/mobile-hours">
                <div class="flex items-center space-x-3">
                  <!-- Clock Icon -->
                  <div class="text-gold-500 bg-gold-500/20 rounded-full p-2 group-hover/mobile-hours:bg-gold-500/30 transition-all duration-300">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                  </div>
                  
                  <!-- Hours Details -->
                  <div class="flex-1">
                    <p class="text-sm font-medium text-white group-hover/mobile-hours:text-gold-400 transition-colors duration-300 font-modern">
                      {{ t('common.daysOpen') }}: {{ t('common.hours') }}
                    </p>
                    <p class="text-xs text-gray-400 font-modern group-hover/mobile-hours:text-gold-300 transition-colors duration-300">
                      {{ t('contact.kitchenCloses') }}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Elegant Bottom Border -->
    <div class="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-gold-500/40 to-transparent"></div>
  </header>
</template>

<style scoped>
/* Smooth transitions for all elements */
* {
  transition-property: transform, opacity, color, background-color, border-color, box-shadow, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

/* Custom scrollbar for mobile menu */
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
</style>