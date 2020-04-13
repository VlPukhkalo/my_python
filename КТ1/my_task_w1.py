from tkinter import *
import json
l=[]

def add_task():
    with open('todo.json','w') as file:
        json.dump({"задача":task.get(),"категория":kind.get(),"время":time.get()},file)
        l.append({"задача":task.get(),"категория":kind.get(),"время":time.get()})
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)

def output_tasks():
    print(l)


window=Tk()
window.title('Task manager')
window.geometry("+300+250")
window["bg"] = "black"

task=StringVar()
kind=StringVar()
time=StringVar()

label1=Label(text='Введите задачу:',bg='pink')
label2=Label(text='Введите категорию:',bg='pink')
label3=Label(text='Введите время:',bg='pink')

label1.grid(row=0,column=0,sticky='w')
label2.grid(row=1,column=0,sticky='w')
label3.grid(row=2,column=0,sticky='w')

ent1=Entry(textvariable=task)
ent2=Entry(textvariable=kind)
ent3=Entry(textvariable=time)

ent1.grid(row=0,column=1,padx=5,pady=5)
ent2.grid(row=1,column=1,padx=5,pady=5)
ent3.grid(row=2,column=1,padx=5,pady=5)

button1=Button(text='Добавить задачу!',bg='grey',command=add_task)
button1.grid(row=4,column=0)

button2=Button(text='Вывести список задач!',bg='grey',command=output_tasks)
button2.grid(row=5,column=0)

button3=Button(text='Выход',bg='grey',command=exit)
button3.grid(row=6,column=1)

window.mainloop()
