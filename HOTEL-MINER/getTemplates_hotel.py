#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:04:04 2017

@author: Di
"""
import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
import codecs
from collections import Counter


with codecs.open('tips.txt', "r", encoding='utf-8', errors='ignore') as f:
    text = f.read().strip()
    allTips = sent_tokenize(text)

tips = []

for tip in allTips:
    tip = tip.lower()
    tip = re.sub('it\'s', 'it is', tip)
    tip = re.sub('you\'re', 'you are', tip)
    tip = re.sub('won\'t', 'will not', tip)
    tip = re.sub('don\'t', 'do not', tip)
    tip = re.sub('can\'t', 'can not', tip)
    tip = re.sub('haven''t', 'have not', tip)
    tip = re.sub('i\'ve', 'i have', tip)
    tip = re.sub('[^a-zA-Z\d]', ' ', tip)
    tip = re.sub(' +', ' ', tip).strip()
    terms = nltk.word_tokenize(tip)
    if len(terms) > 3:
        tips.append(terms)


def getFreq(termsList):
    d = {}
    for i in range(4, 8):
        l = []
        for terms in termsList:
            if len(terms) >= i:
                grams = ngrams(terms, i)
                for g in grams:
                    l.append(g)
        for position in xrange(i):
            thisL = l[:]
            for words in thisL:
                wordsL = list(words)
                wordsL[position] = 'XXX'
                template = ' '.join(wordsL)
                if template in d:
                    d[template] += 1
                else:
                    d[template] = 1
    d = Counter(d)
    return d


templateCounter = getFreq(tips)
with open('templates_hotel.txt', 'w') as f:
    for k, v in templateCounter.most_common(300):
        f.write(k + '\n')
