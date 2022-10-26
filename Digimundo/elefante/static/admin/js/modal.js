const openModal = document.querySelector('.hero__cta');
const abrir_carrito= document.querySelector('abrir_carrito');
const modal = document.querySelector('.modal');
const closeModal = document.querySelector('.modal__close');

openModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.add('modal--show');
});

abrir_carrito.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.add('carrito--show');
});

closeModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.remove('modal--show');
});