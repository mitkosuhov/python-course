from tkinter import *

tasks = [
    ['Почистване', 'Почистване на общи части'],
    ['Преместване', 'Преместване на стари елементи'],
    ['Сортиране', 'Сортиране на нови елементи']
]

root = Tk()
root.geometry('400x230')
root.configure(bg='#a27341')

global edit_window
edit_window = Toplevel()
edit_window.geometry('400x230')
edit_window.configure(bg='#a27341')

def close_window():
    root.destroy()

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
            break
    update_buttons()

def update_buttons():
    for widget in edit_window.winfo_children():
        widget.destroy()
    for task in tasks:
        title = task[0]
        button = Button(edit_window, text=title, command=lambda t=title: display_task_description(t), bg='#4d98d0')
        button.pack()
    exit_button = Button(edit_window, text='Изход', command=edit_window.destroy, bg='#da3636')
    exit_button.pack(side=BOTTOM, anchor=SE, padx=20, pady=20)

def add_task_to_list():
    title = e1.get()
    description = e2.get()
    tasks.append([title, description])
    print("Задачата е добавена успешно.")
    print(tasks)
    update_buttons()

def add_task():
    task = Toplevel()
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
    exit_button.grid(row=350, column=350, sticky="se", padx=20, pady=20)

def edit_task():
    update_buttons()
    edit_window.lift()

def delete_task_window():
    update_buttons()
    edit_window.lift()

button1 = Button(root, text='Въвеждане на задача', command=add_task, bg='#4d98d0')
button2 = Button(root, text='Преглед на задача', command=edit_task, bg='#4d98d0')
button3 = Button(root, text='Редактирване на задача', command=edit_task, bg='#4d98d0')
button4 = Button(root, text='Изтриване на задача', command=delete_task_window, bg='#4d98d0')
button5 = Button(root, text='Изход', command=close_window, bg='#da3636')

button1.pack(padx=2, pady=2)
button2.pack(padx=2, pady=2)
button3.pack(padx=2, pady=2)
button4.pack(padx=2, pady=2)
button5.pack(side=BOTTOM, anchor=SE, padx=20, pady=20)

root.mainloop()
