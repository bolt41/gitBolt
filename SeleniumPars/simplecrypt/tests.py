import requests
import urllib
import hmac
import hashlib

# Функция обработки запроса
def get_response(method, pair = ''):
    # необходимо генерировать параметр nonce при каждом запросе +1 от предыдущего.
    # храним следующее значение в файле nonce.
    # Внимание! Параметр nonce не должен превышать 2147483646
    with open('nonce', "r+") as counter: #открываем файл nonce и инкрементируем параметр
        nonce = int(counter.read())
        counter.seek(0)
        counter.write(str(nonce + 1))
        counter.truncate()

    payload = {
     'method': method,
     'pair': pair,
     'nonce': nonce
     }
    paybytes = urllib.parse.urlencode(payload).encode('utf8')
    sign = hmac.new(SEC_KEY, paybytes, hashlib.sha512).hexdigest()
    headers = {"Content-type": "application/x-www-form-urlencoded",
            "Key": API_KEY,
            "Sign": sign}

    response = requests.post('https://yobit.net/tapi/', headers = headers, data = paybytes)
    if response.status_code == 200:
        response = response.json()
        key_id = {}
        for key, vel in response['return'].items():
            key_id.update({key: vel})
        return (key_id)
    else:
        return 'Error code: ' + str(response.status_code)


API_KEY = b'4C68BABA6CD62B57B0467E7AB4D10F9A' #API key биржи
SEC_KEY = b'f07b3f1c3bf90d91dc73f2543ad60408' #security key биржи
get_inf = 'getInfo' # команда api
pair = 'micro_usd' # валютная пара
result = get_response(get_inf, pair)
print(result)