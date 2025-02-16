<script setup lang="ts">
  import useConfetti from "~/composables/useConfetti";
  import Sparkles from "~/components/Ui/Sparkles.vue";

  function randomInRange(min: number, max: number) {
    return Math.random() * (max - min) + min;
  }
  const triggerConfetti = () => {
    const duration = 5 * 1000;
    const animationEnd = Date.now() + duration;
    const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };
    const interval: NodeJS.Timeout = setInterval(function () {
      const timeLeft = animationEnd - Date.now();

      if (timeLeft <= 0) {
        return clearInterval(interval);
      }

      const particleCount = 50 * (timeLeft / duration);
      useConfetti({
        ...defaults,
        particleCount,
        origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 },
      });
      useConfetti({
        ...defaults,
        particleCount,
        origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 },
      });
    }, 250);
  };
</script>

<template>
  <section class="relative h-dvh flex justify-between items-center mt-[-5rem]">
    <div class="flex flex-col gap-9 items-start justify-center">
      <Sparkles :colors="{ first: '#ffffff', second: '#ffffff' }" :sparkles-count="5">
        <span
          @click="triggerConfetti()"
          class="
          flex gap-2 items-center py-1 pl-2 pr-3 bg-[#7289DA]/25 rounded-xl
          border border-white/10 text-xs font-semibold cursor-pointer
          hover:bg-[#7289DA]/40 transition duration-150
          drop-shadow-[0_0_20px_rgba(0,59,255,1)]"
          v-wave
        >
          <IconsSocialsDiscord :size="16"/>
          {{ $t('main.discord') }}
        </span>
      </Sparkles>
      <span class="text-5xl font-black uppercase whitespace-pre-line">
        {{ $t('main.title') }}
      </span>
      <span class="text-base text-[#CECECE] whitespace-pre-line">
        {{ $t('main.subtitle') }}
      </span>
      <span class="flex gap-3">
        <UiButton>
          {{ $t('main.buttons.first') }}
          <IconsStart :size="16" color="#000"/>
        </UiButton>
        <UiButton variant="ghost">
          {{ $t('main.buttons.second') }}
          <IconsStars :size="16"/>
        </UiButton>
      </span>
    </div>
    <div class="
      before:content-[''] before:absolute before:w-[400px]
      before:h-[400px]
      before:right-[-30px]
      before:bottom-[18rem]
      before:rounded-full before:pointer-events-none
      before:bg-[#A80026]/40
      before:blur-[200px]
      before:-z-10"
    >
      <img src="/images/ValoryLogo3D.webp" height="321" alt="Valory 3D"/>
    </div>
  </section>
</template>