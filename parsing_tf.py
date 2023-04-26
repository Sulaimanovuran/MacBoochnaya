import requests
from bs4 import BeautifulSoup
from format import format_description, format_price, format_description_air

url = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-14"
# url = 'https://tacsafon.ru/magazin/folder/apple-macbook-air'

def get_data_for_tf(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    func_for_formatting = format_description_air if 'air' in url else format_description
    name_arr = []
    price_arr = []

    for product in soup.find_all('div', {'class': 'product-top'}):
        name = product.find('div', {'class':'product-name'}).text.strip()
        name_arr.append(func_for_formatting(name))
        # name_arr.append(name)


    for product1, product2 in zip(soup.find_all('div', {'class': 'product-price'}), soup.find_all('div', class_='product-top')):
        price = product1.find('div', {'class':'price-current'}).text.strip()
        link = product2.find('div', class_='product-image').select_one('a').get('href')
        price = format_price(price)
        price_arr.append(f'=ГИПЕРССЫЛКА("https://tacsafon.ru{link}";"{price}")')

    all_MBs_data_TF = [[name, price] for name, price in zip(name_arr, price_arr)]

    # all_MBs_data_TF = list(zip(name_arr, price_arr))
    # print(all_MBs_data_TF)
    # print(name_arr)
    # print('*****************************************')
    return all_MBs_data_TF


# get_data_for_tf(url)