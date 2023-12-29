from tkinter import *

tasks = [
    ['Почистване', 'Почистване на общи части'],
    ['Преместване', 'Преместване на стари елементи'],
    ['Сортиране', 'Сортиране на нови елементи']
]

root = Tk()
root.geometry('400x150')
root.configure(bg='#a27341')

def display_task(task_title):
    print(f"Selected task: {task_title}")

def clik1():
    new_task_name = entry.get()
    tasks.append([new_task_name, ''])
    update_task_buttons()
    
def clik2():
    for task in tasks:
        # Създаване на бутон за всяко заглавие от списъка
        title = task[0]
        button = Button(root, text=title, command=lambda t=title: display_task(t))
        button.pack()        

button1 = Button(root, text='Въвеждане на задача', command=clik1 ,bg='#4d98d0')
button2 = Button(root, text='Преглед на задача',command=clik2 ,bg='#4d98d0')
button3 = Button(root, text='Редактирване на задача')
button4 = Button(root, text='Изтриване на задача')
button5 = Button(root, text='Изход!')

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

root.mainloop()
