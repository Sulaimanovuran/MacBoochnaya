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

# import re

# string = "M2 Max (12-core CPU, 30-core GPU), 32GB, 8TB, Space Gray"
# pattern = r"M[12]\s*(Pro|Max)?"

# result = re.search(pattern, string)

# if result:
#     substring = result.group(1)
#     print(f"Найдена подстрока: {substring}")
# else:
#     print("Подстрока не найдена")


desc_list = [
    'M2 (8-core GPU), 8GB, 256GB, Midnight',
    'M2 (10-core GPU), 8GB, 256GB, Silver',
    'M2 (8-core GPU), 24GB, 2TB, Starlight',
    'Apple MacBook Pro 13” Z16R0000E (2022, M2, 8C CPU 10C GPU, 16GB 1TB SSD, Touch Bar) «серый космос»',
    'Apple MacBook Pro 13” Z16R0000D (2022, M2, 8C CPU 10C GPU, 16GB 512GB SSD, Touch Bar) «серый космос»',
    'Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 7‑Core GPU - Gold Overview Originally released November 2020 13.3inch diagonal LEDbacklit display with IPS technology 2560by1600 native resolution at 227 pixels per inch 8GB unified memory 256GB SSD1 Touch ID sensor 720p FaceTime HD Camera',
    'Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Space Gray Overview Originally released November 2020 13.3inch diagonal LEDbacklit display with IPS technology 2560by1600 native resolution at 227 pixels per inch 8GB unified memory 512GB SSD1 Touch ID sensor 720p FaceTime HD Camera',
    'Refurbished 13-inch MacBook Air Apple M2 Chip with 8‑Core CPU and 10‑Core GPU - Space Gray Overview Originally released July 2022 13.6inch diagonal LEDbacklit display with IPS technology1 8GB unified memory 256GB SSD 2 1080p FaceTime HD camera Two Thunderbolt USB 4 ports',
    'Refurbished 13-inch MacBook Air Apple M2 Chip with 8‑Core CPU and 10‑Core GPU - Midnight Overview Originally released July 2022 13.6inch diagonal LEDbacklit display with IPS technology1 8GB unified memory 512GB SSD 2 1080p FaceTime HD camera Two Thunderbolt USB 4 ports',
    'M1 (7-core GPU), 8GB, 256GB, Space Gray',
    'M1 (16GB, 1TB, 7-core GPU) Gold',
    'M1 (16GB, 512GB, 8-core GPU) Silver',
    'Air M2 8-CPU 8-GPU 256GB Midnight',
    'Air M2 8-CPU 8-GPU 256GB Gray',
    'Air M2 8-CPU 8-GPU | 16GB | 512GB Gray US',
    'Air M1 8-CPU 7-GPU | 16GB |  256GB Gray KR 🇰🇷'
]
import re

def format_description_air(description, flag=None, resolution=None) -> str:
    if flag and description.count('GB') > 1 or description.count('TB') > 0:
        flag = None
    colors = ['starlight', 'midnight', 'silver', 'space', 'gray', 'gold']
    ru_colors = ['сияющая', 'звезда', 'полночь', 'космос', 'полночь', 'серебристый']
    new_string = re.sub(r'[^\w\s.]', '', description)
    description = new_string.split(' ')
    memory = []
    chip = []
    color = []

    gpu_search = re.compile(r'(\d+core GPU|\d+C GPU|\d+Core GPU|\d+GPU|\d+core)')
    gpu_cores = gpu_search.search(new_string)
    if gpu_cores:
        gpu_cores = gpu_cores.group(1)
        gpu = re.sub(r'\D', '', gpu_cores)
    else:
        gpu_cores = "?"


    for word in description:
        if 'GB' in word or 'TB' in word:
            if flag:
                memory+=['8', word.replace('GB', '')]
                continue
            memory.append(word.replace('GB', ''))
            continue

        if 'M1' in word or 'M2' in word:
            chip.append(word)
            continue

        
        '''Определение цвета'''
        if word.lower() in colors or word.lower() in ru_colors:
            word_check = word.lower()
            if 'сияющая' in word_check and 'звезда' in word_check and len(color) == 0:
                color.append('Starlight')
                continue
            elif 'полночь' in word_check:
                color.append('Midnight')
                continue
            elif 'серый' in word_check or 'космос' in word_check and len(color) == 0:
                color.append('Space Gray')
                continue
            elif 'серебристый' in word_check:
                color.append('Silver')
                continue
            elif 'золотистый' in word_check:
                color.append('Gold')
                continue
            elif 'gold' in word_check:
                color.append('Gold')
                continue
            elif 'space' in word_check or 'gray' in word_check and len(color) == 0:
                color.append('Space Gray')
            else:
                color.append(word) if len(color) == 0 else ...

    if resolution:
        finall_description = f'MacBook Air {resolution} {chip[0] if len(chip) != 0 else None} {gpu}-GPU {"/".join(memory)} {color[0] if len(color) != 0 else None}'
    else:
        finall_description = f'MacBook Air {chip[0] if len(chip) != 0 else None} {gpu}-GPU {"/".join(memory)} {color[0] if len(color) != 0 else None}'
    # print(finall_description)
    return finall_description


# print(format_description_air('M1 (7-core GPU), 8GB, 256GB, Space Gray'))

# for i in desc_list:
#     print('**************************', end='\n\n')
#     print(format_description_air(i))
    


"8core GPU"
"10C GPU"
"7C GPU"
"8C GPU"
"7Core GPU"
"8Core GPU"
"10Core GPU"
"7core GPU"
"8GPU"
"10GPU"

('Apple MacBook Air 13" Late 2020 MGN93RU/A (M1  8GB  256GB SSD  Apple graphics 7-core) серебристый')


# a = {'helllo': 12, 'world':2, 'adam':0}

# b = {'John': 'Snow', 'Sam': 'Smith', 'abc': 1}

# c = {'uran': 7, 'saturn': 34}


import re

descriptions = [
    "APPLE Mac mini M2 PRO Z1700003M\n\nDetailed specification\nApple (ARM) / M2 PRO / Avalanche / LPDDR5 / 16GB / SSD / 1TB / M2 16 core / Built-in speaker / 1Gbps wired / 802.11ax (Wi-Fi 6E) wireless / Bluetooth / HDMI / USB 3.0 (5Gbps) / Thunderbolt 4 / Mac OS Ventura / Mini PC / 1.28kg / Usage: Office/Lecture / Order-made product",
    "M2 (8-core CPU, 10-core GPU), 8GB, 256GB",
    "Apple Mac Mini MMFK3 (2023, M2, 8C CPU, 10C GPU, 8GB, 512GB SSD) Silver (серебристый)",
    "Refurbished Mac mini 3.0GHz 6-core Intel Core i5 - Space Gray Overview Originally released October 2018 8GB of 2666MHz DDR4 SODIMM memory 512GB PCIebased SSD1 Four Thunderbolt 3 ports up to 40 Gbps Intel UHD Graphics 630 Gigabit Ethernet port"
]

# memory_regex = r"(\d+)GB"
# storage_regex = r"(\d+)(GB|TB)"

# for description in descriptions:
#     memory_match = re.search(memory_regex, description)
    
    
#     if memory_match:
#         memory = memory_match.group(1)
#         print(memory)
#         description = description.replace(memory+'GB', '')
#     else: 
#         "Unknown"

#     storage_match = re.search(storage_regex, description)

#     if storage_match:
#         storage = storage_match.group(0)
#         print(storage)

#     else: 
#         "Unknown"
    
