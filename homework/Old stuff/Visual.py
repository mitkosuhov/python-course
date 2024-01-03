from tkinter import *

tasks = [
    ['Почистване', 'Почистване на общи части'],
    ['Преместване', 'Преместване на стари елементи'],
    ['Сортиране', 'Сортиране на нови елементи']
]

root = Tk()
root.geometry('400x230')
root.configure(bg='#a27341')

def display_task(task_title):
    print(f"Selected task: {task_title}")

def close_window():
        exit(Toplevel)

def delete_task(task_title):
        for task in tasks:
            if task[0] == task_title:
                tasks.remove(task)
                break        

def clik1():
    task = Tk()
    task.geometry('400x230')
    task.configure(bg='#a27341')
    Label(task, text='Задача:').grid(row=0)
    Label(task, text='Описание').grid(row=5)
    e1 = Entry(task)
    e2 = Entry(task)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=2)
    exit_button = Button(task, text='Изход',command=task.destroy,bg='#da3636') 
    exit_button.pack(side=BOTTOM,anchor=SE,padx=20, pady=20)

    
def clik2():
    edit = Toplevel()
    edit.geometry('400x230')
    edit.configure(bg='#a27341')
    
    
    for task in tasks:
        # Създаване на бутон за всяко заглавие от списъка
            title = task[0]
            button = Button(edit, text=title, command=lambda t=title: display_task(t) )
            button.pack()       
    exit_button = Button(edit, text='Изход',command=edit.destroy,bg='#da3636') 
    exit_button.pack(side=BOTTOM,anchor=SE,padx=20, pady=20)

def clik4():
    edit = Toplevel()
    edit.geometry('400x230')
    edit.configure(bg='#a27341')
    
    
    for task in tasks:
        # Създаване на бутон за всяко заглавие от списъка
            title = task[0]
            button = Button(edit, text=title, command=lambda  t=title:display_task(t)  )
            button.pack()       
    exit_button = Button(edit, text='Изход',command=close_window,bg='#da3636') 
    exit_button.pack(side=BOTTOM,anchor=SE,padx=20, pady=20)


button1 = Button(root, text='Въвеждане на задача', command=clik1 ,bg='#4d98d0')
button2 = Button(root, text='Преглед на задача',command=clik2 ,bg='#4d98d0')
button3 = Button(root, text='Редактирване на задача',bg='#4d98d0')
button4 = Button(root, text='Изтриване на задача',command=clik4 ,bg='#4d98d0')
button5 = Button(root, text='Изход',command=root.quit,bg='#da3636')

button1.pack(padx=2, pady=2)
button2.pack(padx=2, pady=2)
button3.pack(padx=2, pady=2)
button4.pack(padx=2, pady=2)
button5.pack(side=BOTTOM,anchor=SE,padx=20, pady=20)

root.mainloop()
