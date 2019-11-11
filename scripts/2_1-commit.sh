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
  echo "Escolha a branch que deseja fazer commit. Veja as atuais:"
    git ls-remote
    exit
fi

if [ ! -d ../ACDC-UD ]; then
  echo "Pasta dos scripts do ACDC-UD não encontrada"
  exit
fi

[ ! -d "Repositorio-Branches" ] && mkdir -p "Repositorio-Branches"

git checkout $1
git pull
cp ../Interrogat-rio/www/interrogar-ud/conllu/$1.conllu .
python3 ../ACDC-UD/split_conllu.py $1.conllu
mv $1.conllu Repositorio-Branches/
git diff
git add -u

if [ $# -eq 1 ]
  then
    git commit
  else
    git commit -m "$2"
fi

git push
git checkout master
git pull
