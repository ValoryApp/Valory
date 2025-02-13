import { defineStore } from 'pinia';
import router from "@/router";

interface UserState {
  isAuthenticated: boolean;
  token: string | null;
}

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    isAuthenticated: false,
    token: null,
  }),
  actions: {
    setToken(token: string) {
      this.token = token;
      this.isAuthenticated = true;
    },
    logout() {
      this.token = null;
      this.isAuthenticated = false;
      router.push('/')
    }
  },
});