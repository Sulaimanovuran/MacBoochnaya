import re
import requests


list1 = ['Apple MacBook Pro 14” MMQX3 (2021, Apple M1 Max 10C CPU, 32C GPU, 64GB, 2048GB SSD) серебристый', 
         'Apple MacBook Pro 14” MPHK3 (2023, Apple M2 Max 12C CPU, 30C GPU 32GB, 1024GB SSD)  серебристый', 
         'Apple MacBook Pro 14” MPHJ3 (2023, Apple M2 Pro 12C CPU, 19C GPU, 16GB, 1024GB SSD) серебристый', 
         'Apple MacBook Pro 14” MPHF3 (2023, Apple M2 Pro 12C CPU, 19C GPU, 16GB, 1024GB SSD)  серый космос', 
         'Apple MacBook Pro 14” MKGQ3 (2021, Apple M1 Pro 10C CPU, 16C GPU, 16GB, 1024GB SSD) серый космос', 
         'Apple MacBook Pro 14” MKGR3 (2021, Apple M1 Pro 8C CPU, 14C GPU, 16GB, 512GB SSD) серебристый', 
         'Apple MacBook Pro 14” MKGP3 (2021, Apple M1 Pro 8C CPU, 14C GPU, 16GB, 512GB SSD) серый космос']



list2 = ['M2 Pro (10-core CPU, 16-core GPU), 16GB, 512GB, Space Gray', 
         'M2 Pro (10-core CPU, 16-core GPU), 16GB, 512GB, Silver', 
         'M2 Pro (10-core CPU, 16-core GPU), 16GB, 1TB, Space Gray', 
         'M2 Pro (10-core CPU, 16-core GPU), 16GB, 1TB, Silver', 
         'M2 Pro (10-core CPU, 16-core GPU), 16GB, 2TB, Space Gray', 
         'M2 Pro (10-core CPU, 16-core GPU), 16GB, 2TB, Silver', 
         'M2 Pro (10-core CPU, 16-core GPU), 16GB, 4TB, Space Gray', 
         'M2 Pro (10-core CPU, 16-core GPU), 16GB, 4TB, Silver', 
         'M2 Pro (10-core CPU, 16-core GPU), 16GB, 8TB, Space Gray', 
         'M2 Pro (10-core CPU, 16-core GPU), 16GB, 8TB, Silver']


list3 = ...


def format_description_pro(description, flag=None) -> str:
    colors = ['starlight', 'midnight', 'silver', 'space', 'gray']
    ru_colors = ['сияющая', 'звезда', 'полночь', 'серый', 'космос', 'полночь', 'серебристый']
    CPU_variations = ['10core', '12core', '8core', '10C', '12C', '8C', '10CPU', '12CPU', '8CPU','10Core', '12Core', '8Core']
    GPU_variations = ['14core', '16core', '19core', '30core','32core', '38core', '14C', '16C', '19C', '30C', '32C', '38C', '14GPU', '16GPU', '19GPU', '30GPU', '32GPU', '38GPU']
    inches = ['14', '16', '13', '13.6']

    new_string = re.sub(r'[^\w\s.]', '', description)
    
    description = new_string.split(' ')
    memory = []
    chip = ''
    color = ''
    model = ''
    cgpu = ''
    inch = ''
    for word in description:
        if word in ('Apple', 'MacBook', 'CPU', 'GPU'):
            continue
        '''Определение процессора'''
        if word in CPU_variations:
            cgpu += f"({re.sub(r'[a-zA-Z]', '', word)}-CPU "
            continue
        if word in GPU_variations and ')' not in cgpu:
            cgpu += f"{re.sub(r'[a-zA-Z]', '', word)}-GPU)"
            continue

        '''Определение модели'''
        if word == 'Pro' or word == 'Max':
            model = word
            continue

        # '''Определение разрешения экрана'''
        # if word in inches:
        #     inch = word
        #     continue
        '''Определение памяти'''
        if 'GB' in word or 'TB' in word:
            if len(word) > 5:
                memory.append(word[0]+'TB')
                continue

            elif flag and any(['10-CPU 16-GPU' in cgpu, '12-CPU 19-GPU' in cgpu]):
                memory+=['16', word.replace('GB', '')]
                continue

            elif flag and '12-CPU 30-GPU' in cgpu:
                memory+=['32', word]
                continue

            else:
                memory.append(word.replace('GB', '')) if len(memory) < 2 else ...
                continue

        '''Определение чипа'''
        if 'M1' in word or 'M2' in word:
            chip = word
            continue

        '''Определение цвета'''
        if word.lower() in colors or word.lower() in ru_colors:
            word_check = word.lower()

            if 'серый' in word_check or 'космос' in word_check:
                color = 'Space Gray'
                continue
            elif 'серебристый' in word_check:
                color = 'Silver'
                continue
            elif 'space' in word_check or 'gray' in word_check:
                color = 'Space Gray'
                continue
            else:
                color = word if color == '' else None


    return f'MacBook Pro 14 {chip} {model} {cgpu} {"/".join(memory)} {color}'

