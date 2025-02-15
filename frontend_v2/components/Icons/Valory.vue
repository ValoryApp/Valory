<script setup lang="ts">
defineProps(
  {
    size: {
      type: Number,
      default: 24,
    }
  }
)
</script>

<template>
<svg :width="size" :height="size+5" viewBox="0 0 25 30" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M12.4845 0.457062L0 7.25516V14.3438L12.4845 20.9676L24.969 14.3438V7.25516L12.4845 0.457062ZM12.497 6.11919L6.68313 9.27751V12.5708L12.497 15.6482L18.3109 12.5708V9.27751L12.497 6.11919Z" fill="#FA4454"/>
  <path d="M12.5 23.9643L25 17.3508V22.7576L12.5 29.3712L0 22.7576V17.3508L12.5 23.9643Z" fill="#FA4454"/>
</svg>
</template>

<style scoped>
  svg {
    margin-bottom: 0;
  }
</style>