"""Импортируем tkinter и импортируем функцию квадратного уравнения"""
import tkinter as tk
from logic import kv_ur


class Kvurtkint(tk.Tk):
    """Класс для создания окна программы"""
    def __init__(self):
        super().__init__()
        self.title("Решение квадратного уравнения")

        self.lab_1 = tk.Label(self, width=85, text='Введите значения a,b,c')

        self.ent_1 = tk.Entry(self, width=100)

        self.ent_2 = tk.Entry(self, width=100)

        self.ent_3 = tk.Entry(self, width=100)

        self.but = tk.Button(
            self, width=85,
            text='Вычислить', bg='black', fg='yellow', command=self.vichisl
            )

        self.lab_2 = tk.Label(self, width=85, text='Ваш ответ:')

        self.lab_3 = tk.Label(self, width=86, bg='black', fg='yellow')

        self.but.bind(self, '<Button-1>', self.vichisl)

        self.lab_1.pack()

        self.ent_1.pack()

        self.ent_2.pack()

        self.ent_3.pack()

        self.but.pack()

        self.lab_2.pack()

        self.lab_3.pack()

    def vichisl(self):
        """Функция для вычислений"""
        a = int(self.ent_1.get())
        b = int(self.ent_2.get())
        c = int(self.ent_3.get())
        kv_ur(a, b, c)
        self.lab_3['text'] = kv_ur(a, b, c)


if __name__ == "__main__":
    app = Kvurtkint()
    app.mainloop()
