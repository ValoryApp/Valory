<script lang="ts" setup>
import EditorMain from '@/components/ui/Editor/EditorMain.vue'
</script>

<template>
  <main>
    <div class="main__body">
      <div class="main__container">
        <EditorMain />
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
main {
  height: 100vh;
  width: 100vw;

  .main__body,
  .main__container {
    width: 100%;
    height: 100%;
  }
}
</style>
