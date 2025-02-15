<script setup lang="ts">
interface Props {
  size?: number;
  color?: string;
}

const props = withDefaults(defineProps<Props>(), {
  size: 24,
  color: '#F2F2F2',
});
</script>

<template>
<svg :width="size" :height="size" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12.0015 0L3.43005 8.57143V39.4286H13.7158V48L22.2872 39.4286H29.1443L44.5729 24V0H12.0015ZM41.1443 22.2857L34.2872 29.1429H27.4301L21.4301 35.1429V29.1429H13.7158V3.42857H41.1443V22.2857Z" :fill="color"/>
  <path d="M36.0014 9.42859H32.5729V19.7143H36.0014V9.42859Z" :fill="color"/>
  <path d="M26.5727 9.42859H23.1442V19.7143H26.5727V9.42859Z" :fill="color"/>
</svg>
</template>

<style scoped>
  svg {
    margin-bottom: 0;
  }
</style>