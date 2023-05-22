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

print(result)
