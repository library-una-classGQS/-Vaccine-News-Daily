// Função para obter a data e hora atual
function obterDataHoraAtual() {
    const agora = new Date();  // Objeto Date para pegar a data e hora atual

    const dia = String(agora.getDate()).padStart(2, '0'); // Dia atual
    const mes = String(agora.getMonth() + 1).padStart(2, '0'); // Mês (Janeiro é 0, então somamos 1)
    const ano = agora.getFullYear(); // Ano atual

    const horas = String(agora.getHours()).padStart(2, '0'); // Horas
    const minutos = String(agora.getMinutes()).padStart(2, '0'); // Minutos
    const segundos = String(agora.getSeconds()).padStart(2, '0'); // Segundos

    // Formatação da data e hora no formato "DD/MM/YYYY HH:MM:SS"
    const dataFormatada = `${dia}/${mes}/${ano}`;
    const horaFormatada = `${horas}:${minutos}:${segundos}`;
    const dataHoraFormatada = `${dataFormatada} ${horaFormatada}`;

    // Atualiza o conteúdo do elemento HTML com a data e hora atual
    document.getElementById('data').textContent = dataFormatada;
    document.getElementById('hora').textContent = horaFormatada;
    document.getElementById('datahora').textContent = dataHoraFormatada;
}

// Chama a função inicialmente e depois a cada 1 segundo (1000 ms)
setInterval(obterDataHoraAtual, 1000);

// Chama a função para atualizar logo no carregamento da página
obterDataHoraAtual();
