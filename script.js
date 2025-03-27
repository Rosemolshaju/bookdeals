let slideIndex = 0;

function showSlides() {
    const slides = document.querySelectorAll(".slide");
    slides.forEach((slide) => (slide.style.display = "none"));

    slideIndex++;
    if (slideIndex > slides.length) slideIndex = 1;

    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 3000); // Change image every 3 seconds
}

showSlides();
const partners = document.querySelector('.partners');
let scrollPosition = 0;

setInterval(() => {
  scrollPosition -= 160; // Adjust based on image width + margin
  if (Math.abs(scrollPosition) >= partners.offsetWidth) {
    scrollPosition = 0;
  }
  partners.style.transform = `translateX(${scrollPosition}px)`;
}, 2000);
