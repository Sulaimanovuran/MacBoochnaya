





















'****************************************************************************************************************************************************************'

# x = string.punctuation
# num = string.digits




# url = "https://www.apple.com/shop/refurbished/mac/13-inch-macbook-air"

# def get_data_for_ref(url, flag, need_list=None):
#     macbooks = {}
#     need_macs_count = len(need_list)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'lxml')
#     count_ = 0
#     for product in soup.find('div', role='main').select('a'):
#         if flag in product.text.strip():
#             card_url = "https://www.apple.com"+ product.get('href')
#             response2 = requests.get(card_url)
#             soup2 = BeautifulSoup(response2.content, 'lxml')
#             data = soup2.find('script', {'type':'application/json', 'id':'metrics'})
#             data_dict = json.loads(f'{data.text}')
#             owerview = re.sub(r'\s+', ' ',re.sub(r'[^\w\s.+]', '', soup2.find('div', class_="rc-pdsection-panel Overview-panel row").text).replace('\n', ''))
#             price = int(data_dict['data']['products'][0]['price']['fullPrice'])
#             price_rub = round((price * kgsusd)* kgsrub, 2)
#             name = data_dict['data']['products'][0]['name']
#             if flag == 'MacBook Pro':
#                 description = format_description_pro_ref(name+" "+owerview)

#                 if description in need_list:
#                     macbooks[description] = [price, price_rub, card_url]
                
#                 if len(macbooks) == len(need_list):
#                     return macbooks
#             elif flag == 'Mac mini':

#                 description = format_description_mac_mini(name + ' ' + owerview), ' ––––––––––– ', [price, price_rub]
                
#                 if description in need_list:
#                     macbooks[description] = [price, price_rub, card_url]
                
#                 if len(macbooks) == len(need_list):
#                     return macbooks
#             else:

#                 description = fda(name+" "+owerview)

#                 if description in need_list:
#                     macbooks[description] = [price, price_rub, card_url]
                
#                 if len(macbooks) == len(need_list):
#                     return macbooks
#     return macbooks




# get_data_for_ref(url, 'Mac mini', need_air_list)



'****************************************************************************************************************************************************************'


# import requests
# from bs4 import BeautifulSoup
# from format import format_price
# import re
# from tests import format_description_mac_mini

# def get_data_for_tf(url):
    
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     name_arr = []
#     price_arr = []

#     for product in soup.find_all('div', {'class': 'product-top'}):
#         name = product.find('div', {'class':'product-name'}).text.strip().replace(',', ' ')
#         name_arr.append(format_description_mac_mini(name))


#     for product1, product2 in zip(soup.find_all('div', {'class': 'product-price'}), soup.find_all('div', class_='product-top')):
#         price = product1.find('div', {'class':'price-current'}).text.strip()
#         link = 'https://tacsafon.ru'+product2.find('div', class_='product-name').find('a').get('href')
#         price_usd = format_price(price)
#         price_rub = re.sub(r"\D", "", price)
#         price_arr.append([price_usd, price_rub, link])

#     all_mms_data = {name: price for name, price in zip(name_arr, price_arr)}

#     return all_mms_data

# for k, v in get_data_for_tf('https://tacsafon.ru/magazin/folder/apple-mac-mini').items():
#     print(k, ' ––––––––––– ', v)




'****************************************************************************************************************************************************************'

# def get_data_for_da_mac_mini(url,  headres=None):
#     response = requests.get(url, headers=headers, verify=True)

#     # file = open('danawa.html')
#     # response = file.read()

#     soup = BeautifulSoup(response.text, 'lxml')

#     products = soup.find_all('li', class_='prod_item')
#     all_products = []

#     for prod_item in products:
#         try:
#             if 'mac mini' in translator.translate(prod_item.find('p', class_='prod_name').text.replace('\n', '').replace('/', ' ')).text.lower():
#                 all_products.append(prod_item)
#         except:
#             continue
    
#     macminis = {}


#     for product in all_products:

#         """Получение объявлений"""
#         try:
#             product_info = product.find('p', class_='prod_name').text.replace('\n', '').replace('/', ' ') + product.find('div', 'spec_list').text.replace('\n', '').replace('/', ' ')
#         except AttributeError:
#             continue
#         clean_text = re.sub(r'\s+', ' ', product_info)
        
#         """Перевод и форматирование описания"""
#         translated_text = re.sub(r'\s+(core)',r'\1',translator.translate(clean_text).text)
#         cleaned_data = re.sub(r'[^\w\s.+]', '', translated_text)
#         description = format_description_mac_mini(cleaned_data)
#         # print(cleaned_data, end='\n\n\n')

