import os
import sys
sys.path.append("../ACDC-UD")
import estrutura_ud
import Cristian_Marneffe
import validar_UD
from pprint import pprint
from collections import defaultdict
import itertools

if len(sys.argv) != 4:
    print("usage: evaluate_methods.py system.conllu sistema_guiamodifications.conllu goldenmodifications.conllu")
    exit()

sistema = estrutura_ud.Corpus(recursivo=True)
sistema_guia = estrutura_ud.Corpus(recursivo=True)
golden = estrutura_ud.Corpus(recursivo=True)
sistema.load(sys.argv[1])
sistema_guia.load(sys.argv[2])
golden.load(sys.argv[3])

for sentid, sentence in sistema.sentences.items():
    if all(sentid in x.sentences and len(x.sentences[sentid].tokens) == len(sistema.sentences[sentid].tokens) for x in [sistema, sistema_guia, golden]):
        for t, token in enumerate(sentence.tokens):
            sistema.sentences[sentid].tokens[t].misc = "_"
            sistema_guia.sentences[sentid].tokens[t].misc = "_"
            golden.sentences[sentid].tokens[t].misc = "_"

#DICIONÁRIOS COM OS ERROS APONTADOS, DE VALIDAÇÃO E DE DIVERGÊNCIA
errors_validar_UD = set()
erros = validar_UD.validate(sistema_guia, errorList = "../ACDC-UD/validar_UD.txt").values()
#sys.stderr.write(str(erros))
for assunto in erros:
    for error in assunto:
        if error['sentence']:
            if all(error['sentence'].sent_id in x.sentences for x in [sistema, sistema_guia, golden]) and all(len(error['sentence'].tokens) == len(x.sentences[error['sentence'].sent_id].tokens) for x in [sistema, sistema_guia, golden]):
                errors_validar_UD.add(f"{error['sentence'].sent_id}<tok>{error['t']}")

confusion_matrix = set()
confusion_matrix_errors = set()
confusion_matrix_col = defaultdict(set)
confusion_matrix_hit = defaultdict(lambda: defaultdict(set))
convergence = set()
convergence_col = defaultdict(set)
convergence_hit = defaultdict(set)
for sentid, sentence in sistema_guia.sentences.items():
    if all(sentid in x.sentences for x in [sistema_guia, sistema, golden]) and all(len(sentence.tokens) == len(x.sentences[sentid].tokens) for x in [sistema_guia, sistema, golden]):
        for t, token in enumerate(sentence.tokens):
            for coluna in ['upos', 'deprel', 'dephead']:
                if token.__dict__[coluna] == sistema.sentences[sentid].tokens[t].__dict__[coluna]:
                    convergence_col[coluna].add(f"{sentid}<tok>{t}")
                    if token.__dict__[coluna] == golden.sentences[sentid].tokens[t].__dict__[coluna]:
                        convergence_hit[coluna].add(f"{sentid}<tok>{t}")
                    else:
                        convergence.add(f"{sentid}<tok>{t}")
                elif token.__dict__[coluna] != sistema.sentences[sentid].tokens[t].__dict__[coluna]:
                    confusion_matrix.add(f"{sentid}<tok>{t}")
                    confusion_matrix_col[coluna].add(f"{sentid}<tok>{t}")
                    if golden.sentences[sentid].tokens[t].__dict__[coluna] == sistema_guia.sentences[sentid].tokens[t].__dict__[coluna]:
                        confusion_matrix_hit[coluna]['sistema_guia'].add(f"{sentid}<tok>{t}")
                    elif golden.sentences[sentid].tokens[t].__dict__[coluna] == sistema.sentences[sentid].tokens[t].__dict__[coluna]:
                        confusion_matrix_hit[coluna]['sistema'].add(f"{sentid}<tok>{t}")
                        confusion_matrix_errors.add(f"{sentid}<tok>{t}")
                    else:
                        confusion_matrix_hit[coluna]['none'].add(f"{sentid}<tok>{t}")
                        confusion_matrix_errors.add(f"{sentid}<tok>{t}")

cristian_marneffe_lexicais = set()
for exemplo in Cristian_Marneffe.main(sys.argv[3], 'lexicais'):
    for error in exemplo['frases']:
        if all(error['sent_id'] in x.sentences for x in [sistema, sistema_guia, golden]) and all(len(x.sentences[error['sent_id']].tokens) == len(x.sentences[error['sent_id']].tokens) for x in [sistema, sistema_guia, golden]):
            cristian_marneffe_lexicais.add(f"{error['sent_id']}<tok>{golden.sentences[error['sent_id']].map_token_id[str(error['id1'])]}") #realmente ID1 ou ID2?

