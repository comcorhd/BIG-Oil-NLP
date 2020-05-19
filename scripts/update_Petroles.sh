set -e
curl 'http://interrogatorio.ica.ele.puc-rio.br/interrogar-ud/conllu/Petroles.conllu' -o ~/BIG-Oil-NLP/Petroles.conllu
git checkout -b new_documents
cd ~/BIG-Oil-NLP/
python3 ~/ACDC-UD/split_conllu.py Petroles.conllu
git diff
echo "Commit e merge, ou delete branch new_documents"
