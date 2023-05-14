lst = [
    {'product1': [1500, 11000, 'link'], 'product2': [2000, 20200, 'link'], 'product3': [3000, 34344, 'link'], 'product4': [4000, 322323]},
    {'product1': [1200, 12000, 'link'], 'product5': [2400, 30200, 'link'], 'product3': [3300, 44344, 'link'], 'product8': [6000, 722323, 'link']},
    {'product5': [1600, 17000, 'link'], 'product4': [4000, 322323,], 'product3': [3000, 34344, 'link'], 'product7': [4400, 342323, 'link']},
]

result = []

for dictionary in lst:
    for product, info in dictionary.items():
        description = product
        link = info[2] if len(info) > 2 else 'n/a'
        price = info[0] if len(info) > 0 else 'n/a'
        price_rub = info[1] if len(info) > 1 else 'n/a'
        item = [description]
        if any(item[0] == x[0] for x in result):
            index = next((i for i, x in enumerate(result) if x[0] == item[0]), None)
            result[index].extend([f'{link} {price}', f'{link} {price_rub}'])
        else:
            item.extend([f'{link} {price}', f'{link} {price_rub}'])
            result.append(item)

print(result)

[
 ['product1', 'link 1500', 'link 11000', 'link 1200', 'link 12000'], 
 ['product2', 'link 2000', 'link 20200'], 
 ['product3', 'link 3000', 'link 34344', 'link 3300', 'link 44344', 'link 3000', 'link 34344'], 
 ['product4', 'n/a 4000', 'n/a 322323', 'n/a 4000', 'n/a 322323'], 
 ['product5', 'link 2400', 'link 30200', 'link 1600', 'link 17000'], 
 ['product8', 'link 6000', 'link 722323'], 
 ['product7', 'link 4400', 'link 342323']
 ]