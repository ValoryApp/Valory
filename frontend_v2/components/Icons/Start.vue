<script setup lang="ts">
defineProps(
  {
    size: {
      type: Number,
      default: 24,
    },
    color: {
      type: String,
      default: '#F2F2F2',
    }
  }
)
</script>

<template>
<svg :width="size" :height="size" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M3.33334 3.57436C3.33334 2.92692 3.33334 2.6032 3.46834 2.42475C3.58594 2.26929 3.76569 2.17309 3.96028 2.16147C4.18364 2.14813 4.45298 2.3277 4.99169 2.68684L12.0021 7.36042C12.4472 7.65715 12.6697 7.80555 12.7473 7.99255C12.8151 8.15608 12.8151 8.33982 12.7473 8.50335C12.6697 8.69035 12.4472 8.83868 12.0021 9.13548L4.99169 13.809C4.45298 14.1682 4.18364 14.3478 3.96028 14.3344C3.76569 14.3228 3.58594 14.2266 3.46834 14.0712C3.33334 13.8927 3.33334 13.569 3.33334 12.9216V3.57436Z" :stroke="color" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
</template>

<style scoped>
  svg {
    margin-bottom: 0;
  }
</style>