// Adicione o seguinte código ao seu JavaScript
const supportButton = document.getElementById('support-button');
const supportChat = document.getElementById('support-chat');
const todotChat = document.getElementById('todo-chat');
const supportInput = document.getElementById('support-input');
const sendButton = document.getElementById('send-button');
const supportMessages = document.getElementById('support-messages');

supportButton.addEventListener('click', () => {
 if(todotChat.style.display == 'none'){
  supportChat.style.display = 'block';
  todotChat.style.display = 'block';
 }else{
  supportChat.style.display = 'none';
  todotChat.style.display = 'none';
 }

  
});

sendButton.addEventListener('click', () => {
  const message = supportInput.value;
  if (message!== '') {
    const messageHTML = `<p>${message}</p>`;
    supportMessages.innerHTML += messageHTML;
    supportInput.value = '';
  }
});

supportChat.addEventListener('click', (e) => {
  if (e.target === supportChat) {
    supportChat.style.display = 'none';
  }
});