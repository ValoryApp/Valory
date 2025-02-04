<script lang="ts" setup>
import UiButton from '@/components/ui/ButtonUI.vue'
import { ArrowLeftIcon } from '@untitledui-icons/vue/solid'
</script>

<template>
  <main>
    <div class="main__body">
      <div class="main__container">
        <img alt="" class="s404" src="/404.png" />
        <h1 class="title">Whooops, this page is gone</h1>
        <p class="subtitle">This page is missing or you wrote the link incorrectly.</p>
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
main {
  flex: 1;
  display: flex;
  place-items: center;
  justify-content: center;
  max-width: 1280px;
  margin: 0 auto;

  .main__body {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;

    .main__container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.8rem;

      .btn {
        $btn-text-color: #fffbf5;
        align-items: center;
        background: #fff;
        border: none;
        border-radius: 0.75rem;
        color: $btn-text-color;
        display: flex;
        gap: 0.75rem;
        height: 3.5rem;
        padding: 0 1.5rem;
        font-weight: 600;
        font-size: 1.125rem;
        transition: all 0.2s;
        text-decoration: none;

        &:hover {
          background: #fff;
          cursor: pointer;
        }

        &:active {
          background: #fff;
        }
      }

      .footer {
        opacity: 0.5;
        font-size: 0.875rem;
        font-weight: 300;
      }
    }
  }
}

.s404 {
  filter: drop-shadow(0 0 100px #ff0016);
  width: 100%;
  margin-bottom: 20px;
}

.title {
  margin: 0;
  font-weight: bold;
  font-size: 34px;
}

.subtitle {
  margin: 0;
  font-weight: 300;
  font-size: 15px;
  color: #9f9f9f;
  position: relative;
  top: -20px;
}

svg {
  width: 15px;
}

button {
  margin-top: 15%;
}
</style>
