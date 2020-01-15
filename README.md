# BIG-Oil-NLP

Repositório de Processamento de Linguagem Natural do projeto BIG Oil - Ciência de Dados para a indústria de Óleo & Gás


## Descrição do repositório

Os arquivos anotados com revisão humana encontram-se na pasta `documents`.

Para treinar um modelo a partir deste corpus, utilize o arquivo `bigoil-train.conllu` (em breve).


### Arquivos já adicionados à pasta `documents`

* 5TEM - 5 teses e monografias


### Modelos que utilizamos para anotar os arquivos

* udpipe

* jPTDP


### Publicações

[BIG Oil – Ciência de Dados para a indústria de Óleo & Gás](http://comcorhd.letras.puc-rio.br/category/big-oil-identificacao-e-extracao-de-informacao-semantica-no-dominio-de-oleo-gas/)


## Como começar a editar o corpus com Windows 10

Como instalar o Ubuntu dentro do sistema Windows:

- [Ubuntu - Microsoft Store](https://www.microsoft.com/pt-br/p/ubuntu/9nblggh4msv6)

Para executar programas do Linux depois de instalado o Ubuntu no Windows, instale o Xming:

- [Xming](https://sourceforge.net/projects/xming/)


## Integração com a ET

Para editar o corpus via ET, é necessário utilizar um sistema baseado em Ubuntu e baixar o repositório de dependências [ACDC-UD](https://github.com/alvelvis/ACDC-UD) e a [ET: uma Estação de Trabalho para revisão, edição e avaliação de corpora anotados](http://comcorhd.letras.puc-rio.br/ET) na mesma pasta onde está este repositório (BIG-Oil-NLP).

Para baixar este repositório e as dependências do ACDC-UD, utilize os comandos:

    $ git clone https://github.com/comcorhd/BIG-Oil-NLP.git

    $ git clone https://github.com/alvelvis/ACDC-UD.git
    
Para baixar a ET, veja os comandos em:

1. https://github.com/alvelvis/Interrogat-rio

2. https://github.com/alvelvis/Julgamento


### Para integrar os componentes da ET com o repositório do BIG Oil, siga os passos a seguir:

**No arquivo `Julgamento/config.py`**

1. Mude o valor da variável `COMCORHD` para `True`

2. Na variável `REPOSITORIES`, adicione a linha a seguir entre aspas, editando seu usuário e senha (ou removendo a parte de usuário e senha, caso não seja colaborador do repositório):

    https://SeuUsername:SuaSenha@github.com/comcorhd/BIG-Oil-NLP.git

3. Na variável `VALIDAR_UD`, mude o valor para a linha abaixo (é necessário ter baixo o repositório ACDC-UD):

    f"{os.path.abspath(os.path.dirname(\_\_file\_\_)).rsplit('/', 1)\[0]}/ACDC-UD/validar_UD.txt"

**No arquivo `Interrogat-rio/www/cgi-bin/variables.py`**

1. Mude o valor da variável `validar_UD` para `../../ACDC-UD/validar_UD.txt`


## Edição por regra

Para editar por regra, é necessário instalar Meld e Sublime Text 3. Em um sistema baseado em Ubuntu, execute os comandos:

    $ sudo apt-get install meld

    $ wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -; sudo apt-get install apt-transport-https; echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list; sudo apt-get update; sudo apt-get install sublime-text


## Adicionando novos arquivos ao repositório

### Anotando-os com o UDPipe

Anotar com o UDPipe e redirecionar o output para a pasta do experimento. Exemplo:

    $ ./udpipe/udpipe-1.2.0 --tokenize --tag --parse modelo.udpipe 5TEM/TXT/* > 5TEM/udpipe/5TEM.conllu

Ajeitar o `sent_id` das frases anotadas. Exemplo:

    $ python3 scripts/fix_sent_id.py 5TEM/udpipe/5TEM.conllu > 5TEM/udpipe/5TEM_sent_id.conllu


### Anotando-os com o jPTDP

Baixe o modelo pré-treinado no Bosque-UD 2.5 workbench e adicione à pasta `jPTDP`:

    $ cd jPTDP
    $ wget https://www.dropbox.com/s/fn0r48xhn67inpt/outputs.tar.gz
    $ tar xvzf outputs.tar.gz

Execute o algoritmo no arquivo já anotado anteriormente pelo UDPipe (ver dependências em [README](https://github.com/comcorhd/BIG-Oil-NLP/tree/master/jPTDP)). Exemplo:

    $ cd src
    $ python jPTDP.py --predict --model ../outputs/jPTDP_pt_ud.model --params ../outputs/jPTDP_pt_ud.params --test ../../5TEM/udpipe/5TEM_sent_id.conllu --outdir ../../5TEM/ju --output ../../5TEM/ju/5TEM.conllu


### Para adicionar arquivos anotados à pasta `documents`

Criar a pasta `documents` a partir dessas frases. Exemplo:

    $ cd 5TEM/ju/
    $ python3 ../../../ACDC-UD/split_conllu.py 5TEM.conllu

Copiar os arquivos da pasta `documents` desse experimento para a pasta `documents` raíz, ou seja, para o golden do repositório. Exemplo:

    $ cp 5TEM/ju/documents/* documents