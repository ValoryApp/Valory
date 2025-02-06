import router from '@/router'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: localStorage.getItem('access_token') || null,
    expiresIn: Number(localStorage.getItem('expires_in')) || 0,
  }),
  actions: {
    setTokens(accessToken: string, expiresIn: number) {
      this.accessToken = accessToken
      this.expiresIn = expiresIn

      localStorage.setItem('access_token', accessToken)
      localStorage.setItem('expires_in', String(expiresIn))
    },
    logout() {
      this.accessToken = null
      this.expiresIn = 0

      localStorage.removeItem('access_token')
      localStorage.removeItem('expires_in')

      router.push('/')
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
  },
})
