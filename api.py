"""FastAPI к квадратному уравнению"""
from fastapi import FastAPI
from logic import kv_ur

app = FastAPI()


@app.get("/kv_ur")
def kv_ur_get(a, b, c):
    """эндпоинт для нахождения корней квадратного уравнения"""
    a = int(a)
    b = int(b)
    c = int(c)
    return kv_ur(a, b, c)
