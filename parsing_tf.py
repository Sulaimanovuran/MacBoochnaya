import requests
from bs4 import BeautifulSoup
from format import format_description_pro, format_price, format_description_air
from CHGPT import format_description_air as fda
import re
from tests import format_description_mac_mini

tf_pro_13 = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-13"
# url = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-14"
url = 'https://tacsafon.ru/magazin/folder/apple-macbook-air'

def get_data_for_tf(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    func_for_formatting = fda if 'air' in url else format_description_pro
    name_arr = []
    price_arr = []

    for product in soup.find_all('div', {'class': 'product-top'}):
        name = product.find('div', {'class':'product-name'}).text.strip().replace(',', ' ')
        if func_for_formatting == format_description_pro:
            resolution = url[-2:]
            description = func_for_formatting(name)
            if resolution == '13':
                m1 = '(8-CPU 8-GPU)'
                m2 = '(8-CPU 10-GPU)'
                name_arr.append(f'MacBook Pro {resolution} {description["chip"]} {m1 if description["chip"] == "M1" else m2} {description["memory"]} {description["color"]}')
                
            else:
                name_arr.append(f'MacBook Pro {resolution} {description["chip"]} {description["chip_version"]} {description["cgpu"]} {description["memory"]} {description["color"]}')
        else:
            name_arr.append(func_for_formatting(name))
        # name_arr.append(name)

    for product1, product2 in zip(soup.find_all('div', {'class': 'product-price'}), soup.find_all('div', class_='product-top')):
        price = product1.find('div', {'class':'price-current'}).text.strip()
        link = 'https://tacsafon.ru'+product2.find('div', class_='product-name').find('a').get('href')
        price_usd = format_price(price)
        price_rub = re.sub(r"\D", "", price)
        price_arr.append([price_usd, price_rub, link])

    all_MBs_data_TF = {name: price for name, price in zip(name_arr, price_arr)}

    return all_MBs_data_TF



def get_data_for_tf(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    name_arr = []
    price_arr = []

    for product in soup.find_all('div', {'class': 'product-top'}):
        name = product.find('div', {'class':'product-name'}).text.strip().replace(',', ' ')
        name_arr.append(format_description_mac_mini(name))


    for product1, product2 in zip(soup.find_all('div', {'class': 'product-price'}), soup.find_all('div', class_='product-top')):
        price = product1.find('div', {'class':'price-current'}).text.strip()
        link = 'https://tacsafon.ru'+product2.find('div', class_='product-name').find('a').get('href')
        price_usd = format_price(price)
        price_rub = re.sub(r"\D", "", price)
        price_arr.append([price_usd, price_rub, link])

    all_mms_data = {name: price for name, price in zip(name_arr, price_arr)}

    return all_mms_data