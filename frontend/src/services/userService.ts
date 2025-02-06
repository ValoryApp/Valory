import apiClient from './apiClient'
import { useSettingsStore } from '@/stores/settings'

const settingsStore = useSettingsStore()

export const extractNameAndTag = (input: string): { name: string; tag: string } | null => {
  const regex = /^([^#]+)#([^#]+)$/
  const match = input.match(regex)

  if (match) {
    const [, name, tag] = match
    return { name, tag }
  }

  console.error('Неверный формат строки:', input)
  return null
}

export const getPuuidWithRegion = async (): Promise<boolean> => {
  const riotId = settingsStore.riotId

  if (!riotId) {
    settingsStore.puuid = null
    settingsStore.region = null
    return false
  }

  const { name, tag } = extractNameAndTag(riotId) || { name: '', tag: '' }

  if (!name || !tag) {
    console.error('Invalid Riot ID:', riotId)
    settingsStore.puuid = null
    settingsStore.region = null
    return false
  }

  try {
    const response = await apiClient.get(`/v2/account/${name}/${tag}`)
    settingsStore.puuid = response.data.data.puuid
    settingsStore.region = response.data.data.region
    return true
  } catch (error) {
    console.error('Error getting the PUUID and region:', error)
    settingsStore.puuid = null
    settingsStore.region = null
    return false
  }
}
