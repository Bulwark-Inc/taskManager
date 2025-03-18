/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class', // enables dark mode with the class strategy
    content: [

        // '../templates/**/*.html',
        '../../templates/**/*.html',  // root template
        '../../**/templates/**/*.html',  // app-specific templates

        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        
        /* JS 2: Process all JavaScript files in the project. */
        '../../static/**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                purple: {
                700: '#6B21A8',
                900: '#4C1D95',
                },
                gold: {
                400: '#FFD700',
                },
            },
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
