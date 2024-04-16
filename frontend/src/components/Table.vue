<template>
  <div class="space-around flex flex-row justify-between py-5 pl-4">
    <IconHamburger></IconHamburger>
    <h1 class="text-center text-xl font-bold md:text-3xl">{{ title }}</h1>
    <button
      type="button"
      @click="showAdd()"
      class="mb-2 me-2 rounded-lg bg-green px-5 py-2.5 text-sm font-medium text-white hover:bg-white hover:text-green hover:ring-4 hover:ring-green"
    >
      Add
    </button>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-sm md:text-base lg:text-lg">
      <thead
        class="bg-green text-sm uppercase text-white md:text-base lg:text-lg"
      >
        <tr>
          <th class="px-4 py-2">
            <input type="checkbox" id="" class="accent-white" />
          </th>
          <th
            v-for="field in fields"
            :key="field.key"
            class="px-4 py-2 font-bold"
          >
            {{ field.label }}
          </th>
          <th class="font-bold">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id" class="border-b border-green">
          <td class="px-4 py-2">
            <input type="checkbox" id="" class="accent-green" />
          </td>
          <td v-for="key in displayedFieldKeys" class="px-4 py-2">
            {{ item[key] }}
          </td>
          <td class="px-4 py-2">
            <button
              type="button"
              @click="showEdit(item)"
              class="mb-2 me-2 rounded-lg bg-green px-5 py-2.5 text-sm font-medium text-white hover:bg-white hover:text-green hover:ring-4 hover:ring-green"
            >
              Edit
            </button>
            <button
              type="button"
              @click="showDelete(item.id)"
              class="bg-red-500 hover:text-red-500 hover:ring-red-500 mb-2 me-2 rounded-lg px-5 py-2.5 text-sm font-medium text-white hover:bg-white hover:ring-4"
            >
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <Modal ref="addModal">
    <template #header>Create {{ title }}</template>
    <template #body>
      <slot name="createForm"></slot>
    </template>
  </Modal>
  <Modal ref="editModal">
    <template #header>Edit {{ title }}</template>
    <template #body>
      <slot name="editForm" v-bind="selectedItem"></slot>
    </template>
  </Modal>
  <Modal ref="deleteModal">
    <template #header>Delete {{ title }}</template>
    <template #body>
      Are you sure you want to delete this?
      <button @click="deleteRow()">Yes</button>
      <button @click="closeDelete">No</button>
    </template>
  </Modal>
</template>

<script setup lang="ts">
import IconHamburger from "./icons/IconHamburger.vue";
import Modal from "./Modal.vue";
import { computed, ref, getCurrentInstance } from "vue";
import type { PropType } from "vue";
import axios from "axios";

const addModal = ref<InstanceType<typeof Modal>>();
const editModal = ref<InstanceType<typeof Modal>>();
const deleteModal = ref<InstanceType<typeof Modal>>();

const selectedRow = ref(-1);
let selectedItem: object;

function showEdit(item: object) {
  editModal.value?.open();
  selectedItem = item;
}

function showDelete(id: number) {
  deleteModal.value?.open();
  selectedRow.value = id;
}

function deleteRow() {
  axios
    .delete(`http://localhost:5000/employees/${selectedRow.value}/`)
    .then((response) => {
      console.log("Response:", response.data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
  closeDelete();
}

function closeDelete() {
  deleteModal.value?.close();
}

function showAdd() {
  addModal.value?.open();
}

interface TableField {
  key: string;
  label: string;
}

const props = defineProps({
  fields: {
    type: Array as PropType<TableField[]>,
    default: () => [],
  },
  path: {
    type: String,
    default: "http://localhost:5000/employees/",
  },
  title: {
    type: String,
    default: "Employees",
  },
});

const items = await fetch(props.path).then((r) => r.json());

const displayedFieldKeys = computed(() => {
  return Object.entries(props.fields).map(([_key, value]) => value.key);
});
</script>
