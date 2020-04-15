import os
import sys
sys.path.append("../ACDC-UD")
import estrutura_ud
import validar_UD

if len(sys.argv) != 4:
    print("usage: evaluate_metrics.py system.conllu golden_premodifications.conllu golden_postmodifications.conllu")
    exit()

sistema = estrutura_ud.Corpus(recursivo=False)
golden_pre = estrutura_ud.Corpus(recursivo=False)
golden_post = estrutura_ud.Corpus(recursivo=False)
sistema.load(sys.argv[1])
golden_pre.load(sys.argv[2])
golden_post.load(sys.argv[3])

#DICIONÁRIOS COM OS ERROS APONTADOS, DE VALIDAÇÃO E DE DIVERGÊNCIA
errors_validar_UD = []
for assunto in validar_UD.validate(golden_pre, errorList = "../ACDC-UD/validar_UD.txt").values():
    for error in assunto:
        if all(error['sentence'].sent_id in x.sentences for x in [sistema, golden_pre, golden_post]) and all(len(error['sentence'].tokens) == len(x.sentences[error['sentence'].sent_id].tokens) for x in [sistema, golden_pre, golden_post]):
            if {'sentid': error['sentence'].sent_id, 't': error['t']} not in errors_validar_UD:
                errors_validar_UD.append({'sentid': error['sentence'].sent_id, 't': error['t']})

confusion_matrix = []
for sentid, sentence in golden_pre.sentences.items():
    if all(sentid in x.sentences for x in [golden_pre, sistema]) and all(len(sentence.tokens) == len(x.sentences[sentid].tokens) for x in [golden_pre, sistema]):
        for t, token in enumerate(sentence.tokens):
            for coluna in ['upos', 'deprel']:
                if token.col[coluna] != sistema.sentences[sentid].tokens[t].col[coluna]:
                    if {'sentid': sentid, 't': t} not in confusion_matrix:
                        confusion_matrix.append({'sentid': sentid, 't': t})

#DICIONÁRIO COM TODAS AS MODIFICAÇÕES REALIZADAS
all_modifications = []
for sentid, sentence in golden_post.sentences.items():
    if all(sentid in x.sentences for x in [golden_pre, sistema]) and all(len(sentence.tokens) == len(x.sentences[sentid].tokens) for x in [golden_pre, sistema]):
        for t, token in enumerate(sentence.tokens):
            if token.to_str() != golden_pre.sentences[sentid].tokens[t].to_str():
                if not {'sentid': sentid, 't': t} in all_modifications:
                    all_modifications.append({'sentid': sentid, 't': t})

#COMEÇA A MONTAGEM DOS HTML
html = "<html><body style='width:40%; margin:auto; margin-top:20px;'>"
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

html += "<table border='1'>"
html += f"<tr><td>Frases comparáveis</td><td colspan='2'>{len([x for x in golden_post.sentences if all(x in y for y in [sistema.sentences, golden_pre.sentences])])}</td></tr>"
html += f"<tr><td>Tokens modificados</td><td colspan='2'>{len(all_modifications)}</td></tr>"
html += "</table>"

html += "<h2>Avaliação dos métodos</h2><hr>"
html += "<table border='1'>"
html += "<tr><th>Método</th><th>Erros detectados</th><th>Verdadeiros Positivos</th><th>Falsos Positivos</th></tr>"
html += f"<tr><td>Erros de validação</td><td>{len(errors_validar_UD)}</td><td>{len([x for x in errors_validar_UD if x in all_modifications])}</td><td>{len([x for x in errors_validar_UD if x not in all_modifications])}</td></tr>"
html += f"<tr><td>Matriz de confusão</td><td>{len(confusion_matrix)}</td><td>{len([x for x in confusion_matrix if x in all_modifications])}</td><td>{len([x for x in confusion_matrix if x not in all_modifications])}</td></tr>"
html += f"<tr><td>Nenhum método</td><td colspan='3'>{len([x for x in all_modifications if x not in confusion_matrix and x not in errors_validar_UD])}</td></tr>"
html += f"<tr><td>Todos os métodos</td><td colspan='3'>{len([x for x in all_modifications if x in confusion_matrix and x in errors_validar_UD])}</td></tr>"
html += "</table>"

for erro in [x for x in errors_validar_UD if x not in all_modifications]:
    html += erro['sentid'] + '-' + golden_post.sentences[erro['sentid']].text
    html += "<br>" + golden_pre.sentences[erro['sentid']].tokens[erro['t']].to_str()
    html += "<br>" + golden_post.sentences[erro['sentid']].tokens[erro['t']].to_str() + "<hr>"

html += '</body></html>'

if not os.path.isdir(f"EM-{sys.argv[3].rsplit('/', 1)[1].rsplit('.', 1)[0] if '/' in sys.argv[3] else sys.argv[3].rsplit('.', 1)[0]}"):
    os.mkdir(f"EM-{sys.argv[3].rsplit('/', 1)[1].rsplit('.', 1)[0] if '/' in sys.argv[3] else sys.argv[3].rsplit('.', 1)[0]}")
with open(f"EM-{sys.argv[3].rsplit('/', 1)[1].rsplit('.', 1)[0] if '/' in sys.argv[3] else sys.argv[3].rsplit('.', 1)[0]}/index.html", "w") as f:
    f.write(html)


