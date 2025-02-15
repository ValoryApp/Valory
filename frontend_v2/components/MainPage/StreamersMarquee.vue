<script setup lang="ts">
import { STREAMERS_DATA } from "~/data/Streamers.data";

const middleIndex = Math.floor(STREAMERS_DATA.length / 2);
const [firstRow, secondRow] = [STREAMERS_DATA.slice(0, middleIndex), STREAMERS_DATA.slice(middleIndex)];
</script>

<template>
  <div
    class="relative flex w-full flex-col items-center justify-center overflow-hidden rounded-lg bg-background md:shadow-xl"
  >
    <UiMarquee
      pause-on-hover
      class="[--duration:120s]"
    >
      <UiStreamersCard
        v-for="streamer in secondRow"
        :key="streamer.username"
        :img="streamer.img"
        :username="streamer.username"
        :followers="streamer.followers"
        :live="streamer.live"
        :verified="streamer.verified"
      />
    </UiMarquee>
    <UiMarquee
      reverse
      pause-on-hover
      class="[--duration:120s]"
    >
      <UiStreamersCard
        v-for="streamer in secondRow"
        :key="streamer.username"
        :img="streamer.img"
        :username="streamer.username"
        :followers="streamer.followers"
        :live="streamer.live"
        :verified="streamer.verified"
      />
    </UiMarquee>
    <div
      class="pointer-events-none absolute inset-y-0 left-0 w-1/3 bg-gradient-to-r from-white dark:from-background"
    ></div>
    <div
      class="pointer-events-none absolute inset-y-0 right-0 w-1/3 bg-gradient-to-l from-white dark:from-background"
    ></div>
  </div>
</template>