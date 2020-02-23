element=input("Введите атомный номер элемента: ")
if element:
    numb=int(element)
    if numb==3:
        print("Литий")
    elif numb==25:
        print("Марганец")
    elif numb==80:
        print("Ртуть")
    elif numb==17:
        print("Хлор")
    else:
        print("Я не знаю ответ")
else:
    print('Введите атомный номер элемента!')
