"""Модуль для тестирования квадратного уравнения"""
import unittest
from main import kv_ur


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
