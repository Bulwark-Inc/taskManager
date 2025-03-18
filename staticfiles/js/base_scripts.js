const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuButton.addEventListener('click', () => {
    const isOpen = !mobileMenu.classList.contains('hidden');

    if (isOpen) {
        mobileMenu.classList.add('opacity-0', 'scale-95');
        setTimeout(() => mobileMenu.classList.add('hidden'), 300);
    } else {
        mobileMenu.classList.remove('hidden');
        setTimeout(() => mobileMenu.classList.remove('opacity-0', 'scale-95'), 10);
    }
});

const themeToggleDesktop = document.getElementById('theme-toggle');
const themeToggleMobile = document.getElementById('theme-toggle-mobile');
const themeToggleIcon = document.getElementById('theme-toggle-icon');
const htmlElement = document.documentElement;

const setDarkMode = (enable) => {
    if (enable) {
        htmlElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
        themeToggleIcon.innerHTML = `<use href="#sun" />`;
    } else {
        htmlElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
        themeToggleIcon.innerHTML = `<use href="#moon" />`;
    }
};

const toggleTheme = () => {
    const isDark = htmlElement.classList.contains('dark');
    setDarkMode(!isDark);
};

// Load theme
const currentTheme = localStorage.getItem('theme');
if (currentTheme === 'dark' || (!currentTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    setDarkMode(true);
} else {
    setDarkMode(false);
}

themeToggleDesktop.addEventListener('click', () => {
    toggleTheme();
    themeToggleIcon.classList.add('rotate-180');
    setTimeout(() => themeToggleIcon.classList.remove('rotate-180'), 500);
});

themeToggleMobile.addEventListener('click', toggleTheme);

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Alpine
    if (!window.Alpine) {
        window.Alpine = Alpine;
        Alpine.start();
    }

    // Initialize AOS
    AOS.init({
        duration: 800,
        once: true,
        easing: 'ease-in-out',
    });
    
    // Initialize lucide
    lucide.createIcons();
});