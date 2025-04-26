"""Программа для вычисления квадратного уравнения"""


def kv_ur(a, b, c):
    """Функиця, которая возвращает кортеж"""
    if a == 0 and b == 0 and c == 0:
        massage = "Линейное уравнение, прямая совпадает с осью Оx"
        x = "R"
        return massage, x
    if a == 0 and b == 0:
        count_k = "Линейное уравнение, прямая параллельная оси Ox"
        return count_k, "Корней нет"
    if a == 0:
        x = -c/b
        aisnull = "Линейное уравнение имеет 1 корень"
        return aisnull, x
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
    return count_k, d, 'Нет корней'


if __name__ == "__main__":
    koef_1 = float(input("Введите значение a:"))
    koef_2 = float(input("Введите значение b:"))
    koef_3 = float(input("Введите значение c:"))
    print(kv_ur(koef_1, koef_2, koef_3))
