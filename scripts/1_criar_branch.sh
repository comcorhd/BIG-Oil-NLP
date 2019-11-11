# $1: nome da branch

set -e

if [ ! -d scripts ]; then
	echo 'Execute o script de dentro da pasta do repositório, exemplo: sh scripts/script.sh'
	exit
fi

if [ ! -d ../Interrogat-rio/www/interrogar-ud/conllu/ ]; then
  echo 'Pasta do Interrogatório não encontrada'
  exit
fi

if [ $# -eq 0 ]
  then
    echo 'Escolha o nome da branch. Veja as atuais:'
    git ls-remote
    exit
fi

[ ! -d "Inalterados" ] && mkdir -p "Inalterados"

git checkout master
git pull
git checkout -b $1 master
git push --set-upstream origin $1
cat documents/*.conllu > Inalterados/$1.conllu
sudo chmod a+rwx Inalterados/$1.conllu
cp Inalterados/$1.conllu ../Interrogat-rio/www/interrogar-ud/conllu/
git checkout master
