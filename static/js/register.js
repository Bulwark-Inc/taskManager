document.addEventListener("DOMContentLoaded", function() {
    // Initialize Lucide Icons (assuming it's loaded globally in base)
    lucide.createIcons();
  
    const revealButtons = document.querySelectorAll(".reveal-password");
  
    revealButtons.forEach(button => {
        button.addEventListener("click", () => {
            const targetId = button.getAttribute("data-target");
            const input = document.getElementById(targetId);
    
            if (!input) return;
    
            const icon = button.querySelector("i");
    
            if (input.type === "password") {
            input.type = "text";
            icon.setAttribute("data-lucide", "eye-off");
            } else {
            input.type = "password";
            icon.setAttribute("data-lucide", "eye");
            }
    
            // Reinitialize lucide icon inside button
            lucide.createIcons();
        });
    });
});
  