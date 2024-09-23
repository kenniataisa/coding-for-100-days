let slider = document.querySelector('#slider');
let sizePassword = document.querySelector('#valor');
let password = document.querySelector('#password');
let containerPassword = document.querySelector('#container-password'); 

let charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*';
let novaSenha = '';

sizePassword.innerHTML = slider.value;

slider.oninput = function() {
    sizePassword.innerHTML = this.value;
}

function gerarSenha() {
    let senha = '';

    for (let i = 0, n = charset.length; i < slider.value; ++i) {
        senha += charset.charAt(Math.floor(Math.random() * n));
    }

    containerPassword.classList.remove('hide');
    password.innerHTML = senha;
}

function copiarSenha() {
    navigator.clipboard.writeText(password.innerHTML).then(() => {
        alert("Senha copiada para a área de transferência!");
    }).catch(err => {
        console.log('Erro ao copiar a senha', err);
    });
}
