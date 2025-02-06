import apiClient from './apiClient'
import { useSettingsStore } from '@/stores/settings'

const settingsStore = useSettingsStore()

const isValidApiKey = (apiKey: string | null): boolean => {
  if (!apiKey) {
    return false
  }
  const apiKeyRegex =
    /^HDEV-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/
  return apiKeyRegex.test(apiKey)
}

export const checkApiKey = async (): Promise<boolean> => {
  const apiKey = settingsStore.apiKey

  if (!isValidApiKey(apiKey)) {
    console.error('Invalid API key format:', apiKey)
    return false
  }

  try {
    const response = await apiClient.get('/v1/status/eu')
    const isValid = response.status === 200
    settingsStore.verifyApiKey = isValid
    return isValid
  } catch (error) {
    console.error('API Key verification error:', error)
    settingsStore.verifyApiKey = false
    return false
  }
}
