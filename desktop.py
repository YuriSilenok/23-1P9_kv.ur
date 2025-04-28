import tkinter as tk
from tkinter import messagebox


def kv_ur(a, b, c):
    """Функция, которая возвращает кортеж"""
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b - d**0.5) / (2*a)
        x2 = (-b + d**0.5) / (2*a)
        count_k = "Дискриминант больше нуля, уравнение имеет два корня"
        return count_k, d, x1, x2
    if d == 0:
        count_k = "Дискриминант равен нулю, уравнение имеет один корень"
        x = (-b) / (2*a)
        return count_k, d, x
    count_k = "Дискриминант меньше нуля, уравнение имеет комплексные корни"
    return count_k, d


def solve():
    try:
        a = float(koef_1.get())
        b = float(koef_2.get())
        c = float(koef_3.get())
        result = kv_ur(a, b, c)
        messagebox.showinfo("Результат", str(result))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные коэффициенты")


if __name__ == "__main__":
    koef_1 = float(input("Введите значение a:"))
    koef_2 = float(input("Введите значение b:"))
    koef_3 = float(input("Введите значение c:"))
    print(kv_ur(koef_1, koef_2, koef_3))

root = tk.Tk()
root.title("Решение квадратных уравнений")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Введите коэффициенты квадратного уравнения:").grid(
    row=0, columnspan=2)

tk.Label(frame, text="a:").grid(row=1, column=0, sticky="e")
koef_1 = tk.Entry(frame)
koef_1.grid(row=1, column=1)

tk.Label(frame, text="b:").grid(row=2, column=0, sticky="e")
koef_2 = tk.Entry(frame)
koef_2.grid(row=2, column=1)

tk.Label(frame, text="c:").grid(row=3, column=0, sticky="e")
koef_3 = tk.Entry(frame)
koef_3.grid(row=3, column=1)

solve_button = tk.Button(frame, text="Решить пример", command=solve)
solve_button.grid(row=4, columnspan=2, pady=10)

root.mainloop()
