<script setup lang="ts">
import { FOOTER_NAV_PRODUCT_DATA } from "~/data/FooterNav.data";
import { openLink } from "~/utils/utils";
</script>
<template>
  <footer class="container m-auto flex flex-col gap-10 mt-16">
    <div class="flex justify-between">
      <div class="flex flex-col gap-8">
        <IconsValory :size="25"/>
        <span class=" font-normal">
          Showcase your Valorant stats live and keep your
          <br>audience engaged with every headshot and clutch!
        </span>
        <div class="flex gap-4">
          <UiButton @click="openLink('https://github.com/ValoryApp/Valory')" variant="ghost" class="p-2 h-fit cursor-pointer">
            <IconsSocialsGithub :size="20"/>
          </UiButton>
          <UiButton @click="openLink('https://twitch.tv/MAGICXcmd')" variant="ghost" class="p-2 h-fit cursor-pointer">
            <IconsSocialsTwitch :size="20"/>
          </UiButton>
          <UiButton @click="openLink('https://discord.gg/valory')" variant="ghost" class="p-2 h-fit cursor-pointer">
            <IconsSocialsDiscord :size="20"/>
          </UiButton>
          <UiButton @click="openLink('https://t.me/magicxcmd')" variant="ghost" class="p-2 h-fit cursor-pointer">
            <IconsSocialsTelegram :size="20"/>
          </UiButton>
          <UiButton @click="openLink('https://www.donationalerts.com/r/haxgun')" variant="ghost" class="p-2 h-fit cursor-pointer">
            <IconsDonation color="#FA4454" :size="20"/>
          </UiButton>
        </div>
      </div>
      <div class="flex flex-row gap-32 justify-end">
        <div
          v-for="nav in FOOTER_NAV_PRODUCT_DATA"
          :key="nav.title"
          class="flex flex-col gap-2"
        >
          <span class="font-bold text-base">
            {{ nav.title }}
          </span>
          <ul class="flex flex-col gap-2">
            <NuxtLink
              v-for="children in nav.childrens"
              :key="children.name"
              :to="children.url"
              class="font-normal text-base text-[#A9A9A9] hover:text-[#F2F2F2] transition duration-150"
            >
              {{ children.name }}
            </NuxtLink>
          </ul>
        </div>
      </div>
    </div>
    <div class="flex py-10 items-center justify-between border-t border-white/20">
      <span class="text-normal">Valory © All rights reserved</span>
      <span class="text-normal">Made with ❤️ on 🌎 Earth</span>
    </div>
  </footer>
</template>