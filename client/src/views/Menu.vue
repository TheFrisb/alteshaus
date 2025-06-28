<script setup lang="ts">
import { ref, onMounted, nextTick, onUnmounted } from 'vue'
import AOS from 'aos'
import MenuCard from '../components/MenuCard.vue'

const activeCategory = ref('appetizers')
const showStickyCategories = ref(false)
const categorySectionRef = ref<HTMLElement | null>(null)

const categories = [
  { id: 'appetizers', name: 'Appetizers', icon: '🥗', description: 'Elegant starters to awaken your palate' },
  { id: 'german-classics', name: 'German Classics', icon: '🍖', description: 'Traditional dishes from the heart of Germany' },
  { id: 'macedonian-specialties', name: 'Macedonian Specialties', icon: '🌶️', description: 'Authentic flavors from the Balkans' },
  { id: 'fusion-dishes', name: 'Fusion Dishes', icon: '✨', description: 'Where German tradition meets Macedonian soul' },
  { id: 'desserts', name: 'Desserts', icon: '🍰', description: 'Sweet endings to perfect your experience' },
  { id: 'beverages', name: 'Beverages', icon: '🍷', description: 'Carefully curated drinks to complement your meal' }
]

const menuItems = {
  appetizers: [
    {
      id: 1,
      name: 'Ajvar Bruschetta',
      price: '€8.50',
      image: 'https://images.pexels.com/photos/1647163/pexels-photo-1647163.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'A delightful fusion where Italian tradition meets Macedonian flavors. Our house-made ajvar, crafted from fire-roasted red peppers, crowns artisanal sourdough bread.',
      ingredients: ['Sourdough bread', 'House-made ajvar', 'Fresh basil', 'Extra virgin olive oil', 'Goat cheese', 'Balsamic reduction'],
      badge: { text: 'Popular', color: 'green' }
    },
    {
      id: 2,
      name: 'Käsespätzle Bites',
      price: '€9.00',
      image: 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Traditional Swabian comfort food reimagined as elegant bite-sized portions. Each morsel delivers the soul-warming essence of Alpine cuisine.',
      ingredients: ['Fresh spätzle', 'Gruyère cheese', 'Caramelized onions', 'Fresh chives', 'Butter', 'Black pepper']
    },
    {
      id: 3,
      name: 'Balkan Mezze Platter',
      price: '€12.00',
      image: 'https://images.pexels.com/photos/1099680/pexels-photo-1099680.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'A journey through the Balkans on a single plate. Each element tells a story of sun-drenched valleys and ancient culinary traditions.',
      ingredients: ['Homemade hummus', 'Shopska salad', 'Kajmak cheese', 'Cured olives', 'Fresh flatbread', 'Roasted peppers'],
      badge: { text: 'Sharing', color: 'blue' }
    }
  ],
  'german-classics': [
    {
      id: 4,
      name: 'Wiener Schnitzel',
      price: '€18.50',
      image: 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'The crown jewel of Austrian-German cuisine. Our veal is hand-selected, tenderized with care, and coated in golden breadcrumbs that shatter at first bite.',
      ingredients: ['Premium veal cutlet', 'Fresh breadcrumbs', 'Free-range eggs', 'Clarified butter', 'Lemon wedge', 'Lingonberry sauce'],
      badge: { text: 'Signature', color: 'gold' }
    },
    {
      id: 5,
      name: 'Sauerbraten',
      price: '€22.00',
      image: 'https://images.pexels.com/photos/1438672/pexels-photo-1438672.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'The "Rhineland Roast" - a testament to German patience and precision. Marinated for days in wine and spices, then slow-roasted to perfection.',
      ingredients: ['Beef roast', 'Red wine marinade', 'Juniper berries', 'Bay leaves', 'Ginger snaps', 'Root vegetables'],
      badge: { text: 'Traditional', color: 'blue' }
    },
    {
      id: 6,
      name: 'Currywurst Deluxe',
      price: '€14.00',
      image: 'https://images.pexels.com/photos/5949888/pexels-photo-5949888.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Berlin street food elevated to fine dining. Our artisanal bratwurst meets a complex curry sauce that balances sweet, spicy, and umami.',
      ingredients: ['House-made bratwurst', 'Curry powder blend', 'Tomato base', 'Onions', 'Paprika', 'Fresh herbs'],
      badge: { text: 'Modern', color: 'green' }
    }
  ],
  'macedonian-specialties': [
    {
      id: 7,
      name: 'Tavče Gravče',
      price: '€16.00',
      image: 'https://images.pexels.com/photos/1640772/pexels-photo-1640772.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Macedonia\'s national dish, slow-cooked in traditional clay pots. Each bean absorbs the rich flavors of paprika, onions, and Mediterranean herbs.',
      ingredients: ['White beans', 'Paprika', 'Onions', 'Tomatoes', 'Bay leaves', 'Olive oil'],
      badge: { text: 'National', color: 'red' }
    },
    {
      id: 8,
      name: 'Kebapi Skopje Style',
      price: '€17.50',
      image: 'https://images.pexels.com/photos/5949888/pexels-photo-5949888.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Hand-rolled cylinders of seasoned meat, grilled over open flames. Served with fresh onions and warm lepinja bread, just like in Skopje\'s old bazaar.',
      ingredients: ['Ground beef and lamb', 'Secret spice blend', 'Fresh onions', 'Lepinja bread', 'Kajmak', 'Ajvar'],
      badge: { text: 'Spicy', color: 'red' }
    },
    {
      id: 9,
      name: 'Shopska Salad Supreme',
      price: '€11.00',
      image: 'https://images.pexels.com/photos/1059905/pexels-photo-1059905.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'The colors of the Macedonian flag in a bowl. Crisp vegetables crowned with authentic sirene cheese, dressed in golden olive oil.',
      ingredients: ['Tomatoes', 'Cucumbers', 'Onions', 'Peppers', 'Sirene cheese', 'Olive oil', 'Wine vinegar'],
      badge: { text: 'Fresh', color: 'green' }
    }
  ],
  'fusion-dishes': [
    {
      id: 10,
      name: 'Schnitzel mit Ajvar',
      price: '€19.50',
      image: 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Our signature fusion masterpiece. Traditional German schnitzel meets the fiery passion of Macedonian ajvar in perfect harmony.',
      ingredients: ['Pork schnitzel', 'House-made ajvar', 'Roasted vegetables', 'Fresh herbs', 'Lemon', 'Paprika oil'],
      badge: { text: 'Signature', color: 'gold' }
    },
    {
      id: 11,
      name: 'Balkan Sauerbraten',
      price: '€24.00',
      image: 'https://images.pexels.com/photos/1438672/pexels-photo-1438672.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'German tradition enhanced with Balkan soul. Our sauerbraten is marinated with Macedonian wine and spices, creating a unique cross-cultural experience.',
      ingredients: ['Beef roast', 'Macedonian wine', 'Balkan spices', 'Roasted peppers', 'Traditional gravy', 'Seasonal vegetables'],
      badge: { text: 'Chef\'s Choice', color: 'gold' }
    },
    {
      id: 12,
      name: 'Spätzle Carbonara Balkan',
      price: '€16.50',
      image: 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Italian technique meets German pasta and Balkan flavors. Creamy, rich, and utterly unique - a dish that tells the story of European unity.',
      ingredients: ['Fresh spätzle', 'Pancetta', 'Free-range eggs', 'Parmesan', 'Kajmak', 'Black pepper', 'Fresh parsley'],
      badge: { text: 'Fusion', color: 'blue' }
    }
  ],
  desserts: [
    {
      id: 13,
      name: 'Black Forest Cake',
      price: '€7.50',
      image: 'https://images.pexels.com/photos/291528/pexels-photo-291528.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'The legendary Schwarzwälder Kirschtorte, crafted with authentic Kirsch from the Black Forest. Each layer tells a story of German confectionery mastery.',
      ingredients: ['Chocolate sponge', 'Fresh cherries', 'Kirsch liqueur', 'Whipped cream', 'Dark chocolate shavings', 'Cherry compote'],
      badge: { text: 'Classic', color: 'blue' }
    },
    {
      id: 14,
      name: 'Baklava Fusion',
      price: '€6.50',
      image: 'https://images.pexels.com/photos/1126359/pexels-photo-1126359.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Traditional Macedonian baklava with a modern twist. Layers of phyllo pastry embrace a mixture of nuts and honey, finished with a touch of German precision.',
      ingredients: ['Phyllo pastry', 'Mixed nuts', 'Honey syrup', 'Cinnamon', 'Butter', 'Rose water'],
      badge: { text: 'Sweet', color: 'gold' }
    },
    {
      id: 15,
      name: 'Apfelstrudel Modern',
      price: '€6.00',
      image: 'https://images.pexels.com/photos/1126728/pexels-photo-1126728.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Classic Austrian apple strudel reimagined. Paper-thin pastry wraps spiced apples, served warm with vanilla sauce and a hint of Balkan honey.',
      ingredients: ['Strudel pastry', 'Granny Smith apples', 'Cinnamon', 'Raisins', 'Breadcrumbs', 'Vanilla sauce', 'Balkan honey'],
      badge: { text: 'Warm', color: 'red' }
    }
  ],
  beverages: [
    {
      id: 16,
      name: 'German Wine Selection',
      price: '€6.00 - €12.00',
      image: 'https://images.pexels.com/photos/1407846/pexels-photo-1407846.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Carefully curated wines from German vineyards, each bottle selected to complement our cuisine. From crisp Rieslings to robust Spätburgunders.',
      ingredients: ['Riesling', 'Gewürztraminer', 'Spätburgunder', 'Müller-Thurgau', 'Silvaner', 'Eiswein'],
      badge: { text: 'Premium', color: 'gold' }
    },
    {
      id: 17,
      name: 'Macedonian Rakija',
      price: '€4.50 - €8.00',
      image: 'https://images.pexels.com/photos/1283219/pexels-photo-1283219.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Traditional fruit brandies from Macedonia\'s finest distilleries. Each sip carries the essence of sun-ripened fruits and centuries-old traditions.',
      ingredients: ['Grape rakija', 'Plum rakija', 'Apple rakija', 'Pear rakija', 'Honey rakija', 'Herb-infused varieties'],
      badge: { text: 'Traditional', color: 'blue' }
    },
    {
      id: 18,
      name: 'Craft Beer Selection',
      price: '€4.00 - €7.00',
      image: 'https://images.pexels.com/photos/1552630/pexels-photo-1552630.jpeg?auto=compress&cs=tinysrgb&w=600&h=400&fit=crop',
      story: 'Local and German craft beers that pair perfectly with our dishes. From light wheat beers to rich, malty bocks.',
      ingredients: ['Weissbier', 'Pilsner', 'Märzen', 'Bock', 'Kölsch', 'Local craft varieties'],
      badge: { text: 'Craft', color: 'green' }
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
            <div class="bg-black/30 backdrop-blur-xl rounded-full px-12 py-10 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group cursor-pointer shadow-2xl hover:shadow-gold-500/10">
              <!-- Top Decorative Line -->
              <div class="absolute top-4 left-1/2 transform -translate-x-1/2 w-24 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-32 transition-all duration-500" data-aos="fade-up" data-aos-delay="200"></div>
              
              <!-- Main Title -->
              <h1 class="text-3xl md:text-4xl lg:text-5xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 mb-6 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 transition-all duration-500">
                Our Menu
              </h1>
              
              <!-- Elegant Separator with Icons -->
              <div class="flex items-center justify-center space-x-4 mb-6" data-aos="fade-up" data-aos-delay="400">
                <div class="w-16 h-0.5 bg-gradient-to-r from-transparent to-gold-500 rounded-full group-hover:w-20 transition-all duration-500"></div>
                <div class="text-gold-500 bg-gold-500/20 rounded-full p-3 group-hover:bg-gold-500/30 group-hover:scale-110 transition-all duration-300">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                  </svg>
                </div>
                <div class="w-16 h-0.5 bg-gradient-to-l from-transparent to-gold-500 rounded-full group-hover:w-20 transition-all duration-500"></div>
              </div>
              
              <!-- Subtitle -->
              <p class="text-base text-gray-300 font-modern group-hover:text-gold-200 transition-colors duration-500 tracking-wide max-w-2xl mx-auto leading-relaxed" data-aos="fade-up" data-aos-delay="600">
                A culinary journey through German tradition and Macedonian heritage, where every dish tells a story of passion and artistry
              </p>
              
              <!-- Bottom Decorative Line -->
              <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 w-24 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-32 transition-all duration-500"></div>
            </div>
            
            <!-- Corner Decorative Elements -->
            <div class="absolute -top-2 -left-2 w-8 h-8 border-l-2 border-t-2 border-gold-500/40 rounded-tl-xl" data-aos="fade-in" data-aos-delay="800"></div>
            <div class="absolute -top-2 -right-2 w-8 h-8 border-r-2 border-t-2 border-gold-500/40 rounded-tr-xl" data-aos="fade-in" data-aos-delay="900"></div>
            <div class="absolute -bottom-2 -left-2 w-8 h-8 border-l-2 border-b-2 border-gold-500/40 rounded-bl-xl" data-aos="fade-in" data-aos-delay="1000"></div>
            <div class="absolute -bottom-2 -right-2 w-8 h-8 border-r-2 border-b-2 border-gold-500/40 rounded-br-xl" data-aos="fade-in" data-aos-delay="1100"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Enhanced Category Navigation -->
    <section ref="categorySectionRef" class="py-12 bg-gradient-to-b from-gray-900 to-black border-y border-gold-500/20">
      <div class="max-w-7xl mx-auto px-6">
        <!-- Category Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" data-aos="fade-up" data-aos-duration="800">
          <button
            v-for="category in categories"
            :key="category.id"
            @click="setActiveCategory(category.id)"
            :class="[
              'relative group bg-gradient-to-br from-black/60 via-black/40 to-black/60 backdrop-blur-xl rounded-2xl p-6 border transition-all duration-500 hover:scale-105 hover:-translate-y-2',
              activeCategory === category.id 
                ? 'border-gold-500/50 bg-gradient-to-br from-gold-500/10 via-black/40 to-gold-500/5 shadow-xl shadow-gold-500/20' 
                : 'border-gold-500/20 hover:border-gold-500/40 hover:shadow-lg hover:shadow-gold-500/10'
            ]"
          >
            <!-- Background Pattern -->
            <div class="absolute inset-0 opacity-5 rounded-2xl overflow-hidden">
              <div class="w-full h-full" style="background-image: radial-gradient(circle at 2px 2px, rgba(212, 175, 55, 0.3) 1px, transparent 0); background-size: 20px 20px;"></div>
            </div>
            
            <!-- Content -->
            <div class="relative z-10 text-center">
              <!-- Icon -->
              <div class="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">
                {{ category.icon }}
              </div>
              
              <!-- Title -->
              <h3 :class="[
                'text-lg font-elegant font-bold mb-2 transition-colors duration-300',
                activeCategory === category.id ? 'text-gold-400' : 'text-white group-hover:text-gold-400'
              ]">
                {{ category.name }}
              </h3>
              
              <!-- Separator -->
              <div :class="[
                'h-0.5 rounded-full mx-auto mb-3 transition-all duration-300 ease-in-out',
                activeCategory === category.id ? 'w-16 bg-gold-500' : 'w-8 bg-gold-500/50 group-hover:w-12 group-hover:bg-gold-500'
              ]"></div>
              
              <!-- Description -->
              <p :class="[
                'text-sm font-modern leading-relaxed transition-colors duration-300',
                activeCategory === category.id ? 'text-gold-200' : 'text-gray-400 group-hover:text-gray-300'
              ]">
                {{ category.description }}
              </p>
            </div>
            
            <!-- Active Indicator -->
            <div v-if="activeCategory === category.id" class="absolute -top-2 -right-2 bg-gradient-to-r from-gold-500 to-gold-400 rounded-full p-2 shadow-lg shadow-gold-500/50">
              <svg class="w-4 h-4 text-black" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
              </svg>
            </div>
          </button>
        </div>
      </div>
    </section>

    <!-- Sticky Horizontal Categories -->
    <Transition
      enter-active-class="transition-all duration-500 ease-out"
      leave-active-class="transition-all duration-300 ease-in"
      enter-from-class="transform -translate-y-full opacity-0"
      enter-to-class="transform translate-y-0 opacity-100"
      leave-from-class="transform translate-y-0 opacity-100"
      leave-to-class="transform -translate-y-full opacity-0"
    >
      <div 
        v-if="showStickyCategories"
        class="fixed top-20 left-0 right-0 z-50 bg-black/95 backdrop-blur-xl border-b border-gold-500/20 shadow-2xl shadow-black/50"
      >
        <div class="relative">
          <!-- Scroll Indicators -->
          <div class="absolute left-0 top-0 bottom-0 w-8 bg-gradient-to-r from-black/80 to-transparent z-10 pointer-events-none flex items-center">
            <svg class="w-4 h-4 text-gold-500/60 ml-2 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
            </svg>
          </div>
          <div class="absolute right-0 top-0 bottom-0 w-8 bg-gradient-to-l from-black/80 to-transparent z-10 pointer-events-none flex items-center justify-end">
            <svg class="w-4 h-4 text-gold-500/60 mr-2 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </div>
          
          <!-- Scrollable Categories Container -->
          <div class="overflow-x-auto scrollbar-hide py-4 px-8">
            <div class="flex space-x-4 min-w-max">
              <button
                v-for="category in categories"
                :key="category.id"
                @click="setActiveCategory(category.id)"
                :class="[
                  'flex-shrink-0 group bg-gradient-to-r from-black/60 via-black/40 to-black/60 backdrop-blur-sm rounded-full px-6 py-3 border transition-all duration-300 hover:scale-105',
                  activeCategory === category.id 
                    ? 'border-gold-500/50 bg-gradient-to-r from-gold-500/20 via-black/40 to-gold-500/20 shadow-lg shadow-gold-500/20' 
                    : 'border-gold-500/20 hover:border-gold-500/40'
                ]"
              >
                <div class="flex items-center space-x-3">
                  <!-- Icon -->
                  <div class="text-xl group-hover:scale-110 transition-transform duration-300">
                    {{ category.icon }}
                  </div>
                  
                  <!-- Title -->
                  <span :class="[
                    'text-sm font-elegant font-semibold transition-colors duration-300 whitespace-nowrap',
                    activeCategory === category.id ? 'text-gold-400' : 'text-white group-hover:text-gold-400'
                  ]">
                    {{ category.name }}
                  </span>
                  
                  <!-- Active Indicator -->
                  <div v-if="activeCategory === category.id" class="w-2 h-2 bg-gold-500 rounded-full animate-pulse"></div>
                </div>
              </button>
            </div>
          </div>
          
          <!-- Scroll Hint Text -->
        </div>
      </div>
    </Transition>

    <!-- Spacer to prevent content jump when sticky menu appears -->
    <div 
      v-if="showStickyCategories" 
      class="h-20 transition-all duration-500 ease-out"
    ></div>

    <!-- Menu Items Section -->
    <section class="relative overflow-hidden bg-gradient-to-b from-black via-gray-900 to-black">
      <!-- Background Elements -->
      <div class="absolute inset-0 overflow-hidden">
        <div class="absolute top-1/4 left-1/4 w-40 h-20 bg-gold-500/2 rounded-full -translate-x-20 -translate-y-10 rotate-45"></div>
        <div class="absolute bottom-1/4 right-1/4 w-32 h-16 bg-gold-500/3 rounded-full translate-x-16 translate-y-8 -rotate-45"></div>
      </div>
      
      <div class="max-w-7xl mx-auto relative z-10 section-padding">
        <!-- Category Title -->
        <div class="text-center mb-20" data-aos="fade-up" data-aos-duration="800">
          <div class="inline-block bg-black/30 backdrop-blur-xl rounded-full px-12 py-8 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-500 group cursor-pointer">
            <div class="flex items-center space-x-4 mb-4">
              <div class="text-3xl">{{ categories.find(cat => cat.id === activeCategory)?.icon }}</div>
              <h2 class="text-3xl md:text-4xl font-elegant font-bold text-gold-500 group-hover:text-gold-400 transition-colors duration-300">
                {{ categories.find(cat => cat.id === activeCategory)?.name }}
              </h2>
            </div>
            <div class="w-20 h-0.5 bg-gold-500 rounded-full mx-auto group-hover:w-28 transition-all duration-300"></div>
            <p class="text-sm text-gray-300 font-modern mt-4 group-hover:text-gold-200 transition-colors duration-300">
              {{ categories.find(cat => cat.id === activeCategory)?.description }}
            </p>
          </div>
        </div>

        <!-- Enhanced Dishes Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-12 xl:gap-16 mb-20">
          <MenuCard
            v-for="(item, index) in menuItems[activeCategory]"
            :key="item.id"
            :item="item"
            :index="index"
          />
        </div>
      </div>
    </section>

    <!-- Enhanced Call to Action -->
    <section class="relative overflow-hidden bg-gradient-to-b from-gray-900 to-black">
      <div class="absolute inset-0 overflow-hidden">
        <div class="absolute top-0 left-0 w-64 h-32 bg-gold-500/5 rounded-full -translate-x-32 -translate-y-16 rotate-12"></div>
        <div class="absolute bottom-0 right-0 w-96 h-48 bg-gold-500/3 rounded-full translate-x-48 translate-y-24 -rotate-12"></div>
      </div>
      
      <div class="max-w-5xl mx-auto relative z-10 section-padding text-center" data-aos="fade-up" data-aos-duration="1000">
        <div class="relative">
          <!-- Premium CTA Container -->
          <div class="bg-gradient-to-r from-black/40 via-black/20 to-black/40 backdrop-blur-xl rounded-full px-12 py-8 border border-gold-500/20 hover:border-gold-500/40 transition-all duration-700 group cursor-pointer shadow-2xl hover:shadow-gold-500/20 hover:shadow-2xl hover:scale-[1.02] hover:-translate-y-2">
            
            <!-- Decorative Elements -->
            <div class="absolute top-3 left-1/2 transform -translate-x-1/2 w-20 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-32 group-hover:via-gold-400/80 transition-all duration-500 ease-in-out"></div>
            <div class="absolute bottom-3 left-1/2 transform -translate-x-1/2 w-20 h-0.5 bg-gradient-to-r from-transparent via-gold-500/60 to-transparent group-hover:w-32 group-hover:via-gold-400/80 transition-all duration-500 ease-in-out"></div>
            
            <!-- Floating Particles on Hover -->
            <div class="absolute top-1/4 left-1/4 w-2 h-2 bg-gold-500/0 rounded-full group-hover:bg-gold-500/40 group-hover:animate-pulse transition-all duration-700"></div>
            <div class="absolute top-3/4 right-1/4 w-1.5 h-1.5 bg-gold-400/0 rounded-full group-hover:bg-gold-400/50 group-hover:animate-pulse transition-all duration-700" style="animation-delay: 0.2s;"></div>
            <div class="absolute top-1/2 right-1/3 w-1 h-1 bg-gold-500/0 rounded-full group-hover:bg-gold-500/60 group-hover:animate-pulse transition-all duration-700" style="animation-delay: 0.4s;"></div>
            
            <!-- Content -->
            <div class="space-y-6">
              <div>
                <h2 class="text-2xl md:text-3xl font-elegant font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-400 via-gold-500 to-gold-600 mb-3 group-hover:from-gold-300 group-hover:via-gold-400 group-hover:to-gold-500 group-hover:scale-105 transition-all duration-500">
                  Ready to Experience Our Cuisine?
                </h2>
                <p class="text-sm text-gray-300 font-modern group-hover:text-gold-200 group-hover:scale-105 transition-all duration-500 max-w-xl mx-auto leading-relaxed">
                  Reserve your table today and embark on a culinary journey that bridges cultures and creates unforgettable memories
                </p>
              </div>
              
              <!-- Action Buttons -->
              <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <button class="bg-gradient-to-r from-gold-500 to-gold-600 hover:from-gold-600 hover:to-gold-700 text-black font-bold px-8 py-3 text-sm rounded-full transition-all duration-300 transform hover:scale-110 hover:shadow-xl hover:shadow-gold-500/50 border-2 border-gold-400 hover:border-gold-300 group/btn hover:-translate-y-1">
                  <div class="flex items-center space-x-3">
                    <svg class="w-4 h-4 group-hover/btn:rotate-12 group-hover/btn:scale-110 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                    </svg>
                    <span class="group-hover/btn:tracking-wider transition-all duration-300">Make Reservation</span>
                  </div>
                </button>
                
                <button class="border-2 border-gold-500 text-gold-500 hover:bg-gold-500 hover:text-black font-bold px-8 py-3 text-sm rounded-full transition-all duration-300 hover:scale-110 hover:shadow-xl hover:shadow-gold-500/40 group/btn backdrop-blur-sm bg-black/10 hover:-translate-y-1">
                  <div class="flex items-center space-x-3">
                    <svg class="w-4 h-4 group-hover/btn:scale-110 group-hover/btn:rotate-6 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                    </svg>
                    <span class="group-hover/btn:tracking-wider transition-all duration-300">Contact Us</span>
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