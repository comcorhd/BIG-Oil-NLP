Para baixar os modelos pré-treinados, considerar [ler a página no wiki](https://github.com/comcorhd/BIG-Oil-NLP/wiki/Como-trabalhar-no-reposit%C3%B3rio).

# Neural Network Models for Joint POS Tagging and Dependency Parsing 


Implementations of joint models for  POS tagging and dependency parsing, as described in my papers:
  
  1. Dat Quoc Nguyen and Karin Verspoor. **2018**. [An improved neural network model for joint POS tagging and dependency parsing](http://www.aclweb.org/anthology/K18-2008). In *Proceedings of the CoNLL 2018 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies*, pages 81-91. [[.bib]](http://www.aclweb.org/anthology/K18-2008.bib) (**jPTDP v2.0**)
  2. Dat Quoc Nguyen, Mark Dras and Mark Johnson. **2017**. [A Novel Neural Network Model for Joint POS Tagging and Graph-based Dependency Parsing](http://www.aclweb.org/anthology/K17-3014). In *Proceedings of the CoNLL 2017 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies*, pages 134-142. [[.bib]](http://www.aclweb.org/anthology/K17-3014.bib)  (**jPTDP v1.0**)


### Installation

jPTDP requires the following software packages:

* `Python 2.7`
* [`DyNet` v2.0](http://dynet.readthedocs.io/en/latest/python.html)

      $ virtualenv -p python2.7 .DyNet
      $ source .DyNet/bin/activate
      $ pip install cython numpy
      $ pip install dynet==2.0.3

Once you installed the prerequisite packages above, you can clone or download (and then unzip) jPTDP. Next sections show instructions to train a new joint model for POS tagging and dependency parsing, and then to utilize a pre-trained model.


### Train a joint model 

Suppose that `SOURCE_DIR` is simply used to denote the source code directory. Similar to files `train.conllu` and `dev.conllu` in folder `SOURCE_DIR/sample` or treebanks in the [Universal Dependencies (UD) project](http://universaldependencies.org/), the training and development files are formatted following 10-column data format. For training, jPTDP will only use information from columns 1 (ID), 2 (FORM), 4 (Coarse-grained POS tags---UPOSTAG), 7 (HEAD) and 8 (DEPREL). 


__To train a joint model for POS tagging and dependency parsing, you perform:__

    SOURCE_DIR$ python jPTDP.py --dynet-seed 123456789 [--dynet-mem <int>] [--epochs <int>] [--lstmdims <int>] [--lstmlayers <int>] [--hidden <int>] [--wembedding <int>] [--cembedding <int>] [--pembedding <int>] [--prevectors <path-to-pre-trained-word-embedding-file>] [--model <String>] [--params <String>] --outdir <path-to-output-directory> --train <path-to-train-file>  --dev <path-to-dev-file>

where hyper-parameters in [] are optional:

 * `--dynet-mem`: Specify DyNet memory in MB.
 * `--epochs`: Specify number of training epochs. Default value is 30.
 * `--lstmdims`: Specify number of BiLSTM dimensions. Default value is 128.
 * `--lstmlayers`: Specify number of BiLSTM layers. Default value is 2.
 * `--hidden`: Specify size of MLP hidden layer. Default value is 100.
 * `--wembedding`: Specify size of word embeddings. Default value is 100.
 * `--cembedding`: Specify size of character embeddings. Default value is 50.
 * `--pembedding`: Specify size of POS tag embeddings. Default value is 100.
 * `--prevectors`: Specify path to the pre-trained word embedding file for initialization. Default value is "None" (i.e. word embeddings are randomly initialized).
 * `--model`: Specify a  name for model parameters file. Default value is "model".
 * `--params`: Specify a  name for model hyper-parameters file. Default value is "model.params".
 * `--outdir`: Specify path to directory where the trained model will be saved. 
 * `--train`: Specify path to the training data file.
 * `--dev`: Specify path to the development data file. 


### Utilize a pre-trained model

__To utilize a pre-trained model for POS tagging and dependency parsing, you perform:__

    SOURCE_DIR$ python jPTDP.py --predict --model <path-to-model-parameters-file> --params <path-to-model-hyper-parameters-file> --test <path-to-10-column-input-file> --outdir <path-to-output-directory> --output <String>
 
* `--model`: Specify path to model parameters file.
* `--params`: Specify path to model hyper-parameters file.
* `--test`: Specify path to 10-column input file.
* `--outdir`: Specify path to directory where output file will be saved.
* `--output`: Specify name of the  output file.


