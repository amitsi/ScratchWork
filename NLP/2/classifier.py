import math
import ply.lex as lex
import re
import nltk
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
lis = ['HASH','URL','RT', 'ID', 'SLANG', 'HEMO','SEMO','NEMO','SNAME']
# List of token names.   This is always required
tokens = (
   'HASH',
   'URL',
   'RT',
   'SNAME',
   'SLANG',
   'SKIP',
   'HEMO',
   'NEMO',
   'SEMO',
)

def t_HASH(t):
    r'\#[a-zA-Z0-9]+'
    return t
def t_RT(t):
    r'RT\s'
    return t
def t_URL(t):
    r'http:\/\/[a-zA-Z0-9]+(\.[a-zA-Z0-9]*)*(\/[a-zA-Z0-9]*)?'
    return t
def t_SLANG(t):
    r'[Rr][Oo][Ff][Ll]|[Ll][Oo][Ll]|FYI|[Oo][Mm][Gg]'
    return t
def t_HEMO(t):
    r'[\:\;\^][_\-\.]?[\)\^PD*]'
    return t
def t_SEMO(t):
    r'[\:\;\^TP][_\-\.]?[\(\/Tq*]'
    return t
def t_NEMO(t):
    r'[\:\;\^][_\-\.]?[\|O*]'
    return t
def t_SNAME(t):
    r'[@][_a-zA-Z0-9]+'
    return t
def t_SKIP(t):
    r'\s\s+|[-]+|:\s'
    return t

# Error handling rule
def t_error(t):
    #print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
def getWords(inputFileName):
    tweet = [i for i in open(inputFileName).read().split('\n') if re.search(r'[\w]+',i)]
    for i in tweet:
        i = i.strip()
        lexer.input(i)
        j = i
        for tok in lexer:
            j = j.replace(tok.value,' ')
        #Case conversion to lower
        j = j.lower()
        #Stop words removal and Stemming
        j = re.sub(r'\.+',' ',j)
        j = ''.join([l for l in j if(ord(l)<128)])
        t = re.split(r'\s+',j)
        stopwords = nltk.corpus.stopwords.words()
        stemmer = PorterStemmer()
        for k in range(len(t)):
            t[k] = stemmer.stem(t[k])
            t[k] = wnl.lemmatize(t[k])
            if(t[k] in stopwords):
                t[k] = ''
            t[k] = re.sub(r'\W+','',t[k])
            if(t[k] not in main):
                main[t[k]] = [0.0,0.0,0.0]

def getProbability(inputFileName,index):
    wordCount = {}
    probCount = {}
    tweet = [i for i in open(inputFileName).read().split('\n') if re.search(r'[\w]+',i)]
    for i in tweet:
        i = i.strip()
        lexer.input(i)
        j = i
        for tok in lexer:
            j = j.replace(tok.value,' ')
        #Case conversion to lower
        j = j.lower()
        #Stop words removal and Stemming
        j = re.sub(r'\.+',' ',j)
        j = ''.join([i for i in j if(ord(i)<128)])
        t = re.split(r'\s+',j)
        stopwords = nltk.corpus.stopwords.words()
        stemmer = PorterStemmer()
        for k in range(len(t)):
            t[k] = stemmer.stem(t[k])
            t[k] = wnl.lemmatize(t[k])
            if(t[k] in stopwords):
                t[k] = ''
            t[k] = re.sub(r'\W+','',t[k])
            if(t[k] in wordCount):
                wordCount[t[k]] += 1
            else:
                wordCount[t[k]] = 1
    total = sum(map(lambda x:x+1,wordCount.values()))
    for w in main:
        if(w in wordCount):
            main[w][index] = float((wordCount[w]+1))/total
        else:
            main[w][index] = 1.0/total

def calAccuracy(inputFileName,sentiment):
    tweet = [i for i in open(inputFileName).read().split('\n') if re.search(r'[\w]+',i)]
    count = [0,0]
    for i in tweet:
        i = i.strip()
        lexer.input(i)
        j = i
        for tok in lexer:
            j = j.replace(tok.value,' ')
        #Case conversion to lower
        j = j.lower()
        #Stop words removal and Stemming
        j = re.sub(r'\.+',' ',j)
        j = ''.join([l for l in j if(ord(l)<128)])
        t = re.split(r'\s+',j)
        stopwords = nltk.corpus.stopwords.words()
        stemmer = PorterStemmer()
        maxProb = -1
        maxI = -1
        prob = [1.0, 1.0, 1.0]
        for k in range(len(t)):
            t[k] = stemmer.stem(t[k])
            t[k] = wnl.lemmatize(t[k])
            if(t[k] in stopwords):
                t[k] = ''
            t[k] = re.sub(r'\W+','',t[k])
            if main.get(t[k]):
                prob[0] *= main[t[k]][0]
                prob[1] *= main[t[k]][1]
                prob[2] *= main[t[k]][2]
        for s in range(3):
            if(maxProb<prob[s]):
                maxProb = prob[s]
                maxI = s
        if maxI==sentiment:
            count[0] += 1
        count[1] += 1
    return count

main = {}
getWords('TRAINING.txt')
getProbability("positive_training.txt",0)
getProbability("negative_training.txt",1)
getProbability("neutral_training.txt",2)
c1 = math.log(0.288)
c2 = math.log(0.136)
c3 = math.log(0.576)
for i in main:
    print i,'[Pos_Prob: ',main[i][0],'] [Neg_Prob: ',main[i][1],'] [Neut_Prob: ',main[i][2],']'
    c1 += math.log(main[i][0])
    c2 += math.log(main[i][1])
    c3 += math.log(main[i][2])

a = calAccuracy('positive_test.txt',0)
b = calAccuracy('negative_test.txt',1)
c = calAccuracy('neutral_test.txt',2)
print '---------------------------------------------------'
print 'Accuracy:',float(a[0]+b[0]+c[0])/(a[1]+b[1]+c[1])*100,'%'
print '---------------------------------------------------'
