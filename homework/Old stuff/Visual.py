from tkinter import *
tasks = [['Почистване','Почистване на общи части'],['Преместване','Преместване на стари елементи'],['Сортиране','Сортиране на нови елементи']]
root = Tk()
root.geometry('400x150')
def clik1():
    q = [i[0] for i in tasks]
    l = Label(root , text=q)
    l.pack()


button1 = Button(root,text='Въвеждане на задача ',command=clik1)
button2 = Button(root,text='Преглед на задача ')
button3 = Button(root,text='Редактирване на задача')
button4 = Button(root,text='Изтриване на задача')
button5 = Button(root,text='Изход!')
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
root.mainloop()


