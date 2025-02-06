import { useSettingsStore } from '@/stores/settings.ts'
import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'https://api.henrikdev.xyz/valorant',
  headers: {
    accept: 'application/json',
  },
})

apiClient.interceptors.request.use(
  (config) => {
    const settingsStore = useSettingsStore()
    const apiKey = settingsStore.apiKey

    if (apiKey) {
      config.params = {
        ...config.params,
        api_key: apiKey,
      }
    } else {
      console.warn('API Key is not installed in Pinia!')
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  },
)

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API error:', error)
    return Promise.reject(error)
  },
)

export default apiClient
