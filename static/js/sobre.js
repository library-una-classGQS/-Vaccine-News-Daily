let currentIndex = 0;
const track = document.querySelector('.carousel-track');
const items = document.querySelectorAll('.carousel-track .img');
const prevButton = document.querySelector('.prev-btn');
const nextButton = document.querySelector('.next-btn');
const itemWidth = items[0].offsetWidth + 20; // Largura da imagem + margem
const visibleItems = Math.floor(track.parentElement.offsetWidth / itemWidth);
const totalItems = items.length;

// Move o carrossel
function moveCarousel(direction) {
    currentIndex += direction;

    // Reseta para o início ou final se ultrapassar os limites
    if (currentIndex < 0) currentIndex = totalItems - visibleItems;
    if (currentIndex > totalItems - visibleItems) currentIndex = 0;

    const offset = -currentIndex * itemWidth;
    track.style.transform = `translateX(${offset}px)`;
}

// Auto-scroll
let autoScrollInterval = setInterval(() => moveCarousel(1), 3000);

// Reseta o auto-scroll ao clicar nos botões
function resetAutoScroll() {
    clearInterval(autoScrollInterval);
    autoScrollInterval = setInterval(() => moveCarousel(1), 3000);
}

prevButton.addEventListener('click', () => {
    moveCarousel(-1);
    resetAutoScroll();
});

nextButton.addEventListener('click', () => {
    moveCarousel(1);
    resetAutoScroll();
});

// Ajusta o carrossel ao redimensionar a tela
window.addEventListener('resize', () => {
    moveCarousel(0);
});
