<template>
  <div
    class="relative flex w-full flex-col items-center justify-center overflow-hidden rounded-lg bg-background md:shadow-xl"
  >
    <UiMarquee
      pause-on-hover
      class="[--duration:20s]"
    >
      <UiStreamersCard
        v-for="review in secondRow"
        :key="review.username"
        :img="review.img"
        :username="review.username"
        :followers="review.followers"
      />
    </UiMarquee>
    <UiMarquee
      reverse
      pause-on-hover
      class="[--duration:20s]"
    >
      <UiStreamersCard
        v-for="review in secondRow"
        :key="review.username"
        :img="review.img"
        :username="review.username"
        :followers="review.followers"
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

<script setup lang="ts">
const reviews = [
  {
    username: "@jack",
    followers: "1.2k",
    img: "https://avatar.vercel.sh/jack",
  },
  {
    username: "@jill",
    followers: "800",
    img: "https://avatar.vercel.sh/jill",
  },
  {
    username: "@john",
    followers: "2k",
    img: "https://avatar.vercel.sh/john",
  },
  {
    username: "@jane",
    followers: "3k",
    img: "https://avatar.vercel.sh/jane",
  },
  {
    username: "@jenny",
    followers: "100",
    img: "https://avatar.vercel.sh/jenny",
  },
  {
    username: "@james",
    followers: "99k",
    img: "https://avatar.vercel.sh/james",
  },
];

const firstRow = ref(reviews.slice(0, reviews.length / 2));
const secondRow = ref(reviews.slice(reviews.length / 2));
</script>