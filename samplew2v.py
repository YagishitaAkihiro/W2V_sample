#!/usr/bin/env python
#-*- coding:utf-8 -*-

from gensim.models import word2vec

model = word2vec.Word2Vec.load("./wiki.model")
in_word = "物語"

print "入力単語：「"+ in_word + "」に近似した単語を表示します"

try:
  results = model.wv.most_similar(positive=[in_word.decode('utf-8')])
  for result in results:
      print("(" + result[0] + ", " + str(result[1]) +")")

except KeyError as e:
    print e.message

except:
   print "unkown error"
