from format import rubkgs, kgsusd

'''MacBook Air M1 #######done'''

macbook_air_m1 = {'base': 899, 'ram_16':180, 'storage_512':180, 'storage_1TB': 360, 'storage_2TB': 720}

colors_air_m1 = ['Space Gray', 'Gold', 'Silver']


air_m1 = 'MacBook Air M1 7-GPU 8/256'

airs_m1 = {'MacBook Air M1 7-GPU 8/256': 899}

for k,v in macbook_air_m1.items():
    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v
        airs_m1[f'MacBook Air M1 7-GPU {ram}/256'] = macbook_air_m1['base'] + v 

        for k,v in macbook_air_m1.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                airs_m1[f'MacBook Air M1 7-GPU {ram}/{storage}'] = macbook_air_m1['base'] + ram_cost + v

    else:
        if k.startswith('storage'):
            storage = k.split('_')[1]
            airs_m1[f'MacBook Air M1 7-GPU 8/{storage}'] = macbook_air_m1['base'] + v

m_air_m1 = {}
for name, price in airs_m1.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_air_m1:
        m_air_m1[name + ' ' + color] = [price, price_rub]


'''MacBook Air M2 #######done'''

macbook_air_m2 = {'base': 999, 'GPU_10':100, 'ram_16':180, 'ram_24': 360, 'storage_512':200, 'storage_1TB':380, 'storage_2TB':740}

colors_air_m2 = ['Space Gray', 'Starlight', 'Silver', 'Midnight']

airs_m2 = {'MacBook Air M2 8-GPU 8/256': 999}

for k, v in macbook_air_m2.items():
    if k.startswith('GPU'):
        gpu = k[-2:]
        gpu_cost = v
        airs_m2[f'MacBook Air M2 {gpu}-GPU 8/256'] = macbook_air_m2['base'] + v

        for k, v in macbook_air_m2.items():
            if k.startswith('ram'):
                ram = k[-2:]
                ram_cost = v
                airs_m2[f'MacBook Air M2 {gpu}-GPU {ram}/256'] = macbook_air_m2['base'] + gpu_cost + ram_cost

                for k, v in macbook_air_m2.items():
                    if k.startswith('storage'):
                        storage = k.split('_')[1]
                        airs_m2[f'MacBook Air M2 {gpu}-GPU {ram}/{storage}'] = macbook_air_m2['base'] + gpu_cost + ram_cost + v
            elif k.startswith('storage'):
                for k,v in macbook_air_m2.items():
                    if k.startswith('storage'):
                        storage = k.split('_')[1]
                        airs_m2[f'MacBook Air M2 {gpu}-GPU 8/{storage}'] = macbook_air_m2['base'] + gpu_cost + v


    elif k.startswith('ram'):

        for k,v in macbook_air_m2.items():
            if k.startswith('ram'):
                ram = k[-2:]
                ram_cost = v
                airs_m2[f'MacBook Air M2 8-GPU {ram}/256'] = macbook_air_m2['base'] + ram_cost

                for k, v in macbook_air_m2.items():
                    if k.startswith('storage'):
                        storage = k.split('_')[1]
                        airs_m2[f'MacBook Air M2 8-GPU {ram}/{storage}'] = macbook_air_m2['base'] + ram_cost + v

        
    elif k.startswith('storage'):

        for k,v in macbook_air_m2.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                airs_m2[f'MacBook Air M2 8-GPU 8/{storage}'] = macbook_air_m2['base'] + v


m_air_m2 = {}
for name, price in airs_m2.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_air_m2:
        m_air_m2[name + ' ' + color] = [price, price_rub]


'''MacBook Air 15 M2 '''

macbook_air_15 = {'base': 1199, 'GPU_10':100, 'ram_16':180, 'ram_24': 360, 'storage_512':200, 'storage_1TB':380, 'storage_2TB':740}


airs_15 = {'MacBook Air 15 M2 10-GPU 8/256': 1199}

for k, v in macbook_air_15.items():
    

    if k.startswith('ram'):

        for k,v in macbook_air_15.items():
            if k.startswith('ram'):
                ram = k[-2:]
                ram_cost = v
                airs_15[f'MacBook Air 15 M2 10-GPU {ram}/256'] = macbook_air_15['base'] + ram_cost

                for k, v in macbook_air_15.items():
                    if k.startswith('storage'):
                        storage = k.split('_')[1]
                        airs_15[f'MacBook Air 15 M2 10-GPU {ram}/{storage}'] = macbook_air_15['base'] + ram_cost + v

        
    elif k.startswith('storage'):

        for k,v in macbook_air_15.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                airs_15[f'MacBook Air 15 M2 10-GPU 8/{storage}'] = macbook_air_15['base'] + v


