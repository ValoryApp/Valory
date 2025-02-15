<script setup lang="ts">
interface Props {
  size?: number;
  color?: string;
}

const props = withDefaults(defineProps<Props>(), {
  size: 24,
  color: '#A970FF',
});
</script>

<template>
<svg :width="size" :height="size" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M12.5 3.5 8 2 3.5 3.5 2 8l1.5 4.5L8 14l4.5-1.5L14 8l-1.5-4.5ZM7 11l4.5-4.5L10 5 7 8 5.5 6.5 4 8l3 3Z" :fill="color" clip-rule="evenodd">
  </path>
</svg>
</template>

<style scoped>
  svg {
    margin-bottom: 0;
  }
</style>