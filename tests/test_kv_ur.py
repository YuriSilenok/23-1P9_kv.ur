"""Модуль для тестирования квадратного уравнения"""
import unittest
from logic import kv_ur


class TestStringMethods(unittest.TestCase):
    '''Тест-кейс для тестирования квадратного уравнения'''
    def test_dis_bolsh_nul(self):
        """Дискриминант больше нуля"""
        a = 4
        b = 4
        c = -8
        massage = "Дискриминант больше нуля, уравнение имеет два корня"
        d = 144
        x1 = -2
        x2 = 1
        otv = kv_ur(a, b, c)
        self.assertEqual(len(otv), 4, "Количество элементов не равно четырем")
        self.assertEqual(otv[0], massage, "Неверная строка при выводе")
        self.assertEqual(otv[1], d, "Неправильное значение дискрименанта")
        self.assertEqual(otv[2], x1, "Неправильное значение первого корня")
        self.assertEqual(otv[3], x2, "Неправильное значение второго корня")

    def test_dis_rav_nul(self):
        """Дискриминант равняется нуля"""
        a = 2
        b = 4
        c = 2
        massage = "Дискриминант равен нулю, уравнение имеет один корень"
        d = 0
        x = -1
        otv = kv_ur(a, b, c)
        self.assertEqual(len(otv), 3, "Количество элементов не равно трем")
        self.assertEqual(otv[0], massage, "Неверная строка при выводе")
        self.assertEqual(otv[1], d, "Неправильное значение дискрименанта")
        self.assertEqual(otv[2], x, "Неправильное значение корня")

    def test_same_with_x(self):
        """Прямая совпадает с осью x"""
        a = 0
        b = 0
        c = 0
        massage = "Линейное уравнение, прямая совпадает с осью Оx"
        x = "R"
        otv = kv_ur(a, b, c)
        self.assertEqual(len(otv), 2, "Количество элементов не равно двум")
        self.assertEqual(otv[0], massage, "Неверная строка при выводе")
        self.assertEqual(otv[1], x, "Неправильное значение корня")

    def test_dis_mensh_null(self):
        """Дискриминант меньше нуля"""
        a = 1
        b = 1
        c = 1
        massage = "Дискриминант меньше нуля, уравнение имеет комплексные корни"
        d = -3
        otv = kv_ur(a, b, c)
        self.assertEqual(len(otv), 3, "Количество элементов не равно трем")
        self.assertEqual(otv[0], massage, "Неверная строка при выводе")
        self.assertEqual(otv[1], d, "Неправильное значение дискрименанта")
        self.assertEqual(otv[2], 'Нет корней', "Не верный ответ")

    def test_a_is_0(self):
        '''Прямая пересекает ось Ох'''
        a = 0
        b = 2
        c = 2
        massage = "Линейное уравнение имеет 1 корень"
        x = -1
        otv = kv_ur(a, b, c)
        self.assertEqual(len(otv), 2, "Количество элементов не равно двум")
        self.assertEqual(otv[0], massage, "Неверная строка при выводе")
        self.assertEqual(otv[1], x, "Неправильное значение корня")

    def test_a_b_is_0(self):
        """Прямая параллельная оси Ox"""
        a = 0
        b = 0
        c = 5
        message = "Линейное уравнение, прямая параллельная оси Ox"
        otv = kv_ur(a, b, c)
        self.assertEqual(len(otv), 2, "Количество элементов не равно двум")
        self.assertEqual(otv[0], message, "Неверная строка при выводе")
        self.assertEqual(otv[1], "Корней нет", "Неверная строка при выводе")
