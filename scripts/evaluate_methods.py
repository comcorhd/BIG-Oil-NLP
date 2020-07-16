import os
import sys
sys.path.append("../ACDC-UD")
import estrutura_ud
import Cristian_Marneffe
import validar_UD
import pprint
from collections import defaultdict
import itertools

if len(sys.argv) != 4:
    print("usage: evaluate_methods.py system.conllu golden_premodifications.conllu golden_postmodifications.conllu")
    exit()

sistema = estrutura_ud.Corpus(recursivo=True)
golden_pre = estrutura_ud.Corpus(recursivo=True)
golden_post = estrutura_ud.Corpus(recursivo=True)
sistema.load(sys.argv[1])
golden_pre.load(sys.argv[2])
golden_post.load(sys.argv[3])

for sentid, sentence in sistema.sentences.items():
    if all(sentid in x.sentences and len(x.sentences[sentid].tokens) == len(sistema.sentences[sentid].tokens) for x in [sistema, golden_pre, golden_post]):
        for t, token in enumerate(sentence.tokens):
            sistema.sentences[sentid].tokens[t].misc = "_"
            golden_pre.sentences[sentid].tokens[t].misc = "_"
            golden_post.sentences[sentid].tokens[t].misc = "_"

#DICIONÁRIOS COM OS ERROS APONTADOS, DE VALIDAÇÃO E DE DIVERGÊNCIA
errors_validar_UD = []
erros = validar_UD.validate(golden_pre, errorList = "../ACDC-UD/validar_UD.txt").values()
#sys.stderr.write(str(erros))
for assunto in erros:
    for error in assunto:
        if error['sentence']:
            if all(error['sentence'].sent_id in x.sentences for x in [sistema, golden_pre, golden_post]) and all(len(error['sentence'].tokens) == len(x.sentences[error['sentence'].sent_id].tokens) for x in [sistema, golden_pre, golden_post]):
                if {'sentid': error['sentence'].sent_id, 't': error['t']} not in errors_validar_UD:
                    errors_validar_UD.append({'sentid': error['sentence'].sent_id, 't': error['t']})

confusion_matrix = []
confusion_matrix_col = defaultdict(list)
confusion_matrix_hit = defaultdict(lambda: defaultdict(lambda: 0))
convergence = defaultdict(list)
convergence_hit = defaultdict(lambda: 0)
for sentid, sentence in golden_pre.sentences.items():
    if all(sentid in x.sentences for x in [golden_pre, sistema, golden_post]) and all(len(sentence.tokens) == len(x.sentences[sentid].tokens) for x in [golden_pre, sistema, golden_post]):
        for t, token in enumerate(sentence.tokens):
            for coluna in ['upos', 'deprel', 'dephead']:
                if token.__dict__[coluna] == sistema.sentences[sentid].tokens[t].__dict__[coluna]:
                    convergence[coluna].append({'sentid': sentid, 't': t})
                    if token.__dict__[coluna] == golden_post.sentences[sentid].tokens[t].__dict__[coluna]:
                        convergence_hit[coluna] += 1
                elif token.__dict__[coluna] != sistema.sentences[sentid].tokens[t].__dict__[coluna]:
                    confusion_matrix_col[coluna].append({'sentid': sentid, 't': t})
                    if golden_post.sentences[sentid].tokens[t].__dict__[coluna] == golden_pre.sentences[sentid].tokens[t].__dict__[coluna]:
                        confusion_matrix_hit[coluna]['golden_pre'] += 1
                    elif golden_post.sentences[sentid].tokens[t].__dict__[coluna] == sistema.sentences[sentid].tokens[t].__dict__[coluna]:
                        confusion_matrix_hit[coluna]['sistema'] += 1
                    else:
                        confusion_matrix_hit[coluna]['none'] += 1
                    if {'sentid': sentid, 't': t} not in confusion_matrix:
                        confusion_matrix.append({'sentid': sentid, 't': t})

