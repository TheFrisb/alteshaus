<script setup lang="ts">
import { onMounted, nextTick } from 'vue'
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import AOS from 'aos'
import 'aos/dist/aos.css'

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
  <div class="min-h-screen bg-black text-white">
    <AppHeader />
    <main>
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<style scoped>
/* Component-specific styles can go here */
</style>