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

    $ ./udpipe/udpipe-1.2.0 --tokenize --tag --parse modelo.udpipe 5TEM/TXT/* > 5TEM/udpipe/5TEM.conllu

Ajeitar o `sent_id` das frases anotadas. Exemplo:

    $ python3 scripts/fix_sent_id.py 5TEM/udpipe/5TEM.conllu > 5TEM/udpipe/5TEM_sent_id.conllu

### Com o jPTDP:

Baixe o modelo pré-treinado no Bosque-UD 2.5 workbench e adicione à pasta `jPTDP`:

    $ cd jPTDP
    $ wget https://www.dropbox.com/s/fn0r48xhn67inpt/outputs.tar.gz
    $ tar xvzf outputs.tar.gz

Execute o algoritmo no arquivo já anotado anteriormente pelo UDPipe (ver dependências em [README](https://github.com/comcorhd/BIG-Oil-NLP/tree/master/jPTDP)). Exemplo:

    $ cd src
    $ python jPTDP.py --predict --model ../outputs/jPTDP_pt_ud.model --params ../outputs/jPTDP_pt_ud.params --test ../../5TEM/udpipe/5TEM_sent_id.conllu --outdir ../../5TEM/ju --output ../../5TEM/ju/5TEM.conllu

### Para adicionar arquivos anotados à pasta golden

Criar a pasta `documents` a partir dessas frases. Exemplo:

    $ cd 5TEM/ju/
    $ python3 ../../../ACDC-UD/split_conllu.py 5TEM.conllu

Copiar os arquivos da pasta `documents` desse experimento para a pasta `documents` raíz, ou seja, para o golden do repositório. Exemplo:

    $ cp 5TEM/ju/documents/* documents