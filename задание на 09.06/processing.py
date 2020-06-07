with open('wjrds.txt','r',encoding='utf-8') as f:
    words=f.read()
words=words.split()

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

norm=[morph.parse(w)[0].normal_form for w in words]

s=''
for i in norm:
    s=s+' '+i

with open('norm.txt','w',encoding='utf-8') as file:
    file.write(s)
