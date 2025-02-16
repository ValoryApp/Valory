<script setup lang="ts">

const metaImg = 'images/meta.webp'
const metaTitle = 'Stream Overlays - VALORY'
const metaDescription = 'Elevate your Valorant streaming experience by using VALORY. Keep your viewers engaged and informed, and showcase your progress in the game while making your stream more captivating and memorable!'

useSeoMeta({
  title: metaTitle,
  description: metaDescription,
  ogTitle: metaTitle,
  ogDescription: metaDescription,
  ogImage: metaImg,
  twitterCard: 'summary_large_image',
  twitterTitle: metaTitle,
  twitterDescription: metaDescription,
  twitterImage: metaImg,
  author: 'MAGICX, misha@valory.su',
  keywords:
    'valory, valory tracker, valory obs, valory obs tracker, valory overlay, ' +
    'obs tracker, obs overlay, valory valorant, valorant, valorant obs, ' +
    'valorant tracker, valorant overlay, valory obs overlay,' +
    ' valory valorant overlay, valory valorant obs, valorant tracker, ' +
    'valorant tracker, valorant stream overlay, valorant player tracker, ' +
    'custom display for valorant, valorant leaderboard overlay, ' +
    'radiant rank tracker, winrate tracker for streamers, ' +
    'valorant win/lose display, custom valorant leaderboard, ' +
    'valorant obs overlay, radiant players tracker, valorant stream ' +
    'custom display, streamer winrate overlay, win/lose tracker for valorant, ' +
    'valorant rank display, valorant custom rank overlay, valorant stream ' +
    'leaderboard, radiant rank winrate, streamer valorant overlay, ' +
    'winrate display for valorant players',
});
</script>

<template>
  <NuxtLayout>
    <NuxtPage/>
  </NuxtLayout>
</template>