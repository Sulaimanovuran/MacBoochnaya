import re
import json
import requests
from bs4 import BeautifulSoup
import string
from format import kgsrub, kgsusd

from format import format_description_air_ref as fda
from tests import format_description_pro_ref, format_description_mac_mini
# from CHGPT import format_description_air as fda

x = string.punctuation
num = string.digits


currency = round(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['USD'].get('Value'),4)

url = "https://www.apple.com/shop/refurbished/mac/13-inch-macbook-air"

def get_data_for_ref(url, flag, need_list=None):
    macbooks = {}
    need_macs_count = len(need_list)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    count_ = 0
    for product in soup.find('div', role='main').select('a'):
        if flag in product.text.strip():
            card_url = "https://www.apple.com"+ product.get('href')
            response2 = requests.get(card_url)
            soup2 = BeautifulSoup(response2.content, 'lxml')
            data = soup2.find('script', {'type':'application/json', 'id':'metrics'})
            data_dict = json.loads(f'{data.text}')
            owerview = re.sub(r'\s+', ' ',re.sub(r'[^\w\s.+]', '', soup2.find('div', class_="rc-pdsection-panel Overview-panel row").text).replace('\n', ''))
            price = int(data_dict['data']['products'][0]['price']['fullPrice'])
            price_rub = round((price * kgsusd)* kgsrub, 2)
            name = data_dict['data']['products'][0]['name']
            if flag == 'MacBook Pro':
                description = format_description_pro_ref(name+" "+owerview)

                if description in need_list:
                    macbooks[description] = [price, price_rub, card_url]
                
                if len(macbooks) == len(need_list):
                    return macbooks
            elif flag == 'Mac mini':

                description = format_description_mac_mini(name + ' ' + owerview), ' ––––––––––– ', [price, price_rub]
                
                if description in need_list:
                    macbooks[description] = [price, price_rub, card_url]
                
                if len(macbooks) == len(need_list):
                    return macbooks
            else:

                description = fda(name+" "+owerview)

                if description in need_list:
                    macbooks[description] = [price, price_rub, card_url]
                
                if len(macbooks) == len(need_list):
                    return macbooks
    return macbooks
        
need_pro_list = [
    # 'MacBook Pro 13 M2 (8-CPU 10-GPU) 16/256 Space Gray',
    # 'MacBook Pro 13 M2 (8-CPU 10-GPU) 16/256 Silver',
    # 'MacBook Pro 13 M2 (8-CPU 10-GPU) 16/512 Space Gray',
    # 'MacBook Pro 13 M2 (8-CPU 10-GPU) 16/512 Silver',

    'MacBook Pro 14 M1 Pro (8-CPU 14-GPU) 16/512 Silver',
    'MacBook Pro 14 M1 Pro (8-CPU 14-GPU) 16/512 Space Gray',
    'MacBook Pro 14 M1 Pro (10-CPU 16-GPU) 16/1TB Silver',
    'MacBook Pro 14 M1 Pro (10-CPU 16-GPU) 16/1TB Space Gray',

    'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Space Gray',
    'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Silver',

    'MacBook Pro 16 M1 Pro (10-CPU 16-GPU) 16/512 Silver',
    'MacBook Pro 16 M1 Pro (10-CPU 16-GPU) 16/512 Space Gray',

    # 'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Space Gray',
    # 'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Silver',

    # 'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Space Gray',
    # 'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Silver',
    ]


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
