<script setup lang="ts">
import { useUserStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import IconLoading2 from "@/components/icons/IconLoading2.vue";

const userStore = useUserStore();
const router = useRouter();

const getCookie = (name: string): string | null => {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop()?.split(';').shift() || null;
  return null;
};

const token = getCookie('Authorization');
if (token) {
  userStore.setToken(token);
  router.push('/configurator');
} else {
  console.error('Токен не найден в cookie');
  router.push('/');
}
</script>

<template>
  <div class="main">
    <div class="container">
      <span class="text">Authorization...</span>
      <span class="loader">
        Waiting for response
        <IconLoading2 color="#0083fc" :size="16"/>
      </span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.main {
  display: flex;
  align-items: center;
  align-content: center;
  justify-content: center;
  margin: auto;

  .container {
    display: flex;
    flex-direction: column;
    align-content: center;
    align-items: center;
    justify-content: center;
    width: 1080px;
    gap: 12px;

    .text {
      font-weight: 400;
      font-size: 24px;
    }

    .loader {
      background: #c0ddff0a;
      color: #0083fc;

      display: flex;
      align-items: center;
      gap: 5px;

      font-size: 14px;

      padding: 8px 12px;
      border-radius: 6px;
    }
  }
}
</style>
