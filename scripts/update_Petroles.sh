set -e
git pull
curl 'http://interrogatorio.ica.ele.puc-rio.br/interrogar-ud/conllu/Petroles.conllu' -o ~/BIG-Oil-NLP/Petroles.conllu
git checkout -b new_documents
cd ~/BIG-Oil-NLP/
python3 ~/ACDC-UD/split_conllu.py Petroles.conllu
git diff
git add -u
git commit -m "update Petroles from interrogatorio.ica.ele.puc-rio.br"
git checkout master
echo "git merge new_documents ou git branch -D new_documents"
