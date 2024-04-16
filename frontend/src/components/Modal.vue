<template>
  <dialog ref="modal" @click="closeIfClickedOut" @close="visible = false">
    <header
      class="justify-between flex p-4 text-2xl font-bold"
      v-if="visible"
      method="dialog"
      :class="{
        [props.classes]: props.classes,
      }"
    >
        <slot name="header""> TITLE </slot>
        <button type="button" class="font-normal text-2xl" @click="close">x</button>

    </header>

    <section
      class="flex p-4 text-xl"
      v-if="visible"
      method="dialog"
      :class="{
        [props.classes]: props.classes,
      }"
    >
      <slot name="body"> This is the default body! </slot>
    </section>
  </dialog>
</template>

<script setup lang="ts">
import { ref } from "vue";

const modal = ref<HTMLDialogElement>();
const visible = ref(false);

const props = defineProps({
  classes: {
    type: String,
    default: "",
  },
});

function closeIfClickedOut(e: Event) {
  if (e.currentTarget === e.target) {
    close();
  }
}

const open = () => {
  console.log("opening modal");
  modal.value?.showModal();
  visible.value = true;
};

function close() {
  modal.value?.close();
  visible.value = false;
}

defineExpose({
  open: open,
  close: close,
  visible,
});
</script>
