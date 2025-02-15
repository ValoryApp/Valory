// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  devtools: { enabled: false },
  ssr: false,
  nitro: {
    prerender: {
      routes: [
        '/_ipx/w_120/ValoryLogo3D.png',
        '/_ipx/w_140/ValoryLogo3D.png',
      ]
    }
  },

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
  ],

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
});