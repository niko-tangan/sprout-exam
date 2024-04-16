<template>
  <div class="w-full p-4 text-2xl font-bold md:text-3xl lg:text-4xl">
    <h1>Employees</h1>
    <h1 class="text-center">Employees</h1>
    <div
      class="grid grid-cols-2 items-center gap-12 p-4 text-2xl font-bold md:grid-cols-3 md:justify-center lg:grid-cols-4"
    >
      <div
        class="flex aspect-square max-h-[300px] min-h-[150px] min-w-[150px] max-w-[300px] shrink items-center justify-center border-2 border-black hover:text-orange"
        v-for="employee in employees"
      >
        <h1>{{ employee.first_name }}</h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EmployeeGrid",
  data() {
    return {
      employees: "",
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/employees";
      axios
        .get(path)
        .then((res) => {
          this.employees = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
