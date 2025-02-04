<script setup lang="ts">
import DropdownMenuItem from "@/components/ui/DropdownMenu/DropdownMenuItem.vue";
import DropdownMenu from "@/components/ui/DropdownMenu/DropdownMenu.vue";
</script>

<template>
  <div class="user_menu">
    <DropdownMenu size="medium">
      <template #button>
        <div class="user_account">
          <div class="avatar">
            <img width="40px" src="https://static-cdn.jtvnw.net/jtv_user_pictures/a917baec-006e-4ee8-a89a-6f8fda5b09a0-profile_image-300x300.png" alt="">
          </div>
        </div>
      </template>
      <template #title>
        <span>Hi, Username!</span>
      </template>
      <DropdownMenuItem>Settings</DropdownMenuItem>
      <DropdownMenuItem>Feedback</DropdownMenuItem>
      <DropdownMenuItem>About</DropdownMenuItem>
      <DropdownMenuItem>Support</DropdownMenuItem>
      <DropdownMenuItem>Logout</DropdownMenuItem>
      <template #footer>
        <span>© 2023-2025 VALORY</span>
      </template>
    </DropdownMenu>
  </div>
</template>

<style scoped lang="scss">
.user_menu {
  position: fixed;
  top: 30px;
  right: 30px;
  z-index: 999;
}

.user_account {
  background-color: #171717;
  border-radius: 999px;


  box-shadow: 0 0 0 1px hsla(222, 6%, 30%, 0.25);

  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 12px;

  transition: .2s all;

  &:hover {
    box-shadow: 0 0 0 4px hsla(222, 6%, 30%, 0.6);
  }

  &:focus {
    box-shadow: 0 0 0 4px hsla(222, 6%, 30%, 0.8);
  }

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