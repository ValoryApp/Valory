<script lang="ts" setup>
const { $getLocale, $switchLocale, $getLocales, $t } = useNuxtApp()
const currentLocale = ref($getLocale())

const switchLocale = (newLocale: string) => {
  $switchLocale(newLocale)
  currentLocale.value = newLocale
}
</script>

<template>
  <div class="flex w-full items-center justify-center">
    <UiDropdownMenu>
      <UiDropdownMenuTrigger as-child>
        <UiButton variant="ghost" class="px-3">
          <IconsLanguage :size="16" />
        </UiButton>
      </UiDropdownMenuTrigger>

      <UiDropdownMenuContent class="w-48">
        <UiDropdownMenuLabel :label="$t('nav.language')" />
        <UiDropdownMenuSeparator />
        <UiDropdownMenuRadioGroup v-model="currentLocale">
          <UiDropdownMenuRadioItem
            v-for="locale in $getLocales()"
            :key="locale.code"
            :value="locale.code"
            :title="locale.displayName"
            :text-value="locale.displayName"
            @select="() => switchLocale(locale.code)"
          >
            {{ locale.displayName }}
          </UiDropdownMenuRadioItem>
        </UiDropdownMenuRadioGroup>
      </UiDropdownMenuContent>
    </UiDropdownMenu>
  </div>
</template>
