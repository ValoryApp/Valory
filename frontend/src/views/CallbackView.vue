<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import { useRouter, useRoute } from "vue-router";
import { onMounted } from "vue";

const authStore = useAuthStore();
const router = useRouter();
const route = useRoute();

onMounted(() => {
  const accessToken = route.query.access_token as string;
  const expiresIn = Number(route.query.expires_in);

  if (accessToken) {
    authStore.setTokens(accessToken, expiresIn);
    router.push("/configurator");
  } else {
    console.error("Ошибка авторизации");
    router.push("/");
  }
});
</script>

<template>
  <div>Loading...</div>
</template>
