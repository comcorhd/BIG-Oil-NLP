# 5TEM - 5 TESES E MONOGRAFIAS

## Pastas

`PDF`: arquivos PDF completos

`raw`: arquivos TXT completos

`raw/intro`: arquivos TXT apenas com a seção de introdução. Conversão para UTF-8 e seleção da introdução foram feitas manualmente.

`UDPIPE`: seções de introdução anotadas pelo UDPipe treinado no Bosque-UD 2.5 (workbench). O arquivo `5TEM_udpipe_sentid.conllu` contém, no metadado sent_id, a indicação de qual o arquivo de origem de cada sentença, o que foi realizado com o script `fix_sent_id.py`.

`JPTDP`: os arquivos anteriormente anotados pelo UDPipe, já com as sent_id corrigidas, foram reanotados pelo jPDTP, no arquivo `5TEM_ju.conllu`. A partir daí, fizemos a revisão humana, o que resultou no arquivo `5TEM_golden.conllu` e na pasta `documents`.

`golden-tokenizado-anotado`: neste pasta-se emcontram-se o golden das 5TEM, bem tokenizado e bem anotado; a anotação do JPTDP tokenizada igual ao golden, e a anotação do UDPIPE tokenizada igual ao golden.

## Descrição

5TEM compõe-se da introdução de duas teses e duas monografias. Os arquivos foram anotadas por dois modelos e passaram por revisão humana da anotação morfossintática.

(descrição em breve)