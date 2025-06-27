<script setup lang="ts">
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const isOpen = ref(false)

const languages = [
  { code: 'en', name: 'English', flag: '🇺🇸' },
  { code: 'de', name: 'Deutsch', flag: '🇩🇪' },
  { code: 'mk', name: 'Македонски', flag: '🇲🇰' }
]

const currentLanguage = computed(() => 
  languages.find(lang => lang.code === locale.value) || languages[0]
)

const switchLanguage = (langCode: string) => {
  locale.value = langCode
  localStorage.setItem('locale', langCode)
  isOpen.value = false
}

const toggleDropdown = () => {
  isOpen.value = !isOpen.value
}

// Close dropdown when clicking outside
const closeDropdown = () => {
  isOpen.value = false
}
</script>

<template>
  <div class="relative" @click.stop>
    <!-- Language Switcher Button -->
    <button
      @click="toggleDropdown"
      class="relative group bg-gradient-to-br from-black/40 via-black/30 to-black/40 backdrop-blur-xl rounded-full px-4 py-2 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-300 hover:bg-black/60 shadow-lg hover:shadow-xl hover:shadow-gold-500/20"
    >
      <div class="flex items-center space-x-2">
        <!-- Flag -->
        <span class="text-lg group-hover:scale-110 transition-transform duration-300">
          {{ currentLanguage.flag }}
        </span>
        
        <!-- Language Code -->
        <span class="text-sm font-modern font-medium text-white group-hover:text-gold-400 transition-colors duration-300 uppercase">
          {{ currentLanguage.code }}
        </span>
        
        <!-- Dropdown Arrow -->
        <svg 
          class="w-3 h-3 text-gold-500 group-hover:text-gold-400 transition-all duration-300"
          :class="isOpen ? 'rotate-180' : ''"
          fill="none" 
          stroke="currentColor" 
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
        </svg>
      </div>
    </button>

    <!-- Dropdown Menu -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      leave-active-class="transition-all duration-200 ease-in"
      enter-from-class="transform scale-95 opacity-0 translate-y-2"
      enter-to-class="transform scale-100 opacity-100 translate-y-0"
      leave-from-class="transform scale-100 opacity-100 translate-y-0"
      leave-to-class="transform scale-95 opacity-0 translate-y-2"
    >
      <div 
        v-if="isOpen"
        class="absolute top-full right-0 mt-2 w-48 bg-gradient-to-br from-black/95 via-black/90 to-black/95 backdrop-blur-2xl rounded-2xl border border-gold-500/30 shadow-2xl shadow-black/50 overflow-hidden z-50"
      >
        <!-- Dropdown Header -->
        <div class="px-4 py-3 border-b border-gold-500/20">
          <p class="text-xs text-gray-400 font-modern uppercase tracking-wider">
            Select Language
          </p>
        </div>
        
        <!-- Language Options -->
        <div class="py-2">
          <button
            v-for="language in languages"
            :key="language.code"
            @click="switchLanguage(language.code)"
            :class="[
              'w-full flex items-center space-x-3 px-4 py-3 text-left transition-all duration-200 group',
              locale === language.code 
                ? 'bg-gradient-to-r from-gold-500/20 via-gold-400/10 to-gold-500/20 text-gold-400' 
                : 'text-white hover:bg-black/50 hover:text-gold-400'
            ]"
          >
            <!-- Flag -->
            <span class="text-lg group-hover:scale-110 transition-transform duration-200">
              {{ language.flag }}
            </span>
            
            <!-- Language Info -->
            <div class="flex-1">
              <div class="text-sm font-medium font-modern">
                {{ language.name }}
              </div>
              <div class="text-xs text-gray-400 uppercase font-modern">
                {{ language.code }}
              </div>
            </div>
            
            <!-- Active Indicator -->
            <div v-if="locale === language.code" class="w-2 h-2 bg-gold-500 rounded-full animate-pulse"></div>
          </button>
        </div>
      </div>
    </Transition>

    <!-- Backdrop to close dropdown -->
    <div 
      v-if="isOpen"
      @click="closeDropdown"
      class="fixed inset-0 z-40"
    ></div>
  </div>
</template>

<style scoped>
/* Smooth transitions for all elements */
* {
  transition-property: transform, opacity, color, background-color, border-color, box-shadow, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}
</style>