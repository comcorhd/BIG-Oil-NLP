set -e
branch=${PWD##*/}

if [ ! -e $branch.conllu ]; then
  echo 'Primeiro você deve criar uma branch para editar por regra'
  exit
fi

cd ..
cd ..
sh scripts/3_apagar_branch.sh $branch
rm -r regras/$branch
