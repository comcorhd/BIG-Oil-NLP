# 400TEM - 400 Teses e Monografias

Trata-se do PetroText (ou Petrolês) anotado utilizando o modelo jPTDP treinado no Bosque-UD 2.5 workbench. Não há revisão humana da anotação morfossintática, mas garantimos um bom pré-processamento na conversão do PDF para o TXT. Os experimentos realizados encontram-se no notebook `400TEM.ipynb`.

Em `gambiarra-utf8` é possível encontrar o TXT das 400 TESES E MONOGRAFIAS e os arquivos anotados pelo UDPipe e pelo jPTDP. O TXT foi obtido utilizando as técnicas menos sofisticadas de conversão de PDF para TXT. Já na pasta `processado-utf8`, encontram-se os mesmos arquivos, porém utilizando-se uma ferramenta desenvolvida pelo projeto especificamente para lidar com a conversão de PDF para TXT. Abaixo, encontramos as estatísticas de ambas as versões das 400TEM.

## Descrição dos corpora

|Versão|Sentenças|Tokens|
|---|---|---|
|GAMBIARRA|983615|19873003|
|FINAL|268663|6792345|

## Distribuição bruta das categorias gramaticais

| Anotação                  | GAMBIARRA                 | FINAL                     |
| ---                       | ---                       | ---                       |
| ADJ                       |                   1159480 |                    431953 |
| ADP                       |                   2876098 |                   1120538 |
| ADV                       |                    393759 |                    172318 |
| AUX                       |                    352013 |                    158102 |
| CCONJ                     |                    432498 |                    169891 |
| DET                       |                   2243620 |                    942251 |
| INTJ                      |                      4007 |                       516 |
| NOUN                      |                   4196733 |                   1553242 |
| NUM                       |                   1282043 |                    221234 |
| PRON                      |                    310189 |                    135963 |
| PROPN                     |                   2051089 |                    404111 |
| PUNCT                     |                   2950228 |                    839898 |
| ROOT-POS                  |                      2860 |                       108 |
| SCONJ                     |                    196300 |                     89200 |
| SYM                       |                     88581 |                     18718 |
| VERB                      |                   1309589 |                    530764 |
| X                         |                     23916 |                      3538 |
| acl                       |                    277673 |                    111724 |
| acl:relcl                 |                    105921 |                     44746 |
| advcl                     |                    238195 |                    102720 |
| advmod                    |                    353065 |                    155579 |
| amod                      |                   1040935 |                    379450 |
| appos                     |                    501333 |                    122653 |
| appos:parataxis           |                    127773 |                     34745 |
| aux                       |                     32584 |                     14188 |
| aux:pass                  |                    171653 |                     79135 |
| case                      |                   2850078 |                   1097916 |
| cc                        |                    431019 |                    172614 |
| ccomp                     |                     54289 |                     23330 |
| ccomp:parataxis           |                        16 |                         8 |
| compound                  |                     15930 |                      5091 |
| conj                      |                    824433 |                    245054 |
| cop                       |                    156577 |                     68630 |
| csubj                     |                     23301 |                      9417 |
| det                       |                   2247292 |                    939892 |
| discourse                 |                       608 |                       239 |
| dislocated                |                         6 |                         1 |
| expl                      |                     65400 |                     29638 |
| fixed                     |                    180713 |                     54764 |
| flat                      |                    391525 |                      7600 |
| flat:foreign              |                      6027 |                       900 |
| flat:name                 |                   1004018 |                    155620 |
| iobj                      |                      3080 |                      1146 |
| mark                      |                    217240 |                     97532 |
| nmod                      |                   1835516 |                    693562 |
| nsubj                     |                    548915 |                    222608 |
| nsubj:pass                |                    163408 |                     74412 |
| nummod                    |                    500610 |                    109042 |
| obj                       |                    600981 |                    228087 |
| obl                       |                    713092 |                    299986 |
| obl:agent                 |                     66660 |                     28751 |
| orphan                    |                         0 |                         1 |
| parataxis                 |                     97158 |                     14120 |
| punct                     |                   2904621 |                    840643 |
| root                      |                    981720 |                    268984 |
| vocative                  |                         4 |                         3 |
| xcomp                     |                    139634 |                     57814 |

## Distribuição relativa das categorias gramaticais

