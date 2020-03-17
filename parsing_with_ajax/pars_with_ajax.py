import csv
import requests


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    field = ['name', 'url', 'rate']
    with open('liveinternet.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=field)
        writer.writerow(data)


def main():
    for i in range(1, 6761):
        url = f'https://www.liveinternet.ru/rating/ru//today.tsv?page={i}'
        response = get_html(url).strip().split('\n')[1:]
        for row in response:
            columns = row.strip().split('\t')
            data = {'name': columns[0],
                    'url': columns[1],
                    'rate': columns[3]}
            write_csv(data)


if __name__ == '__main__':
    main()