# print(format_description_pro('M2 Pro (12-core CPU, 19-core GPU), 32GB, 512GB, Silver', ))


# for i in list2:
#     print(format_description_pro(i))



# print(format_description_pro('Apple MacBook Pro 14” MMQX3 (2021, Apple M1 Max 10C CPU, 32C GPU, 64GB, 2048GB SSD) серебристый'))



def format_description_air(description, flag=None) -> str:
    colors = ['starlight', 'midnight', 'silver', 'space', 'gray']
    ru_colors = ['сияющая', 'звезда', 'полночь', 'космос', 'полночь', 'серебристый']
    new_string = re.sub(r'[^\w\s.]', '', description)
    
    description = new_string.split(' ')
    print(description)
    memory = []
    chip = []
    color = []

    for word in description:
        if 'GB' in word or 'TB' in word:
            if flag:
                memory+=['8', word.replace('GB', '')]
                continue
            
            memory.append(word.replace('GB', '')) if len(memory) < 2 else ...
            continue

        if 'M1' in word or 'M2' in word:
            chip.append(word)
            continue
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
            elif 'space' in word_check or 'gray' in word_check and len(color) == 0:
                color.append('Space Gray')
            else:
                color.append(word) if len(color) == 0 else ...


    return f'MacBook Air {chip[0] if len(chip) != 0 else None} {"/".join(memory)} {color[0] if len(color) != 0 else None}'





[['MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Space Gray', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-pro-14-inch-2023/MPHE3LL/A";"$1,849.00")', 'n/a', '1\xa0940'], ['MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Silver', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-pro-14-inch-2023/MPHH3LL/A";"$1,849.00")', 'n/a', '1\xa0940'], ['MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Space Gray', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-pro-14-inch-2023/MPHF3LL/A";"$2,349.00")', '=ГИПЕРССЫЛКА("https://tacsafon.ru/magazin/product/apple-macbook-pro-14-mphf3-2023-apple-m2-pro-12c-cpu-19c-gpu-16gb-1024gb-ssd-seryj-kosmos";"$2452.06")', '2\xa0460'], ['MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Silver', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-pro-14-inch-2023/MPHJ3LL/A";"$2,349.00")', '=ГИПЕРССЫЛКА("https://tacsafon.ru/magazin/product/apple-macbook-pro-14-mphj3-2023-apple-m2-pro-12c-cpu-19c-gpu-16gb-1024gb-ssd-serebristyj";"$2501.1")', '2\xa0460'], ['MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Space Gray', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-pro-14-inch-2023/MPHG3LL/A";"$2,849.00")', 'n/a', '3\xa0100'], ['MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Silver', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-pro-14-inch-2023/MPHK3LL/A";"$2,849.00")', '=ГИПЕРССЫЛКА("https://tacsafon.ru/magazin/product/apple-macbook-pro-14-mphk3-2023-apple-m2-max-12c-cpu-30c-gpu-32gb-1024gb-ssd-serebristyj";"$3273.54")', '3\xa0100']]
[['MacBook Air M2 8/256 Space Gray', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-air-m2/MLXW3LL/A";"$1,049.00")', 'n/a', '1\xa0140'], ['MacBook Air M2 8/256 Silver', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-air-m2/MLXY3LL/A";"$1,049.00")', 'n/a', 'n/a'], ['MacBook Air M2 8/256 Starlight', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-air-m2/MLY13LL/A";"$1,049.00")', 'n/a', 'n/a'], ['MacBook Air M2 8/256 Midnight', '=ГИПЕРССЫЛКА("https://prices.appleinsider.com/product/macbook-air-m2/MLY33LL/A";"$1,049.00")', 'n/a', '1\xa0140']]











list1 = [["Товар1", 1000], ["Товар2", 2000], ["Товар3", 3000]]
list2 = [["Товар1", 1000], ["Товар4", 2000], ["Товар5", 3000]]
list3 = [["Товар7", 1000], ["Товар2", 2000], ["Товар5", 3000]]
item_names = ['Товар1', 'Товар3', 'Товар7']

def func(list1, list2, list3=None, item_names=None):

    result = {}

    for item in item_names:
        result[item] = []
        for lst in [list1, list2, list3]:
            for sub_lst in lst:
                if sub_lst[0] == item:
                    result[item].append(sub_lst[1])
                    break
            else:
                result[item].append("n/a")
                

