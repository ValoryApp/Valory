<script lang="ts" setup>
import Down from '@/components/icons/plus/down.vue'
import Down_plus from '@/components/icons/plus/down_plus.vue'
import Down_plusplus from '@/components/icons/plus/down_plusplus.vue'
import Up from '@/components/icons/plus/up.vue'
import Up_plus from '@/components/icons/plus/up_plus.vue'
import Up_plusplus from '@/components/icons/plus/up_plusplus.vue'
import type { PlayerInformation } from '@/services/overlayService'

interface OverlayProps {
  backgroundSwitch?: boolean
  progressSwitch?: boolean
  statisticsSwitch?: boolean
  backgroundColor?: string
  textColor?: string
  primaryColor?: string
  progressColor?: string
  winColor?: string
  loseColor?: string
  PlayerInfo: PlayerInformation | null
}

defineProps<OverlayProps>()

function getTierClass(tierId: number): string {
  if (tierId <= 2) return 'unranked'
  if (tierId >= 3 && tierId <= 5) return 'iron'
  if (tierId >= 6 && tierId <= 8) return 'bronze'
  if (tierId >= 9 && tierId <= 11) return 'silver'
  if (tierId >= 12 && tierId <= 14) return 'gold'
  if (tierId >= 15 && tierId <= 17) return 'platinum'
  if (tierId >= 18 && tierId <= 20) return 'diamond'
  if (tierId >= 21 && tierId <= 23) return 'ascendant'
  if (tierId >= 24 && tierId <= 26) return 'immortal'
  if (tierId === 27) return 'radiant'
  return 'unknown'
}
</script>

