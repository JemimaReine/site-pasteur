let index = 0;
    const slides = document.querySelectorAll('.mini-slider .slides img');

    function showSlide() {
        slides.forEach((slide, i) => {
            slide.classList.remove('active');
        });
        slides[index].classList.add('active');
        index = (index + 1) % slides.length;
    }

    showSlide(); // Afficher la première image
    setInterval(showSlide, 3000);

