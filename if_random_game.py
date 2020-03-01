import random
r=random.randint(1,4)
m=int(input("Попробуйте угадать число:"))
if m==r:
    print("Победа")
elif m>r:
    print("Загаданное число меньше")
else:
    print("Загаданное число больше")

    
#https://drakonhub.com/ide/doc/if_random_game/2
