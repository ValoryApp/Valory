<script setup lang="ts">
import { NAV_DATA } from "~/data/HeaderNav.data";

const moveTo = (container: string) => {
    const scrollTopOffset = document.getElementById(container)!.getBoundingClientRect().top + document.body.scrollTop - 25;

    window.scrollTo({
        top: scrollTopOffset,
        left: 0,
        behavior: "smooth",
    });
}
</script>

<template>
<header class="text-sm sticky top-0 bg-black/30 h-20 backdrop-blur-sm z-10 flex justify-center">
  <div class="container flex m-auto justify-between items-center">
    <div class="left">
      <ul class="flex justify-between items-center gap-6">
        <li
          v-for="nav in NAV_DATA"
          :key="nav.name"
          @click="moveTo(`${nav.point}`)"
          class="cursor-pointer  font-medium text-[#F2F2F2]/80 hover:text-[#F2F2F2] transition duration-150"
        >
          {{ nav.name }}
        </li>
      </ul>
    </div>
    <div class="logo absolute left-1/2">
      <IconsValory :size="30"/>
    </div>
    <div class="right">
      <UiButton class="text-sm" size="sm">
        Try for free
        <IconsSocialsTwitch :size="16" color="#000"/>
      </UiButton>
    </div>
  </div>
</header>
</template>

<style scoped lang="scss">

</style>