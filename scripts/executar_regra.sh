#deve printar o corpus.to_str() ao final de tudo, e somente isso
#set -e
branch=${PWD##*/}
python3 $branch.py > $branch-2.conllu
cd ../../
pasta=${PWD##*/}
sudo chmod a+rwx regras/$branch/$branch.conllu
cp regras/$branch/$branch-2.conllu ../Interrogat-rio/www/interrogar-ud/conllu/$branch.conllu
sh scripts/2_1-commit.sh $branch
mv regras/$branch/$branch-2.conllu regras/$branch/$branch.conllu