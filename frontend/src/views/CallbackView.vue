<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import IconLoading2 from "@/components/icons/IconLoading2.vue";

const authStore = useAuthStore()
const router = useRouter()
const route = useRoute()

const validateToken = async (token: string) => {
  try {
    const response = await axios.get('https://id.twitch.tv/oauth2/validate', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    return response.status === 200
  } catch (error) {
    console.error('Ошибка проверки токена:', error)
    return false
  }
}

onMounted(async () => {
  const accessToken = route.query.access_token as string
  const expiresIn = Number(route.query.expires_in)

  if (accessToken) {
    const isValid = await validateToken(accessToken)

    if (isValid) {
      authStore.setTokens(accessToken, expiresIn)
      router.push('/configurator')
    } else {
      console.error('Недействительный токен')
      router.push('/')
    }
  } else {
    console.error('Ошибка авторизации')
    router.push('/')
  }
})
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
