'''
# Домашнее задание к лекции 2.4 «Database. Mongo. ORM»

1. Вы реализуете приложение для поиска билетов на концерт. 
Заполните коллекцию в Монго данными о предстоящих концертах и 
реализуйте следующие функции:

- `read_data`: импорт данных из csv [файла](https://github.com/netology-code/py-homework-advanced/blob/master/2.4.DB.Mongo.ORM/artists.csv);
- `find_cheapest`: отсортировать билеты из базы по возрастанию цены;
- `find_by_name`: найти билеты по исполнителю, где имя исполнителя 
может быть задано не полностью, и вернуть их по возрастанию цены.


## Дополнительное задание

- Реализовать сортировку по дате мероприятия. Для этого вам потребуется 
строку с датой в csv-файле приводить к объекту datetime (можете считать,
 что все они текущего года) и сохранять его.

Пример поиска: найти все мероприятия с 1 по 30 июля.


python
'''

import csv
import re

from pymongo import MongoClient


def mk_mongodb():
    client = MongoClient('localhost')
    db = client.artists
    db.art_collection
    return db

def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    result = []
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        for row in reader:
            db.art_collection.insert(row)
    return db.name

def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    result = mydb.art_collection.find().sort('Price', pymongo.ASCENDING)
    return result


def find_by_name(name, db_collection):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """

    result = db_collection.find_one({'Исполнитель' : name})

    #regex = re.compile('укажите регулярное выражение для поиска. ' \
    #                   'Обратите внимание, что в строке могут быть \
    #                   специальные символы, их нужно экранировать')
    return result


def clear_db(dbname):
    client = MongoClient('localhost')
    client.drop_database(dbname)

    db.drop_database('')

if __name__ == '__main__':
    mydb = mk_mongodb()
    mydb_name = read_data('artists.csv', mydb)
    for k in mydb.art_collection.find():
        print('ispolnitel:', k['Исполнитель'],'cena',k['Price'])
    search_name = input('Введите имя для поиска: ')
    searched_name = find_by_name(search_name, mydb.art_collection)
    print(searched_name)


