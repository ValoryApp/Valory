import { defineStore } from 'pinia';
import router from "@/router";

interface UserState {
  isAuthenticated: boolean;
  token: string | null;
}

export const useUserStore = defineStore('user', {
  state: (): UserState => {
    const token = document.cookie
      .split('; ')
      .find(row => row.startsWith('Authorization='))
      ?.split('=')[1] || null;
    return {
      isAuthenticated: token !== null,
      token: token,
    };
  },
  actions: {
    setToken(token: string) {
      this.token = token;
      this.isAuthenticated = true;
    },
    logout() {
      this.token = null;
      this.isAuthenticated = false;
      document.cookie = 'Authorization=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
      router.push('/');
    }
  },
});
