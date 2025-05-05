"""Импортируем tkinter и импортируем функцию квадратного уравнения"""
import tkinter as tk
from logic import kv_ur


root = tk.Tk()
root.title("Решение квадратного уравнения")

lab_1 = tk.Label(width=85, text='Введите значения a,b,c')

ent_1 = tk.Entry(width=100)

ent_2 = tk.Entry(width=100)

ent_3 = tk.Entry(width=100)

but = tk.Button(width=85, text='Вычислить', bg='black', fg='yellow')

lab_2 = tk.Label(width=85, text='Ваш ответ:')

lab_3 = tk.Label(width=86, bg='black', fg='yellow')


def vichisl(event):
    """fdasf"""
    a = int(ent_1.get())
    b = int(ent_2.get())
    c = int(ent_3.get())
    kv_ur(a, b, c)
    lab_3['text'] = kv_ur(a, b, c)


but.bind('<Button-1>', vichisl)

lab_1.pack()

ent_1.pack()

ent_2.pack()

ent_3.pack()

but.pack()

lab_2.pack()

lab_3.pack()

root.mainloop()
