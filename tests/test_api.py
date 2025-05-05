"""Модуль для тестирования квадратного уравнения в FastAPI"""
import unittest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


class TestKvUrAPI(unittest.TestCase):
    '''Тест-кейс для тестирования квадратного уравнения'''
    def test_a_rav_0_and_b_ne_rav_0(self):
        """Тест а == 0 и b != 0"""
        response = client.get("/kv_ur", params={"a": 0, "b": 5, "c": 3})
        self.assertEqual(response.status_code, 200)
        expected = ["Линейное уравнение имеет 1 корень", -3/5]
        self.assertEqual(response.json(), expected)
