import re



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



def format_description_pro(description) -> str:
    colors = ['starlight', 'midnight', 'silver', 'space', 'gray']
    ru_colors = ['сияющая', 'звезда', 'полночь', 'серый', 'космос', 'полночь', 'серебристый']
    CPU_variations = ['10core', '12core', '8core', '10C', '12C', '8C', ]
    GPU_variations = ['14core', '16core', '19core', '30core','32core', '38core', '14C', '16C', '19C', '30C', '32C', '38C']
    inches = ['14', '16', '13', '13.6']

    new_string = re.sub(r'[^\w\s.]', '', description)
    
    description = new_string.split(' ')
    # print(description)
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


    return f'MacBook Pro 14     {chip} {model} {cgpu} {"/".join(memory)} {color}'

'MacBook Pro 14 M2 (10-CPU 16-GPU) 16/512 Space Gray'

for i in list2:
    print(format_description_pro(i))



# print(format_description_pro('Apple MacBook Pro 14” MMQX3 (2021, Apple M1 Max 10C CPU, 32C GPU, 64GB, 2048GB SSD) серебристый'))

words = ['TB', 'GB', 'MB']
words2 = ['256GB', '1TB', 'HETBllo', '512MB' , 'Hello', 'John']

def format_description_air(description) -> str:
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
# print(format_description_air('M2 (8-core GPU), 16GB, 256GB, Space Gray'))

# for i in list1:
#     print(format_description_air(i))


['MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/51216/512 Space Gray', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/51216/512 Silver', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/1TB16/1TB Space Gray', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/1TB16/1TB Silver', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/2TB16/2TB Space Gray', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/2TB16/2TB Silver', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/4TB16/4TB Space Gray', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/4TB16/4TB Silver', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/8TB16/8TB Space Gray', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 16/8TB16/8TB Silver', 'MacBook Pro Pro 14 M2 (10-CPU 16-GPU) 32/51232/512 Space Gray']