// Burger menus
    document.addEventListener('DOMContentLoaded', function () {
    // open
    const burger = document.querySelectorAll('.navbar-burger');
    const menu = document.querySelectorAll('.navbar-menu');

    if (burger.length && menu.length) {
        for (var i = 0; i < burger.length; i++) {
        burger[i].addEventListener('click', function () {
            for (var j = 0; j < menu.length; j++) {
                menu[j].classList.toggle('hidden');
            }
        });
        }
    }

    // close
    const close = document.querySelectorAll('.navbar-close');
    const backdrop = document.querySelectorAll('.navbar-backdrop');

    if (close.length) {
        for (var i = 0; i < close.length; i++) {
        close[i].addEventListener('click', function () {
            for (var j = 0; j < menu.length; j++) {
                menu[j].classList.toggle('hidden');
            }
        });
        }
    }

    if (backdrop.length) {
        for (var i = 0; i < backdrop.length; i++) {
        backdrop[i].addEventListener('click', function () {
            for (var j = 0; j < menu.length; j++) {
                menu[j].classList.toggle('hidden');
            }
        });
        }
    }
})

    // Get all radio buttons
    const radioButtons = document.querySelectorAll('input[type="radio"]');

// Add click event listener to each radio button
radioButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Get the value of the selected radio button
            const targetSectionId = button.value;

            // Scroll to the target section
            const targetSection = document.getElementById(targetSectionId);
            targetSection.scrollIntoView({ behavior: 'smooth' });
        });
})

    function toggleAnswer(id) {
    var answer = document.getElementById(id);
    if (answer.style.display === "none" || answer.style.display === "") {
        answer.style.display = "block";
    } else {
        answer.style.display = "none";
    }
}


