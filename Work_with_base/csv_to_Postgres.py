'''Выполняется выгрузка csv файла с текущими курсами спарсеными с сайта
coinmarket в локальную БД Postgres'''

import csv
from peewee import *

db = PostgresqlDatabase(database='test', user = 'postgres', password = '1',
                        host = 'localhost')# строка инициализации подключения к БД Postgres

class coin(Model): #класс с определением полей таблицы
    name = CharField()
    url = TextField()
    price = CharField()

    class Meta:
        database = db

def main():
    db.connect() #коннектимся к БД
    db.create_tables([coin])# создаем таблицу coin в БД

    param = ['name', 'url', 'price']
    with open('cpc2.csv') as f: # открываем файл с данными на чтение
        reader = csv.DictReader(f, fieldnames= param) # считываем все строки по полям определенным в param
        coins = list(reader) #преобразуем словарь в список, для дальнейшей выгрузки в БД

    with db.atomic(): #записываем в БД
        for index in range(0,len(coins),100): #записываем по 100 строк
            coin.insert_many(coins[index:index+100]).execute()

if __name__ == '__main__':
    main()