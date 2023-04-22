import string
import requests


data = round(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['USD'].get('Value'),2)

punctuation = (string.punctuation + '”')

need = ['14','M1','M2','Pro', 'Max','CPU','GPU','16GB','32GB','64GB','512GB','1024GB','2048GB','SSD','серебристый','серый','космос']

def format_description(text):
    fromated_desc = ''

    for char in punctuation:
        text = text.replace(char,'')

    for char in range(len(text.split())):
        if text.split()[char] in need:
            if text.split()[char] == 'CPU':
                fromated_desc += text.split()[char-1][0:-1]+'-'
            if text.split()[char] == 'GPU':
                fromated_desc += text.split()[char-1][0:-1]+'-'
            if text.split()[char] in fromated_desc:continue
            else:
                fromated_desc += text.split()[char]+' '


    return fromated_desc

def format_price(price):
    usd = int(price.split()[0])/data
    return ('$' + str(round(usd,2)))
