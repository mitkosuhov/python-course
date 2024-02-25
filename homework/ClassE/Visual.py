from tkinter import *

tasks = [
    ['Почистване', 'Почистване на общи части'],
    ['Преместване', 'Преместване на стари елементи'],
    ['Сортиране', 'Сортиране на нови елементи']
]

root = Tk()
root.geometry('400x230')
root.configure(bg='#a27341')





def close_window():
        exit(Toplevel)

def display_task_description(task_title):
    for task in tasks:
        if task[0] == task_title:
            description_label.config(text=task[1])
            break
def delete_task(task_title):
    for task in tasks:
        if task[0] == task_title:
            tasks.remove(task)
            print(f"Задачата '{task_title}' е изтрита успешно.")
            print(tasks)
            return
    print("Задачата не е намерена.")


def clik1():
    def add_task_to_list():
        title = e1.get()
        description = e2.get()
        tasks.append([title, description])
        print("Задачата е добавена успешно.")
        print(tasks)
        task.destroy()
        
    task = Tk()
    task.geometry('400x230')
    task.configure(bg='#a27341')

    # Етикети
    Label(task, text='Задача:').grid(row=0, column=0)
    Label(task, text='Описание').grid(row=1, column=0)

    # Текстови полета
    e1 = Entry(task)
    e2 = Entry(task)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    add_button = Button(task, text='Добави задача', command=add_task_to_list, bg='#4d98d0')
    add_button.grid(row=2, columnspan=2, pady=10)

    # Бутон за изход
    exit_button = Button(task, text='Изход', command=task.destroy, bg='#da3636') 
    exit_button.grid(row=2, column=1, sticky="se", padx=20, pady=20)

    
def clik2():
    edit = Toplevel()
    edit.geometry('400x230')
    edit.configure(bg='#a27341')
    
    global description_label
    description_label = Label(edit, text="", bg='#a27341')
    description_label.pack(padx=20, pady=20)
    
    for task in tasks:
        # Създаване на бутон за всяко заглавие от списъка
            title = task[0]
            button = Button(edit, text=title, command=lambda t=title: display_task_description(t) )
            button.pack()       
    exit_button = Button(edit, text='Изход', command=edit.destroy, bg='#da3636')
    exit_button.pack(side=BOTTOM,anchor=SE,padx=20, pady=20)

def clik3():
    
    edit = Toplevel()
    edit.geometry('400x230')
    edit.configure(bg='#a27341')

    for task in tasks:
        # Създаване на бутон за всяко заглавие от списъка
            title = task[0]
            button = Button(edit, text=title, command=lambda  t=title:delete_task(t)  )
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
            button = Button(edit, text=title, command=lambda  t=title:delete_task(t)  )
            button.pack()       
    exit_button = Button(edit, text='Изход',command=edit.destroy,bg='#da3636') 
    exit_button.pack(side=BOTTOM,anchor=SE,padx=20, pady=20)


button1 = Button(root, text='Въвеждане на задача', command=clik1 ,bg='#4d98d0')
button2 = Button(root, text='Преглед на задача',command=clik2 ,bg='#4d98d0')
button3 = Button(root, text='Редактирване на задача',command=clik3 ,bg='#4d98d0')
button4 = Button(root, text='Изтриване на задача',command=clik4 ,bg='#4d98d0')
button5 = Button(root, text='Изход',command=root.quit,bg='#da3636')

button1.pack(padx=2, pady=2)
button2.pack(padx=2, pady=2)
button3.pack(padx=2, pady=2)
button4.pack(padx=2, pady=2)
button5.pack(side=BOTTOM,anchor=SE,padx=20, pady=20)

root.mainloop()
