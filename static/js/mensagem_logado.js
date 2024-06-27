document.addEventListener('DOMContentLoaded', (event) => {
    const messages = document.getElementById('messages');
    
    // mostrar a lista (mensagem)
    messages.style.display = 'block';

    // Fazer essa mensagem aparecer por 5 segundos (5000 milliseconds)
    setTimeout(() => {
        messages.style.display = 'none';
    }, 5000);
});
