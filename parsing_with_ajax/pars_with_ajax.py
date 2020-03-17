import csv
from multiprocessing import Pool #импорт модуля мультизадачности
import requests


def get_html(url): #функция получения кода страницы
    r = requests.get(url)
    return r.text


def write_csv(data): #функция записи данных в csv файл
    field = ['name', 'url', 'rate'] #определяем последовательность полей для записи
    with open('liveinternet.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=field)
        writer.writerow(data)

def gate_page_data(text): #функция обработки полученного текста и подготовка его к записи
    response = text.strip().split('\n')[1:] # удаляем лишние пробелы и разделяем строки по символу переноса
    for row in response: # бежим циклом по получившемуся списку
        columns = row.strip().split('\t') #текущую строку разбиваем по табуляции
        data = {'name': columns[0], #записываем необходимые значения из получившегося списка в словарь
                'url': columns[1],
                'rate': columns[3]}
        write_csv(data) #отправляем словарь на запись

def make_all(url): #функция-посредник получает текст из запроса текущего
    text = get_html(url)
    gate_page_data(text)


def main():
    #6761
    urls = [f'https://www.liveinternet.ru/rating/ru//today.tsv?page={i}' for i in range(1, 6762)]

    with Pool(20) as p: #устанавливаем количсетво процессов = 20
        p.map(make_all, urls) #запускаем функцию по значениям списка

if __name__ == '__main__':
    main()
