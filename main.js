document.addEventListener("DOMContentLoaded", function () {
    const sections = document.querySelectorAll(".section");

    function revealOnScroll() {
        sections.forEach((section) => {
            const sectionTop = section.getBoundingClientRect().top;
            if (sectionTop < window.innerHeight * 0.75) {
                section.classList.add("active");
            } else {
                section.classList.remove("active");
            }
        });
    }

    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll();

    // Smooth scrolling
    document.querySelectorAll("nav a").forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetSection = document.getElementById(targetId);
            targetSection.scrollIntoView({ behavior: "smooth" });
        });
    });

    // Scroll to next section
    window.scrollToNext = function (nextSectionId) {
        const nextSection = document.getElementById(nextSectionId);
        if (nextSection) {
            nextSection.scrollIntoView({ behavior: "smooth" });
        }
    };

    // Form Submission Handling
    const form = document.querySelector("form");
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        alert("Thank you for reaching out! I'll get back to you soon.");
        form.reset();
    });

    // Enhance Project and About Sections
    document.querySelectorAll(".project-card").forEach(card => {
        card.addEventListener("mouseover", () => {
            card.classList.add("hover-effect");
        });
        card.addEventListener("mouseout", () => {
            card.classList.remove("hover-effect");
        });
    });
});
