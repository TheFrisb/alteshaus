<script setup lang="ts">
interface TeamMember {
  id: number
  name: string
  position: string
  image: string
  description: string
  specialties: string[]
  experience: string
  quote?: string
}

defineProps<{
  member: TeamMember
  index: number
}>()
</script>

<template>
  <div 
    class="group" 
    :data-aos="index % 2 === 0 ? 'fade-right' : 'fade-left'" 
    :data-aos-delay="index * 150"
    :data-aos-duration="1000"
  >
    <div class="relative">
      <!-- Premium Background Frame -->
      <div class="absolute inset-0 bg-gradient-to-br from-gold-500/8 via-transparent to-gold-400/5 rounded-3xl transform rotate-1 scale-105"></div>
      <div class="absolute inset-0 bg-gradient-to-tl from-gold-400/6 via-transparent to-gold-500/6 rounded-3xl transform -rotate-1 scale-105"></div>
      
      <!-- Main Card Container -->
      <div class="relative bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-2xl rounded-3xl overflow-hidden border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group cursor-pointer shadow-2xl hover:shadow-gold-500/20 transform hover:-translate-y-4 hover:scale-[1.02]">
        
        <!-- Premium Corner Accents -->
        <div class="absolute top-0 right-0 w-20 h-20 bg-gradient-to-bl from-gold-500/15 to-transparent rounded-bl-full"></div>
        <div class="absolute bottom-0 left-0 w-16 h-16 bg-gradient-to-tr from-gold-500/10 to-transparent rounded-tr-full"></div>
        
        <!-- Image Section with Enhanced Frame -->
        <div class="relative p-8 pb-4">
          <!-- Outer Glow Effect -->
          <div class="absolute top-8 left-8 right-8 bottom-4 bg-gradient-to-r from-gold-500/20 via-gold-400/10 to-gold-500/20 rounded-full blur-xl group-hover:blur-2xl transition-all duration-700"></div>
          
          <!-- Image Container -->
          <div class="relative w-48 h-48 sm:w-56 sm:h-56 lg:w-48 lg:h-48 xl:w-56 xl:h-56 mx-auto">
            <!-- Premium Border Frame -->
            <div class="absolute inset-0 rounded-full bg-gradient-to-br from-gold-500/40 via-gold-400/25 to-gold-500/40 p-1 group-hover:from-gold-500/60 group-hover:via-gold-400/35 group-hover:to-gold-500/60 transition-all duration-500">
              <div class="w-full h-full rounded-full bg-gradient-to-br from-black/80 to-black/60 p-1">
                <div class="relative w-full h-full rounded-full overflow-hidden bg-gradient-to-br from-gold-500/10 to-transparent">
                  <img 
                    :src="member.image" 
                    :alt="member.name" 
                    class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700 filter group-hover:brightness-110"
                  >
                  <!-- Subtle Overlay -->
                  <div class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent group-hover:from-black/20 transition-all duration-500"></div>
                </div>
              </div>
            </div>
            
            <!-- Experience Badge -->
            <div class="absolute -top-2 -right-2 bg-gradient-to-r from-gold-500 to-gold-600 rounded-full p-3 shadow-xl shadow-gold-500/50 group-hover:scale-110 group-hover:shadow-gold-500/70 transition-all duration-300 border-2 border-gold-300/50">
              <div class="text-black font-elegant font-bold text-xs">
                {{ member.experience }}
              </div>
            </div>
          </div>
        </div>

        <!-- Content Section -->
        <div class="px-8 pb-8 space-y-6">
          <!-- Name and Position -->
          <div class="text-center">
            <div class="bg-black/30 backdrop-blur-sm rounded-2xl px-6 py-4 border border-gold-500/20 group-hover:border-gold-500/40 group-hover:bg-black/40 transition-all duration-300">
              <h3 class="text-xl sm:text-2xl font-elegant font-bold text-gold-500 mb-2 group-hover:text-gold-400 transition-colors duration-300">
                {{ member.name }}
              </h3>
              <div class="w-16 h-0.5 bg-gold-500 rounded-full mx-auto mb-3 group-hover:w-20 transition-all duration-300"></div>
              <p class="text-sm text-gray-300 font-modern group-hover:text-gray-200 transition-colors duration-300">
                {{ member.position }}
              </p>
            </div>
          </div>

          <!-- Description -->
          <div class="bg-black/20 backdrop-blur-sm rounded-2xl px-6 py-4 border border-gold-500/10 hover:border-gold-500/30 hover:bg-black/30 transition-all duration-300">
            <p class="text-sm text-gray-300 leading-relaxed font-modern hover:text-gray-100 transition-colors duration-300 text-center">
              {{ member.description }}
            </p>
          </div>

          <!-- Specialties -->
          <div class="space-y-3">
            <div class="flex items-center justify-center space-x-2">
              <div class="w-8 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full"></div>
              <h4 class="text-sm font-elegant font-semibold text-gold-500 tracking-wider uppercase">
                Specialties
              </h4>
              <div class="w-8 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full"></div>
            </div>
            <div class="flex flex-wrap justify-center gap-2">
              <span
                v-for="specialty in member.specialties"
                :key="specialty"
                class="bg-black/40 text-gray-300 px-3 py-1.5 rounded-full text-xs font-modern hover:bg-gold-500/20 hover:text-gold-300 transition-all duration-300 cursor-pointer hover:scale-105 border border-gray-600/30 hover:border-gold-500/40 backdrop-blur-sm"
              >
                {{ specialty }}
              </span>
            </div>
          </div>

          <!-- Quote (if available) -->
          <div v-if="member.quote" class="bg-gradient-to-r from-gold-500/10 via-gold-400/5 to-gold-500/10 rounded-2xl px-6 py-4 border border-gold-500/20 hover:border-gold-500/40 hover:from-gold-500/15 hover:via-gold-400/10 hover:to-gold-500/15 transition-all duration-300">
            <div class="text-gold-500 mb-2 text-center">
              <svg class="w-5 h-5 mx-auto" fill="currentColor" viewBox="0 0 24 24">
                <path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h4v10h-10z"/>
              </svg>
            </div>
            <p class="text-sm text-gray-300 font-modern italic leading-relaxed text-center hover:text-white transition-colors duration-300">
              "{{ member.quote }}"
            </p>
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
      <div class="absolute -top-3 -left-3 w-8 h-8 border-l-2 border-t-2 border-gold-500/30 rounded-tl-2xl group-hover:border-gold-500/50 transition-all duration-500"></div>
      <div class="absolute -top-3 -right-3 w-8 h-8 border-r-2 border-t-2 border-gold-500/30 rounded-tr-2xl group-hover:border-gold-500/50 transition-all duration-500"></div>
      <div class="absolute -bottom-3 -left-3 w-8 h-8 border-l-2 border-b-2 border-gold-500/30 rounded-bl-2xl group-hover:border-gold-500/50 transition-all duration-500"></div>
      <div class="absolute -bottom-3 -right-3 w-8 h-8 border-r-2 border-b-2 border-gold-500/30 rounded-br-2xl group-hover:border-gold-500/50 transition-all duration-500"></div>
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