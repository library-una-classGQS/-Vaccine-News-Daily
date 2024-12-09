let currentPassword = 0;
let queue = [];
let history = [];

// Referências ao DOM
const currentPasswordDisplay = document.getElementById('current-password');
const queueList = document.getElementById('queue-list');
const callNextButton = document.getElementById('call-next');
const resetButton = document.getElementById('reset');

// Gerar as próximas senhas
function generateNextPasswords() {
    for (let i = 1; i <= 10; i++) {
        queue.push(`A${i.toString().padStart(3, '0')}`);
    }
    updateQueueDisplay();
}

// Atualizar a fila na tela
function updateQueueDisplay() {
    queueList.innerHTML = '';
    queue.forEach(password => {
        const li = document.createElement('li');
        li.textContent = password;
        queueList.appendChild(li);
    });
}

// Chamar próxima senha
callNextButton.addEventListener('click', () => {
    if (queue.length > 0) {
        currentPassword = queue.shift();
        currentPasswordDisplay.textContent = currentPassword;

        // Adicionar a senha ao histórico
        if (currentPassword) {
            history.push(currentPassword);
            localStorage.setItem('history', JSON.stringify(history));
        }

        updateQueueDisplay();
    } else {
        alert('Não há mais senhas na fila!');
    }
});

// Reiniciar senhas
resetButton.addEventListener('click', () => {
    currentPassword = 0;
    queue = [];
    history = [];
    currentPasswordDisplay.textContent = '-';
    localStorage.removeItem('history');
    generateNextPasswords();
});

// Inicialização
generateNextPasswords();
