#wget http://mattmahoney.net/dc/text8.zip -P /tmp
#unzip text8.zip

import json
import requests
import gensim.models

model = gensim.models.Word2Vec()
sentences = gensim.models.word2vec.LineSentence("/home/shashank/Downloads/text8")
model.build_vocab(sentences)
model.train(sentences)
model.save("/home/shashank/Downloads/model")
