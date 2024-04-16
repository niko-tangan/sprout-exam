<template>
  <div
    id="sidebar"
    class="absolute flex h-screen w-full -translate-x-full flex-col justify-center bg-opacity-50 bg-gradient-to-r from-light-green to-green px-8 py-24 text-2xl transition-[transform] duration-300 md:w-1/4 md:justify-normal md:text-3xl lg:w-1/5 lg:text-5xl"
  >
    <IconClose class="absolute left-0 top-0 px-4 py-4"></IconClose>
    <h1 class="font-bold">Menu</h1>
    <ul class="">
      <li class="hover:text-orange">Employees</li>
      <li class="hover:text-orange">Profile</li>
      <li class="hover:text-orange">Logout</li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import IconClose from "./icons/IconClose.vue";
</script>
