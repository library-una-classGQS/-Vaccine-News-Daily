// Referências ao DOM
const currentPasswordHistory = document.getElementById('current-password-history2');
const lastPasswordsList = document.getElementById('last-passwords');

// Obter histórico do Local Storage
const history = JSON.parse(localStorage.getItem('history')) || [];

// Atualizar histórico de senhas
function updateHistory() {
    if (history.length > 0) {
        currentPasswordHistory.textContent = history[history.length - 1];
    } else {
        currentPasswordHistory.textContent = '-';
    }

    lastPasswordsList.innerHTML = '';
    history.slice(-5).reverse().forEach(password => {
        const li = document.createElement('li');
        li.textContent = password;
        lastPasswordsList.appendChild(li);
    });
}

// Inicialização
updateHistory();
