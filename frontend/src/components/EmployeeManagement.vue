<script setup lang="ts">
import Table from "./Table.vue";
import Sidebar from "./Sidebar.vue";
import { ref, getCurrentInstance } from "vue";
import axios from "axios";

const employeeFields = ref([
  { key: "id", label: "ID" },
  { key: "first_name", label: "First Name" },
  { key: "last_name", label: "Last Name" },
  { key: "email", label: "Email" },
]);

const emit = defineEmits<{
  showModal: [selector: string];
  closeModal: [selector: string];
}>();

function createEmployee(submitEvent: any) {
  let form_data = submitEvent.target.elements;

  let requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      first_name: form_data.firstName.value,
      last_name: form_data.lastName.value,
      email: form_data.email.value,
    }),
  };
  fetch("http://localhost:5000/employees/", requestOptions)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
}

function editEmployee(submitEvent: any) {
  let form_data = submitEvent.target.elements;

  let requestOptions = {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      first_name: form_data.firstName.value,
      last_name: form_data.lastName.value,
      email: form_data.email.value,
    }),
  };
  fetch(
    `http://localhost:5000/employees/${form_data.employeeId.value}/`,
    requestOptions,
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
}
</script>

<template>
  <Main class="flex font-josefin">
    <Sidebar />
    <div class="w-full">
      <Suspense>
        <Table
          title="Employees"
          path="http://localhost:5000/employees"
          :fields="employeeFields"
        >
          <template #createForm>
            <form @submit.prevent="createEmployee">
              <input type="hidden" name="employeeId" id="employeeId" />
              <div class="flex flex-col">
                <label for="firstName">First Name</label>
                <input
                  class="mb-4 outline outline-1 outline-green"
                  type="text"
                  name="firstName"
                  id="firstName"
                />
                <label for="lastName">Last Name</label>
                <input
                  class="mb-4 outline outline-1 outline-green"
                  type="text"
                  name="lastName"
                  id="lastName"
                />
                <label for="email">Email</label>
                <input
                  class="mb-4 outline outline-1 outline-green"
                  type="text"
                  name="email"
                  id="email"
                />
                <button
                  type="submit"
                  class="hover:text-white-500 hover:ring-green-500 hover:text-green-500 mb-2 me-2 rounded-lg bg-green px-5 py-2.5 text-sm font-medium text-white hover:bg-white hover:ring-4"
                >
                  Submit
                </button>
              </div>
            </form>
          </template>
          <template #editForm="{ id, first_name, last_name, email }">
            <form @submit.prevent="editEmployee">
              <input
                type="hidden"
                name="employeeId"
                id="employeeId"
                :value="id"
              />
              <div class="flex flex-col">
                <label for="firstName">First Name</label>
                <input
                  class="mb-4 outline outline-1 outline-green"
                  type="text"
                  name="firstName"
                  id="firstName"
                  :value="first_name"
                />
                <label for="lastName">Last Name</label>
                <input
                  class="mb-4 outline outline-1 outline-green"
                  type="text"
                  name="lastName"
                  id="lastName"
                  :value="last_name"
                />
                <label for="email">Email</label>
                <input
                  class="mb-4 outline outline-1 outline-green"
                  type="text"
                  name="email"
                  id="email"
                  :value="email"
                />
                <button
                  type="submit"
                  class="hover:text-white-500 hover:ring-green-500 hover:text-green-500 mb-2 me-2 rounded-lg bg-green px-5 py-2.5 text-sm font-medium text-white hover:bg-white hover:ring-4"
                >
                  Submit
                </button>
              </div>
            </form>
          </template>
        </Table>
      </Suspense>
    </div>
  </Main>
</template>
