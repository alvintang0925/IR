import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os
jieba.load_userdict('dict.txt')
idx = []
doc = []
for file in os.listdir(r'D:\資訊檢索\python\txt'):
    domain = os.path.abspath(r'D:\資訊檢索\python\txt')
    str = file[:-4]
    idx.append(str)
    file = os.path.join(domain, file)
    file = open(file, 'r', encoding='utf-8')
    txt = file.read()
    sent_words = [list(jieba.cut(txt))]
    document = [" ".join(sent0) for sent0 in sent_words]
    doc += document
    #print(jieba.lcut(txt, cut_all=True, HMM=True))
    file.close()

# 轉換TFIDF
vectorizer = TfidfVectorizer(sublinear_tf=False, stop_words=None,
                             token_pattern="(?u)\\b\\w+\\b", smooth_idf=True, norm='l2')
tfidf = vectorizer.fit_transform(doc)
df_tfidf = pd.DataFrame(tfidf.toarray(
), columns=vectorizer.get_feature_names(), index=idx)
#print("TFIDF", df_tfidf)

df_tfidf.to_csv(r'test_tfidf.csv',  mode='a',
                columns=vectorizer.get_feature_names(), index=idx)

# print(jieba.lcut(text, cut_all=True, HMM=True))
# print(text)
