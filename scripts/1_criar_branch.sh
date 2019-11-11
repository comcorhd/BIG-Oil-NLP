# $1: nome da branch

set -e

if [ $# -eq 0 ]
  then
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