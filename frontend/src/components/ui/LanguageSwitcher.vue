<script lang="ts" setup>
import DropdownMenu from '@/components/ui/DropdownMenu/DropdownMenu.vue'
import DropdownMenuItem from '@/components/ui/DropdownMenu/DropdownMenuItem.vue'
import { AVAILABLE_LOCALES } from '@/i18n'
import { useLocalStorage } from '@vueuse/core'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n<{ locale: string; availableLocales: string[] }>()
const currentLocale = useLocalStorage<string>('valory-locale', 'en')
</script>

<template>
  <div>
    <DropdownMenu size="medium">
      <DropdownMenuItem
        v-for="lang of AVAILABLE_LOCALES"
        :key="lang.code"
        :checked="currentLocale === lang.code"
        @select="
          () => {
            locale = lang.code
            currentLocale = lang.code
          }
        "
      >
        <Icon :icon="`flag:${lang.flag}-4x3`" height="18" width="18" />
        {{ lang.name }}
      </DropdownMenuItem>
      <template #title>
        {{ $t('landing.languageSwitcher') }}
      </template>
      <template #button>
        <Icon :icon="`flag:${$t('flag')}-4x3`" height="18" width="18" />
<!--        {{ $t('languageName') }}-->
      </template>
    </DropdownMenu>
  </div>
</template>
