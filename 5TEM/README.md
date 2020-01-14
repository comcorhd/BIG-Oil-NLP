# 5TEM - 5 TESES E MONOGRAFIAS

## Pastas

`PDF`: arquivos PDF completos

`TXT`: arquivos TXT completos

`TXT_intro` arquivos TXT apenas com a introdução. Conversão para UTF-8 e seleção da introdução foram feitas manualmente.

`udpipe_intro`: arquivos `TXT_intro` anotados pelo UDPipe treinado no Bosque-UD 2.5 (workbench). O arquivo `5TEM_udpipe.conllu` contém, no metadado sent_id, a indicação de qual o arquivo de origem de cada sentença, o que foi realizado com o script `fix_sent_id.py`.

`ju_intro`: os arquivos anotados pelo UDPipe, já com as sent_id corrigidas, foram reanotados pelo jPDTP, no arquivo `5TEM_ju.conllu`. A partir daí, fizemos a revisão humana, o que resultou no arquivo `5TEM_golden.conllu`.

## Descrição

* 0-20150121-TESEMSC_0
* 10-20150122-MONOGRAFIA_0
* 2-20150126-TESEDSC_0
* 6-20140908-MONOGRAFIA_0

|Corpus|Sentenças|Tokens|
|---|---|---|
|jUD|257|7185|
|GOLDEN|257|7185|

|Anotação|jUD|GOLDEN|
|---|---|---|
|ADJ|557|571|
|ADP|1167|1175|
|ADV|205|197|
|AUX|134|135|
|CCONJ|237|243|
|DET|913|905|
|NOUN|1742|1754|
|NUM|171|172|
|PRON|123|131|
|PROPN|343|347|
|PUNCT|980|983|
|SCONJ|68|64|
|SYM|18|20|
|VERB|526|482|
|X|1|6|
|acl|103|97|
|acl:relcl|56|59|
|advcl|96|89|
|advmod|188|168|
|amod|491|505|
|appos|140|117|
|appos:parataxis|47|77|
|appos:transl|0|4|
|aux|18|16|
|aux:pass|54|61|
|case|1146|1123|
|cc|236|262|
|ccomp|10|7|
|compound|0|23|
|conj|384|371|
|cop|64|56|
|csubj|6|4|
|det|906|897|
|expl|22|23|
|fixed|64|84|
|flat|0|3|
|flat:foreign|1|0|
|flat:name|125|255|
|iobj|2|5|
|mark|70|68|
|nmod|724|709|
|nsubj|245|227|
|nsubj:pass|50|44|
|nummod|54|45|
|obj|244|223|
|obl|281|270|
|obl:agent|35|32|
|parataxis|9|15|
|punct|981|925|
|root|257|257|
|xcomp|76|64|