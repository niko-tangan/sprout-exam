<template>
  <div @click="toggleMenu" class="">
    <button class="aspect-square w-[25px] text-2xl hover:text-orange">X</button>
  </div>
</template>

<script setup lang="ts">
function toggleMenu(e: Event) {
  let sidebar = document.getElementById("sidebar");
  sidebar?.classList.toggle("-translate-x-full");
}
</script>
