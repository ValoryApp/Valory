<script lang="ts" setup>
import EditorMain from '@/components/ui/Editor/EditorMain.vue'
import UserAccount from "@/components/ui/UserAccount.vue";
import IconValory from "@/components/icons/IconValory.vue";
</script>

<template>
  <main>
    <UserAccount v-if="$route.meta.showHeader" />
    <IconValory class="logo" :size="36" v-if="$route.meta.showHeader" @click="$router.push('/')"/>
    <div class="main__body">
      <div class="main__container">
        <EditorMain />
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
.logo {
  cursor: pointer;

  position: fixed;
  top: 30px;
  left: 24px;
}

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
