import apiClient from '@/services/apiClient'
import { useSettingsStore } from '@/stores/settings'
import type { AxiosResponse } from 'axios'

const settingsStore = useSettingsStore()

export interface PlayerInformation {
  lastMatchId: string
  lastFiveMatches: MatchResult[]
  seasonWinrate: number
  mmr: MMR
}

export interface MMR {
  tier: {
    id: number
    name: string
  }
  rr: number
  lastChange: number
  elo: number
  leaderboard_placement: {
    rank: number
    updated_at: string
  }
}

interface MatchResponse {
  data: MatchData[] | null
}

interface MatchData {
  metadata: {
    match_id: string
  }
}

export interface ApiResponse {
  status: number
  data: PlayerMMRData | null
}

interface PlayerMMRData {
  current: {
    tier: {
      id: number
      name: string
    }
    rr: number
    last_change: number
    elo: number
    leaderboard_placement: {
      rank: number
      updated_at: string
    }
  }
}

interface SeasonalStatsResponse {
  status: number
  data: {
    seasonal: {
      season: {
        short: string
      }
      wins: number
      games: number
    }[]
  }
}

export const getInformation = async (): Promise<PlayerInformation | null> => {
  try {
    const lastMatchId = await fetchLastMatchId()
    if (!lastMatchId) {
      settingsStore.userDataLoaded = false
      return null
    }

    const playerMMR = await fetchPlayerMMR()
    if (!playerMMR) {
      settingsStore.userDataLoaded = false
      return null
    }

    const lastFiveMatches = await getLastFiveMatches()
    if (!lastFiveMatches) {
      settingsStore.userDataLoaded = false
      return null
    }

    const seasonWinrate = await getSeasonWinrate()
    if (seasonWinrate === null) {
      settingsStore.userDataLoaded = false
      return null
    }

    settingsStore.userDataLoaded = true

    return {
      lastMatchId,
      lastFiveMatches,
      seasonWinrate,
      mmr: playerMMR,
    }
  } catch (error) {
    console.error('Error fetching player information:', error)
    settingsStore.userDataLoaded = false
    return null
  }
}

const fetchLastMatchId = async (): Promise<string | null> => {
  try {
    const response: AxiosResponse<MatchResponse> = await apiClient.get(
      `/v4/by-puuid/matches/${settingsStore.region}/pc/${settingsStore.puuid}?mode=competitive&size=1`,
    )
    if (response.status === 200 && response.data.data) {
      return response.data.data[0].metadata.match_id
    }
    return null
  } catch (error: any) {
    console.error('Error fetching last match:', error.message)
    return null
  }
}

export type MatchResult = 'Win' | 'Lose' | 'Draw'

const getLastFiveMatches = async (): Promise<MatchResult[]> => {
  try {
    const response: AxiosResponse = await apiClient.get(
      `/v4/by-puuid/matches/${settingsStore.region}/pc/${settingsStore.puuid}?mode=competitive&size=5`,
    )

    if (response.data.status !== 200) {
      console.error('Failed to fetch matches:', response.data)
      return []
    }

    const matches = response.data.data

    return matches.map((match: any) => {
      const player = match.players.find((p: any) => p.puuid === settingsStore.puuid)

      if (!player) {
        console.error(
          `Player with puuid ${settingsStore.puuid} not found in match ${match.metadata.match_id}`,
        )
        return 'Draw'
      }

      const playerTeamId = player.team_id

      const team = match.teams.find((t: any) => t.team_id === playerTeamId)

      if (!team) {
        console.error(`Team for player ${puuid} not found in match ${match.metadata.match_id}`)
        return 'Draw'
      }

      return team.won ? 'Win' : 'Lose'
    })
  } catch (error) {
    console.error('Error fetching match data:', error)
    return []
  }
}

const fetchPlayerMMR = async (): Promise<MMR | null> => {
  try {
    const response: AxiosResponse<ApiResponse> = await apiClient.get(
      `/v3/by-puuid/mmr/${settingsStore.region}/pc/${settingsStore.puuid}`,
    )
    if (response.status === 200 && response.data.data) {
      const current = response.data.data.current
      return {
        tier: current.tier,
        rr: current.rr,
        lastChange: current.last_change,
        elo: current.elo,
        leaderboard_placement: current.leaderboard_placement,
      }
    }
    return null
  } catch (error: any) {
    console.error('Error fetching player MMR:', error.message)
    return null
  }
}

export const getSeasonWinrate = async (): Promise<number | null> => {
  try {
    const settingsStore = useSettingsStore()

    const statsResponse: AxiosResponse<SeasonalStatsResponse> = await apiClient.get(
      `/v3/by-puuid/mmr/${settingsStore.region}/pc/${settingsStore.puuid}`,
    )

    if (statsResponse.status !== 200 || !statsResponse.data.data) {
      console.error('Failed to fetch seasonal stats')
      return null
    }

    const lastSeasonStats = statsResponse.data.data.seasonal.at(-1)

    if (!lastSeasonStats) {
      console.error('No seasonal stats available')
      return null
    }

    const { wins, games } = lastSeasonStats

    if (games === 0) {
      console.warn('No games played in the last season')
      return 0
    }

    const winrate = (wins / games) * 100
    return Math.ceil(winrate)
  } catch (error) {
    console.error('Error fetching season winrate:', error)
    return null
  }
}
