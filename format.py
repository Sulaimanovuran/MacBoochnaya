import string
import requests
import re
import math

import gspread

"""Авторизация"""
sa = gspread.service_account()

"""Подключаемся к документу"""
sh = sa.open("MacPython")

"""Подключаемся к странице"""
wks = sh.worksheet('TestData2')

kgsusd = float(wks.acell('Z3').value.replace(',', '.'))
kgsrub = float(wks.acell('Y3').value.replace(',', '.'))

data = round(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['USD'].get('Value'),2)

x = string.punctuation
num = string.digits

need = ['Max','CPU','GPU']
hard = ['8GB','16GB','32GB','64GB','96GB']

def format_description_pro(description, flag=None) -> str:
    colors = ['silver', 'space', 'gray']
    ru_colors = ['сияющая', 'звезда', 'полночь', 'серый', 'космос', 'полночь', 'серебристый']
    CPU_variations = ['10core', '12core', '8core', '10C', '12C', '8C', '10CPU', '12CPU', '8CPU',]
    GPU_variations = ['14core', '16core', '19core', '30core','32core', '38core', '24core','14C', '16C', '19C', '24C', '30C', '32C', '38C', '14GPU', '16GPU', '19GPU', '24GPU','30GPU', '32GPU', '38GPU', '14gpu', '16gpu', '19gpu', '24gpu','30gpu', '32gpu', '38gpu']
    text = description
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
        if word in CPU_variations or word.lower().replace('-','') in CPU_variations:
            cgpu += f"({re.sub(r'[a-zA-Z]', '', word)}-CPU "
            continue
        if word in GPU_variations or word.lower().replace('-','') in GPU_variations:
            cgpu += f"{re.sub(r'[a-zA-Z]', '', word)}-GPU)"
            continue

        '''Определение модели'''
        pattern = r"M[12]\s*(Pro|Max)?"

        result = re.search(pattern, text)

        if result:
            chip_version = result.group(1)
        else:
            chip_version = None

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
                memory.append(word.replace('GB', ''))
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

    # if chip_version:
    #     return f'{chip} {chip_version} {cgpu} {"/".join(memory)} {color}'
    
    # else:
    #     return f'{chip} {cgpu} {"/".join(memory)} {color}'
    return {'chip':chip, 'chip_version':chip_version, 'cgpu':cgpu, 'memory': '/'.join(memory), 'color': color}







def format_description_air(description, flag=None) -> str:
    colors = ['starlight', 'midnight', 'silver', 'space', 'gray', 'gold']
    ru_colors = ['сияющая', 'звезда', 'полночь', 'космос', 'полночь', 'серебристый']
    new_string = re.sub(r'[^\w\s.]', '', description)
    
    description = new_string.split(' ')
    memory = []
    chip = []
    color = []

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


    return f'MacBook Air {chip[0] if len(chip) != 0 else None} {"/".join(memory)} {color[0] if len(color) != 0 else None}'


def format_price(price):
    usd = int(price.split()[0])/data
    return ('$'+str(round(usd,2)))


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


def func(list1, list2, list3=None, item_names=None):

    products = {}

    for item in item_names:
        products[item] = []
        for lst in [list1, list2, list3]:
            for sub_lst in lst:
                if sub_lst[0] == item:
                    products[item].append('$'+sub_lst[1] if '$' not in sub_lst[1] else sub_lst[1])
                    break
            else:
                products[item].append("n/a")

    result  = [[k] + [j for j in v] for k, v in products.items()]
    return result



def format_description_air_ref(description, flag=None) -> str:
    if flag and description.count('GB') > 1 or description.count('TB') > 0:
        flag = None
    colors = ['starlight', 'midnight', 'silver', 'space', 'gray', 'gold']
    ru_colors = ['сияющая', 'звезда', 'полночь', 'космос', 'полночь', 'серебристый']
    new_string = re.sub(r'[^\w\s.]', '', description)
    description = new_string.split(' ')
    memory = []
    chip = []
    color = []

    gpu_search = re.compile(r'(\d+core GPU|\d+C GPU|\d+Core GPU|\d+GPU)')
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
                
            memory.append(word.replace('GB', ''))
            

        if 'M1' in word or 'M2' in word:
            chip.append(word)
            

        
        '''Определение цвета'''
        if word.lower() in colors or word.lower() in ru_colors:
            word_check = word.lower()
            if 'сияющая' in word_check and 'звезда' in word_check and len(color) == 0:
                color.append('Starlight')
                
            elif 'полночь' in word_check:
                color.append('Midnight')
                
            elif 'серый' in word_check or 'космос' in word_check and len(color) == 0:
                color.append('Space Gray')
                
            elif 'серебристый' in word_check:
                color.append('Silver')
                
            elif 'золотистый' in word_check:
                color.append('Gold')
                
            elif 'gold' in word_check:
                color.append('Gold')

            elif 'space' in word_check or 'gray' in word_check and len(color) == 0:
                color.append('Space Gray')
            else:
                color.append(word) if len(color) == 0 else ...


    return f'MacBook Air {chip[0] if len(chip) != 0 else None} {gpu}-GPU {"/".join(memory)} {color[0] if len(color) != 0 else None}'









# print(format_description_pro('M2 (12-core CPU, 30-core GPU), 32GB, 8TB, Space Gray'))

'''
def format_description(text):
    new_ = 'MacBook '

    for char in x:
        text = text.replace(char,'')

    if "Pro" in text:
        new_ += "Pro 14 "
    elif "Air" in text:
        new_ += "Air "
    if "Pro" not in text:
        new_ += "Pro 14 "
    if "M1" in text:
        new_ += 'M1 '
    elif "M2" in text:
        new_ += 'M2 '

    processed = text.split()

    for char in range(len(processed)):
        if processed[char] in need:

            if processed[char] == 'CPU':
                new_ += '('
                for i in range(len(processed[char])-1):
                    if (processed[char-1])[i] in num:
                        new_ += (processed[char-1])[i]
                new_ += '-'

            if processed[char] == 'GPU':
                for i in range(len(processed[char])):
                    if (processed[char-1])[i] in num:
                        new_ += (processed[char-1])[i]
                new_ += '-'
                new_ += processed[char]+') '

            if processed[char] in new_:continue
            else:new_ += processed[char]+' '

    arr = []
    for char in range(len(processed)):
        if processed[char] in hard:
            arr.append(processed[char].replace('GB',''))
            arr.append(processed[char+1].replace('GB',''))
    if len(arr) > 0:
        if len(arr[1]) > 3:
            arr[1] = f'{arr[1][0]}TB'
        else:
            new_ += f'{arr[0]}/{arr[1]}'

    if 'Space' and 'Gray' in processed:
        new_ += ' Space Gray'

    if 'Silver' in processed:
        new_ += ' Silver'

    if 'Midnight' in processed:
        new_ += ' Midnight'

    if 'Starlight' in processed:
        new_ += ' Starlight'

    if 'серебристый' in processed:
        new_ += ' Silver'

    if 'серый' and 'космос' in processed:
        new_ += ' Space Gray'

    
    return new_

'''