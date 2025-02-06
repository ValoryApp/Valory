<script setup lang="ts">
import LogoutIcon from '@/components/icons/LogoutIcon.vue'
import SettingsIcon from '@/components/icons/SettingsIcon.vue'
import SupportIcon from '@/components/icons/SupportIcon.vue'
import DropdownMenu from '@/components/ui/DropdownMenu/DropdownMenu.vue'
import DropdownMenuItem from '@/components/ui/DropdownMenu/DropdownMenuItem.vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
</script>

<template>
  <div class="user_menu">
    <DropdownMenu size="medium">
      <template #button>
        <div class="user_account">
          <div class="avatar">
            <img
              width="40px"
              src="https://static-cdn.jtvnw.net/jtv_user_pictures/a917baec-006e-4ee8-a89a-6f8fda5b09a0-profile_image-300x300.png"
              alt=""
            />
          </div>
        </div>
      </template>
      <template #title>
        <span>Hi, Username!</span>
      </template>
      <DropdownMenuItem>
        <SettingsIcon :size="16" />
        Settings
      </DropdownMenuItem>
      <DropdownMenuItem>
        <SupportIcon :size="16" />
        Support
      </DropdownMenuItem>
      <DropdownMenuItem @click="authStore.logout()">
        <LogoutIcon :size="16" />
        Logout
      </DropdownMenuItem>
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

  transition: 0.2s all;

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
