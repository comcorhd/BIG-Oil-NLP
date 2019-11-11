# $1: nome da branch

set -e

if [ $# -eq 0 ]
  then
    git ls-remote
    exit
fi

git checkout master
git pull
git pull origin $1
git push
