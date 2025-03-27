const slider = document.querySelector('.slider-container');
let scrollAmount = 0;

document.getElementById('next').addEventListener('click', () => {
    scrollAmount += 110; // Adjust based on image width and spacing
    slider.scrollTo({ left: scrollAmount, behavior: 'smooth' });
});

document.getElementById('prev').addEventListener('click', () => {
    scrollAmount -= 110; // Adjust based on image width and spacing
    slider.scrollTo({ left: scrollAmount, behavior: 'smooth' });
});
