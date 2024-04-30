import type { Config } from 'tailwindcss';
/** @type {import('tailwindcss').Config} */
export default <Partial<Config>>{
    content: [
	`components/**/*.{vue,js,ts}`,
    `layouts/**/*.vue`,
    `pages/**/*.vue`,
    `App.{js,ts,vue}`,
    `app.{js,ts,vue}`
	],
	theme: {
		extend: {},
	},
	darkMode: 'class'
};
