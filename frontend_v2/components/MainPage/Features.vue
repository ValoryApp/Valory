<script setup lang="ts">

</script>

<template>
<section id="features" class="container flex flex-col gap-10 justify-center items-center">
  <div class="flex flex-col gap-6 items-center">
    <span class="font-bold uppercase text-xs bg-gradient-to-r from-[#5AB2F7] to-[#12CFF3] text-transparent bg-clip-text inline-block">
      Features
    </span>
    <span class="uppercase text-2xl font-bold">
      Everything You Need to Elevate Your Stream
    </span>
    <span class="text-center text-[#CECECE] text-base font-normal">
      Packed with powerful tools, our app makes it effortless to display and
      <br>customize your Valorant stats. From seamless setup to full
      <br>personalization, we’ve got everything to make your stream shine.
    </span>
  </div>
  <div class="grid grid-cols-[repeat(2,1fr)] grid-rows-[repeat(2,1fr)] gap-4 justify-items-stretch">
    <div
      class="row-span-1 col-span-2 w-auto flex flex-row gap-4 self-stretch content-stretch rounded-2xl border border-white/10"
      style="background: radial-gradient(328.59% 136.88% at 98.5% -23.88%, rgba(0, 143, 253, 0.20) 0%, rgba(0, 0, 0, 0.00) 100%), radial-gradient(246.95% 120.87% at 15.83% 173.23%, #008FFD 0%, rgba(0, 0, 0, 0.00) 100%), #000A11;"
    >
      <div class="flex p-12 flex-col justify-center items-start gap-5 content-stretch">
        <span class="text-xl font-medium">
          Compatible with Popular Streaming Software
        </span>
        <span class="text-base font-normal text-[#CECECE]">
          We support all major streaming platforms,
          <br>including OBS Studio, Streamlabs, XSplit, and more.
          <br>Integration is quick and easy, ensuring your stats
          <br>are live without technical hassle.
        </span>
      </div>
      <div class="">
        <img src="/images/features.png" alt="Features" width="327">
      </div>
    </div>
    <div
      class="flex flex-col px-12 pt-12 pb-48 rounded-2xl border border-white/10"
    >
      <div class="flex flex-col gap-5 pr-5">
        <span class="text-xl font-medium">
          Design Reflects Your Style
        </span>
        <span class="text-[#CECECE] text-base font-normal">
          Make your stream yours!
          <br>Customize overlay colors and layout to match
          <br>your unique style and stand out with
          <br>a professional look.
        </span>
      </div>
    </div>
    <div
      class="flex flex-col px-12 pt-12 pb-48 rounded-2xl border border-white/10"
    >
      <div class="flex flex-col gap-5 pr-5">
        <span class="text-xl font-medium">
          Set It and Forget It
        </span>
        <span class="text-[#CECECE] text-base font-normal">
          Enjoy a hassle-free experience!
          <br>Once you set up the overlay, the app works
          <br>automatically to display your live stats,
          <br>ensuring everything stays updated
          <br>without requiring manual adjustments.
        </span>
      </div>
    </div>
  </div>
</section>
</template>

<style scoped>

</style>