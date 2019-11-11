# BIG-Oil-NLP
Repositório de Processamento de Linguagem Natural do projeto BIG Oil

Para executar os scripts dentro do repositório, é necessário antes baixar o repositório [ACDC-UD](https://github.com/alvelvis/ACDC-UD) na mesma pasta em que se baixou este repositório (BIG Oil NLP):

    $ git clone https://github.com/comcorhd/BIG-Oil-NLP.git

    $ git clone https://github.com/alvelvis/ACDC-UD.git

Para utilizar qualquer componente da [ET](http://comcorhd.letras.puc-rio.br/ET), é necessário que os ambientes tenham sido clonados na mesma pasta em que se baixou o BIG Oil NLP:

    $ git clone https://github.com/alvelvis/Interrogat-rio.git

    $ git clone https://github.com/alvelvis/Julgamento.git

Para editar por regra, é necessário instalar Sublime-Text 3 e Meld. Em um sistema baseado em Ubuntu, execute os comandos:

    $ sudo apt-get install meld

    $ wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -; sudo apt-get install apt-transport-https; echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list; sudo apt-get update; sudo apt-get install sublime-text