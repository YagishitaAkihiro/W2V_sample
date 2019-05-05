# W2V_sample
gensimのword2vecをやってみるコード(python2)

__参考サイト__  
[python] word2vecの使い方  
https://qiita.com/kenta1984/items/93b64768494f971edf86  

__やり方__  
1. コーパスを作る  
wikipediaからxmlを落とし、変換してMeCabで分かち書きした状態(utf-8形式)にする  
2. 学習モデルを作る  
このディレクトリに移動して  
`$ python make_model.py` 
3. 実行  
`$ python samplew2v.py`