cristian_marneffe_lexicais = []
for exemplo in Cristian_Marneffe.main(sys.argv[3], 'lexicais'):
    for error in exemplo['frases']:
        if all(error['sent_id'] in x.sentences for x in [sistema, golden_pre, golden_post]) and all(len(x.sentences[error['sent_id']].tokens) == len(x.sentences[error['sent_id']].tokens) for x in [sistema, golden_pre, golden_post]):
            cristian_marneffe_lexicais.append({'sentid': error['sent_id'], 't': golden_post.sentences[error['sent_id']].map_token_id[str(error['id1'])]}) #realmente ID1 ou ID2?

cristian_marneffe_gramaticais = []
for exemplo in Cristian_Marneffe.main(sys.argv[3], 'gramaticais'):
    for error in exemplo['frases']:
        if all(error['sent_id'] in x.sentences for x in [sistema, golden_pre, golden_post]) and all(len(x.sentences[error['sent_id']].tokens) == len(x.sentences[error['sent_id']].tokens) for x in [sistema, golden_pre, golden_post]):
            cristian_marneffe_gramaticais.append({'sentid': error['sent_id'], 't': golden_post.sentences[error['sent_id']].map_token_id[str(error['id1'])]}) #realmente ID1 ou ID2?

#DICIONÁRIO COM TODAS AS MODIFICAÇÕES REALIZADAS
all_modifications = []
for sentid, sentence in golden_post.sentences.items():
    if all(sentid in x.sentences for x in [golden_pre, sistema]) and all(len(sentence.tokens) == len(x.sentences[sentid].tokens) for x in [golden_pre, sistema]):
        for t, token in enumerate(sentence.tokens):
            if token.to_str() != golden_pre.sentences[sentid].tokens[t].to_str():
                if not {'sentid': sentid, 't': t} in all_modifications:
                    all_modifications.append({'sentid': sentid, 't': t})

#combinações
metodos = {
    'Erros de validação': errors_validar_UD, 
    'Matriz de confusão': confusion_matrix, 
    'N-grams gramaticais': cristian_marneffe_gramaticais, 
    'N-grams lexicais': cristian_marneffe_lexicais
    }
combinatoria = []
somas = {}
for i in range(len(metodos)+1):
    combinatoria.extend(list(itertools.combinations(metodos.keys(), i)))
for combination in combinatoria:
    somas[combination] = []
    for metodo in combination:
        for erro in metodos[metodo]:
            if erro not in somas[combination]:
                somas[combination].append(erro)

#COMEÇA A MONTAGEM DOS HTML
html = "<html><body style='width:40%; padding-bottom:100px; margin:auto; margin-top:20px;'>"
html += "<h1>Avaliação dos métodos de correção do Julgamento</h1><hr>"
html += f"<h3>Sistema: {sys.argv[1]}</h3>"
html += f"<h3>Pré-golden (pré-correções): {sys.argv[2]}</h3>"
html += f"<h3>Golden (pós-correções): {sys.argv[3]}</h3>"

html += "<h2>Características do corpus</h2><hr>"
html += "<table border='1'>"
html += "<tr><th>Arquivos</th><th>Sentenças</th><th>Tokens</th></tr>"
html += f"<tr><td>Sistema</td><td>{len(sistema.sentences)}</td><td>{len([x for sentence in sistema.sentences.values() for x in sentence.tokens if not '-' in x.id])}</td></tr>"
html += f"<tr><td>Pré-golden</td><td>{len(golden_pre.sentences)}</td><td>{len([x for sentence in golden_pre.sentences.values() for x in sentence.tokens if not '-' in x.id])}</td></tr>"
html += f"<tr><td>Golden</td><td>{len(golden_post.sentences)}</td><td>{len([x for sentence in golden_post.sentences.values() for x in sentence.tokens if not '-' in x.id])}</td></tr>"
html += "</table>"

html += "<hr><table border='1'>"
html += f"<tr><td>Sentenças comparáveis</td><td colspan='2'>{len([x for x in golden_post.sentences if all(x in y for y in [sistema.sentences, golden_pre.sentences])])}</td></tr>"
html += f"<tr><td>Tokens corrigidos</td><td colspan='2'>{len(all_modifications)}</td></tr>"
html += "</table><hr>"

