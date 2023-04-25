import string
import requests


data = round(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['USD'].get('Value'),2)

x = string.punctuation
num = string.digits

need = ['Max','CPU','GPU']
hard = ['8GB','16GB','32GB','64GB','96GB']

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

    if len(arr[1]) > 3:
        arr[1] = f'{arr[1][0]}TB'
    else:
        new_ += f'{arr[0]}/{arr[1]}'
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

def format_price(price):
    usd = int(price.split()[0])/data
    return ('$'+str(round(usd,2)))
