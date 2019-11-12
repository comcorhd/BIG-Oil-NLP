# BIG-Oil-NLP
Repositório de Processamento de Linguagem Natural do projeto BIG Oil

## Como começar com Windows 10+

Como instalar o Ubuntu dentro do sistema Windows:

[Ubuntu - Microsoft Store](https://www.microsoft.com/pt-br/p/ubuntu/9nblggh4msv6)

Para executar programas do Linux depois de instalado o Ubuntu no Windows, instale o Xming:

[Xming](https://sourceforge.net/projects/xming/)

## Requisitos

Para executar os scripts dentro do repositório, é necessário baixar o repositório de dependências [ACDC-UD](https://github.com/alvelvis/ACDC-UD) na mesma pasta onde está este repositório (BIG-Oil-NLP):

    $ git clone https://github.com/comcorhd/BIG-Oil-NLP.git

    $ git clone https://github.com/alvelvis/ACDC-UD.git


## ET

Para utilizar qualquer componente da [ET: uma Estação de Trabalho para revisão, edição e avaliação de corpora anotados](http://comcorhd.letras.puc-rio.br/ET), é necessário que os ambientes tenham sido clonados na mesma pasta em que se baixou o BIG-Oil-NLP:

    $ git clone https://github.com/alvelvis/Interrogat-rio.git

    $ git clone https://github.com/alvelvis/Julgamento.git

Experimente também mudar a variável `COMCORHD` no arquivo `config.py` para `True` e habilite funções extras (necessário ter a pasta Interrogat-rio na mesma pasta em que se baixou o BIG-Oil-NLP). Na variável `REPOSITORIES`, adicione também a linha a seguir, editando seu usuário e senha:

    https://SeuUsername:SuaSenha@github.com/comcorhd/BIG-Oil-NLP.git

## Edição por regra

Para editar por regra, é necessário instalar Sublime-Text 3 e Meld. Em um sistema baseado em Ubuntu, execute os comandos:

    $ sudo apt-get install meld

    $ wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -; sudo apt-get install apt-transport-https; echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list; sudo apt-get update; sudo apt-get install sublime-text