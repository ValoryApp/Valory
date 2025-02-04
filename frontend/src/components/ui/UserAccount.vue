<script setup lang="ts">

</script>

<template>
  <div class="user_account">
    <div class="avatar">
      <img width="40px" src="https://static-cdn.jtvnw.net/jtv_user_pictures/a917baec-006e-4ee8-a89a-6f8fda5b09a0-profile_image-300x300.png" alt="">
    </div>
  </div>
</template>

<style scoped lang="scss">
.user_account {
  background-color: #171717;
  border-radius: 999px;

  z-index: 999;
  border: 1px solid hsla(222, 6%, 30%, 0.25);

  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 12px;

  position: fixed;
  top: 30px;
  right: 30px;

  .avatar {
    display: inline-flex;
    align-items: center;
    justify-content: center;

    img {
      border-radius: 100%;
    }
  }
}
</style>