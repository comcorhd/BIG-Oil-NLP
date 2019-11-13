# BIG-Oil-NLP
Repositório de Processamento de Linguagem Natural do projeto BIG Oil - Ciência de Dados para a indústria de Óleo & Gás

## Como começar com Windows 10+

Como instalar o Ubuntu dentro do sistema Windows:

- [Ubuntu - Microsoft Store](https://www.microsoft.com/pt-br/p/ubuntu/9nblggh4msv6)

Para executar programas do Linux depois de instalado o Ubuntu no Windows, instale o Xming:

- [Xming](https://sourceforge.net/projects/xming/)

## Integração com a ET

Para executar os scripts dentro do repositório, é necessário baixar o repositório de dependências [ACDC-UD](https://github.com/alvelvis/ACDC-UD) e a [ET: uma Estação de Trabalho para revisão, edição e avaliação de corpora anotados](http://comcorhd.letras.puc-rio.br/ET) na mesma pasta onde está este repositório (BIG-Oil-NLP):

    $ git clone https://github.com/comcorhd/BIG-Oil-NLP.git

    $ git clone https://github.com/alvelvis/ACDC-UD.git

    $ git clone https://github.com/alvelvis/Interrogat-rio.git

    $ git clone https://github.com/alvelvis/Julgamento.git

Para habilitar funções extras do Julgamento, experimente mudar o valor da variável `COMCORHD` no arquivo `Julgamento/config.py` para `True`, e, na variável `REPOSITORIES`, adicione a linha a seguir, editando seu usuário e senha (ou removendo a parte de usuário e senha, caso não seja colaborador do repositório):

    https://SeuUsername:SuaSenha@github.com/comcorhd/BIG-Oil-NLP.git

## Edição por regra

Para editar por regra, é necessário instalar Meld e Sublime Text 3. Em um sistema baseado em Ubuntu, execute os comandos:

    $ sudo apt-get install meld

    $ wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -; sudo apt-get install apt-transport-https; echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list; sudo apt-get update; sudo apt-get install sublime-text
