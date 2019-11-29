import sys
with open(sys.argv[1]) as f:
    arquivo = f.read().splitlines()
if len(sys.argv) == 1:
    print("Entre como parâmetro o arquivo que deseja adicionar # sent_id. É necessário ter # newdoc id.")
    print("Parâmetro opcional: sigla")

source = ""
novo_conllu = []
sigla = "-" + sys.argv[2] if len(sys.argv) > 2 else ""
for linha in arquivo:
    if linha.startswith("# newdoc id ="):
        source = linha.rsplit("/", 1)[1].rsplit(".txt", 1)[0]
    if not any(linha.startswith(y) for y in ["# newdoc id", "# newpar"]):
        novo_conllu.append(linha.replace("# sent_id = ", "# sent_id = " + source + sigla + "-"))

print("\n".join(novo_conllu))
