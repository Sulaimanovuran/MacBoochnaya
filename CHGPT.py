lst = [
    {'product1': [1500, 11000], 'product2':[2000, 20200], 'product3': [3000, 34344], 'product4': [4000, 322323]},
    {'product1': [1200, 12000], 'product5':[2400, 30200], 'product3': [111, 22222], 'product8': [6000, 722323]},
    {'product5': [1600, 17000], 'product4':[4000, 322323], 'product3': [3000, 34344], 'product7': [4400, 342323]},
]

need_lst = ['product1', 'product3', 'product5', 'product7']

result = {}

for dictionary in lst:
    for product in need_lst:
        if product in dictionary:
            prices = dictionary[product]
            if len(prices) == 2:
                result.setdefault(product, []).extend(prices)
            else:
                result.setdefault(product, []).extend(['n/a', 'n/a'])
        else:
            result.setdefault(product, []).extend(['n/a', 'n/a'])

# print(result)


# import re

# string = 'Pro 14" M2 Pro 10-CPU 16-GPU 512GB Silver'
# pattern = r'(\d+)\"'

# match = re.search(pattern, string)
# if match:
#     numbers = match.group(1)
#     print(numbers)

from bs4 import BeautifulSoup

# Предположим, что у вас есть HTML-код
html = '''
<html>
<head>
</head>
<body>
    <tr class="item-row">
        <td class="item-desc"><a
                href="https://prices.appleinsider.com/product/macbook-pro-14-inch-2023/MPHH3LL/A">M2
                Pro (10-core CPU, 16-core GPU), 16GB, 512GB, Silver</a></td>
        <td class="item-price ">$1,999.00</td>
        <td class="item-price coupon blue-light">
            <div class="price-with-coupon-wrap">
                <a class="coupon-link"
                    href="https://prices.appleinsider.com/offer/29142,918?refl=pg-macbook-pro-14-inch-2023"
                    data-sid="0" rel="nofollow opener" target="_blank">$1,849.00</a>
                <div class="tool-tip">
                    <a class="symbol" href="#"><i class="fa fa-tag"></i></a>
                    <p>Price with $150 promo code <span
                            class="pg-coupon-code">APINSIDER</span>. Plus, save $60 on
                        AppleCare with the same code. As always, if you have any issues, you
                        can reach out to us at <a
                            href="/cdn-cgi/l/email-protection#3d59585c514e7d5c4d4d515854534e5459584f135e5250"><span
                                class="__cf_email__"
                                data-cfemail="acc8c9cdc0dfeccddcdcc0c9c5c2dfc5c8c9de82cfc3c1">[email&#160;protected]</span></a>
                        and we'll try and help.</p>
                </div>
            </div>
        </td>
        <td class="item-price blue-light blue-bold"><a
                href="https://prices.appleinsider.com/pg-out/?sid=29144&ref=grid&refl=pg-macbook-pro-14-inch-2023"
                rel="nofollow noopener" target="_blank">$1,799.00</td>
        <td class="item-price blue-light"><a
                href="https://prices.appleinsider.com/pg-out/?sid=29258&ref=grid&refl=pg-macbook-pro-14-inch-2023"
                rel="nofollow noopener" target="_blank">$1,999.00</td>
        <td class="item-price blue-light blue-bold"><a
                href="https://prices.appleinsider.com/pg-out/?sid=28960&ref=grid&refl=pg-macbook-pro-14-inch-2023"
                rel="nofollow noopener" target="_blank">$1,799.00</td>
        <td class="item-price blue-light"><a
                href="https://prices.appleinsider.com/pg-out/?sid=29254&ref=grid&refl=pg-macbook-pro-14-inch-2023"
                rel="nofollow noopener" target="_blank">$1,929.00</td>
        <td class="item-price blue-light"><a
                href="https://prices.appleinsider.com/pg-out/?sid=28968&ref=grid&refl=pg-macbook-pro-14-inch-2023"
                rel="nofollow noopener" target="_blank">$1,899.05</td>
        <td class="item-discount">$200.00</td>
    </tr>
</body>
</html>
'''
'''
# Создаем объект BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Ищем элементы с классом, содержащим определенную подстроку
substring = 'blue-bold'
items = soup.find(class_=lambda class_name: class_name and substring in class_name).find('a').get('href')

# Выводим найденные элементы

# print(items)
'''

import re

string = "M2 Max (12-core CPU, 30-core GPU), 32GB, 8TB, Space Gray"
pattern = r"M[12]\s*(Pro|Max)?"

result = re.search(pattern, string)

if result:
    substring = result.group(1)
    print(f"Найдена подстрока: {substring}")
else:
    print("Подстрока не найдена")


