<script setup lang="ts">
import { onMounted } from 'vue'
import HeroSection from '../components/HeroSection.vue'
import FeaturedDishes from '../components/FeaturedDishes.vue'
import RestaurantStory from '../components/RestaurantStory.vue'
import LocationContact from '../components/LocationContact.vue'
</script>

<template>
  <div>
    <HeroSection />
    <RestaurantStory />
    <FeaturedDishes />
    <LocationContact />
  </div>
</template>