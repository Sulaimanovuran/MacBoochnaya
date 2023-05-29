import requests
from bs4 import BeautifulSoup
from format import format_description_pro, format_price, format_description_air
import re



# url = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-14"
url = 'https://tacsafon.ru/magazin/folder/apple-macbook-air'

def get_data_for_tf(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    func_for_formatting = format_description_air if 'air' in url else format_description_pro
    name_arr = []
    price_arr = []

    for product in soup.find_all('div', {'class': 'product-top'}):
        name = product.find('div', {'class':'product-name'}).text.strip().replace(',', ' ')
        if func_for_formatting == format_description_pro:
            name_arr.append(f'MacBook Pro {url[-2:]} ' + func_for_formatting(name))
        # name_arr.append(name)


    for product1, product2 in zip(soup.find_all('div', {'class': 'product-price'}), soup.find_all('div', class_='product-top')):
        price = product1.find('div', {'class':'price-current'}).text.strip()
        link = 'https://tacsafon.ru'+product2.find('div', class_='product-name').find('a').get('href')
        price_usd = format_price(price)
        price_rub = re.sub(r"\D", "", price)
        price_arr.append([price_usd, price_rub, link])

    all_MBs_data_TF = {name: price for name, price in zip(name_arr, price_arr)}

    # all_MBs_data_TF = list(zip(name_arr, price_arr))
    # print(all_MBs_data_TF)
    # print(name_arr)
    # print('*****************************************')
    return all_MBs_data_TF