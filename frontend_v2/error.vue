<script setup lang="ts">
import type { NuxtError } from '#app'

const props = defineProps({
  error: Object as () => NuxtError
})
</script>

<template>
  <div class="h-dvh container m-auto flex flex-col gap-8 items-center justify-center">
    <span class="font-extrabold text-7xl">{{ error.statusCode }}</span>
    <span class="font-extrabold text-5xl">Whooops, this page is gone!</span>
    <span class="font-normal text-xl text-[#CECECE]">This page is missing or you wrote the link incorrectly.</span>
    <UiButton @click="navigateTo('/')" variant="outline">
      Go back home
      <IconsHome :size="16"/>
    </UiButton>
  </div>
</template>