| Anotação                  | GAMBIARRA                 | FINAL                     |
| ---                       | ---                       | ---                       |
| ADJ                       | 5.834447868799698%        | 6.359409011173608%        |
| ADP                       | 14.47238748970148%        | 16.497071335451896%       |
| ADV                       | 1.9813764432079037%       | 2.5369441628774747%       |
| AUX                       | 1.7713125691170075%       | 2.327649729217229%        |
| CCONJ                     | 2.176309237209897%        | 2.5012127623081573%       |
| DET                       | 11.289788463273517%       | 13.872248833061334%       |
| INTJ                      | 0.02016303223020698%      | 0.007596787265664509%     |
| NOUN                      | 21.1177596058331%         | 22.86753691103735%        |
| NUM                       | 6.451179019094397%        | 3.257107817697717%        |
| PRON                      | 1.5608562027590898%       | 2.0017092771347746%       |
| PROPN                     | 10.320981685556028%       | 5.949506392858431%        |
| PUNCT                     | 14.845406101936382%       | 12.365361300110639%       |
| ROOT-POS                  | 0.014391383124130762%     | 0.0015900252416507113%    |
| SCONJ                     | 0.987772205338066%        | 1.3132430699559579%       |
| SYM                       | 0.4457353526288905%       | 0.2755749303075742%       |
| VERB                      | 6.589789172778769%        | 7.814149605180538%        |
| X                         | 0.12034416741143752%      | 0.052088049120002006%     |
| acl                       | 1.397237246932434%        | 1.6448516675757783%       |
| acl:relcl                 | 0.53298940275911%         | 0.6587710135453956%       |
| advcl                     | 1.1985858402980163%       | 1.5122906742811209%       |
| advmod                    | 1.7766061827696598%       | 2.2905049728775553%       |
| amod                      | 5.23793510220876%         | 5.586435906892244%        |
| appos                     | 2.52268366285659%         | 1.8057533885572654%       |
| appos:parataxis           | 0.642947620950895%        | 0.5115317316773514%       |
| aux                       | 0.16396112857226458%      | 0.20888220489389156%      |
| aux:pass                  | 0.8637496809113349%       | 1.1650615509076763%       |
| case                      | 14.34145609498474%        | 16.164019937149835%       |
| cc                        | 2.1688669799929077%       | 2.541302009836073%        |
| ccomp                     | 0.27317964979927795%      | 0.34347489710843604%      |
| ccomp:parataxis           | 8.05112342608714e-05%     | 0.00011777964752968232%   |
| compound                  | 0.08015899761098008%      | 0.07495202319670158%      |
| conj                      | 4.148507399712062%        | 3.607796718217346%        |
| cop                       | 0.7878879704290288%       | 1.0104021512452621%       |
| csubj                     | 0.11724951684453527%      | 0.13864136759837728%      |
| det                       | 11.308265791536387%       | 13.83751855949602%        |
| discourse                 | 0.003059426901913113%     | 0.003518666969949259%     |
| dislocated                | 3.0191712847826773e-05%   | 1.472245594121029e-05%    |
| expl                      | 0.32908967004131184%      | 0.4363441491855906%       |
| fixed                     | 0.9093391673115533%       | 0.8062605771644403%       |
| flat                      | 1.9701350621242297%       | 0.1118906651531982%       |
| flat:foreign              | 0.030327575555641993%     | 0.01325021034708926%      |
| flat:name                 | 5.052170525008223%        | 2.291108593571145%        |
| iobj                      | 0.015498412595217744%     | 0.01687193450862699%      |
| mark                      | 1.0931412831769813%       | 1.4359105728581218%       |
| nmod                      | 9.236228666598603%        | 10.21093598749769%        |
| nsubj                     | 2.762114009644139%        | 3.27733647216094%         |
| nsubj:pass                | 0.8222612355062796%       | 1.09552739149734%         |
| nummod                    | 2.519045561458427%        | 1.6053660407414523%       |
| obj                       | 3.024107629833297%        | 3.358000808262831%        |
| obl                       | 3.588244816347082%        | 4.41653066797991%         |
| obl:agent                 | 0.3354299297393554%       | 0.423285330765737%        |
| orphan                    |                         0 | 1.472245594121029e-05%    |
| parataxis                 | 0.48889440614485896%      | 0.20788107788988927%      |
| punct                     | 14.615913860627908%       | 12.37632952978684%        |
| root                      | 4.939968056161416%        | 3.960105088890508%        |
| vocative                  | 2.012780856521785e-05%    | 4.4167367823630867e-05%   |
| xcomp                     | 0.7026316052989072%       | 0.8511640677851315%       |

## Quantidade de lemas diferentes

|                         |GAMBIARRA                |FINAL                    |
|---                      |---                      |---                      |
|Lemas diferentes         |                   343451|                   134016|

## Distribuição dos lemas encontrados em ambas as versões