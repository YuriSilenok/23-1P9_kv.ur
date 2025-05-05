"""Создание модели через peewee"""

from peewee import SqliteDatabase, Model, IntegerField

db = SqliteDatabase('models.db')


class Table(Model):
    """Класс для соединения с таблицей"""
    class Meta:
        """Класс Meta"""
        database = db


class Values(Table):
    """Класс для хранения значений коэффициентов"""
    a = IntegerField()
    b = IntegerField()
    c = IntegerField()


if __name__ == '__main__':
    db.create_tables([Values])
