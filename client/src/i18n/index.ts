import { createI18n } from 'vue-i18n'
import en from './locales/en.json'
import de from './locales/de.json'
import mk from './locales/mk.json'

const messages = {
  en,
  de,
  mk
}

// Get saved locale from localStorage or default to English
const savedLocale = localStorage.getItem('locale') || 'en'

const i18n = createI18n({
  legacy: false,
  locale: savedLocale,
  fallbackLocale: 'en',
  messages,
  globalInjection: true
})

export default i18n