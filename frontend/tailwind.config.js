/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,ts,vue}", "./*.html"],
  theme: {
    extend: {},
  },
  plugins: ["prettier-plugin-tailwindcss"],
}

