import requests
from bs4 import BeautifulSoup
import re
from googletrans import Translator
from format_da import format_desc_air

currency = round(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['KRW'].get('Value'),4)



translator = Translator()

url = 'https://prod.danawa.com/list/?cate=11336467'
# url = 'https://prod.danawa.com/list/?cate=11336468' #AIR

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' 
}

def get_data_for_da(url, flag=None, headres=None):
    response = requests.get(url, headers=headers, verify=True)

    # file = open('danawa.html')
    # response = file.read()

    soup = BeautifulSoup(response.text, 'lxml')

    products = soup.find_all('li', class_='prod_item')

    all_products = []

    for prod_item in products:
            try:
                if len(prod_item.find('div', class_='prod_info').find_all('span', class_='cm_mark')) >= 12:
                    all_products.append(prod_item)
            except:
                continue

    macbooks_pro = {}


    for product in all_products:

        """Получение объявлений"""
        product_info = product.find('p', class_='prod_name').text.replace('\n', '').replace('/', ' ') + product.find('div', 'spec_list').text.replace('\n', '').replace('/', ' ')
        clean_text = re.sub(r'\s+', ' ', product_info)
        
        """Перевод и форматирование описания"""
        translated_text = re.sub(r'\s+(core)',r'\1',translator.translate(clean_text).text)
        clean_text2 = translated_text.replace(' Core', 'core')
        cleaned_data = re.sub(r'[^\w\s.+]', '', clean_text2)

        
        description = format_desc_air(cleaned_data)


        if description:
            """Обработка цен"""
            prices = product.find('div', class_='prod_pricelist').find_all('p', class_='price_sect')
            memories = product.find('div', class_='prod_pricelist').find_all('p', class_='memory_sect')

            for price_item, memory_item in zip(prices, memories):
                test_price = price_item.find('strong').text.replace(',','')
                if test_price.isdigit():
                    price = test_price
                    price_rub = round(int(price) * ((currency / 1000) * 1.045),2)
                try:
                    ram = re.findall(r'(\d+)GB', memory_item.text)[0]
                    storage = re.findall(r'SSD (\d+TB|\d+GB)', memory_item.text)[0].replace('GB', '')
                except:
                    ram = ''
                    storage = ''
                
                link = price_item.find('a').get('href')

                m = re.search(r"(\d+)core", memory_item.text)
                if description['m_version'] == 'Pro':
                    if m:
                        gpu = m.group(1)
                        full_desc = f"MacBook {description['m_version']} {description['resolution']} {description['chip']} {description['c_version']} ({description['cpu']}-CPU {gpu}-GPU) {ram}/{storage} {description['color']}"
                    
                    else:
                        full_desc = f"MacBook {description['m_version']} {description['resolution']} {description['chip']} {description['c_version']} ({description['cpu']}-CPU {description['gpu']}-GPU) {ram}/{storage} {description['color']}"
                else:

                    full_desc = f"MacBook {description['m_version']} {description['chip']} {ram}/{storage} {description['color']}"

                if full_desc in macbooks_pro:
                    if price_rub < macbooks_pro[full_desc][1]:
                        macbooks_pro[full_desc] = [price, price_rub, link]
                else:
                    macbooks_pro[full_desc] = [price, price_rub, link]
        else:
            continue
    return macbooks_pro        



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






