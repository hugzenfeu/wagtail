/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html" // for app-specific templates
  ],

  theme: {
    extend: {},
  },
  plugins: [],
};
