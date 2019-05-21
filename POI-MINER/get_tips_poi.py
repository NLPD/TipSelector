#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:44:21 2017

@author: Di
"""
import re
from nltk import tokenize
from collections import Counter
reviews=[]
sentences=[]
with open('d84082.txt') as f:
    for line in f:
        x,y=line.decode('utf-8').strip().split('\t')
        reviews.append(y.replace('<br/>', ' '))

for x in reviews:
    y=tokenize.sent_tokenize(x)
    for z in y:
        sentences.append(z.lower())

temps=[]
with open('templates_baseline.txt') as f:
    for line in f:
        x=line.strip()
        temps.append(x)

candidates=set()
reason=[]   
count={}     
for sentence in sentences:
    for t in temps:
        if re.search(' '+t+' ',sentence):
            if sentence not in candidates:
                candidates.add(sentence)
                reason.append(t)
#                print sentence, t
                if t in count:
                    count[t]+=1
                else:
                    count[t]=1

c=Counter(count)
l=[]
for x in c.most_common(5):
    l.append(x[0])

#print l
candidates=set()
reason=[]  


for sentence in sentences:
    for t in l:
        if re.search(' '+t+' ',sentence):
            if sentence not in candidates:
                candidates.add(sentence)
                reason.append(t)
                print sentence, t  
                
with open('d84082_tips_poi.txt','w') as f:
    for x in candidates:
        f.write(x.encode('utf-8')+'\n')

print len(candidates)
