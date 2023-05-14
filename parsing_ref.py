import re
import json
import requests
from bs4 import BeautifulSoup
import string

from format import format_description_air
from tests import format_description_pro_ref

x = string.punctuation
num = string.digits


currency = round(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['USD'].get('Value'),4)

url = "https://www.apple.com/shop/refurbished/mac/13-inch-macbook-air"

def get_data_for_ref(url, need_list, flag):
    macbooks = {}
    need_macs_count = len(need_list)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    for product in soup.find('div', role='main').select('a'):
        if flag in product.text.strip():
            card_url = "https://www.apple.com"+ product.get('href')
            response2 = requests.get(card_url)
            soup2 = BeautifulSoup(response2.content, 'lxml')
            data = soup2.find('script', {'type':'application/json', 'id':'metrics'})
            data_dict = json.loads(f'{data.text}')
            owerview = re.sub(r'\s+', ' ',re.sub(r'[^\w\s.+]', '', soup2.find('div', class_="rc-pdsection-panel Overview-panel row").text).replace('\n', ''))
            price = int(data_dict['data']['products'][0]['price']['fullPrice'])
            price_rub = round((price * currency)* 1.045, 2)
            name = data_dict['data']['products'][0]['name']
            if flag == 'MacBook Pro':
                description = format_description_pro_ref(name+" "+owerview)
            else:
                description = format_description_air(name+" "+owerview)
            
            if description in need_list:
                macbooks[description] = [price, price_rub, card_url]

            if need_macs_count == len(macbooks):
                return macbooks
            



















# url = "https://www.apple.com/shop/refurbished/mac/14-inch-macbook-pro"

# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'lxml')

# def get_url():
#     for product in soup.find('div', role='main').select('a'):
#         if '14-inch' in product.get('href'):
#             card_url = 'https://www.apple.com' + product.get('href')
#             yield card_url


# for url in get_url():
#     response2 = requests.get(url)
#     soup2 = BeautifulSoup(response2.content, 'lxml')

#     data = soup2.find('script', {'type':'application/json', 'id':'metrics'})
#     data_dict = json.loads(f'{data.text}')
#     price = '$' + str(int(data_dict['data']['products'][0]['price']['fullPrice'])+(int(data_dict['data']['products'][0]['price']['fullPrice'])/100*4))
#     name = data_dict['data']['products'][0]['name']
    
#     new_ = 'MacBook Pro 14 '

#     for char in x:
#         name = name.replace(char,'')

#     if "M1" in name: new_ += 'M1 '
#     elif "M2" in name: new_ += 'M2 '
#     if "Max" not in name: new_ += 'Pro '

#     processed = name.split()

#     for char in range(len(processed)):
#         if processed[char] in need:
#             if processed[char] == 'CPU':
#                 new_ += '('
#                 for i in range(len(processed[char])-1):
#                     if (processed[char-1])[i] in num:
#                         new_ += (processed[char-1])[i]
#                 new_ += '-'
#             if processed[char] == 'GPU':
#                 if 'CPU' not in processed:
#                     new_ += '('
#                 for i in range(len(processed[char])):
#                     if (processed[char-1])[i] in num:
#                         new_ += (processed[char-1])[i]
#                 new_ += '-'
#                 new_ += processed[char]+') '
#             if processed[char] in new_:continue
#             else:new_ += processed[char]+' '

#     for item in soup2.find_all('div', class_='rc-pdsection-mainpanel column large-9 small-12'):
#         for info in item.find_all('p'):
#             for ram in hard:
#                 if ram in new_:
#                     continue
#                 else:
#                     if ram in info.text.strip():
#                         new_ += (info.text.strip()).split()[0]+'/'
#             for ssd in memory:
#                 if ssd in new_:
#                     continue
#                 else:
#                     if ssd in info.text.strip():
#                         new_ += (info.text.strip()).split()[0]

#     if 'Space' and 'Gray' in processed: new_ += ' Space Gray'
#     if 'Silver' in processed: new_ += ' Silver'
#     if 'Midnight' in processed: new_ += ' Midnight'
#     if 'Starlight' in processed: new_ += ' Starlight'
                    
    # print(new_, price)

# with open('file.txt', 'w') as f:
#     f.write(soup.prettify())
