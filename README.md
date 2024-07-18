<h1 align="center">Vaccine News Daily</h1>


### Sumário:
- [Introdução](#introdução)
- [Instalação](#instalação)
- [Execução e uso](#execução-e-uso)


### Introdução
<p>
Este projeto visa trazer as últimaas notícias sobre vacinas ao redor de todo o mundo. Um projeto desenvolvido
em sala, na universidade UNA Contagem no curso de Análise e Desenvolvimento de Sistemas.
Por ser um projeto onde o Backend foi feito em python, decidimos utilizar o framework Flask
com elementos HTML, CSS e JavaScript. Utilizamos o ORM SQLAlchemy para criação e manutenção
do banco de dados e para gerenciamento de dependências utilizamos o Poetry.
</p>

<p>
Abaixo alguns tópicos para melhor entendimento e visualização:
</p>
<br>

1. _Capturas de tela:_
<br>
<br>
- Tela inicial:
<br>
<br>
<img src="https://i.imgur.com/citYjaB.png" alt="Página Inicial" width="700">
<br>
<br>
- Cuidados:
<br>
<br>
<img src="https://i.imgur.com/gO17ZHl.png" alt="Página Inicial" width="700">
<br>
<br>
- Login:
<br>
<br>
<img src="https://i.imgur.com/2fqltEZ.png" alt="Página Inicial" width="700">
<br>
<br>
- Fórum:
<br>
<br>
<img src="https://i.imgur.com/XeLkut8.png" alt="Página Inicial" width="700">
<br>
<br>

### Instalação

<p>
O projeto utiliza o gerenciador de dependências <strong>Poetry</strong>. Aqui está o passo a passo da instalação:
</p>
<br>

#### Windows:

1. *Abra o cmd / prompt de comando:*

   > ``tecla windows + R``
   > 
   > ``cmd``

2. *Clonar o repositório do projeto:*  

   > ``git clone <chave_do_projeto>``

3. *Navegar até o diretório onde foi clonado:*

   > ``cd <caminho/para/o/projeto>``

4. *Instalar as dependências do projeto (Caso não possua o Poetry ou o Python instalado,siga o passo a passo clicando [aqui¹](#instalação-do-python-e-do-poetry))*

   > ``poetry install``

5. *Ativar ambiente virtual:*

   > `poetry shell`

<br>

### Execução e uso


- **Utilizando o cmd:**
  - Defina o aplicativo Flask:
     `set FLASK_APP=vaccine_news.py`
  - Execute:
     `flask run --debug`

<br>

- **Utilizando Pycharm:**
  - Procure onde seu ambiente virtual foi instalado e copie o caminho que foi dado:
    > `poetry env info --path`
  - Adicione o interpretadir criado ao Pycharm:
  - No canto superior esquerdo clique nas 4 barrinhas
  - Vá até *Settings - Project: Vaccine-News-Daily - Python interpreter*
  - Selecione *Add interpreter - Add local interpreter*
  - Selecione *Poetery Environment - Existing Environment - Interpreter: ...*
  - Cole o caminho do projeto, navegue até a pasta *Scripts* e selecione o arquivo *python.exe*
  - Aplique as modificações e reinicie o Pycharm
<br>

- **Utilizando VsCode:**
  - Procure onde seu ambiente virtual foi instalado e copie o caminho que foi dado:
    > `poetry env info --path`
  - Adicione o interpretador criado ao VsCode:
  - Pressione as teclas *Ctrl + Shift + P*
  - Digite `Python: Select Interpreter`
  - Selecione *Enter interpreter path... - Find...*
  - Cole o caminho do projeto, navegue até a pasta *Scripts* e selecione o arquivo *python.exe*
  - Clique em *Select interpreter* e reinicie o VsCode

Após instalado, vá até o navegador e digite ```http://127.0.0.1:5000``` ou clique no link
ao executar pelo editor de código de sua preferência.

### ¹ Instalação do python e do poetry

- O interpretador Python pode ser instalado pelo [site oficial](https://www.python.org/downloads/)
- Após instalar o python instale o Poetry:
- Abra o cmd (Windows) ou o terminal (linux)
- Digite `pip install poetry`
