<script lang="ts" setup>
interface PreviewProps {
  userDataLoaded: boolean
}

defineProps<PreviewProps>()
</script>

<template>
  <div class="preview">
    <div class="preview__container">
      <div class="preview__component">
        <div v-if="userDataLoaded">
          <slot></slot>
        </div>
        <div v-else class="text">
          {{ $t('editor.preview.title') }}
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.preview {
  flex: 2;
  height: 100%;

  .preview__container {
    width: auto;
    height: 100%;
    padding: calc(0.25 * 6rem);
    background-image: url('/breeze.webp');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;

    &::before {
      content: '';
      height: 100%;
      width: 100%;
      position: absolute;
      background: rgb(0 0 0 / 0.2);
      backdrop-filter: blur(3px);
      z-index: 0;
    }

    .preview__component {
      width: auto;
      z-index: 1;

      .text {
        text-align: center;
      }
    }
  }
}

.slide-fade-enter-active {
  transition: all 0.2s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
