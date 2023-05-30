# import gspread
# from parsing_ai import get_data_for_ai, headers
# from parsing_tf import get_data_for_tf
# from parsing_gs import pro_from_gs, air_from_gs
# from parsing_da import get_data_for_da
# from parsing_ref import get_data_for_ref
# # from gsheet import need_pro_list



# ai_pro14 = 'https://prices.appleinsider.com/macbook-pro-14-inch-2023'
# tf_pro14 = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-14"
# da_pro = 'https://prod.danawa.com/list/?cate=11336467'
# ref_pro = "https://www.apple.com/shop/refurbished/mac/13-inch-macbook-air"


# need_pro_list = [
#     'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Space Gray',
#     'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Silver',

#     'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Space Gray',
#     'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Silver',

#     'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Space Gray',
#     'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Silver',]


# macs_ai = get_data_for_ai(ai_pro14, headers)
# macs_da = get_data_for_da(da_pro)
# macs_ref = get_data_for_ref(ref_pro, need_pro_list, 'MacBook Pro')
# macs_tf = get_data_for_tf(tf_pro14)
# macs_gs = pro_from_gs


# lst = [macs_ai, macs_da, macs_ref, macs_tf, macs_gs]

# for macs_dict in lst:
#     for k, v in macs_dict.items():


# lst = [
#     {'product1': [1500, 11000, 'link'], 'product2':[2000, 20200, 'link'], 'product3': [3000, 34344, 'link'], 'product4': [4000, 322323]},
#     {'product1': [1200, 12000, 'link'], 'product5':[2400, 30200, 'link'], 'product3': [111, 22222], 'product8': [6000, 722323, 'link']},
#     {'product5': [1600, 17000, 'link'], 'product4':[4000, 322323,], 'product3': [3000, 34344, 'link'], 'product7': [4400, 342323, 'link']},
#     ]
def get_need_data(lst, need_list):

    result = {}
    c = 0
    for dictionary in lst:
        for product in need_list:
            if product in dictionary:
                pre_prices = dictionary[product]
                if len(pre_prices) == 3:
                    prices = [f'=ГИПЕРССЫЛКА("{pre_prices[2]}";"{pre_prices[0]}")', pre_prices[1]]
                else:
                    prices = pre_prices
                if len(prices) == 2:
                    result.setdefault(product, []).extend(prices)
                else:
                    result.setdefault(product, []).extend(['n/a', 'n/a'])
            else:
                result.setdefault(product, []).extend(['n/a', 'n/a'])

    for_gsheet = [[k] + v for k, v in result.items()]
    return for_gsheet



'''
#####last commit 


for i in lst:
    for k,v in i.items():
        if k not in result and len(v) == 3 and k in need_pro_list:
            result[k] = [f'=ГИПЕРССЫЛКА("{v[2]}";"{v[0]}")', f'=ГИПЕРССЫЛКА("{v[2]}";"{v[1]}")']
        elif k not in result and len(v) == 2 and k in need_pro_list:
            result[k] = [v[0], v[1]]
        
        elif k in result and len(v) == 3 and k in need_pro_list:
            result[k]+=[f'=ГИПЕРССЫЛКА("{v[2]}";"{v[0]}")', f'=ГИПЕРССЫЛКА("{v[2]}";"{v[1]}")']
        elif k in result and len(v) == 2 and k in need_pro_list:
            result[k]+=[v[0], v[1]]

for_gsheet = [[k] + v for k, v in result.items()]


'''