<script lang="ts" setup>
import Footer from '@/components/FooterItem.vue'
import IconBillCheck from '@/components/icons/IconBillCheck.vue'
import IconMagicStick from '@/components/icons/IconMagicStick.vue'
import IconPalette from '@/components/icons/IconPalette.vue'
import IconValory from '@/components/icons/IconValory.vue'
import Button from '@/components/ui/ButtonUI.vue'
import IconTwitch from "@/components/icons/IconTwitch.vue";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();

const redirectToAuth = () => {
  window.location.href = "http://localhost:8080/api/auth/twitch/login";
};
</script>

<template>
  <main>
    <div class="main__body">
      <div class="main__container">
        <p class="pretitle">{{ $t('landing.pretitle') }}</p>
        <div class="logo">
          <IconValory :size="60" />
          <h1 class="title">VALORY</h1>
        </div>
        <p class="description">{{ $t('landing.description') }}</p>
        <div class="features">
          <div class="feature">
            <IconPalette />
            <p>{{ $t('landing.features.first') }}</p>
          </div>
          <div class="feature">
            <IconBillCheck />
            <p>
              {{ $t('landing.features.second') }}
            </p>
          </div>
          <div class="feature">
            <IconMagicStick />
            <p>{{ $t('landing.features.third') }}</p>
          </div>
        </div>
        <div class="buttons">
          <Button :disabled="true" variant="outline">{{ $t('landing.buttons.first') }}</Button>
          <Button v-if="authStore.isAuthenticated" @click="$router.push('/configurator')">
            {{ $t('landing.buttons.second.auth') }}
          </Button>
          <Button v-else @click="redirectToAuth">
            {{ $t('landing.buttons.second.unauth') }}
            <IconTwitch color="#000" :size="15"/>
          </Button>
        </div>
      </div>
      <Footer />
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

.main__container {
  width: 70%;
}

.description {
  width: 70%;
}

.logo {
  display: flex;
  align-items: center;
  gap: 18px;
}

.title {
  margin: 0;
  font-family: 'Russo One', sans-serif;
  font-size: 3rem;
  font-weight: 600;
  letter-spacing: -0.025em;
  line-height: 1;
  background-color: #fffbf5;
  background-image: linear-gradient(to bottom, #fff, #ccc);
  background-size: 100%;
  background-repeat: repeat;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.description {
  margin: 0;
  font-size: 1.4rem;
  line-height: 1.2;
  font-weight: 700;
  background-color: #fffbf5;
  background-image: linear-gradient(to bottom, #fff, #ccc);
  background-size: 100%;
  background-repeat: repeat;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-align: center;
}

.pretitle {
  margin: 0;
  font-size: 10px;
  font-weight: 600;
  color: #00c4ff;
  padding: 6px 12px;
  background: rgba(0, 196, 255, 0.3);
  border: 1px solid #00c4ff;
  box-shadow: rgb(0 191 255 / 10%) 0 0 40px;
  border-radius: 999px;
  line-height: 1;
  animation: blink 2s linear infinite;
}

@keyframes blink {
  0% {
    box-shadow: rgb(0 191 255 / 3%) 0 0 40px;
  }
  50% {
    box-shadow: rgb(0 191 255 / 10%) 0 0 40px;
  }
  100% {
    box-shadow: rgb(0 191 255 / 3%) 0 0 40px;
  }
}

.features {
  display: grid;
  gap: 12px;
  width: 75%;

  .feature {
    display: flex;
    gap: 12px;
    align-items: center;
    line-height: 1.3;

    --icons-color: hsla(0, 0%, 100%, 1);
    stroke: var(--icons-color);
    fill: var(--icons-color);

    p {
      margin: 0;
      font-weight: 400;
      font-size: 1.1rem;
    }
  }
}

.buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
}
</style>
