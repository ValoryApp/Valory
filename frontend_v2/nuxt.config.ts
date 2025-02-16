export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  devtools: { enabled: false },
  ssr: false,
  app: {
    head: {
      title: 'VALORY'
    }
  },
  css: ['@/assets/css/main.css'],
  modules: [
    "@nuxtjs/tailwindcss",
    "@nuxtjs/color-mode",
    "@vueuse/nuxt",
    "@nuxt/icon",
    "@nuxt/fonts",
    '@nuxtjs/google-fonts',
    "@nuxt/image",
    "v-wave/nuxt",
    "nuxt-i18n-micro",
    "nuxt-umami"
  ],
  umami: {
    id: 'e4411117-0d97-4a72-a9b2-68ccea557a20',
    host: 'https://cloud.umami.is',
    autoTrack: true,
  },
  i18n: {
    locales: [
      { code: 'en', iso: 'en-US', dir: 'ltr', displayName: 'English' },
      { code: 'ru', iso: 'ru-RU', dir: 'ltr', displayName: 'Русский' },
    ],
    defaultLocale: 'en',
    fallbackLocale: 'en',
    localeCookie: 'lang',
    translationDir: 'locales',
    meta: true,
  },
  googleFonts: {
    families: {
      Inter: '200..900',
    },
    prefetch: true,
    preconnect: true,
    preload: true,
    download: true,
    inject: true,
  },
  tailwindcss: {
    exposeConfig: true,
    editorSupport: true,
  },
  colorMode: {
    classSuffix: "",
  },
  hooks: {
    'prerender:routes' ({ routes }) {
      routes.clear()
    }
  },
  router: {
    options: {
      hashMode: false,
    }
  },
  imports: {
    imports: [
      {
        from: "tailwind-variants",
        name: "tv",
      },
      {
        from: "tailwind-variants",
        name: "VariantProps",
        type: true,
      },
    ],
  },
  nitro: {
    preset: 'bun'
  }
});