m_air_15 = {}
for name, price in airs_15.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_air_m2:
        m_air_15[name + ' ' + color] = [price, price_rub]

############################################
colors_pro = ['Silver', 'Space Gray']

'''MacBook Pro 13 #######done'''

macbook_pro_13_m2 = {'base': 1199, 'ram_16': 180, 'ram_24': 360, 'storage_512': 200, 'storage_1TB': 380, 'storage_2TB': 740}


pro_13 = {'MacBook Pro 13 M2 (8-CPU 10-GPU) 8/256': 1199}


for k, v in macbook_pro_13_m2.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        pro_13[f'MacBook Pro 13 M2 (8-CPU 10-GPU) {ram}/256'] = macbook_pro_13_m2['base'] + ram_cost

        for k, v in macbook_pro_13_m2.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                pro_13[f'MacBook Pro 13 M2 (8-CPU 10-GPU) {ram}/{storage}'] = macbook_pro_13_m2['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        pro_13[f'MacBook Pro 13 M2 (8-CPU 10-GPU) 8/{storage}'] = macbook_pro_13_m2['base'] + v


m_pro_13 = {}
for name, price in pro_13.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_pro:
        m_pro_13[name + ' ' + color] = [price, price_rub]


############################################


'''MacBook Pro 14 M2 Pro (10-16) #######done'''

macbook_pro_14_m2_pro_1 = {'base': 1849, 'ram_32': 360, 'storage_1TB': 180, 'storage_2TB': 540, 'storage_4TB': 1080, 'storage_8TB': 2160}

pro_14_1 = {'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512': 1849}


for k, v in macbook_pro_14_m2_pro_1.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        pro_14_1[f'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) {ram}/512'] = macbook_pro_14_m2_pro_1['base'] + ram_cost

        for k, v in macbook_pro_14_m2_pro_1.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                pro_14_1[f'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) {ram}/{storage}'] = macbook_pro_14_m2_pro_1['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        pro_14_1[f'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/{storage}'] = macbook_pro_14_m2_pro_1['base'] + v


m_pro_14_1 = {}
for name, price in pro_14_1.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_pro:
        m_pro_14_1[name + ' ' + color] = [price, price_rub]


'''MacBook Pro 14 M2 Pro (12-19)  #######done'''

macbook_pro_14_m2_pro_2 = {'base': 2119, 'ram_32': 360, 'storage_1TB': 180, 'storage_2TB': 540, 'storage_4TB': 1080, 'storage_8TB': 2160}


pro_14_2 = {'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/512': 2119}



for k, v in macbook_pro_14_m2_pro_2.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        pro_14_2[f'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) {ram}/512'] = macbook_pro_14_m2_pro_2['base'] + ram_cost

        for k, v in macbook_pro_14_m2_pro_2.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                pro_14_2[f'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) {ram}/{storage}'] = macbook_pro_14_m2_pro_2['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        pro_14_2[f'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/{storage}'] = macbook_pro_14_m2_pro_2['base'] + v


m_pro_14_2 = {}
for name, price in pro_14_2.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_pro:
        m_pro_14_2[name + ' ' + color] = [price, price_rub]


'''MacBook Pro 14 M2 Max (12-30)  #######done'''

macbook_pro_14_m2_max_1 = {'base': 2619, 'ram_64': 360, 'storage_1TB': 180, 'storage_2TB': 540, 'storage_4TB': 1080, 'storage_8TB': 2160}


pro_14_3 = {'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/512': 2619}



for k, v in macbook_pro_14_m2_max_1.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        pro_14_3[f'MacBook Pro 14 M2 Max (12-CPU 30-GPU) {ram}/512'] = macbook_pro_14_m2_max_1['base'] + ram_cost

        for k, v in macbook_pro_14_m2_max_1.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                pro_14_3[f'MacBook Pro 14 M2 Max (12-CPU 30-GPU) {ram}/{storage}'] = macbook_pro_14_m2_max_1['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        pro_14_3[f'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/{storage}'] = macbook_pro_14_m2_max_1['base'] + v


m_pro_14_3 = {}
for name, price in pro_14_3.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_pro:
        m_pro_14_3[name + ' ' + color] = [price, price_rub]


'''MacBook Pro 14 M2 Max (12-38) #######done'''

macbook_pro_14_m2_max_2 = {'base': 2799, 'ram_64': 360, 'ram_96': 720, 'storage_1TB': 180, 'storage_2TB': 540, 'storage_4TB': 1080, 'storage_8TB': 2160}


pro_14_4 = {'MacBook Pro 14 M2 Max (12-CPU 38-GPU) 32/512': 2799}


for k, v in macbook_pro_14_m2_max_2.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        pro_14_4[f'MacBook Pro 14 M2 Max (12-CPU 38-GPU) {ram}/512'] = macbook_pro_14_m2_max_2['base'] + ram_cost

        for k, v in macbook_pro_14_m2_max_2.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                pro_14_4[f'MacBook Pro 14 M2 Max (12-CPU 38-GPU) {ram}/{storage}'] = macbook_pro_14_m2_max_2['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        pro_14_4[f'MacBook Pro 14 M2 Max (12-CPU 38-GPU) 32/{storage}'] = macbook_pro_14_m2_max_2['base'] + v


m_pro_14_4 = {}
for name, price in pro_14_4.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_pro:
        m_pro_14_4[name + ' ' + color] = [price, price_rub]

############################################


'''MacBook Pro 16 M2 Pro (12-19) #######done'''

macbook_pro_16_m2_pro_1 = {'base': 2299, 'ram_32': 360, 'storage_1TB': 200, 'storage_2TB': 560, 'storage_4TB': 1100, 'storage_8TB': 2180}


pro_16_1 = {'MacBook Pro 16 M2 Pro (12-CPU 19-GPU) 16/512': 2299}


for k, v in macbook_pro_16_m2_pro_1.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        pro_16_1[f'MacBook Pro 16 M2 Pro (12-CPU 19-GPU) {ram}/512'] = macbook_pro_16_m2_pro_1['base'] + ram_cost

        for k, v in macbook_pro_16_m2_pro_1.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                pro_16_1[f'MacBook Pro 16 M2 Pro (12-CPU 19-GPU) {ram}/{storage}'] = macbook_pro_16_m2_pro_1['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        pro_16_1[f'MacBook Pro 16 M2 Pro (12-CPU 19-GPU) 16/{storage}'] = macbook_pro_16_m2_pro_1['base'] + v


m_pro_16_1 = {}
for name, price in pro_16_1.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_pro:
        m_pro_16_1[name + ' ' + color] = [price, price_rub]


'''MacBook Pro 16 M2 Max (12-30) #######done'''

macbook_pro_16_m2_pro_2 = {'base': 2839, 'ram_64': 360, 'storage_1TB': 200, 'storage_2TB': 560, 'storage_4TB': 1100, 'storage_8TB': 2180}


pro_16_2 = {'MacBook Pro 16 M2 Max (12-CPU 30-GPU) 32/512': 2839}


for k, v in macbook_pro_16_m2_pro_2.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        pro_16_2[f'MacBook Pro 16 M2 Max (12-CPU 30-GPU) {ram}/512'] = macbook_pro_16_m2_pro_2['base'] + ram_cost

        for k, v in macbook_pro_16_m2_pro_2.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                pro_16_2[f'MacBook Pro 16 M2 Max (12-CPU 30-GPU) {ram}/{storage}'] = macbook_pro_16_m2_pro_2['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        pro_16_2[f'MacBook Pro 16 M2 Max (12-CPU 30-GPU) 32/{storage}'] = macbook_pro_16_m2_pro_2['base'] + v


m_pro_16_2 = {}
for name, price in pro_16_2.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_pro:
        m_pro_16_2[name + ' ' + color] = [price, price_rub]

'''MacBook Pro 16 M2 Max (12-38) #######done'''

macbook_pro_16_m2_max_1 = {'base': 2999, 'ram_64': 360, 'ram_96': 720, 'storage_1TB': 200, 'storage_2TB': 560, 'storage_4TB': 1100, 'storage_8TB': 2180}


pro_16_3 = {'MacBook Pro 16 M2 Max (12-CPU 38-GPU) 32/512': 2999}


for k, v in macbook_pro_16_m2_max_1.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        pro_16_3[f'MacBook Pro 16 M2 Max (12-CPU 38-GPU) {ram}/512'] = macbook_pro_16_m2_max_1['base'] + ram_cost

        for k, v in macbook_pro_16_m2_max_1.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                pro_16_3[f'MacBook Pro 16 M2 Max (12-CPU 38-GPU) {ram}/{storage}'] = macbook_pro_16_m2_max_1['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        pro_16_3[f'MacBook Pro 16 M2 Max (12-CPU 38-GPU) 32/{storage}'] = macbook_pro_16_m2_max_1['base'] + v


m_pro_16_3 = {}
for name, price in pro_16_3.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    for color in colors_pro:
        m_pro_16_3[name + ' ' + color] = [price, price_rub]

########################################################################################


air_from_edu = {}

air_from_edu.update(m_air_m1)
air_from_edu.update(m_air_m2)


pro_from_edu = {}

pro_from_edu.update(m_pro_13)
pro_from_edu.update(m_pro_14_1)
pro_from_edu.update(m_pro_14_2)
pro_from_edu.update(m_pro_14_3)
pro_from_edu.update(m_pro_14_4)

pro_from_edu.update(m_pro_16_1)
pro_from_edu.update(m_pro_16_2)
pro_from_edu.update(m_pro_16_3)


########################################################################################

'''Mac mini M2 #######done'''

mac_mini_m2 = {'base': 499, 'ram_16': 180, 'ram_24': 360, 'storage_512': 200, 'storage_1TB': 380, 'storage_2TB': 740, }

mini_m2 = {'Mini M2 10-GPU 8/256': 499, }

for k, v in mac_mini_m2.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        mini_m2[f'Mini M2 10-GPU {ram}/256'] = mac_mini_m2['base'] + ram_cost

        for k, v in mac_mini_m2.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                mini_m2[f'Mini M2 10-GPU {ram}/{storage}'] = mac_mini_m2['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        mini_m2[f'Mini M2 10-GPU 8/{storage}'] = mac_mini_m2['base'] + v

m_mini_m2 = {}
for name, price in mini_m2.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    m_mini_m2[name] = [price, price_rub]
    price = price + 90
    price_rub = round(price * kgsusd * rubkgs, 2)
    m_mini_m2[name + ' ' + '10GbE'] = [price, price_rub]








'''Mac mini M2 Pro 16-GPU #######done'''

mac_mini_m2_pro_1 = {'base': 1199, 'ram_32': 360, 'storage_1TB': 180, 'storage_2TB': 540, 'storage_4TB': 1080, 'storage_8TB': 2160}

mini_m2_pro_1 = {'Mini M2 Pro 16-GPU 16/512': 1199, }

for k, v in mac_mini_m2_pro_1.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        mini_m2_pro_1[f'Mini M2 Pro 16-GPU {ram}/512'] = mac_mini_m2_pro_1['base'] + ram_cost

        for k, v in mac_mini_m2_pro_1.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                mini_m2_pro_1[f'Mini M2 Pro 16-GPU {ram}/{storage}'] = mac_mini_m2_pro_1['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        mini_m2_pro_1[f'Mini M2 Pro 16-GPU 16/{storage}'] = mac_mini_m2_pro_1['base'] + v

m_mini_m2_pro_1 = {}


for name, price in mini_m2_pro_1.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    m_mini_m2_pro_1[name] = [price, price_rub]
    price = price + 90
    price_rub = round(price * kgsusd * rubkgs, 2)
    m_mini_m2_pro_1[name + ' ' + '10GbE'] = [price, price_rub]



'''Mac mini M2 Pro 19-GPU #######done'''

mac_mini_m2_pro_2 = {'base': 1469, 'ram_32': 360, 'storage_1TB': 180, 'storage_2TB': 540, 'storage_4TB': 1080, 'storage_8TB': 2160}

mini_m2_pro_2 = {'Mini M2 Pro 19-GPU 16/512': 1469, }

for k, v in mac_mini_m2_pro_2.items():

    if k.startswith('ram'):
        ram = k[-2:]
        ram_cost = v

        mini_m2_pro_2[f'Mini M2 Pro 19-GPU {ram}/512'] = mac_mini_m2_pro_2['base'] + ram_cost

        for k, v in mac_mini_m2_pro_2.items():
            if k.startswith('storage'):
                storage = k.split('_')[1]
                mini_m2_pro_2[f'Mini M2 Pro 19-GPU {ram}/{storage}'] = mac_mini_m2_pro_2['base'] + ram_cost + v

    elif k.startswith('storage'):
        storage = k.split('_')[1]
        mini_m2_pro_2[f'Mini M2 Pro 19-GPU 16/{storage}'] = mac_mini_m2_pro_2['base'] + v

m_mini_m2_pro_2 = {}


for name, price in mini_m2_pro_2.items():
    price_rub = round(price * kgsusd * rubkgs, 2)
    m_mini_m2_pro_2[name] = [price, price_rub]
    price = price + 90
    price_rub = round(price * kgsusd * rubkgs, 2)
    m_mini_m2_pro_2[name + ' ' + '10GbE'] = [price, price_rub]


###############################################################################################


mini_from_edu = {}

mini_from_edu.update(m_mini_m2)
mini_from_edu.update(m_mini_m2_pro_1)
mini_from_edu.update(m_mini_m2_pro_2)


###############################################################################################