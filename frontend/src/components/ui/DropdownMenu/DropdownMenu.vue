<script lang="ts" setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'

const props = defineProps<{
  size?: 'small' | 'medium' | 'large'
}>()

const isOpen = ref(false)
const dropdownRef = ref<HTMLElement | null>(null)
const isDropdownUp = ref(false)
const isDropdownRight = ref(false)

const toggleDropdown = () => {
  isOpen.value = !isOpen.value
  if (dropdownRef.value) {
    const rect = dropdownRef.value.getBoundingClientRect()
    const screenHeight = window.innerHeight
    const screenWidth = window.innerWidth

    isDropdownUp.value = rect.top > screenHeight / 2
    isDropdownRight.value = rect.right > screenWidth / 2
  }
}

const closeDropdown = (event: Event) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target as Node)) {
    isOpen.value = false
  }
}

const dropdownClass = computed(() => `dropdown-menu dropdown-menu--${props.size ?? 'medium'}`)

onMounted(() => {
  document.addEventListener('click', closeDropdown)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', closeDropdown)
})
</script>

<template>
  <div ref="dropdownRef" class="dropdown">
    <button class="dropdown-button" @click="toggleDropdown">
      <slot name="button"></slot>
    </button>
    <!-- Используем v-if для анимации -->
    <Transition name="slide-fade">
      <ul v-if="isOpen" :class="[dropdownClass, { 'dropdown-menu-up': isDropdownUp }, { 'dropdown-menu-right': isDropdownRight }]">
        <li v-if="$slots.title" class="title">
          <slot name="title"></slot>
        </li>
        <li v-if="$slots.title" class="separator"></li>
        <slot
          @click="
            () => {
              isOpen.value = false
              $emit('select', event.target.dataset.key)
            }
          "
        ></slot>
        <li v-if="$slots.footer" class="separator"></li>
        <li v-if="$slots.footer" class="footer">
          <slot name="footer"></slot>
        </li>
      </ul>
    </Transition>
  </div>
</template>

<style lang="scss">
.dropdown {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;

  &-button {
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;

    display: inline-flex;
    align-items: center;
    gap: 0.5rem;

    color: #fff;
    font-weight: 500;
  }

  &-menu {
    cursor: default;
    position: absolute;
    width: 224px;
    top: 100%;
    left: 0;
    background-color: hsl(0, 0%, 9%);
    border: 1px solid hsla(222, 6%, 30%, 0.25);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 6px;
    list-style: none;
    margin: 15px 0 0 0;
    padding: 4px;
    z-index: 1000;

    &--small {
      .title,
      .dropdown-item {
        padding: 4px 8px;
      }
    }

    &--medium {
      .title,
      .dropdown-item {
        padding: 8px 12px;
      }
    }

    &--large {
      .title,
      .dropdown-item {
        padding: 12px 16px;
      }
    }

    &.dropdown-menu-up {
      top: auto;
      bottom: 100%;
      margin: 0 0 15px 0;
    }

    &.dropdown-menu-right {
      left: auto;
      right: 0;
    }
  }

  .title {
    padding: 10px 12px;
    font-weight: 500;
  }

  .separator {
    height: 1px;
    background: hsla(222, 6%, 30%, 0.25);
    margin: 0.25rem -0.25rem;
  }

  .footer {
    font-size: 12px;
    color: rgb(134, 140, 148);
    padding: 12px;
    margin: -4px;
    background-color: #111;
    border-radius: 0 0 6px 6px;
  }

  &-item {
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 300;
    transition: background-color 0.2s ease;
    display: flex;
    align-items: center;
    gap: 12px;

    &.active,
    &:not(.title):hover {
      background-color: hsl(0, 0%, 12%);
    }
  }
}

.slide-fade-enter-active {
  transition: all 0.1s ease-in;
}

.slide-fade-leave-active {
  transition: all 0.1s ease-out;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
}
</style>
