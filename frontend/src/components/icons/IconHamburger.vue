<template>
  <div @click="toggleMenu" class="">
    <svg
      id="hamburgerButton"
      xmlns="http://www.w3.org/2000/svg"
      class="h-8 w-8"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M4 6h16M4 12h16M4 18h16"
      />
    </svg>
  </div>
</template>

<script setup lang="ts">
function toggleMenu(e: Event) {
  let sidebar = document.getElementById("sidebar");
  sidebar?.classList.toggle("-translate-x-full");
}
</script>
