import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export const openLink = (url: string) => {
  window.open(url, '_blank');
};

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export type ObjectValues<T> = T[keyof T];