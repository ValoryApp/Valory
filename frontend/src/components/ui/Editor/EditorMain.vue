<script lang="ts" setup>
import Overlay from '@/components/OverlayItem.vue'
import Button from '@/components/ui/ButtonUI.vue'
import ColorPicker from '@/components/ui/ColorPicker.vue'
import HeaderEditor from '@/components/ui/Editor/HeaderEditor.vue'
import ModalSettingsEditor from '@/components/ui/Editor/Modal/ModalSettingsEditor.vue'
import PreviewEditor from '@/components/ui/Editor/PreviewEditor.vue'
import SectionSettingsEditor from '@/components/ui/Editor/SectionSettingsEditor.vue'
import Input from '@/components/ui/InputUI.vue'
import UiModal from '@/components/ui/ModalWindow.vue'
import Switch from '@/components/ui/Switch.vue'
import { getTopLeaderboard } from '@/services/leaderboardService'
import { getInformation } from '@/services/overlayService'
import type { PlayerInformation } from '@/services/overlayService'
import { checkApiKey } from '@/services/statusService'
import { getPuuidWithRegion } from '@/services/userService'
import { useSettingsStore } from '@/stores/settingsStore'
import { computed, onMounted, ref, watch } from 'vue'
import { toast } from 'vue-sonner'

const settingsStore = useSettingsStore()

const riotId = computed({
  get: () => settingsStore.riotId,
  set: (value) => (settingsStore.riotId = value),
})

const apiKey = computed({
  get: () => settingsStore.apiKey,
  set: (value) => (settingsStore.apiKey = value),
})

const verifyApiKey = computed({
  get: () => settingsStore.verifyApiKey,
  set: (value) => (settingsStore.verifyApiKey = value),
})

const userDataLoaded = computed({
  get: () => settingsStore.userDataLoaded,
  set: (value) => (settingsStore.userDataLoaded = value),
})

const backgroundSwitch = computed({
  get: () => settingsStore.backgroundSwitch,
  set: (value) => (settingsStore.backgroundSwitch = value),
})

const progressSwitch = computed({
  get: () => settingsStore.progressSwitch,
  set: (value) => (settingsStore.progressSwitch = value),
})

const statisticsSwitch = computed({
  get: () => settingsStore.statisticsSwitch,
  set: (value) => (settingsStore.statisticsSwitch = value),
})

const backgroundColor = computed({
  get: () => settingsStore.backgroundColor,
  set: (value) => (settingsStore.backgroundColor = value),
})

const textColor = computed({
  get: () => settingsStore.textColor,
  set: (value) => (settingsStore.textColor = value),
})

const primaryColor = computed({
  get: () => settingsStore.primaryColor,
  set: (value) => (settingsStore.primaryColor = value),
})

const progressColor = computed({
  get: () => settingsStore.progressColor,
  set: (value) => (settingsStore.progressColor = value),
})

const winColor = computed({
  get: () => settingsStore.winColor,
  set: (value) => (settingsStore.winColor = value),
})

const loseColor = computed({
  get: () => settingsStore.loseColor,
  set: (value) => (settingsStore.loseColor = value),
})

const isProfileModalVisible = ref(false)
const isConfigurationModalVisible = ref(false)

const playerInfo = ref<PlayerInformation | null>({
  lastMatchId: 0,
  mmr: {
    tier: {
      id: 0,
      name: '',
    },
    rr: 0,
    lastChange: 0,
    elo: 0,
    leaderboard_placement: 0,
  },
})

const openProfileModal = () => {
  isProfileModalVisible.value = true
}

const openConfigurationModal = () => {
  isConfigurationModalVisible.value = true
}

const generateRandomId = async () => {
  const leaderboardPlayers = await getTopLeaderboard()

  if (leaderboardPlayers.length > 0) {
    const randomIndex = Math.floor(Math.random() * leaderboardPlayers.length)
    riotId.value = leaderboardPlayers[randomIndex]
  } else {
    riotId.value = 'MAGICX#1337'
  }
  await getUserPuuid()
}

const checkKey = async () => {
  if (apiKey.value && apiKey.value.length > 40) {
    try {
      const status = await checkApiKey()
      if (!status) {
        toast.error('API key is invalid. Verify that the key is correct.')
      }
    } catch (error) {
      toast.error('Failed to validate API key. Please try again.')
      console.error(error)
    }
  } else {
    verifyApiKey.value = false
  }
}

