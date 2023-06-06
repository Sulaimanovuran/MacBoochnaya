import requests
from bs4 import BeautifulSoup
import re
from format import format_description_air, format_description_pro
from CHGPT import format_description_air as fda
currency = round(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['USD'].get('Value'),4)


'''Определение адреса и заголовков'''
ai_pro_16 = "https://prices.appleinsider.com/macbook-pro-16-inch-2023"
ai_pro_13 = "https://prices.appleinsider.com/macbook-pro-13-inch-late-2020"
# url = 'https://prices.appleinsider.com/macbook-pro-14-inch-2023'
url2 = 'https://prices.appleinsider.com/macbook-pro-14-inch-2021'
url = 'https://prices.appleinsider.com/macbook-air-2022'



headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

def get_data_for_ai(url, headers):

    html_code = requests.get(url, headers=headers)


    """Создание дерева объектов"""

    soup = BeautifulSoup(html_code.text, 'lxml')

    # with open('apple_insider.html', 'w') as f:
    #     f.write(html_code.text)


    """Определение названий магазинов"""

    # store_names = [store.get('title') for store in soup.find('table', class_='price-guide').find('tr').find_all('th')[0:-1]]


    """Выявление всех объявлений"""

    all_rows_count = int(len(soup.find_all('tr', class_='item-row'))/2)
    all_rows = soup.find_all('tr', class_='item-row')[:all_rows_count]
    all_MBs_data_AI = {}

    """Запуск цикла для каждой строки"""
    c = 0
    for row in all_rows:

        best_price = ''
        counter = -1
        store = ''

        """Определение цен для каждой строки, а также описание и ссылка на товар"""

        all_prices = row.find_all('td', class_=re.compile('item-price'))
        # row_desc = row.find('td', class_='item-desc').text.replace('\n', ' ').replace('\t', '')
        
        if 'air' in url or 'Air' in url:
            row_desc = fda(row.find('td', class_='item-desc').text.replace('\n', ' ').replace('\t', ''))
        else:
            pattern = r'(\d+(?:\.\d+)?)\-inch'
            match = re.search(pattern, url)
            if match:
                numbers = match.group(1)


            desc_dict = format_description_pro(description=row.find('td', class_='item-desc').text.replace('\n', ' ').replace('\t', ''))
            if numbers == '14':
                row_desc = f'MacBook Pro {numbers} {desc_dict["chip"]} {desc_dict["chip_version"]} {desc_dict["cgpu"]} {desc_dict["memory"]} {desc_dict["color"]}'
                
            elif numbers == '13':
                if desc_dict['chip'] == 'M1':
                    row_desc = f'MacBook Pro {numbers} {desc_dict["chip"]} (8-CPU 8-GPU) {desc_dict["memory"]} {desc_dict["color"]}'
                    
                elif desc_dict['chip'] == 'M2':
                    row_desc = f'MacBook Pro {numbers} {desc_dict["chip"]} (8-CPU 10-GPU) {desc_dict["memory"]} {desc_dict["color"]}'

            elif numbers == '16':
                if desc_dict['chip'] == 'M1':
                    row_desc = f'MacBook Pro {numbers} {desc_dict["chip"]} {desc_dict["chip_version"]} {desc_dict["cgpu"]} {desc_dict["memory"]} {desc_dict["color"]}'
                    
                elif desc_dict['chip'] == 'M2':
                    row_desc = f'MacBook Pro {numbers} {desc_dict["chip"]} {desc_dict["chip_version"]} (12-CPU {desc_dict["cgpu"]} {desc_dict["memory"]} {desc_dict["color"]}'


        substring = 'blue-bold'

        try:
            row_link = row.find('td', class_=lambda class_name: class_name and substring in class_name).find('a').get('href')
        except AttributeError:
            row_link = row.find('td', class_='item-desc').find('a').get('href')
            
        # row_link = row.find('td', class_='item-desc').find('a').get('href')
        
        """Проходимся по ценам """

        try:
            best_price = row.find('td', class_=re.compile('bold')).text
            if 'place order' in best_price:
                best_price = '$' + str(round(float(all_prices[0].text[1:].replace(',','')) - float(row.find('td', class_='item-discount').text[1:]), 2))
                price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price)) * currency )* 1.045, 2)
                all_MBs_data_AI[row_desc] = [best_price, price_rub, row_link]
            else:
                best_price = row.find('td', class_=re.compile('bold')).find('a').text
                price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price)) * currency )* 1.045, 2)
                all_MBs_data_AI[row_desc] = [best_price, price_rub, row_link]
        except AttributeError:
            
            best_price = row.find('td', class_='item-price').text
            if best_price.startswith('$'):
                price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price)) * currency )* 1.045, 2)
                all_MBs_data_AI[row_desc] = [best_price, price_rub, row_link]


        
    return all_MBs_data_AI

# get_data_for_ai('https://prices.appleinsider.com/macbook-pro-16-inch-2021', headers)

# print('MacBook Pro 16 M1 Pro (10-CPU 16-GPU) 16/512 Silver' == 'MacBook Pro 16 M1 Pro (10-CPU 16-GPU) 16/512 Silver')
# for k,v in get_data_for_ai(ai_pro_16, headers).items():
# print(get_data_for_ai(url, headers))


























'''
#####after 111 row


 for price in all_prices:
        #     counter += 1
        #     class_name = price.get('class')
        #     if 'coupon' in class_name and 'blue-bold' in class_name:

        #         """Выявляем лучшую цену с использованием купона"""

        #         best_price = price.find('a', class_='coupon-link').text
        #         store = store_names[counter]

        #         if best_price == 'place order' and store == 'adorama':
        #             best_price = '$' + str(round(float(all_prices[0].text[1:].replace(',','')) - float(row.find('td', class_='item-discount').text[1:]), 2))
        #             price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price)) * currency )* 1.045, 2)


        #             all_MBs_data_AI[row_desc] = [best_price, price_rub, row_link]
                    

        #     elif 'bold' in class_name:
        #         """Выявляем лучшую цену без использованием купона"""

        #         best_price = price.text
        #         store = store_names[counter]

        #         if best_price == 'place order':
        #             best_price = '$' + str(float(all_prices[0].text[1:].replace(',','')) - float(row.find('td', class_='item-discount').text[1:]))
        #             price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price)) * currency )* 1.045, 2)

        #             all_MBs_data_AI[row_desc] = [best_price, price_rub, row_link]

        #         else:
        #             price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price)) * currency )* 1.045, 2)
        #             all_MBs_data_AI[row_desc] = [best_price, price_rub, row_link]
            
        #     elif price.text.startswith('$'):
        #         # best_price = row.find('td', class_='item-price').text
        #         best_price = price.text
        #         price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price)) * currency )* 1.045, 2)
        #         all_MBs_data_AI[row_desc] = [best_price, price_rub, row_link]

'''