<script lang="ts" setup>
import IconClose from '@/components/icons/IconClose.vue'
import { onBeforeUnmount, ref, watch } from 'vue'

interface ModalProps {
  modelValue: boolean
  title?: string
  closeOnOverlay?: boolean
}

type EmitFn = (event: 'update:modelValue', value: boolean) => void

const props = defineProps<ModalProps>()

const emit = defineEmits<EmitFn>()

const isVisible = ref(props.modelValue)

watch(
  () => props.modelValue,
  (newValue) => {
    isVisible.value = newValue
  },
)

const close = () => {
  const overlay = document.querySelector('.modal-overlay')
  const content = document.querySelector('.modal-content')

  overlay?.classList.add('fade-out')
  content?.classList.add('fade-out')

  setTimeout(() => {
    isVisible.value = false
    emit('update:modelValue', false)
  }, 300)
}

onBeforeUnmount(() => {
  isVisible.value = false
})
</script>

<template>
  <Teleport to="body">
    <div v-if="isVisible" class="modal-overlay" @click="close">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h1 class="title">
            <slot name="title">{{ props.title }}</slot>
          </h1>
          <button class="close-button" @click="close">
            <IconClose :width="12" />
          </button>
        </div>
        <div class="modal-body">
          <slot />
        </div>
      </div>
    </div>
  </Teleport>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  color: #fffbf5;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  opacity: 0;
  animation: fadeIn 0.3s forwards;
  backdrop-filter: blur(5px);
}

.modal-content {
  background: hsl(0, 0%, 9%);
  border-radius: 8px;
  border: 1px solid hsla(222deg 6% 30% / 0.25);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);

  width: 100%;
  max-width: 575px;
  height: fit-content;
  max-height: 90%;
  transform: scale(0.9);
  animation: scaleUp 0.1s forwards;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid hsla(222, 6%, 30%, 0.25);
  display: flex;
  justify-content: space-between;
  align-items: flex-start;

  .title {
    font-weight: 600;
    margin: 0;
    font-size: calc(0.25 * 4.5rem);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 5px;
  }
}

.close-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: auto;
  padding: 0;
  line-height: 0;

  background: none;
  border: none;
  color: #fffbf5;
  font-size: 1.5rem;
  cursor: pointer;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes scaleUp {
  0% {
    transform: scale(0.9);
  }
  100% {
    transform: scale(1);
  }
}

.modal-overlay.fade-out {
  animation: fadeOut 0.1s forwards;
}

.modal-content.fade-out {
  animation: scaleDown 0.1s forwards;
}

@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

@keyframes scaleDown {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(0.9);
  }
}
</style>
