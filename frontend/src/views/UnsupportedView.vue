<script lang="ts" setup>
import IconValory from '@/components/icons/IconValory.vue'
</script>

<template>
  <main>
    <div class="main__body">
      <div class="main__container">
        <IconValory color="#fff" :size="52" />
        <h1 class="title">Unsupported Device</h1>
        <div class="subtitle">
          <p>We're sorry, but this website is not supported on mobile devices at the moment.</p>
          <p>For the best experience, please access the site using a desktop browser.</p>
          <p>Thank you for your understanding!</p>
        </div>
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
body {
  background: #fa4454 !important;
}

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

.title {
  margin: 0;
  font-weight: bold;
  font-size: 34px;
  text-transform: uppercase;
  text-align: center;
}

.subtitle {
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 75%;
  position: relative;
  top: -20px;
  margin-top: 1rem;

  p {
    text-align: center;
    margin: 0;
    font-weight: 600;
    font-size: 18px;
    color: #ffff;
  }
}
</style>
