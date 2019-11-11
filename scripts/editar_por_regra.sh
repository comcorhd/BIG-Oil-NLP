
#$1 = branch
#set -e

if [ ! -d scripts ]; then
	echo 'Execute o script de dentro da pasta do repositório, exemplo: sh scripts/script.sh'
	exit
fi

if [ ! -d ../ACDC-UD ]; then
  echo 'Pasta de scripts do ACDC-UD não encontrada'
  exit
fi

if [ $# -eq 0 ]
  then
    echo 'Escolha o nome do branch que deseja criar para editar por regra. Veja os atuais:'
    git ls-remote
    exit
fi

sh scripts/1_criar_branch.sh $1
mkdir regras
mkdir regras/$1
ln -nfrs ../ACDC-UD/estrutura_ud.py regras/$1
cat documents/*.conllu > regras/$1/$1.conllu
cp scripts/executar_regra.sh regras/$1
cp scripts/verificar_regra.sh regras/$1
cp scripts/excluir_regra.sh regras/$1
cd regras/$1
echo "import estrutura_ud
corpus = estrutura_ud.Corpus(recursivo=True)
corpus.load('$1.conllu')

for sentid, sentence in corpus.sentences.items():
	for t, token in enumerate(sentence.tokens):
		#code

print(corpus.to_str())" > $1.py
subl $1.py
echo "Vá para regras/$1"
