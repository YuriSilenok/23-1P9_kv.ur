"""Создание модели через peewee"""

from peewee import SqliteDatabase, Model, FloatField, CharField
# pylint: disable=R0903

db = SqliteDatabase('models.db')


class Table(Model):
    """Класс для соединения с таблицей"""
    class Meta:
        """Класс Meta"""
        database = db


class Values(Table):
    """Класс для хранения значений коэффициентов"""
    a = FloatField()
    b = FloatField()
    c = FloatField()
    result = CharField()


if __name__ == '__main__':
    db.create_tables([Values])
