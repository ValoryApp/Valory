<template>
  <div id="streamers" class="container m-auto flex flex-col gap-10 items-center">
    <div class="flex flex-col gap-6 items-center">
      <span class="font-bold uppercase text-xs bg-gradient-to-r from-[#FF930F] to-[#FFF95B] text-transparent bg-clip-text inline-block">
        {{ $t('streamers.category') }}
      </span>
      <span class="uppercase text-2xl font-bold text-center">
        {{ $t('streamers.title') }}
      </span>
      <span class="text-center text-[#CECECE] text-base font-normal whitespace-pre-line">
        {{ $t('streamers.subtitle') }}
      </span>
      <div class="container">
        <MainPageStreamersMarquee/>
      </div>
    </div>
    <div></div>
  </div>
</template>
