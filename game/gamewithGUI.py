'''ДОБАВИТЬ:
ПРОВЕРКУ НА ПУСТОЕ ПОЛЕ ВВОДА'''

import random
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

def gen(): # функция генерации случайного числа
    global gen_number # глобальное значение загадонного числа
    gen_number = random.randint(0,1000) # рандомим
    btn['state'] = 'normal' # устанавливаем видимость кнопки проверки числа
    history.delete(1.0, END) # удаляем всю историю из scrolledtext

def clicked(): # функция обработчик проверки
    input_number = int(txt.get()) # читаем введенное число
    status = check_number(input_number, gen_number) # отправляем его на проверку в функцию
    history.insert(INSERT, txt.get() + ' - ' + status +'\n') # добавляем запись в scrolledtext
    txt.delete(0,END) # чистим поле ввода

def check_number(input_number, gen_number): # проверка
    if input_number == gen_number:
        btn['state'] = 'disabled' # если число угадано статус кнопки "неактивна"
        messagebox.showinfo('Ура!!!', 'Ты угадал число!')
        return 'Число угадано, поздравляю!'
    elif input_number > gen_number:
        return 'Введенное число больше загаданного'
    else:
        return 'Введенное число меньше загаданного'

#Создаем окно программы, задаем его настройки
window = Tk()
window.resizable(0,0)
window.title("Игра 'Угадай число'")
w = window.winfo_screenmmwidth()
h = window.winfo_screenheight()
window.geometry(f'358x260+{w}+{h}')

lbl = Label(window, text="Введи число:")
lbl.place(x=10, y=5)

txt = Entry(window,width=10)
txt.place(x=110, y=5)


btn = Button(window, text="Проверить", command = clicked)
btn.place(x=200, y=2)

btn2 = Button(window, text="Генерировать новое число", command = gen)
btn2.place(x=10, y=220)

history = scrolledtext.ScrolledText(window, width=40, height=10)
history.place(x=10, y=40)

gen()

window.mainloop()