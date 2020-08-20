import requests
from bs4 import BeautifulSoup as BS

def get_html_get(url, head, session): #функция get запроса
    r = session.get(url, headers = head)
    return r.text

def get_html_post(url, data, head, session): #функция post запроса
    r = session.post(url, data = data, headers = head)
    return r.text

def main():
    url = 'https://pf-7.com/vhod'
    login = input('Введи логин:')
    password = input('Введи пароль:')
    auth_data = {'mail': login, 'pass': password, 'auth': 'Войти'}
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    session = requests.session() #начинаем сессию
    r = get_html_post(url, auth_data, headers, session) #авторизация


    soup = BS(r, 'lxml')
    a = soup.find('div', class_='plssis').find_all('p')
    balans = dict()  # словарь с текущими кошельками

    for text in a:
        temp = text.get_text().split()
        if temp[2][-1] == '$':
            balans[temp[0]] = temp[2][0:-1]
        else:
            balans[temp[0]] = temp[2]

    r = get_html_get('https://pf-7.com/vdepo', headers, session)
    soup = BS(r, 'lxml')
    trs = soup.find('table', class_='tablecon silkatab').find_all('tr')


    print(trs)
    print(balans)
main()