from googletrans import Translator



translator = Translator()


currency = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

from parsing_ai import get_data_for_ai, url as url_ai, headers
from parsing_da import get_data_for_da, url as url_da

need_pro_list = [
    'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Space Gray',
    'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Silver',

    'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Space Gray',
    'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Silver',

    'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Space Gray',
    'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Silver'
    ]


def create_merged_dict(list_of_dicts, need_list):
    merged_dict = {}
    counter = 0
    for d in list_of_dicts:
        for key, value in d.items():
            if key not in merged_dict and key in need_list:
                merged_dict[key] = [value]
            else:
                if key in need_list:
                    merged_dict[key].append(value)
                    counter +=1
    need_macs_data = []

    for desc, prices in merged_dict.items():
        for prc in prices:
            if len(prc) > 2:
                prc = [f'=HYPERLINK("{prc[2]}", "{prc[0]}")', f'=HYPERLINK("{prc[2]}", "{prc[1]}")']
    
    for key, value in merged_dict.items():
        need_macs_data.append([key] + [price for price in value])
    return need_macs_data









# list_of_dicts = [get_data_for_ai(url_ai, headers=headers),get_data_for_da(url_da)]
# merged_dict = create_merged_dict(list_of_dicts, need_pro_list)


# ai = get_data_for_ai(url_ai, headers=headers)
# da = get_data_for_da(url_da)


# for i in merged_dict:
#     print(i)



# d = {'hello': [1,2,3], 'John': [2,4,5]}

# for k, v in d.items():
#     for i in v:
#         v = i**2

# print(d)
# 
'''
ref             da

FGND3LL         MGND3KH/A
FLY43LL/A       MLY43KH/A 
FLXY3LL/A       MLXW3KH/A
'''


############ Определение ядер ######################

lst = ['Refurbished 14-inch MacBook Pro Apple M1 Pro Chip with 8‑Core CPU and 14‑Core GPU - Space GrayOverview Originally released October 2021 14.2inch diagonal Liquid Retina XDR display1 3024by1964 native resolution at 254 pixels per inch 16GB unified memory 512GB SSD 2 Touch ID 1080p FaceTime HD camera Three Thunderbolt 4 ports ',
       'Refurbished 13-inch MacBook Pro Apple M2 Chip with 8‑Core CPU and 10‑Core GPU - SilverOverview Originally released June 2022 13.3inch diagonal LEDbacklit display with IPS technology 2560by1600 native resolution at 227 pixels per inch 16GB unified memory 512GB SSD¹ 720p FaceTime HD camera Two Thunderbolt USB 4 ports ',
       'Refurbished 14-inch MacBook Pro Apple M1 Pro Chip with 10‑Core CPU and 14‑Core GPU - Space GrayOverview Originally released October 2021 14.2inch diagonal Liquid Retina XDR display1 3024by1964 native resolution at 254 pixels per inch 16GB unified memory 512GB SSD 2 Touch ID 1080p FaceTime HD camera Three Thunderbolt 4 ports ',
       'Refurbished 13-inch MacBook Pro Apple M2 Chip with 8‑Core CPU and 10‑Core GPU - SilverOverview Originally released June 2022 13.3inch diagonal LEDbacklit display with IPS technology 2560by1600 native resolution at 227 pixels per inch 8GB unified memory 1TB SSD¹ 720p FaceTime HD camera Two Thunderbolt USB 4 ports']

# for text in lst:

#     cpu_cores = None
#     gpu_cores = None

#     cpu_regex = re.compile(r'(\d+)[‑-]?Core\s+CPU', re.IGNORECASE)
#     gpu_regex = re.compile(r'(\d+)[‑-]?Core\s+GPU', re.IGNORECASE)

#     cpu_match = cpu_regex.search(text)
#     if cpu_match:
#         cpu_cores = cpu_match.group(1)

#     gpu_match = gpu_regex.search(text)
#     if gpu_match:
#         gpu_cores = gpu_match.group(1)

    # print("CPU Cores:", cpu_cores)
    # print("GPU Cores:", gpu_cores)
    # print('############################################')



############# Определение разрешения экрана

import math
import re

def find_screen_resolution(description):
    pattern = r'(\d+(?:\.\d+)?)\s*-?\s*inch'
    matches = re.findall(pattern, description)
    if matches:
        return math.floor(float(matches[0]))
    return None

description = "Refurbished 13-inch MacBook Pro Apple M2 Chip with 8‑Core CPU and 10‑Core GPU - SilverOverview Originally released June 2022 13.3inch diagonal LEDbacklit display with IPS technology 2560by1600 native resolution at 227 pixels per inch 16GB unified memory 512GB SSD¹ 720p FaceTime HD camera Two Thunderbolt USB 4 ports"

