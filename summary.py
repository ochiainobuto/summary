
# coding: utf-8

######################################################
# Python27 Version
#########################################################


#######https://qiita.com/riverwell/items/310e0a31f2e5097df7ff
#!/usr/bin/env python                                                                                                                                                    
# -*- coding: utf-8 -*-      
import collections
import re
import sys
import numpy as np
from scipy.spatial import distance
from gensim.models import word2vec
from janome.tokenizer import Tokenizer


def lexrank(sentences, N, threshold):

    CosineMatrix = np.zeros([N, N])
    degree = np.zeros(N)
    L = np.zeros(N)

    vector = compute_word2vec(sentences)

    # Computing Adjacency Matrix                                                                                                                                         
    for i in range(N):
        for j in range(N):
            CosineMatrix[i,j] = compute_cosine(vector[i], vector[j])*((N - abs(i-j))/float(N))
    
    # Computing LexRank Score                                                                                                                                            
    for i in range(N):
        for j in range(N):
            CosineMatrix[i,j] = CosineMatrix[i,j]/N
    
    L = PowerMethod(CosineMatrix, N, err_tol=10e-6)

    return L


def PowerMethod(CosineMatrix, N, err_tol):
    p_old = np.array([1.0/N]*N)
    err = 1

    while err > err_tol:
        err = 1
        p = np.dot(CosineMatrix.T, p_old)
        err = np.linalg.norm(p - p_old)
        p_old = p
    return p


def compute_cosine(v1, v2):

    return 1 - distance.cosine(v1, v2)

def sent2vec(bow, model_w):
    
    N = len(bow)
    vector = np.zeros(200) #200 is models length (len(model_w.wv[bow[b])!!!!!!!!)

    for b in range(len(bow)):
        try:
            vector += model_w.wv[bow[b]]
        except:
            continue
            
    vector = vector / float(N)
    
    ###########################################################
    word = model_w.most_similar( [ vector ], [], 1)
    
    ###########################################################
    return vector


def compute_word2vec(sentences):
    
    model_w = word2vec.Word2Vec.load("wiki.model")
    
    vector = []
    
    for i in range(len(sentences)):
        vector.append(sent2vec(sentences[i], model_w))
    
    
    return vector

if __name__ == "__main__":

    pass     



def sent_splitter_ja(text):

    sentences = re.split(ur'[。？！（） ]', text )

    return sentences



tokenizer = Tokenizer()


def word_splitter(sent):
    def _is_stopword(n):
        if len(n.surface) == 0:
            return True
        elif re.search(r'^[\s!-@\[-`\{-~　、-〜！-＠［-｀]+$', n.surface):
            return True
        elif re.search(u'^(接尾|非自立)', n.part_of_speech.split(ur',')[1]):
            return True
        elif 'サ変・スル' == n.infl_form or u'ある' == n.base_form:
            return True
        elif re.search(u'^(名詞|形容詞|副詞)', n.part_of_speech.split(ur',')[0]):
            return False
        else:
            return True

    return [n.base_form for n in tokenizer.tokenize(sent) if not _is_stopword(n)]



import codecs

# pn_ja.dicファイルから、単語をキー、極性値を値とする辞書を得る
def load_pn_dict():
    dic = {}
    
    with codecs.open('./pn_ja.dic', 'r', 'shift_jis') as f:
        lines = f.readlines()
        
        for line in lines:
            columns = line.split(':')
            dic[columns[0]] = float(columns[3])
            
    return dic



def get_summary(sentences):

    sent_limit = 16
    
    sentences = sentences.strip() #空白と改行を削除する
    sentences = sentences.replace('\n','')
    sentences = sentences.replace('\r','')
    
    ##### 行に分ける　##### 
    sentences = sent_splitter_ja(sentences)
    
    ##### sentencesリストからn文字以内の行を削除する　##### 
    del_lest = []
    for i in range(len(sentences)):
        words = word_splitter(sentences[i])

        if len(words) < 4:
            del_lest.append(i)
            
    del_lest.reverse()
    for num in del_lest:
        sentences.pop(num)
    
    # sentence -> tf
    sent_tf_list = []
    for sent in sentences:
        words = word_splitter(sent)
        sent_tf_list.append(words)
    
    ##### lexrank ##################################
    scores = lexrank(sent_tf_list, len(sentences),0.1)
    
    ############ 感情極性対応表のList ###################
    pn_dic = load_pn_dict()
    pn_dic_list = []

    for sent in sent_tf_list:
        #### Apply Sentiment Value #####
        pn_dic_val = 0
        for word in sent:
            try:
                pn_dic_val += abs(pn_dic[word])*0.5
            except:
                pass
        pn_dic_val = pn_dic_val/len(sent)
        pn_dic_list.append(pn_dic_val)
        
    dict = {}
    for i in range(len(sentences)):
        dict[i] = scores[i]*(1 - pn_dic_list[i])
    
    dict_sort = sorted(dict.items(), key=lambda x: x[1])
    
    ##### Check sent_limit ####
    if sent_limit > len(dict_sort):
        sent_limit = len(dict_sort)
    
    dict_limit = []
    for i in range(sent_limit):
        dict_limit.append(dict_sort[i][0])
    
    dict_limit = sorted(dict_limit)
    
    result = []
    for d in dict_limit:
        result.append(sentences[d])
        
        #print(sentences[d])
    result = u'。'.join(result) + u"。"
    return result




"""
#f = open('test4.txt',encoding='utf-8')
f = open('test8.txt','rb')
text = f.read()
f.close()

text = unicode(text,'utf-8')
#print text

####################################
results = summarize(text, sent_limit = 20)
#for result in results:

print results
"""



