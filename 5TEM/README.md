# 5TEM - 5 TESES E MONOGRAFIAS

## Pastas

`PDF`: arquivos PDF completos

`TXT`: arquivos TXT completos

`TXT_intro` arquivos TXT apenas com a introdução. Conversão para UTF-8 e seleção da introdução foram feitas manualmente.

`udpipe_intro`: arquivos `TXT_intro` anotados pelo UDPipe treinado no Bosque-UD 2.5 (workbench). O arquivo `5TEM_udpipe.conllu` contém, no metadado sent_id, a indicação de qual o arquivo de origem de cada sentença, o que foi realizado com o script `fix_sent_id.py`.

`ju_intro`: os arquivos anotados pelo UDPipe, já com as sent_id corrigidas, foram reanotados pelo jPDTP, no arquivo `5TEM_ju.conllu`. A partir daí, fizemos a revisão humana, o que resultou no arquivo `5TEM_golden.conllu`.

## Descrição

O corpus 5TEM é composto pelas introduções anotadas automaticamente dos seguintes arquivos:

1. 0-20150121-TESEMSC_0.conllu
2. 2-20150126-TESEDSC_0.conllu
3. 10-20150122-MONOGRAFIA_0.conllu
4. 6-20140908-MONOGRAFIA_0.conllu

A revisão humana da anotação linguística foi feita pelos seguintes anotadores:

* Aline Silveira
* Elvis de Souza
* Tatiana Cavalcanti
* Wograine Evelyn

O corpus é composto por 257 sentenças, totalizando 3776 tokens anotados no formato CoNLL-U, conforme o framework Universal Dependencies.