const textarea = document.querySelector('textarea');
const count = document.querySelector('.count');

function contarLetras(){
    const texto = textarea.value;
    const qtdLetras = textarea.value.length;
    count.innerText = `${qtdLetras}`;
}