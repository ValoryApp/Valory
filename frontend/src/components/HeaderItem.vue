<script setup lang="ts">
import IconValory from '@/components/icons/IconValory.vue'
import LanguageSwitcher from '@/components/ui/LanguageSwitcher.vue'
import UserAccount from "@/components/ui/UserAccount.vue";
</script>

<template>
  <header>
    <div class="highlight"></div>
    <div class="header">
      <div class="left">
        <ul class="nav">
          <RouterLink to="/">{{ $t('nav.home') }}</RouterLink>
          <RouterLink to="/configurator">{{ $t('nav.configuration') }}</RouterLink>
        </ul>
      </div>
      <div class="center">
        <IconValory :size="36" />
      </div>
      <div class="right">
        <LanguageSwitcher />
        <UserAccount />
      </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
header {
  backdrop-filter: blur(10px);

  position: fixed;
  top: 0;
  left: 0;
  right: 0;

  display: flex;
  align-items: center;
  justify-content: center;

  margin: 0 auto;
  padding: 30px 0;
  z-index: 1;

  .highlight {
    position: fixed;
    top: -450px;
    left: 30%;
    width: 743px;
    height: 207px;
    flex-shrink: 0;

    border-radius: 743px;
    background: #f3465a;

    filter: blur(235.5px);
  }

  .header {
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 60vw;

    .left {
      position: relative;
      left: 0;

      .nav {
        display: inline-flex;
        list-style: none;
        align-items: flex-start;
        gap: 0.5rem;
        margin: 0;
        padding: 0;

        a {
          color: #fff;
          text-decoration: none;

          font-size: 16px;
          font-style: normal;
          font-weight: 500;
          line-height: normal;

          transition: font-weight 0.2s;

          padding: 0.75rem 0.5rem;

          &.router-link-active,
          &.router-link-exact-active {
            font-weight: 600;
          }
        }
      }
    }

    .center {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);

      display: flex;
      align-items: center;
    }

    .right {
      position: relative;
      right: 0;

      display: inline-flex;
      gap: 12px;
      align-items: center;
    }
  }
}
</style>
