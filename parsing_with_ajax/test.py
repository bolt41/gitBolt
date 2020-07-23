import requests
import csv
from bs4 import BeautifulSoup


def write_to_csv(data):
    columns = ['author', 'since', 'mail', 'tel']
    with open('tel.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames= columns)
        writer.writerow(data)

def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    r = requests.get(url, headers= headers)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    comment_array = soup.find('div', class_='builder-posts-wrap').find_all('article', class_='post')
    return comment_array #[] ИЛИ [1,2,3]

def search_data(text):
    for comment in text:
        try:
            author = comment.find('p', class_='testimonial-author').text
        except:
            author = ''
        try:
            since = comment.find('p', class_='traxer-since').text
        except:
            since = ''
        try:
            mail = comment.find('li', class_='email').text
        except:
            mail = ''
        try:
            tel = comment.find('li', class_='tel').text
        except:
            tel = ''
        data = {'author': author,
                'since': since,
                'mail': mail,
                'tel': tel}
        print(data)
        write_to_csv(data)

def main():
    index = 1
    while True:
        url = f'https://catertrax.com/why-catertrax/traxers/page/{index}/'
        response = get_data(get_html(url))
        if response:
            search_data(response)
            index += 1
        else:
            break
def main1():
    url = f'https://catertrax.com/why-catertrax/traxers/page/1/'
    response = get_data(get_html(url))
    search_data(response)
if __name__ == '__main__':
    main1()