cristian_marneffe_gramaticais = set()
for exemplo in Cristian_Marneffe.main(sys.argv[3], 'gramaticais'):
    for error in exemplo['frases']:
        if all(error['sent_id'] in x.sentences for x in [sistema, sistema_guia, golden]) and all(len(x.sentences[error['sent_id']].tokens) == len(x.sentences[error['sent_id']].tokens) for x in [sistema, sistema_guia, golden]):
            cristian_marneffe_gramaticais.add(f"{error['sent_id']}<tok>{golden.sentences[error['sent_id']].map_token_id[str(error['id1'])]}") #realmente ID1 ou ID2?

#DICIONÁRIO COM TODAS AS MODIFICAÇÕES REALIZADAS
all_modifications = set()
for sentid, sentence in golden.sentences.items():
    if all(sentid in x.sentences for x in [sistema_guia, sistema]) and all(len(sentence.tokens) == len(x.sentences[sentid].tokens) for x in [sistema_guia, sistema]):
        for t, token in enumerate(sentence.tokens):
            if token.to_str() != sistema_guia.sentences[sentid].tokens[t].to_str():
                all_modifications.add(f"{sentid}<tok>{t}")

#combinações
metodos = {
    'Erros de validação': errors_validar_UD, 
    'Matriz de confusão': confusion_matrix, 
    'N-grams gramaticais': cristian_marneffe_gramaticais, 
    'N-grams lexicais': cristian_marneffe_lexicais
    }
combinatoria = []
somas = defaultdict()
for i in range(len(metodos)+1):
    combinatoria.extend(list(itertools.combinations(metodos.keys(), i)))
pprint(combinatoria)

#COMEÇA A MONTAGEM DOS HTML
html = "<html><body style='width:40%; padding-bottom:100px; margin:auto; margin-top:20px;'>"
html += "<h1>Avaliação dos métodos de correção do Julgamento</h1><hr>"
html += f"<h3>Sistema: {sys.argv[1]}</h3>"
html += f"<h3>Sistema guia (pré-correções): {sys.argv[2]}</h3>"
html += f"<h3>Golden (pós-correções): {sys.argv[3]}</h3>"

html += "<h2>Características do corpus</h2><hr>"
html += "<table border='1'>"
html += "<tr><th>Arquivos</th><th>Sentenças</th><th>Tokens</th></tr>"
html += f"<tr><td>Sistema</td><td>{len(sistema.sentences)}</td><td>{len([x for sentence in sistema.sentences.values() for x in sentence.tokens if not '-' in x.id])}</td></tr>"
html += f"<tr><td>Sistema guia</td><td>{len(sistema_guia.sentences)}</td><td>{len([x for sentence in sistema_guia.sentences.values() for x in sentence.tokens if not '-' in x.id])}</td></tr>"
html += f"<tr><td>Golden</td><td>{len(golden.sentences)}</td><td>{len([x for sentence in golden.sentences.values() for x in sentence.tokens if not '-' in x.id])}</td></tr>"
html += "</table>"

html += "<hr><table border='1'>"
html += f"<tr><td>Sentenças comparáveis</td><td colspan='2'>{len([x for x in golden.sentences if all(x in y for y in [sistema.sentences, sistema_guia.sentences])])}</td></tr>"
html += f"<tr><td>Tokens corrigidos</td><td colspan='2'>{len(all_modifications)}</td></tr>"
html += "</table><hr>"

html += "<h2>Avaliação dos métodos</h2><hr>"
html += "<table border='1'>"
html += "<tr><th>Método</th><th>Erros detectados (por token)</th><th>VP</th><th>FP</th><th title='Erros detectados por todos os métodos DESSA linha'>Erros repetidos</th><th>Repetidos VP</th></tr>"

html += f"<tr><td>Nenhum método</td><td colspan='42'>{len(all_modifications - set.union(*metodos.values()))}</td></tr>"

