# $1: nome da branch

if [ ! -d scripts ]; then
	echo 'Execute o script de dentro da pasta do repositório, exemplo: sh scripts/script.sh'
	exit
fi

if [ $# -eq 0 ]
  then
    echo "Escolha a branch que deseja excluir. Veja as atuais:"
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
