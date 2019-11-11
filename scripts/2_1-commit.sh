# $1: nome da branch

set -e

if [ $# -eq 0 ]
  then
    git ls-remote
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