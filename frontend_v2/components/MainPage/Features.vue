<template>
<section id="features" class="container flex flex-col gap-10 justify-center items-center">
  <div class="flex flex-col gap-6 items-center">
    <span class="font-bold uppercase text-xs bg-gradient-to-r from-[#5AB2F7] to-[#12CFF3] text-transparent bg-clip-text inline-block">
      {{ $t('features.category') }}
    </span>
    <span class="uppercase text-2xl font-bold text-center">
      {{ $t('features.title') }}
    </span>
    <span class="text-center text-[#CECECE] text-base font-normal whitespace-pre-line">
      {{ $t('features.subtitle') }}
    </span>
  </div>
  <div class="grid grid-cols-[repeat(2,1fr)] grid-rows-[repeat(2,1fr)] gap-4 justify-items-stretch">
    <div
      class="row-span-1 col-span-2 w-auto flex flex-row gap-4 self-stretch content-stretch rounded-2xl border border-white/10"
      style="background: radial-gradient(328.59% 136.88% at 98.5% -23.88%, rgba(0, 143, 253, 0.20) 0%, rgba(0, 0, 0, 0.00) 100%), radial-gradient(246.95% 120.87% at 15.83% 173.23%, #008FFD 0%, rgba(0, 0, 0, 0.00) 100%), #000A11;"
    >
      <div class="flex p-12 flex-col justify-center items-start gap-5 content-stretch">
        <span class="text-xl font-medium whitespace-pre-line">
          {{ $t('features.blocks.first.title') }}
        </span>
        <span class="text-base font-normal text-[#CECECE] whitespace-pre-line">
          {{ $t('features.blocks.first.description') }}
        </span>
      </div>
      <img src="/images/features.webp" alt="Features" class="h-auto">
    </div>
    <div
      class="flex flex-col px-12 pt-12 rounded-2xl border border-white/10"
    >
      <div class="flex flex-col gap-5 pr-5">
        <span class="text-xl font-medium">
          {{ $t('features.blocks.second.title') }}
        </span>
        <span class="text-[#CECECE] text-base font-normal whitespace-pre-line">
          {{ $t('features.blocks.second.description') }}
        </span>
      </div>
      <img src="/images/configuration.webp" alt="configuration">
    </div>
    <div
      class="flex flex-col px-12 pt-12 pb-48 rounded-2xl border border-white/10"
    >
      <div class="flex flex-col gap-5 pr-5">
        <span class="text-xl font-medium">
          {{ $t('features.blocks.third.title') }}
        </span>
        <span class="text-[#CECECE] text-base font-normal whitespace-pre-line">
          {{ $t('features.blocks.third.description') }}
        </span>
      </div>
    </div>
  </div>
</section>
</template>