<template>
  <div v-if="PlayerInfo" class="overlay">
    <div
      :style="{
        backgroundColor: backgroundSwitch ? `${backgroundColor}99` : 'transparent',
        borderColor: backgroundSwitch ? 'rgba(255, 255, 255, 0.1)' : 'transparent',
      }"
      class="overlay__body"
    >
      <div class="overlay__content">
        <div class="overlay__left">
          <div class="rank__img">
            <img
              :class="[getTierClass(PlayerInfo.mmr.tier.id)]"
              :src="`/ranks/${PlayerInfo.mmr.tier.id}.webp`"
              width="55px"
            />
          </div>
        </div>
        <div class="overlay__right">
          <section class="overlay__rank">
            <div
              :style="{
                color: textColor,
              }"
              class="rank"
            >
              <span v-if="PlayerInfo.mmr.leaderboard_placement">
                {{ PlayerInfo.mmr.tier.name }} #{{ PlayerInfo.mmr.leaderboard_placement.rank }}
              </span>
              <span v-else>
                {{ PlayerInfo.mmr.tier.name }}
              </span>
            </div>
            <div
              :style="{
                color: primaryColor,
              }"
              class="elo_with_rr"
            >
              {{ PlayerInfo.mmr.elo }} elo - {{ PlayerInfo.mmr.rr }} RR
              <span
                v-if="PlayerInfo.mmr.lastChange != 0"
                class="plus"
                :style="{ color: PlayerInfo.mmr.lastChange > 0 ? '#27d6c4' : '#ff7986' }"
              >
                <span>
                  {{
                    PlayerInfo.mmr.lastChange > 0
                      ? `+${PlayerInfo.mmr.lastChange}`
                      : PlayerInfo.mmr.lastChange
                  }}
                </span>
                <div v-if="PlayerInfo.mmr.lastChange > 0">
                  <span v-if="PlayerInfo.mmr.lastChange <= 10">
                    <up />
                  </span>
                  <span v-else-if="PlayerInfo.mmr.lastChange <= 20">
                    <up_plus />
                  </span>
                  <span v-else-if="20 < PlayerInfo.mmr.lastChange">
                    <up_plusplus />
                  </span>
                </div>
                <div v-else>
                  <span v-if="-10 <= PlayerInfo.mmr.lastChange">
                    <down />
                  </span>
                  <span v-else-if="-20 < PlayerInfo.mmr.lastChange">
                    <down_plus />
                  </span>
                  <span v-else-if="-20 >= PlayerInfo.mmr.lastChange">
                    <down_plusplus />
                  </span>
                </div>
              </span>
            </div>
            <div class="last_matches">
              <span
                class="match"
                v-for="(result, index) in PlayerInfo.lastFiveMatches"
                :key="index"
                :class="{
                  win_match: result === 'Win',
                  lose_match: result === 'Lose',
                  draw_match: result === 'Draw',
                }"
              >
                <span class="match_text" v-if="result === 'Win'">W</span>
                <span v-else-if="result === 'Lose'">L</span>
                <span v-else-if="result === 'Draw'">D</span>
                <span v-else>-</span>
              </span>
              <span class="wl">{{ `${PlayerInfo.seasonWinrate}%` }}</span>
            </div>
          </section>
          <section
            :style="{
              display: statisticsSwitch ? 'flex' : 'none',
              color: primaryColor,
            }"
            class="overlay__stats"
          >
            <p>1.25 KD</p>
            <p>175 ADR</p>
            <p>369 ACS</p>
            <p>60% HS</p>
          </section>
        </div>
      </div>
      <div
        :style="{
          display: progressSwitch ? 'block' : 'none',
          backgroundColor: progressColor,
        }"
        class="progressbar"
      ></div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.overlay {
  display: flex;
  flex-direction: column;
  gap: 6px;
  position: relative;
  font-family: 'Inter', sans-serif;

  .logo {
    display: flex;
    align-items: center;
    gap: 5px;

    .text {
      line-height: 1;
      font-size: 14px;
      color: white;
      font-family: 'Russo One', sans-serif;
    }
  }

  .overlay__body {
    width: 370px;
    height: 113px;
    overflow: hidden;
    border-radius: 8px;
    background-color: rgba(7, 9, 14, 0.6);
    border: 2px solid;
    border-color: rgba(255 255 255 / 0.1);

    .overlay__content {
      width: 100%;
      height: 100%;
      position: relative;
      z-index: 1;
      display: flex;
      align-items: center;

      .overlay__left {
        margin-left: 6px;

        .rank__img {
          width: 82px;
          height: 106px;
          display: flex;
          align-items: center;
          justify-content: center;


          .iron, .unranked {
            filter: drop-shadow(0 0 20px rgba(148, 148, 148, 0.5));
          }

          .bronze {
            filter: drop-shadow(0 0 20px rgba(153, 110, 24, 0.5));
          }

          .silver {
            filter: drop-shadow(0 0 20px rgba(202, 210, 207, 0.5));
          }

          .gold {
            filter: drop-shadow(0 0 20px rgba(237, 211, 88, 0.5));
          }

          .platinum {
            filter: drop-shadow(0 0 20px rgba(83, 214, 222, 0.5));
          }

          .diamond {
            filter: drop-shadow(0 0 20px rgba(239, 150, 241, 0.5));
          }

          .ascendant {
            filter: drop-shadow(0 0 20px rgba(50, 166, 110, 0.5));
          }

          .immortal {
            filter: drop-shadow(0 0 20px rgba(176, 38, 59, 0.5));
          }

          .radiant {
            filter: drop-shadow(0 0 20px rgba(255, 255, 177, 0.5));
          }
        }
      }

      .overlay__right {
        display: flex;
        height: 100%;
        width: 100%;
        gap: 24px;
        align-items: center;

        .overlay__rank {
          display: flex;
          flex-direction: column;
          height: 100%;
          position: relative;
          justify-content: center;
          padding-left: 3px;
          gap: 6px;

          .rank {
            text-transform: uppercase;
            color: rgb(255 255 255);
            font-size: 18px;
            font-weight: 700;
            line-height: 1;
          }

          .elo_with_rr {
            color: rgb(190 190 191);
            font-size: 16px;
            font-weight: 400;
            display: flex;
            align-items: center;
            line-height: 1;
            gap: 6px;
          }

          span.plus {
            width: 20px;
            height: 12px;
            font-size: 10px;
            font-weight: 400;
            display: flex;
            gap: 3px;
            line-height: 1;
            align-items: center;
          }

          .last_matches {
            font-size: 12px;
            font-weight: 700;
            display: flex;
            gap: 4px;
            align-items: center;

            margin-top: 3px;

            .wl {
              color: rgb(190 190 191);
              font-weight: 500;
              font-size: 14px;
              margin-left: 5px;
            }

            .match {
              display: flex;
              width: 20px;
              height: 20px;
              border-radius: 4px;
              color: rgb(164, 164, 164);
              background: rgb(190 190 191);
              align-items: center;
              justify-content: center;
              filter: drop-shadow(0 0 10px rgba(190, 190, 191, 0.5));
            }

            .win_match {
              display: flex;
              width: 20px;
              height: 20px;
              border-radius: 4px;
              color: #00ffe3;
              background: #61c4b9;
              align-items: center;
              justify-content: center;
              filter: drop-shadow(0 0 10px rgba(97, 196, 185, 0.5));
            }

            .lose_match {
              display: flex;
              width: 20px;
              height: 20px;
              border-radius: 4px;
              color: #ff7986;
              background: #b95861;
              align-items: center;
              justify-content: center;
              filter: drop-shadow(0 0 10px rgba(185, 88, 97, 0.5));
            }

            .draw_match {
              display: flex;
              width: 20px;
              height: 20px;
              border-radius: 4px;
              color: #fff2bb;
              background: #cbb765;
              align-items: center;
              justify-content: center;
              filter: drop-shadow(0 0 10px rgba(203, 183, 101, 0.5));
            }
          }
        }

        .overlay__stats {
          display: none;
          flex-direction: column;
          gap: 6px;

          p {
            margin: 0;
            font-size: 14px;
            font-weight: 600;
            line-height: 1;
            color: #ececec;
          }
        }
      }
    }
  }

  .progressbar {
    width: 370px;
    height: 7px;
    left: 0;
    bottom: 0;
    position: absolute;
    background: rgba(0 255 226.67 / 0.9);
    border-bottom-right-radius: 8px;
    border-bottom-left-radius: 8px;
    z-index: 2;
    filter: drop-shadow(0 0 10px rgba(97, 196, 185, 0.5));
  }
}
</style>