const getUserPuuid = async () => {
  if (apiKey.value && apiKey.value.length > 40 && riotId.value) {
    try {
      const successGetPuuid = await getPuuidWithRegion()
      if (!successGetPuuid) {
        toast.error('Riot ID is invalid')
      } else toast.success('Uploading player data...')
      fetchPlayerInfo()
    } catch (error) {
      toast.error('Failed to get Riot ID. Please try again.')
      console.error(error)
    }
  } else if (apiKey.value || (apiKey.value && apiKey.value.length <= 40)) {
    toast.error('Verify that the API key and the Riot ID are correct.')
  }
}

const fetchPlayerInfo = async () => {
  playerInfo.value = await getInformation()
}

watch(backgroundSwitch, (newValue) => {
  if (!newValue) {
    progressSwitch.value = false
  }
})

onMounted(() => {
  settingsStore.userDataLoaded = false
  if (settingsStore.verifyApiKey && settingsStore.puuid) {
    fetchPlayerInfo()
  }
})
</script>

<template>
  <div class="editor">
    <div class="editor__body">
      <div key="form" class="editor__container">
        <HeaderEditor />
        <div class="editor__container__body">
          <SectionSettingsEditor :is-modal="true">
            <template #title>
              {{ $t('editor.profile.title') }}
            </template>
            <template #description>
              {{ $t('editor.profile.description') }}
            </template>
            <template #input>
              <Button class="editor__button" @click="openProfileModal">
                {{ $t('editor.profile.button') }}
              </Button>
            </template>
          </SectionSettingsEditor>
          <SectionSettingsEditor v-if="verifyApiKey && riotId" :is-modal="true">
            <template #title>
              {{ $t('editor.configuration.title') }}
            </template>
            <template #description>
              {{ $t('editor.configuration.description') }}
            </template>
            <template #input>
              <Button class="editor__button" @click="openConfigurationModal">
                {{ $t('editor.configuration.button') }}
              </Button>
            </template>
          </SectionSettingsEditor>
          <SectionSettingsEditor v-if="verifyApiKey && riotId">
            <template #title>
              {{ $t('editor.url.title') }}
            </template>
            <template #description>
              {{ $t('editor.url.description') }}
            </template>
            <template #input>
              <Input placeholder="Overlay URL" style="flex: 2" />
            </template>
            <template #footer>
              <p>{{ $t('editor.url.dimensions') }}</p>
            </template>
          </SectionSettingsEditor>
          <ui-modal v-model="isProfileModalVisible">
            <template #title>
              {{ $t('editor.profile.title') }}
            </template>
            <ModalSettingsEditor>
              <template #header>
                <h1 class="title">{{ $t('editor.profile.riotId.title') }}</h1>
                <p class="description">{{ $t('editor.profile.riotId.description') }}</p>
              </template>
              <template #input>
                <Input
                  v-model.lazy="riotId"
                  @blur="getUserPuuid"
                  placeholder="Riot ID"
                  style="flex: 2"
                />
              </template>
              <template #footer>
                <span class="under_description" @click="generateRandomId">
                  {{ $t('editor.profile.riotId.random') }}
                </span>
              </template>
            </ModalSettingsEditor>
            <ModalSettingsEditor>
              <template #header>
                <h1 class="title">{{ $t('editor.profile.hdevKey.title') }}</h1>
                <span class="description">
                  {{ $t('editor.profile.hdevKey.description') }}
                </span>
              </template>
              <template #input>
                <Input
                  v-model.lazy="apiKey"
                  @blur="checkKey"
                  placeholder="HDEV-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
                  style="flex: 2"
                />
              </template>
              <template #footer>
                <span class="under_description">
                  {{ $t('editor.profile.hdevKey.instruction-dis') }}
                </span>
              </template>
            </ModalSettingsEditor>
          </ui-modal>
          <ui-modal v-model="isConfigurationModalVisible">
            <template #title>
              <div style="display: flex; flex-direction: column; gap: 6px">
                <span>{{ $t('editor.configuration.title') }}</span>
                <span
                  @click="settingsStore.resetConfiguration()"
                  style="color: hsl(222, 5%, 62%); font-size: 0.875rem; cursor: pointer"
                >
                  {{ $t('editor.configuration.reset') }}
                </span>
              </div>
            </template>
            <ModalSettingsEditor>
              <template #header>
                <h1 class="title">{{ $t('editor.configuration.display.title') }}</h1>
                <p class="description">
                  {{ $t('editor.configuration.display.description') }}
                </p>
              </template>
              <template #options>
                <div class="item">
                  <span>
                    {{ $t('editor.configuration.display.items.background') }}
                  </span>
                  <Switch v-model="backgroundSwitch" />
                </div>
                <div class="item">
                  <span>
                    {{ $t('editor.configuration.display.items.progress') }}
                  </span>
                  <Switch v-model="progressSwitch" :disabled="!backgroundSwitch" />
                </div>
