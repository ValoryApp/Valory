<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

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
  <div>Loading...</div>
</template>
