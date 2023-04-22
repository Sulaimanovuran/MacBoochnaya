import requests
from bs4 import BeautifulSoup
from format import format_description, format_price

url = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-14"

def get_data_for_tf(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    name_arr = []
    price_arr = []

    for product in soup.find_all('div', {'class': 'product-top'}):
        name = product.find('div', {'class':'product-name'}).text.strip()
        name_arr.append(format_description(name))



    for product in soup.find_all('div', {'class': 'product-price'}):
        price = product.find('div', {'class':'price-current'}).text.strip()
        price_arr.append(format_price(price))

    all_MBs_data_TF = list(zip(name_arr, price_arr))

    return all_MBs_data_TF
