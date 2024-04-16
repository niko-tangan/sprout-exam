/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/components/*.{html,js,ts,vue}", "./src/components/**/*.{html,js,ts,vue}", "./*.html"],
  theme: {

    extend: {
      fontFamily: {
        "josefin": ["Josefin Sans", "sans-serif"]
      },
      colors: {
        transparent: "transparent",
        "white": "white",
        "black": "black",
        "green": "#2EB55B",
        "light-green": "#78CF95",
        "orange": "#E57E26"
      },
    },
  },
  plugins: ["prettier-plugin-tailwindcss"],
}

