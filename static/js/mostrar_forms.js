// Captura o botão e o formulário
const botao_atestado = document.getElementById('btn_atestado');
const formulario_atestado = document.getElementById('form_atestado');



// Adiciona o evento de clique no botão
botao_atestado.addEventListener('click', function() {
    // Verifica se o formulário está oculto ou visível
    if (formulario_atestado.style.display === 'none') {
        formulario_atestado.style.display = 'block'; // Mostra o formulário
    } else {
        formulario_atestado.style.display = 'none'; // Oculta o formulário
        
    }
    
 
});

const botao_receita = document.getElementById('btn_receita');
const formulario_receita  = document.getElementById('form-receita');

    // Adiciona o evento de clique no botão
    botao_receita.addEventListener('click', function() {
    // Verifica se o formulário está oculto ou visível
    if (formulario_receita.style.display === 'none') {
        formulario_receita.style.display = 'block'; // Mostra o formulário
    } else {
        formulario_receita.style.display = 'none'; // Oculta o formulário
        
    }
});