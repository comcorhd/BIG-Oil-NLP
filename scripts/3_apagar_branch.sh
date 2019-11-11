# $1: nome da branch

if [ $# -eq 0 ]
  then
    git ls-remote
    exit
fi

git checkout master
git pull
git branch -D $1
git push --delete origin $1
rm Inalterados/$1.conllu
rm ../Interrogat-rio/www/interrogar-ud/conllu/$1.conllu
rm $1.conllu
