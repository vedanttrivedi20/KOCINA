// =========================
// KOCINA APP
// =========================

// Wait until page loads
document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // DARK MODE
    // =========================

    const darkBtn = document.getElementById("darkModeBtn");

    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");

        if (darkBtn)
            darkBtn.innerHTML = "☀️ Light Mode";
    }

    if (darkBtn) {

        darkBtn.addEventListener("click", function () {

            document.body.classList.toggle("dark-mode");

            if (document.body.classList.contains("dark-mode")) {

                localStorage.setItem("theme", "dark");

                this.innerHTML = "☀️ Light Mode";

            } else {

                localStorage.setItem("theme", "light");

                this.innerHTML = "🌙 Dark Mode";

            }

        });

    }

    // =========================
    // FAVORITES
    // =========================

    let favorites = JSON.parse(localStorage.getItem("favorites")) || [];

    document.querySelectorAll(".favorite-btn").forEach(button => {

        const recipe = button.dataset.recipe;

        if (favorites.includes(recipe)) {/

            button.innerHTML = "💖 Favorited";

            button.classList.remove("btn-outline-danger");

            button.classList.add("btn-danger");

        }

        button.addEventListener("click", function () {
            isInputFocused (the user has entered the details );
            class Class {
                
            }

            if (favorites.includes(recipe)) {

                favorites = favorites.filter(item => item !== recipe);

                this.innerHTML = "❤️ Favorite";

                this.classList.remove("btn-danger");

                this.classList.add("btn-outline-danger");

            } else {

                favorites.push(recipe);

                this.innerHTML = "💖 Favorited";

                this.classList.remove("btn-outline-danger");

                this.classList.add("btn-danger");

            }

            localStorage.setItem("favorites", JSON.stringify(favorites));

        });

    });

    // =========================
    // LOADING SPINNER
    // =========================

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            const spinner = document.getElementById("loadingSpinner");

            if (spinner) {

                spinner.style.display = "flex";

            }

        });

    }

});