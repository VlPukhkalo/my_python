import tkinter
import random

eng=['time','person' ,'year' ,'way' ,'day','thing','man' ,'World' ,'life' ,'hand','part','child' ,'eye','woman' ]
rus=["время", "личность", "год", "путь", "день", "вещь", "мужчина" ,"мир", "жизнь", "рука","часть","ребёнок", "глаз", "женщина"]
d=dict(zip(eng,rus))

def click():
    if d.get(r)==entry.get():
        label.config(text='Вы угадали!')
    else:
        label.config(text='Вы не угадали :(')

window = tkinter.Tk()

first = tkinter.Label(window, text='Случайное слово:')
first.pack()

r=random.choice(eng)
second = tkinter.Label(window, text=r)
second.pack()

third = tkinter.Label(window, text='Укажите перевод слова:')
third.pack()

entry = tkinter.Entry(window)
entry.pack()

label = tkinter.Label(window)
label.pack()

button = tkinter.Button(window, text='Готово!', command=click)
button.pack()

window.mainloop()
