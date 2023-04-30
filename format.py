import string
import requests
import re


data = round(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['USD'].get('Value'),2)

x = string.punctuation
num = string.digits

need = ['Max','CPU','GPU']
hard = ['8GB','16GB','32GB','64GB','96GB']

def format_description_pro(description, flag=None) -> str:
    colors = ['starlight', 'midnight', 'silver', 'space', 'gray']
    ru_colors = ['сияющая', 'звезда', 'полночь', 'серый', 'космос', 'полночь', 'серебристый']
    CPU_variations = ['10core', '12core', '8core', '10C', '12C', '8C', '10CPU', '12CPU', '8CPU',]
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
        if word in GPU_variations :
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


    return f'MacBook Pro 14 {chip} {model} {cgpu} {"/".join(memory)} {color}'

def format_description_air(description, flag=None) -> str:
    colors = ['starlight', 'midnight', 'silver', 'space', 'gray']
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


def format_price(price):
    usd = int(price.split()[0])/data
    return ('$'+str(round(usd,2)))



def get_need_models(models1, models2, models3=None, need_models=None):
    # for model in models1:
    #     if model[0] in need_models:
    #         print(model[0])

    # print('******************')
    # for model in models2:
    #     if model[0] in need_models:
    #         print(model[0])
    # print('******************')

    # for model in models3:
    #     if model[0] in need_models:
    #         print(model[0])
    # Создаем пустой словарь для хранения товаров и цен
    products = {}

    # Проходим по первому списку и добавляем товары и цены в словарь
    for product in models1:
        if product[0] in need_models:
            products[product[0]] = [product[1], 'n/a']

    # Проходим по второму списку и добавляем цены к существующим товарам или создаем новые
    for product in models2:
        if product[0] in products and product[0] in need_models:
            products[product[0]].pop(-1)
            products[product[0]].append(product[1])
            products[product[0]].append('n/a')


        else:
            if product[0] in need_models:
                products[product[0]] = ['n/a', product[1], 'n/a']

    if models3:
        for product in models3:
            if product[0] in products and product[0] in need_models:
                products[product[0]].pop(-1)
                products[product[0]].append('$'+product[1])
            else:
                if product[0] in need_models:
                    products[product[0]] = ['n/a','n/a', '$'+product[1]]


    result  = [[k] + [j for j in v] for k, v in products.items()]
    return result


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