<!--                <div class="item">-->
<!--                  <span>-->
<!--                    {{ $t('editor.configuration.display.items.statistics') }}-->
<!--                  </span>-->
<!--                  <Switch v-model="statisticsSwitch" />-->
<!--                </div>-->
              </template>
            </ModalSettingsEditor>
            <ModalSettingsEditor>
              <template #header>
                <h1 class="title">{{ $t('editor.configuration.color.title') }}</h1>
                <p class="description">
                  {{ $t('editor.configuration.color.description') }}
                </p>
              </template>
              <template #options>
                <div class="item">
                  <span>
                    {{ $t('editor.configuration.color.items.background') }}
                  </span>
                  <ColorPicker v-model="backgroundColor" />
                </div>
                <div class="item">
                  <span>
                    {{ $t('editor.configuration.color.items.main') }}
                  </span>
                  <ColorPicker v-model="textColor" />
                </div>
                <div class="item">
                  <span>
                    {{ $t('editor.configuration.color.items.primary') }}
                  </span>
                  <ColorPicker v-model="primaryColor" />
                </div>
                <div class="item">
                  <span>
                    {{ $t('editor.configuration.color.items.progress') }}
                  </span>
                  <ColorPicker v-model="progressColor" />
                </div>
                <div class="item">
                  <span>
                    {{ $t('editor.configuration.color.items.win') }}
                  </span>
                  <ColorPicker v-model="winColor" />
                </div>
                <div class="item">
                  <span>
                    {{ $t('editor.configuration.color.items.lose') }}
                  </span>
                  <ColorPicker v-model="loseColor" />
                </div>
              </template>
            </ModalSettingsEditor>
          </ui-modal>
        </div>
      </div>
      <PreviewEditor :userDataLoaded="userDataLoaded">
        <Overlay
          v-if="verifyApiKey && userDataLoaded"
          :backgroundSwitch="backgroundSwitch"
          :progressSwitch="progressSwitch"
          :statisticsSwitch="statisticsSwitch"
          :backgroundColor="backgroundColor"
          :textColor="textColor"
          :primaryColor="primaryColor"
          :progressColor="progressColor"
          :winColor="winColor"
          :loseColor="loseColor"
          :PlayerInfo="playerInfo"
        />
      </PreviewEditor>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.title {
  font-weight: 600;
  font-size: calc(0.25 * 4.5rem);
}

.description {
  color: hsla(222deg 5% 62% / 1);
  font-size: 0.875rem;
  line-height: 1.5;

  display: flex;
  flex-direction: column;
}

.editor {
  width: 100%;
  height: 100%;
  background: hsl(0, 0%, 9%);
  border-radius: 8px;
  border: 1px solid hsla(222deg 6% 30% / 0.25);
  overflow: hidden;
  color: #fffbf5;

  h1,
  p {
    margin: 0;
  }

  .editor__body {
    display: flex;
    align-items: center;
    height: 100%;

    .editor__container {
      flex: 1;

      .editor__settings {
        padding: calc(0.25 * 6rem);
        border-bottom: 1px solid hsla(222deg 6% 30% / 0.25);
        display: flex;
        flex-direction: column;
        gap: 12px;

        &.modal,
        &.switch {
          flex-direction: row;
          justify-content: space-between;
          align-items: center;

          .reset {
            color: red;
            font-size: 12px;
            font-weight: 400;
          }
        }

        .editor__settings__options {
          border-top: 1px dashed hsla(222deg 6% 30% / 0.25);
        }

        .editor__input {
          display: flex;
          gap: 8px;
          align-items: center;

          .editor__button {
            border-radius: 5px;
            padding: 0.7rem 1.1rem;
            font-size: 0.75rem;
          }
        }

        .editor__settings__header {
          display: flex;
          flex-direction: column;
          gap: 12px;
        }

        .editor__settings__footer {
          p {
            color: hsl(222deg 3.53% 27.53%);
            font-size: 0.875rem;
          }
        }

        &:last-child {
          border-bottom: none;
        }
      }
    }
  }
}

.item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 0;

  &:first-child {
    margin-top: 15px;
  }
}

.under_description {
  color: rgb(0, 143, 253);
  font-size: 0.875rem;
  line-height: 1.5;
  cursor: pointer;
  transition: box-shadow 0.2s linear;
  box-shadow: none;
  width: fit-content;

  &:hover {
    box-shadow: 0 1px 0 rgb(0, 143, 253);
  }
}
</style>
