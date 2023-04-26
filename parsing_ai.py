import requests
from bs4 import BeautifulSoup
import re
from format import format_description, format_description_air


'''Определение адреса и заголовков'''

url = 'https://prices.appleinsider.com/macbook-pro-14-inch-2023'
# url = 'https://prices.appleinsider.com/macbook-air-2022'

headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

def get_data_for_ai(url, headers):

    html_code = requests.get(url, headers=headers)


    """Создание дерева объектов"""

    soup = BeautifulSoup(html_code.text, 'lxml')

    # with open('apple_insider.html', 'w') as f:
    #     f.write(html_code.text)


    """Определение названий магазинов"""

    store_names = [store.get('title') for store in soup.find('table', class_='price-guide').find('tr').find_all('th')[0:-1]]


    """Выявление всех объявлений"""

    all_rows = soup.find_all('tr', class_='item-row')[:90]

    all_MBs_data_AI = []

    """Запуск цикла для каждой строки"""

    for row in all_rows:

        best_price = ''
        counter = -1
        store = ''

        """Определение цен для каждой строки, а также описание и ссылка на товар"""

        all_prices = row.find_all('td', class_=re.compile('item-price'))
        # row_desc = row.find('td', class_='item-desc').text.replace('\n', ' ').replace('\t', '')
        if 'air' in url or 'Air' in url:
            row_desc = format_description_air(row.find('td', class_='item-desc').text.replace('\n', ' ').replace('\t', ''))
        else:
            row_desc = format_description(row.find('td', class_='item-desc').text.replace('\n', ' ').replace('\t', ''))
        row_link = row.find('td', class_='item-desc').find('a').get('href')
        
        """Проходимся по ценам """

        for price in all_prices:
            counter += 1
            class_name = price.get('class')

            if 'coupon' in class_name and 'blue-bold' in class_name:

                """Выявляем лучшую цену с использованием купона"""

                best_price = price.find('a', class_='coupon-link').text
                store = store_names[counter]

                if best_price == 'place order' and store == 'adorama':
                    best_price = '$' + str(float(all_prices[0].text[1:].replace(',','')) - float(row.find('td', class_='item-discount').text[1:]    ))
                    if row_desc not in all_MBs_data_AI:
                        # all_MBs_data_AI.append(row_desc)
                        all_MBs_data_AI.append([row_desc,  f'=ГИПЕРССЫЛКА("{row_link}";"{best_price}")'])#,  f'=ГИПЕРССЫЛКА("{row_link}";"{best_price}")'])
                    
                else:
                    if row_desc not in all_MBs_data_AI:
                        # all_MBs_data_AI.append(row_desc)
                        all_MBs_data_AI.append([row_desc,  f'=ГИПЕРССЫЛКА("{row_link}";"{best_price}")'])#,  f'=ГИПЕРССЫЛКА("{row_link}";"{best_price}")'])
            
            elif 'blue-bold' in class_name:
                """Выявляем лучшую цену без использованием купона"""

                best_price = price.text
                store = store_names[counter]

                if best_price == 'place order' and store == 'adorama':
                    best_price = '$' + str(float(all_prices[0].text[1:].replace(',','')) - float(row.find('td', class_='item-discount').text[1:]))
                    if row_desc not in all_MBs_data_AI:
                        # all_MBs_data_AI.append(row_desc)
                        all_MBs_data_AI.append([row_desc,  f'=ГИПЕРССЫЛКА("{row_link}";"{best_price}")'])#,  f'=ГИПЕРССЫЛКА("{row_link}";"{best_price}")'])

                else:
                    if row_desc not in all_MBs_data_AI:
                        # all_MBs_data_AI.append(row_desc)
                        all_MBs_data_AI.append([row_desc,  f'=ГИПЕРССЫЛКА("{row_link}";"{best_price}")'])
    return all_MBs_data_AI
                

# print(get_data_for_ai(url, headers))




'MacBook Pro 14 M2 (10-CPU 16-GPU) 16/512 Space Gray'

'''
['MacBook Pro 14 M2 (10-CPU 16-GPU) 16/512 Space Gray',
'MacBook Pro 14 M2 (10-CPU 16-GPU) 16/512 Silver',
'MacBook Pro 14 M2 (12-CPU 19-GPU) 32/1Tb Space Gray', 
'MacBook Pro 14 M2 (12-CPU 19-GPU) 32/1Tb Silver',
'MacBook Pro 14 M2 (12-CPU 19-GPU) 32/1Tb Silver',
'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1Tb Space Gray',
'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1Tb Silver',]

'''

'''
'MacBook Air M2 8/256 Midnight'

['MacBook Air M2 8/256 Space Gray',
'MacBook Air M2 8/256 Silver',
'MacBook Air M2 8/256 Starlight',
'MacBook Air M2 8/256 Midnight',
]

'''