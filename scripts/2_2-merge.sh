# $1: nome da branch

set -e

if [ ! -d scripts ]; then
	echo 'Execute o script de dentro da pasta do repositório, exemplo: sh scripts/script.sh'
	exit
fi

if [ $# -eq 0 ]
  then
  echo "Escolha a branch que deseja mesclar com a master. Veja as atuais:"
    git ls-remote
    exit
fi

git checkout master
git pull
git merge -s recursive -Xignore-space-at-eol $1
git push
