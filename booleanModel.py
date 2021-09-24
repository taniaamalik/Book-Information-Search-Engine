# Erlina Rohmawati	    175150201111045
# Tania Malik Iryana	175150201111053
# Alvina Eka Damayanti	175150201111056
# Jeowandha Ria Wiyani	175150207111029

import re
import pandas as pd
from pythonds.basic import Stack

###############################Proses Cleaning, Tokenization, Case Folding###############################
def cleaningTag(readCorpus) :
    #Membersihkan Tag
    regex = r"(<\w{3,}>|</\w{3,}>|[A-Z].*</\w{2}>)"
    corpusTanpaTag = re.sub(regex,"",readCorpus)
    corpusSplit = corpusTanpaTag.split('<id>\n')
    corpusSplit.remove("")

    return corpusSplit


def getCorpusLine(corpus):
    judul = []
    penulis = []
    for c in corpus:
        tes = c.split('\n')
        judul.append(tes[0])
        penulis.append(tes[1])

    return judul, penulis


def cleaningTokenisasi(corpus) :
    #Membersihkan Tanda Baca dan Case Folding
    for c in range(len(corpus)):
        corpus[c] = re.sub(r"[^a-zA-Z]", " ", corpus[c]).lower()
        corpus[c] = re.split(r"[\s+]+", corpus[c])
        corpus[c].remove("")

    return corpus


###############################Proses Menghilangkan Stopword###############################
def stopwordRemoval(corpusToken) :
    stopwordTeks = open('D:/Tania/UB/Semester 6/STKI/Project Akhir/Stopword.txt', 'r')
    stopwordRead = stopwordTeks.read().split('\n')
    stopwordTeks.close()
    for kata in stopwordRead :
        for c in range(len(corpusToken)):
            while(kata in corpusToken[c]):
                corpusToken[c].remove(kata)

    return corpusToken


###############################Boolean Retrieve###############################
def cariTerm(document):
    termsTraining = []
    for doc in range(0, len(document)):
        for word in document[doc]:
            if word not in termsTraining:
                termsTraining.append(word)

    return termsTraining


def kemunculanKata(term, document):
    inMatrix = {}

    for kata in term :
        temp = []
        inMatrix.get(kata,0)
        for doc in range(0, len(document)):            
            if kata in document[doc]:
                temp.append(1)
            else:
                temp.append(0)
        inMatrix[kata] = temp

    return inMatrix


def infixToPostfix(infixQuery,term):
    queryList = infixQuery.split() 
    queryStack = Stack()
    postfixQuery = []
    precOperator = {}
    precOperator["not"] = 4
    precOperator["and"] = 3
    precOperator["or"] = 2
    precOperator["("] = 1

    for query in queryList:
        if query in term:
            postfixQuery.append(query)
            indexNext = queryList.index(query)+1
            if indexNext != len(queryList) and (queryList[indexNext] in term):
                queryStack.push("and")
        elif query == '(':
            queryStack.push(query)
        elif query == ')':
            stackTeratas = queryStack.pop()
            while stackTeratas != '(':
                postfixQuery.append(stackTeratas)
                stackTeratas = queryStack.pop()
        else:
            while (queryStack.isEmpty() != True) and (precOperator[queryStack.peek()] >= precOperator[query]):
                  postfixQuery.append(queryStack.pop())
            queryStack.push(query)

    while (queryStack.isEmpty() != True):
        postfixQuery.append(queryStack.pop())

    return postfixQuery


def hasilPostfix(queryList,doc, term, matrix):
    queryStack = Stack()
    hasil = []    
    for query in queryList:
        if(len(queryList) == 1) :
            hasil = matrix.get(query)
            break
        if query in term:
            queryStack.push(matrix.get(query))
        elif query == "not":
            queryNot = queryStack.pop()
            queryNotUpdateValue = booleanNot(queryNot)
            hasil = queryNotUpdateValue
            queryStack.push(queryNotUpdateValue)
        else:
            query2 = queryStack.pop()
            query1 = queryStack.pop()
            hasil = boolean(query, doc, query1, query2)
            queryStack.push(hasil)

    return hasil


def booleanNot(query):
    for q in range (len(query)):
        query[q] = int(not query[q])

    return query


def boolean(operator, document, queryA, queryB):
    hasil = []
    
    for doc in range (len(document)):
        if(operator == "and"):
            query = queryA[doc] & queryB[doc]
        if(operator == "or"):
            query = queryA[doc] | queryB[doc]
        if query:
            hasil.append(1)
        else:
            hasil.append(0)

    return hasil