html += "<h2>Avaliação dos métodos</h2><hr>"
html += "<table border='1'>"
html += "<tr><th>Método</th><th>Erros detectados (por token)</th><th title='Erros detectados por todos os métodos DESSA linha'>Erros repetidos</th><th>Verdadeiros Positivos</th><th>Falsos Positivos</th></tr>"

html += f"<tr><td>Nenhum método</td><td>{len([x for x in all_modifications if not x in [k for metodo in metodos for k in metodos[metodo]]])}</td><td>Não se aplica</td><td>Não se aplica</td><td>Não se aplica</td></tr>"

for combination in sorted([x for x in list(somas.keys()) if x], key=lambda x: x[0]):
    html += f"<tr><td>{'<b>' if len(combination) == 1 else ''}{' + '.join(combination)}{'</b>' if len(combination) == 1 else ''}</td><td>{len(somas[combination])}</td><td>{len([x for x in somas[combination] if all(x in somas[(y, )] for y in combination)]) if len(combination) > 1 else 'Não se aplica'}</td><td>{len([x for x in somas[combination] if x in all_modifications])}</td><td>{len([x for x in somas[combination] if x not in all_modifications])}</td></tr>"

html += "</table><hr>"

html += "<h2>Detalhe: matriz de confusão</h2><hr>"
html += "<table border='1'>"
html += "<tr><th></th><th>Divergências (por coluna)</th><th>golden_pre estava correto</th><th>sistema estava correto</th><th>Ninguém estava correto</th><th>Convergências</th><th>Convergência estava correta</th></tr>"
for coluna in confusion_matrix_col:
    html += f"<tr><td>{coluna}</td><td>{len(confusion_matrix_col[coluna])}</td><td>{confusion_matrix_hit[coluna]['golden_pre']}</td><td>{confusion_matrix_hit[coluna]['sistema']}</td><td>{confusion_matrix_hit[coluna]['none']}</td><td>{len(convergence[coluna])}</td><td>{convergence_hit[coluna]}</td></tr>"
html += f"<tr><td>Total</td><td>{sum([len(confusion_matrix_col[coluna]) for coluna in confusion_matrix_col])}</td><td>{sum([confusion_matrix_hit[coluna]['golden_pre'] for coluna in confusion_matrix_col])}</td><td>{sum([confusion_matrix_hit[coluna]['sistema'] for coluna in confusion_matrix_col])}</td><td>{sum([confusion_matrix_hit[coluna]['none'] for coluna in confusion_matrix_col])}</td><td>{sum([len(convergence[coluna]) for coluna in confusion_matrix_col])}</td><td>{sum([convergence_hit[coluna] for coluna in confusion_matrix_col])}</td></tr>"
html += "</table><hr>"

'''
for erro in [x for x in errors_validar_UD if x not in all_modifications]:
    html += erro['sentid'] + '-' + golden_post.sentences[erro['sentid']].text
    html += "<br>" + golden_pre.sentences[erro['sentid']].tokens[erro['t']].to_str()
    html += "<br>" + golden_post.sentences[erro['sentid']].tokens[erro['t']].to_str() + "<hr>"
'''

html += '</body></html>'

if not os.path.isdir(f"EM-{sys.argv[3].rsplit('/', 1)[1].rsplit('.', 1)[0] if '/' in sys.argv[3] else sys.argv[3].rsplit('.', 1)[0]}"):
    os.mkdir(f"EM-{sys.argv[3].rsplit('/', 1)[1].rsplit('.', 1)[0] if '/' in sys.argv[3] else sys.argv[3].rsplit('.', 1)[0]}")
with open(f"EM-{sys.argv[3].rsplit('/', 1)[1].rsplit('.', 1)[0] if '/' in sys.argv[3] else sys.argv[3].rsplit('.', 1)[0]}/index.html", "w") as f:
    f.write(html)


