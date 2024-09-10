// app.js
/*
document.getElementById('agendamento-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o envio do formulário

    // Captura os valores do formulário
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const data = document.getElementById('data').value;
    const hora = document.getElementById('hora').value;
    const especialidade = document.getElementById('especialidade').value;
    const sexo = document.getElementById('sexo').value;
    const descricao = document.getElementById('descricao').value;

    // Validação básica (pode ser expandida)
    if (nome && email && data && hora && especialidade && sexo && descricao) {
        // Cria um novo item para o histórico
        const historicoItem = document.createElement('tr');
        historicoItem.innerHTML = `
            <td>${data}</td>
            <td>${hora}</td>
            <td>${descricao}</td>
        `;

        // Adiciona o novo item à tabela de histórico
        document.querySelector('#historico-consultas tbody').appendChild(historicoItem);

        // Limpa o formulário após o agendamento
        document.getElementById('agendamento-form').reset();

        alert('Consulta agendada com sucesso!');
    } else {
        alert('Por favor, preencha todos os campos!');
    }
});

*/

document.getElementById('agendamento-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o envio do formulário

    // Captura os valores do formulário
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const data = document.getElementById('data').value;
    const hora = document.getElementById('hora').value;
    const especialidade = document.getElementById('especialidade').value;
    const sexo = document.getElementById('sexo').value;
    const descricao = document.getElementById('descricao').value;

    // Função para verificar disponibilidade da data e hora
    fetch('/verificar_disponibilidade', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data, hora }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.disponivel) {
            // Se a data e hora estiverem disponíveis, faça o agendamento
            realizarAgendamento(nome, email, data, hora, especialidade, sexo, descricao);
        } else {
            alert('Data e hora já estão ocupadas. Por favor, selecione outro horário.');
        }
    })
    .catch(error => console.error('Erro:', error));
});

function realizarAgendamento(nome, email, data, hora, especialidade, sexo, descricao) {
    fetch('/agendar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nome, email, data, hora, especialidade, sexo, descricao }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Consulta agendada com sucesso!');

            // Cria um novo item para o histórico
            const historicoItem = document.createElement('tr');
            historicoItem.innerHTML = `
                <td>${data}</td>
                <td>${hora}</td>
                <td>${descricao}</td>
            `;

            // Adiciona o novo item à tabela de histórico
            document.querySelector('#historico-consultas tbody').appendChild(historicoItem);

            // Limpa o formulário após o agendamento
            document.getElementById('agendamento-form').reset();
        } else {
            alert(data.message);
        }
    })
    .catch(error => console.error('Erro ao agendar:', error));
}
