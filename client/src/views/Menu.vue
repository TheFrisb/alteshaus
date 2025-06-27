Here's the fixed script with all missing closing brackets added:

<script setup lang="ts">
import { ref, onMounted, nextTick, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'
import AOS from 'aos'
import MenuCard from '../components/MenuCard.vue'

const { t } = useI18n()
const activeCategory = ref('appetizers')
const showStickyCategories = ref(false)
const categorySectionRef = ref<HTMLElement | null>(null)

const categories = [
  { id: 'appetizers', name: t('menu.appetizers'), icon: '🥗', description: t('menu.appetizersDesc') },
  { id: 'german-classics', name: t('menu.germanClassics'), icon: '🍖', description: t('menu.germanClassicsDesc') },
  { id: 'macedonian-specialties', name: t('menu.macedonianSpecialties'), icon: '🌶️', description: t('menu.macedonianSpecialtiesDesc') },
  { id: 'fusion-dishes', name: t('menu.fusionDishes'), icon: '✨', description: t('menu.fusionDishesDesc') },
  { id: 'desserts', name: t('menu.desserts'), icon: '🍰', description: t('menu.dessertsDesc') },
  { id: 'beverages', name: t('menu.beverages'), icon: '🍷', description: t('menu.beveragesDesc') }
]

const menuItems = {
  appetizers: [
    {
      id: 1,
      name: t('menu.ajvarBruschetta'),
      price: '€8.50',
      image: 'https://images.pexels.com/photos/1647163/pexels-photo-1647163.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.ajvarBruschettaStory'),
      ingredients: t('menu.ajvarBruschettaIngredients').split(', '),
      badge: { text: t('menu.popular'), color: 'green' }
    },
    {
      id: 2,
      name: t('menu.kasespatzleBites'),
      price: '€9.00',
      image: 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.kasespatzleBitesStory'),
      ingredients: t('menu.kasespatzleBitesIngredients').split(', ')
    },
    {
      id: 3,
      name: t('menu.balkanMezzePlatter'),
      price: '€12.00',
      image: 'https://images.pexels.com/photos/1099680/pexels-photo-1099680.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.balkanMezzePlatteStory'),
      ingredients: t('menu.balkanMezzePlatteIngredients').split(', '),
      badge: { text: t('menu.sharing'), color: 'blue' }
    }
  ],
  'german-classics': [
    {
      id: 4,
      name: t('menu.wienerSchnitzel'),
      price: '€18.50',
      image: 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.wienerSchnitzelStory'),
      ingredients: t('menu.wienerSchnitzelIngredients').split(', '),
      badge: { text: t('menu.signature'), color: 'gold' }
    },
    {
      id: 5,
      name: t('menu.sauerbraten'),
      price: '€22.00',
      image: 'https://images.pexels.com/photos/1438672/pexels-photo-1438672.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.sauerbratenStory'),
      ingredients: t('menu.sauerbratenIngredients').split(', '),
      badge: { text: t('menu.traditional'), color: 'blue' }
    },
    {
      id: 6,
      name: t('menu.currywurstDeluxe'),
      price: '€14.00',
      image: 'https://images.pexels.com/photos/5949888/pexels-photo-5949888.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.currywurstDeluxeStory'),
      ingredients: t('menu.currywurstDeluxeIngredients').split(', '),
      badge: { text: t('menu.modern'), color: 'green' }
    }
  ],
  'macedonian-specialties': [
    {
      id: 7,
      name: t('menu.tavceGravce'),
      price: '€16.00',
      image: 'https://images.pexels.com/photos/1640772/pexels-photo-1640772.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.tavceGravceStory'),
      ingredients: t('menu.tavceGravceIngredients').split(', '),
      badge: { text: t('menu.national'), color: 'red' }
    },
    {
      id: 8,
      name: t('menu.kebapiSkopjeStyle'),
      price: '€17.50',
      image: 'https://images.pexels.com/photos/5949888/pexels-photo-5949888.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.kebapiSkopjeStyleStory'),
      ingredients: t('menu.kebapiSkopjeStyleIngredients').split(', '),
      badge: { text: t('menu.spicy'), color: 'red' }
    },
    {
      id: 9,
      name: t('menu.shopskaSaladSupreme'),
      price: '€11.00',
      image: 'https://images.pexels.com/photos/1059905/pexels-photo-1059905.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.shopskaSaladSupremeStory'),
      ingredients: t('menu.shopskaSaladSupremeIngredients').split(', '),
      badge: { text: t('menu.fresh'), color: 'green' }
    }
  ],
  'fusion-dishes': [
    {
      id: 10,
      name: t('menu.schnitzelMitAjvar'),
      price: '€19.50',
      image: 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.schnitzelMitAjvarStory'),
      ingredients: t('menu.schnitzelMitAjvarIngredients').split(', '),
      badge: { text: t('menu.signature'), color: 'gold' }
    },
    {
      id: 11,
      name: t('menu.balkanSauerbraten'),
      price: '€24.00',
      image: 'https://images.pexels.com/photos/1438672/pexels-photo-1438672.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.balkanSauerbratenStory'),
      ingredients: t('menu.balkanSauerbratenIngredients').split(', '),
      badge: { text: t('menu.chefsChoice'), color: 'gold' }
    },
    {
      id: 12,
      name: t('menu.spatzleCarbonaraBalkan'),
      price: '€16.50',
      image: 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.spatzleCarbonaraBalkanStory'),
      ingredients: t('menu.spatzleCarbonaraBalkanIngredients').split(', '),
      badge: { text: t('menu.fusion'), color: 'blue' }
    }
  ],
  desserts: [
    {
      id: 13,
      name: t('menu.blackForestCake'),
      price: '€7.50',
      image: 'https://images.pexels.com/photos/291528/pexels-photo-291528.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.blackForestCakeStory'),
      ingredients: t('menu.blackForestCakeIngredients').split(', '),
      badge: { text: t('menu.classic'), color: 'blue' }
    },
    {
      id: 14,
      name: t('menu.baklavaFusion'),
      price: '€6.50',
      image: 'https://images.pexels.com/photos/1126359/pexels-photo-1126359.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.baklavaFusionStory'),
      ingredients: t('menu.baklavaFusionIngredients').split(', '),
      badge: { text: t('menu.sweet'), color: 'gold' }
    },
    {
      id: 15,
      name: t('menu.apfelstrudelModern'),
      price: '€6.00',
      image: 'https://images.pexels.com/photos/1126728/pexels-photo-1126728.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.apfelstrudelModernStory'),
      ingredients: t('menu.apfelstrudelModernIngredients').split(', '),
      badge: { text: t('menu.warm'), color: 'red' }
    }
  ],
  beverages: [
    {
      id: 16,
      name: t('menu.germanWineSelection'),
      price: '€6.00 - €12.00',
      image: 'https://images.pexels.com/photos/1407846/pexels-photo-1407846.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.germanWineSelectionStory'),
      ingredients: t('menu.germanWineSelectionIngredients').split(', '),
      badge: { text: t('menu.premium'), color: 'gold' }
    },
    {
      id: 17,
      name: t('menu.macedonianRakija'),
      price: '€4.50 - €8.00',
      image: 'https://images.pexels.com/photos/1283219/pexels-photo-1283219.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.macedonianRakijaStory'),
      ingredients: t('menu.macedonianRakijaIngredients').split(', '),
      badge: { text: t('menu.traditional'), color: 'blue' }
    },
    {
      id: 18,
      name: t('menu.craftBeerSelection'),
      price: '€4.00 - €7.00',
      image: 'https://images.pexels.com/photos/1552630/pexels-photo-1552630.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: t('menu.craftBeerSelectionStory'),
      ingredients: t('menu.craftBeerSelectionIngredients').split(', '),
      badge: { text: t('menu.craft'), color: 'green' }
    }
  ]
}

const setActiveCategory = (categoryId: string) => {
  activeCategory.value = categoryId
  nextTick(() => {
    AOS.refresh()
  })
}

const handleScroll = () => {
  if (categorySectionRef.value) {
    const rect = categorySectionRef.value.getBoundingClientRect()
    // Show sticky categories when the main category section is scrolled past
    showStickyCategories.value = rect.bottom < 80 // 80px is the header height
  }
}

onMounted(() => {
  nextTick(() => {
    AOS.refresh()
  })
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>