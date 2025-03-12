"use strict"

function toggleCardFlip(card) {
    console.log("flipped");
    console.log(card)
    const cardFront = card.querySelector('.card-front')
    cardFront.classList.toggle('visible')
    const cardBack= card.querySelector('.card-back')
    cardBack.classList.toggle('visible')
    cardFront.classList.toggle('hidden')
    cardBack.classList.toggle('hidden')
      
}

const cards = document.querySelectorAll('.card');
cards.forEach(card => {
    card.addEventListener('click', () => {
            toggleCardFlip(card);
    })
});