"""Интерфейс решения квадратного уравнения на Tkinter"""
import tkinter as tk
from logic import kv_ur


class Labitext(tk.Tk):
    """Класс для разделения атрибутов"""
    def __init__(self):
        super().__init__()
        self.f2 = tk.Frame(self, bg="white")

        self.f2.pack(side='bottom', anchor='s')

        self.f1 = tk.Frame(self, bg="white")

        self.f1.pack(side='top', anchor='n')

        self.f3 = tk.Frame(self.f1, bg="white")

        self.f3.pack(side='left', anchor='nw')

        self.f4 = tk.Frame(self.f1, bg="white")

        self.f4.pack(side='right', anchor='ne')

        self.lab_text_1 = tk.Label(self.f2, width=80, bg='white')

        self.lab_text_2 = tk.Label(self.f2, width=80, bg='white')

        self.lab_text_3 = tk.Label(self.f2, width=80, bg='white')


class Labichsl(Labitext):
    """Класс для разделения атрибутов"""
    def __init__(self):
        super().__init__()

        self.lab_otv = tk.Label(
            self.f2, width=80, bg='white', text='Ваш ответ:'
            )
        
        self.lab_message = tk.Label(self.f2, width=80, bg='gray')

        self.lab_1 = tk.Label(self.f2, width=80, bg='gray')

        self.lab_2 = tk.Label(self.f2, width=80, bg='gray')

        self.lab_3 = tk.Label(self.f2, width=80, bg='gray')


class Kvurtkint(Labichsl):
    """Класс для создания окна программы"""

    def __init__(self):
        super().__init__()

        self.title("Решение квадратного уравнения")

        self.lab_a = tk.Label(
            self.f3, width=43, text='Введите значение a:', bg='white', height=1
            )

        self.lab_b = tk.Label(
            self.f3, width=43, text='Введите значение b:', bg='white', height=1
            )

        self.lab_c = tk.Label(
            self.f3, width=43, text='Введите значение c:', bg='white', height=1
            )

        self.ent_a = tk.Entry(self.f4, width=43, bg='gray')

        self.ent_b = tk.Entry(self.f4, width=43, bg='gray')

        self.ent_c = tk.Entry(self.f4, width=43, bg='gray')

        self.but = tk.Button(
            self.f2, width=80,
            text='Вычислить', bg='black', fg='white', command=self.vichisl
            )

        self.but.bind(self, '<Button-1>', self.vichisl)

        self.ent_a.pack(expand='false', fill='none', anchor='ne', pady=2)

        self.lab_a.pack(expand='false', fill='none', anchor='nw', pady=1)

        self.lab_b.pack(expand='false', fill='none', anchor='w', pady=1)

        self.ent_b.pack(expand='false', fill='none', anchor='e', pady=2)

        self.lab_c.pack(expand='false', fill='none', anchor='sw', pady=1)

        self.ent_c.pack(expand='false', fill='none', anchor='se', pady=2)

        self.but.pack()

        self.lab_otv.pack()

        self.lab_message.pack()

        self.lab_text_1.pack()

        self.lab_1.pack()

        self.lab_text_2.pack()

        self.lab_2.pack()

        self.lab_3.pack()

    def vichisl(self):
        """Функция для вычислений"""
        self.lab_1['text'] = ''
        self.lab_2['text'] = ''
        self.lab_3['text'] = ''
        self.lab_text_1['text'] = ''
        self.lab_text_2['text'] = ''
        self.lab_text_3['text'] = ''
        a = int(self.ent_a.get())
        b = int(self.ent_b.get())
        c = int(self.ent_c.get())
        otvet = kv_ur(a, b, c)
        self.lab_message['text'] = otvet[0]
        if len(otvet) == 4:
            self.lab_text_1['text'] = "Дискриминант:"
            self.lab_1['text'] = otvet[1]
            self.lab_text_2['text'] = "Корни:"
            self.lab_2['text'] = f'x1={otvet[2]}'
            self.lab_3['text'] = f'x2={otvet[3]}'
        elif len(otvet) == 3:
            self.lab_text_1['text'] = "Дискриминант:"
            self.lab_1['text'] = otvet[1]
            self.lab_text_2['text'] = "Корни:"
            self.lab_2['text'] = otvet[2]
        elif len(otvet) == 2:
            self.lab_text_1['text'] = "Корни:"
            self.lab_1['text'] = otvet[1]


if __name__ == "__main__":
    app = Kvurtkint()
    app.mainloop()
