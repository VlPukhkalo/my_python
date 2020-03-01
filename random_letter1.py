l=['самовар', 'весна', 'лето']
import random
w=random.choice(l)
s=random.choice(w)
p=w.find(s)
print(w[:p],'?',w[p+1:],sep='')
x=input('Введите букву: ')
if x==s:
    print('Победа!')
else:
    print('Увы! Попробуйте в другой раз.')
print('Слово: ',w)
