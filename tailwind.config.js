/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: ['./guard_tower/templates/**/*.{html,js}', './assets/**/*.{html,js}'],
  theme: {
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      colors: {
        'primary': '5FBDFF',
        'secondary': '7B66FF',
        'neutral': '2e2f2f',
        'dark': '051014',
        'light': 'acf7c1'
      },
      spacing: {
        '8xl': '96rem',
        '9xl': '128rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
    }
  },
};
