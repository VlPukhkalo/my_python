film=input("Выберите фильм: ")
date=input("Выберите дату: ")
time=int(input("Выберите время: "))
num=int(input("Укажите количество билетов: "))
if film=="Паразиты":
    if time==12:
        p=250*num
    elif time==16:
        p=350*num
    elif time==20:
        p=450*num
elif film=="1917":
    if time==10:
        p=250*num
    elif time==13:
        p=350*num
    elif time==16:
        p=350*num
elif film=="Соник в кино":
    if time==10:
        p=350*num
    elif time==14:
        p=450*num
    elif time==18:
        p=450*num
if date=="Завтра"or date=="завтра":
    p=p*0.95
if num>=20:
    p=p*0.8
print("Выбрали фильм:",film,",  День:" ,date, ", Время:" ,time, ", Количество билетов:",num,"\n","Результат:",p,"руб.")

    
        

