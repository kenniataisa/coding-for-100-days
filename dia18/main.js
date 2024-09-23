let bloco = document.querySelectorAll('td');
let msg = document.querySelector('p');
let jogada = 'O';
let reset = document.querySelector('#reset');
let jogoAtivo = true;  

bloco.forEach(casa => {
    casa.addEventListener('click', event => {
        if (casa.innerHTML == "" && jogoAtivo) {  
            casa.innerHTML = jogada;
            verificarVencedor();
            if (jogoAtivo) {  
                jogada = (jogada == 'X') ? 'O' : 'X';
                msg.innerText = 'Vez de ' + jogada;
            }
        }
    });
});

reset.addEventListener('click', event => {
    bloco.forEach(casa => {
        casa.innerText = '';  
    });
    jogada = 'O';  
    msg.innerText = 'Vez de ' + jogada;  
    jogoAtivo = true;  
});

function verificarVencedor() {
    let combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];

    for (let combinacao of combinacoes) {
        let [a, b, c] = combinacao;
        if (bloco[a].innerText != '' && bloco[a].innerText == bloco[b].innerText && bloco[a].innerText == bloco[c].innerText) {
            msg.innerHTML = `<h1 style="color: green;">Jogador ${bloco[a].innerText} venceu!</h1>`;
            jogoAtivo = false;  
            return;
        }
    }

    let todasCasasPreenchidas = true;
    bloco.forEach(casa => {
        if (casa.innerText == '') {
            todasCasasPreenchidas = false;
        }
    });

    if (todasCasasPreenchidas) {
        msg.innerHTML = '<h1 style="color: red;">Deu velha!</h1>';
        jogoAtivo = false;  
    }
}
