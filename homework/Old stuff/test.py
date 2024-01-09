from tkinter import *

tasks = [
    ['Почистване', 'Почистване на общи части'],
    ['Преместване', 'Преместване на стари елементи'],
    ['Сортиране', 'Сортиране на нови елементи'] ]

root = Tk()
root.geometry('400x230')
root.configure(bg='#a27341')


button1 = Button(root, text='Въвеждане на задача', bg='#4d98d0')
button2 = Button(root, text='Преглед на задача',bg='#4d98d0')
button3 = Button(root, text='Редактирване на задача',bg='#4d98d0')
button4 = Button(root, text='Изтриване на задача',bg='#4d98d0')
button5 = Button(root, text='Изход',command=root.quit,bg='#da3636')

button1.pack(padx=2, pady=2)
button2.pack(padx=2, pady=2)
button3.pack(padx=2, pady=2)
button4.pack(padx=2, pady=2)
button5.pack(side=BOTTOM,anchor=SE,padx=20, pady=20)
root.mainloop()