#         if description:
#             """Обработка цен"""
#             price_item = product.find('div', class_='prod_pricelist').find('p', class_='price_sect')
#             # memories = product.find('div', class_='prod_pricelist').find_all('p', class_='memory_sect')

            
#             test_price = price_item.find('strong').text.replace(',','')
#             # print(test_price)
#             if test_price.isdigit():
#                 price = test_price
#                 price_rub = round(int(price) * ((currency / 1000) * 1.045),2)
#             # try:
#             #     ram = re.findall(r'(\d+)GB', memory_item.text)[0]
#             #     storage = re.findall(r'SSD (\d+TB|\d+GB)', memory_item.text)[0].replace('GB', '')
#             # except:
#             #     ram = ''
#             #     storage = ''
            
#             link = price_item.find('a').get('href')

#             # m = re.search(r"(\d+)core", memory_item.text)
            

#             full_desc = description
            
#             if full_desc in macminis:
#                 if price_rub < macminis[full_desc][1]:
#                     macminis[full_desc] = [price, price_rub, link]
#             else:
#                 macminis[full_desc] = [price, price_rub, link]


#         else:
#             continue
    
#     return macminis


'****************************************************************************************************************************************************************'

# for k in get_data_for_da(da_air_m2, headres=headers).keys():
#     print(k)

    # price_list = re.sub(r'\b\d+\s*mall\s+product\s+comparison\b', '/', translator.translate(prices).text, flags=re.IGNORECASE).split('/')


    #re.sub(r'\s+', ' '

    # for price_item in price_list:
    #     link = product.find('div', class_='prod_pricelist').find('a', class_='click_log_product_standard_price_').get('href')
    #     match = re.search(r"KRW\s*([\d,]+)", price_item, re.IGNORECASE)
    #     if match:
    #         price = match.group(1).replace(",", "")
    #     ram = re.findall(r'(\d+)GB,', price_item)[0]
    #     storage = re.findall(r'SSD (\d+TB|\d+GB)', price_item)[0]


        




    

    # print(format_description_pro(translated_text))



# with open('danawa.html', 'w') as f:
#     for i in products:
#         try:
#             if len(i.find('div', class_='prod_info').find_all('span', class_='cm_mark')) >= 12:
#                 f.write(str(i))
#         except:
#             continue


# product_list = soup.find_all('')


# # product_list = soup.find('ul', class_='product_list')




































































# from tests import format_description_mac_mini
# from bs4 import BeautifulSoup
# import re
# import requests
# from format import kgsrub, kgsusd

# headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

# def get_data_for_ai_mac_mini(url, headers):

#     html_code = requests.get(url, headers=headers)

#     """Создание дерева объектов"""

#     soup = BeautifulSoup(html_code.text, 'lxml')


#     """Выявление всех объявлений"""

#     all_rows_count = int(len(soup.find_all('tr', class_='item-row'))/2)
#     all_rows = soup.find_all('tr', class_='item-row')[:all_rows_count]
#     all_mms_data = {}

#     """Запуск цикла для каждой строки"""
#     c = 0
#     for row in all_rows:

#         best_price = ''
#         counter = -1
#         store = ''

#         """Определение цен для каждой строки, а также описание и ссылка на товар"""

#         all_prices = row.find_all('td', class_=re.compile('item-price'))
#         row_desc = row.find('td', class_='item-desc').text.replace('\n', ' ').replace('\t', '')
#         row_desc = format_description_mac_mini(row_desc)
        

#         substring = 'blue-bold'

#         try:
#             row_link = row.find('td', class_=lambda class_name: class_name and substring in class_name).find('a').get('href')
#         except AttributeError:
#             row_link = row.find('td', class_='item-desc').find('a').get('href')
            
#         # row_link = row.find('td', class_='item-desc').find('a').get('href')
        
#         """Проходимся по ценам """

#         try:
#             best_price = row.find('td', class_=re.compile('bold')).text
#             if 'place order' in best_price:
#                 best_price = '$' + str(round(float(all_prices[0].text[1:].replace(',','')) - float(row.find('td', class_='item-discount').text[1:]), 2))
#                 price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price))* kgsusd )* kgsrub, 2)
#                 all_mms_data[row_desc] = [best_price, price_rub, row_link]
#             else:
#                 best_price = row.find('td', class_=re.compile('bold')).find('a').text
#                 price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price)) * kgsusd )* kgsrub, 2)
#                 all_mms_data[row_desc] = [best_price, price_rub, row_link]
#         except AttributeError:
            
#             best_price = row.find('td', class_='item-price').text
#             if best_price.startswith('$'):
#                 price_rub = round((float(re.sub(r"[^\w\s\.]", "", best_price)) * kgsusd )* kgsrub, 2)
#                 all_mms_data[row_desc] = [best_price, price_rub, row_link]


        
#     return all_mms_data

