# 5TEM - 5 TESES E MONOGRAFIAS garimpadas para o primeiro experimento com revisão da anotação morfossintática via ET

`PDF`: arquivos PDF completos

`TXT`: arquivos TXT completos

`TXT_intro` arquivos TXT apenas com a introdução. Conversão para UTF-8 e seleção da introdução foram feitas manualmente.

`udpipe_intro`: arquivos `TXT_intro` anotados pelo UDPipe treinado no Bosque-UD 2.5 (workbench). O arquivo 5TEM_sent_id.conllu contém, no metadado sent_id, a indicação de qual o arquivo de origem de cada sentença, o que foi realizado com o script `fix_sent_id.py`.

`ju_intro`: os arquivos anotados pelo UDPipe, já com as sent_id corrigidas, foram reanotados pelo jPDTP. Do arquivo .conllu, foi gerada a pasta `documents`, que é considerada a nossa pasta "golden", utilizando o script `split_conllu.py`.
