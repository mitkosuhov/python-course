from tkinter import *

tasks = [
    ['Почистване', 'Почистване на общи части'],
    ['Преместване', 'Преместване на стари елементи'],
    ['Сортиране', 'Сортиране на нови елементи']
]

root = Tk()
root.geometry('400x150')

def display_task(task_title):
    print(f"Selected task: {task_title}")

def clik1():
    for task in tasks:
        # Създаване на бутон за всяко заглавие от списъка
        title = task[0]
        button = Button(root, text=title, command=lambda t=title: display_task(t))
        button.pack()

button1 = Button(root, text='Въвеждане на задача', command=clik1)
button2 = Button(root, text='Преглед на задача')
button3 = Button(root, text='Редактирване на задача')
button4 = Button(root, text='Изтриване на задача')
button5 = Button(root, text='Изход!')

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

root.mainloop()


