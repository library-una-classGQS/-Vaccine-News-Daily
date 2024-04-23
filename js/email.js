const form = document.getElementById('email-form');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  const nome = document.getElementById('nome').value;
  const email = document.getElementById('email').value;
  const mensagem = document.getElementById('mensagem').value;

  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://api.emailjs.com/api/v1.0/email/send', true);
  xhr.setRequestHeader('Content-Type', 'application/json');

  const data = {
    service_id: 'default_service',
    template_id: 'template_id',
    user_id: 'your_user_id',
    template_params: {
      nome,
      email,
      mensagem
    }
  };

  xhr.send(JSON.stringify(data));

  xhr.onload = function() {
    if (xhr.status === 200) {
      alert('Email enviado com sucesso!');
    } else {
      alert('Erro ao enviar email. Tente novamente mais tarde.');
    }
  };
});