for combination in sorted([x for x in list(combinatoria) if x], key=lambda x: x[0]):
    html += f"<tr><td>{'<b>' if len(combination) == 1 else ''}{' + '.join(combination)}{'</b>' if len(combination) == 1 else ''}</td><td>{len(set.union(*[metodos[metodo] for metodo in combination]))}</td><td>{len(all_modifications.intersection(set.union(*[metodos[metodo] for metodo in combination])))}</td><td>{len(set.union(*[metodos[metodo] for metodo in combination]) - all_modifications)}</td><td>{ len(set.intersection(*[metodos[metodo] for metodo in combination])) if len(combination) > 1 else 'Não se aplica'}</td><td>{ len(all_modifications.intersection(set.intersection(*[metodos[metodo] for metodo in combination]))) if len(combination) > 1 else 'Não se aplica'}</td></tr>"

html += "</table><hr>"

html += "<h2>Detalhe: matriz de confusão</h2><hr>"
html += "<table border='1'>"
html += "<tr><th>Coluna</th><th>Divergências (por coluna)</th><th>sistema_guia estava correto (não é erro)</th><th>sistema estava correto (erro de fato)</th><th>Ninguém estava correto (erro de fato)</th></tr>"
for coluna in confusion_matrix_col:
    html += f"<tr><td>{coluna}</td><td>{len(confusion_matrix_col[coluna])}</td><td>{len(confusion_matrix_hit[coluna]['sistema_guia'])}</td><td>{len(confusion_matrix_hit[coluna]['sistema'])}</td><td>{len(confusion_matrix_hit[coluna]['none'])}</td></tr>"
html += f"<tr><td>Total</td><td>{sum([len(confusion_matrix_col[coluna]) for coluna in confusion_matrix_col])}</td><td>{sum([len(confusion_matrix_hit[coluna]['sistema_guia']) for coluna in confusion_matrix_col])}</td><td>{sum([len(confusion_matrix_hit[coluna]['sistema']) for coluna in confusion_matrix_col])}</td><td>{sum([len(confusion_matrix_hit[coluna]['none']) for coluna in confusion_matrix_col])}</td></tr>"
html += "</table><br>"

html += "<table border='1'>"
html += "<tr><th>Coluna</th><th>Convergências (por coluna)</th><th>Convergência correta</th><th>Convergência incorreta</th></tr>"
for coluna in confusion_matrix_col:
    html += f"<tr><td>{coluna}</td><td>{len(convergence_col[coluna])}</td><td>{len(convergence_hit[coluna])}</td><td>{len(convergence_col[coluna] - convergence_hit[coluna])}</td></tr>"
html += f"<tr><td>Total</td><td>{sum([len(convergence_col[coluna]) for coluna in confusion_matrix_col])}</td><td>{sum([len(convergence_hit[coluna]) for coluna in confusion_matrix_col])}</td><td>{sum([len(convergence_col[coluna]) - len(convergence_hit[coluna]) for coluna in confusion_matrix_col])}</td></tr>"
html += "</table><br>"

html += "<table border='1'>"
html += f"<tr><th></th><th>Dos {len(confusion_matrix_errors)} tokens com erros de fato, o método encontrou:</th><th>Dos {len(convergence)} tokens com convergência incorreta, o método encontrou:</th></tr>"
html += f"<tr><td>Nenhum método</td><td>{len(confusion_matrix_errors - set.union(*[metodos[metodo] for metodo in metodos if metodo not in ['Matriz de confusão']]))}</td><td>{len(convergence - set.union(*[metodos[metodo] for metodo in metodos if metodo not in ['Matriz de confusão']]))}</td></tr>"
for metodo in [x for x in metodos if x not in ["Matriz de confusão"]]:
    html += f"<tr><td>{metodo}</td><td>{len(set.intersection(confusion_matrix_errors, metodos[metodo]))}</td><td>{len(set.intersection(convergence, metodos[metodo]))}</td></tr>"
html += "</table><hr>"

html += '</body></html>'

if not os.path.isdir(f"EM-{sys.argv[3].rsplit('/', 1)[1].rsplit('.', 1)[0] if '/' in sys.argv[3] else sys.argv[3].rsplit('.', 1)[0]}"):
    os.mkdir(f"EM-{sys.argv[3].rsplit('/', 1)[1].rsplit('.', 1)[0] if '/' in sys.argv[3] else sys.argv[3].rsplit('.', 1)[0]}")
with open(f"EM-{sys.argv[3].rsplit('/', 1)[1].rsplit('.', 1)[0] if '/' in sys.argv[3] else sys.argv[3].rsplit('.', 1)[0]}/index.html", "w") as f:
    f.write(html)


