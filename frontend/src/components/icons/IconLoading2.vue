<script lang="ts" setup>
defineProps({
  size: {
    type: Number,
    default: 48,
  },
  color: {
    type: String,
    default: '#fff',
  }
})
</script>

<template>
  <span>
    <svg :width="size" :height="size" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 2V6M12 18V22M6 12H2M22 12H18M19.0784 19.0784L16.25 16.25M19.0784 4.99994L16.25 7.82837M4.92157 19.0784L7.75 16.25M4.92157 4.99994L7.75 7.82837" :stroke="color" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </span>
</template>

<style scoped>
span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: auto;
  padding: 0;
  line-height: 0;
}
</style>
