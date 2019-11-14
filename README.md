# BIG-Oil-NLP
Repositório de Processamento de Linguagem Natural do projeto BIG Oil - Ciência de Dados para a indústria de Óleo & Gás

## Como começar com Windows 10+

Como instalar o Ubuntu dentro do sistema Windows:

- [Ubuntu - Microsoft Store](https://www.microsoft.com/pt-br/p/ubuntu/9nblggh4msv6)

Para executar programas do Linux depois de instalado o Ubuntu no Windows, instale o Xming:

- [Xming](https://sourceforge.net/projects/xming/)

## Integração com a ET

É necessário baixar o repositório de dependências [ACDC-UD](https://github.com/alvelvis/ACDC-UD) e a [ET: uma Estação de Trabalho para revisão, edição e avaliação de corpora anotados](http://comcorhd.letras.puc-rio.br/ET) na mesma pasta onde está este repositório (BIG-Oil-NLP).

Para baixar este repositório e as dependências do ACDC-UD, utilize os comandos:

    $ git clone https://github.com/comcorhd/BIG-Oil-NLP.git

    $ git clone https://github.com/alvelvis/ACDC-UD.git
    
Para baixar a ET, veja os comandos em:

https://github.com/alvelvis/Interrogat-rio

https://github.com/alvelvis/Julgamento

Para habilitar funções extras do Julgamento, experimente mudar o valor da variável `COMCORHD` no arquivo `Julgamento/config.py` para `True`, e, na variável `REPOSITORIES`, adicione a linha a seguir, editando seu usuário e senha (ou removendo a parte de usuário e senha, caso não seja colaborador do repositório):

    https://SeuUsername:SuaSenha@github.com/comcorhd/BIG-Oil-NLP.git

## Edição por regra

Para editar por regra, é necessário instalar Meld e Sublime Text 3. Em um sistema baseado em Ubuntu, execute os comandos:

    $ sudo apt-get install meld

    $ wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -; sudo apt-get install apt-transport-https; echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list; sudo apt-get update; sudo apt-get install sublime-text

## Anotando novos arquivos

### Com o UDPipe:

Anotar com o UDPipe e redirecionar o output para a pasta do experimento. Exemplo:

    $ ./udpipe/udpipe-1.2.0 modelo.udpipe 5TEM/TXT/* > 5TEM/udpipe/5TEM.conllu

Ajeitar o `sent_id` das frases anotadas. Exemplos:

    $ python3 scripts/fix_sent_id.py 5TEM/udpipe/5TEM.conllu > 5TEM/udpipe/5TEM_sent_id.conllu

Criar a pasta `documents` a partir dessas frases. Exemplo:

    $ cd 5TEM/udpipe/

    $ python3 ../../../ACDC-UD/split_conllu.py 5TEM_sent_id.conllu

Copiar os arquivos da pasta `documents` desse experimento para a pasta `documents` global. Exemplo:

    $ cp 5TEM/udpipe/documents/* documents

