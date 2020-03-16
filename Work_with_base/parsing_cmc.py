import requests
from bs4 import BeautifulSoup
import csv

def write_csv(data): #функция производит запись в файл cpc2.csv
    with open('cpc2.csv', 'a') as f:
        fieldname = ['name', 'price', 'change']
        writer = csv.DictWriter(f, fieldnames= fieldname)
        writer.writerow(data)

def upper_dollar(string_with_dollar): #функция отрезает первый символ строки
    return string_with_dollar[1:]

def upper_percent(string_with_percent): #функция отрезает последний символ строки
    return string_with_percent[:-1]

def get_html(url): #функция возвращает html код запрашиваемой страницы
    r = requests.get(url)
    return r

def get_data(html): #функция получает необходимые данные из передаваемого ей html кода
    soup = BeautifulSoup(html, 'lxml')
    array_coin = soup.find_all('tr', class_ = 'cmc-table-row')

    for elem in array_coin:
        name = elem.find('td', class_ = 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name').text
        price = upper_dollar(elem.find('td', class_ = 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price').text)
        change = upper_percent(elem.find('td', class_ = 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h').text)
        data_to_write = {
            'name': name,
            'price': price,
            'change': change
        }
        write_csv(data_to_write)

def main():
    index = 1
    while True:
        req = get_html(f"https://coinmarketcap.com/{index}")
        if req.status_code == 200:
            get_data(req.text)
            index += 1
        else:
            break

if __name__ == '__main__':
    main()