# resolution = find_screen_resolution(description)
# print("Resolution (in inches):", resolution)


################## Определение чипа и его версии
def find_chip_version(description):
    pattern = r'(M[12])\s*(?:Chip\b\s*)?(Pro|Max)?'
    matches = re.search(pattern, description, re.IGNORECASE)
    if matches:
        chip_version = matches.group()
        chip_version = re.sub(r'\bChip\b', '', chip_version)
        return chip_version.strip()
    return ""

description = "Refurbished 13-inch MacBook Pro Apple M2 Chip with 8‑Core CPU and 10‑Core GPU - SilverOverview Originally released June 2022 13.3inch diagonal LEDbacklit display with IPS technology 2560by1600 native resolution at 227 pixels per inch 16GB unified memory 512GB SSD¹ 720p FaceTime HD camera Two Thunderbolt USB 4 ports"

# chip_version = find_chip_version(description)
# print("Chip Version:", [chip_version])



############## Определение памяти 



def find_capacity(description):
    pattern = r'(\d+(?:\.\d+)?)\s*(?:TB|GB)\b'
    matches = re.findall(pattern, description)
    memory_capacity = ""
    storage_capacity = ""
    if matches:
        if len(matches) >= 2:
            memory_capacity = matches[-2]
            storage_capacity = matches[-1]
        else:
            memory_capacity = matches[-1]
    return memory_capacity, storage_capacity

description = "Refurbished 13.3-inch MacBook Pro Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Space GrayOverview Originally released November 2020 13.3inch diagonal LEDbacklit display with IPS technology 2560by1600 native resolution at 227 pixels per inch 8GB unified memory 256GB SSD1 Touch Bar and Touch ID 720p FaceTime HD Camera "

# memory_capacity, storage_capacity = find_capacity(description)


################# Определение цвета



def find_color(description):
    pattern = r'\b(silver|space gray|silver)\b'
    match = re.search(pattern, description, flags=re.IGNORECASE)
    if match:
        return match.group(0)
    else:
        return None

description = "Refurbished 16-inch MacBook Pro Apple M2 Max Chip with 12‑Core CPU and 38‑Core GPU - Silver Overview Originally released January 2023 16.2inch diagonal Liquid Retina XDR display1 3456by2234 native resolution at 254 pixels per inch 96GB unified memory 8TB SSD2 Touch ID 1080p FaceTime HD camera Three Thunderbolt 4 USBC ports"

# color = find_color(description)
# print("Color:", color)

def format_description_pro_ref(text):
    ''' Разрешение экрана'''
    res_pattern = r'(\d+(?:\.\d+)?)\s*-?\s*inch'
    res_matches = re.findall(res_pattern, text)
    if res_matches:
        resolution = math.floor(float(res_matches[0]))
    else:
        resolution = None

    '''CPU GPU'''
    cpu_cores = None
    gpu_cores = None

    cpu_regex = re.compile(r'(\d+)[‑-]?Core\s+CPU', re.IGNORECASE)
    gpu_regex = re.compile(r'(\d+)[‑-]?Core\s+GPU', re.IGNORECASE)

    cpu_match = cpu_regex.search(text)
    if cpu_match:
        cpu_cores = cpu_match.group(1)

    gpu_match = gpu_regex.search(text)
    if gpu_match:
        gpu_cores = gpu_match.group(1)

    '''RAM Storage'''
    rs_pattern = r'(\d+(?:\.\d+)?)\s*(?:TB|GB)\b'
    rs_matches = re.findall(rs_pattern, text)
    memory_capacity = ""
    storage_capacity = ""
    if rs_matches:
        if len(rs_matches) >= 2:
            memory_capacity = rs_matches[-2]
            storage_capacity = rs_matches[-1]
            if len(storage_capacity) <= 2:
                storage_capacity = storage_capacity+'TB'
        else:
            memory_capacity = rs_matches[-1]
    
    '''Chip and version'''
    ch_pattern = r'(M[12])\s*(?:Chip\b\s*)?(Pro|Max)?'
    matches = re.search(ch_pattern, text, re.IGNORECASE)
    if matches:
        chip_version = matches.group()
        chip_version = re.sub(r'\bChip\b', '', chip_version)
        chip_version = chip_version.strip()
    else:
        chip_version = ""

    '''Color'''
    color = ''
    c_pattern = r'\b(silver|space gray|silver)\b'
    match = re.search(c_pattern, text, flags=re.IGNORECASE)
    if match:
        color = match.group(0)
    else:
        color = None

    return f'MacBook Pro {resolution} {chip_version} ({cpu_cores}-CPU {gpu_cores}-GPU) {memory_capacity}/{storage_capacity} {color}'
