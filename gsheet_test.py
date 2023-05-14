import gspread
from parsing_ai import get_data_for_ai, headers
from parsing_tf import get_data_for_tf
from parsing_gs import pro_from_gs, air_from_gs
from parsing_da import get_data_for_da
from parsing_ref import get_data_for_ref
from gsheet import need_pro_list

ai_pro14 = 'https://prices.appleinsider.com/macbook-pro-14-inch-2023'
tf_pro14 = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-14"
da_pro = 'https://prod.danawa.com/list/?cate=11336467'
ref_pro = "https://www.apple.com/shop/refurbished/mac/13-inch-macbook-air"


macs_ai = get_data_for_ai(ai_pro14, headers)
macs_da = get_data_for_da(da_pro)
macs_ref = get_data_for_ref(ref_pro)


# lst = [macs_ai, macs_da, macs_ref]

# for macs_dict in lst:
#     for k, v in macs_dict.items():


lst = [
    {'product1': [1500, 11000, 'link'], 'product2':[2000, 20200, 'link'], 'product3': [3000, 34344, 'link'], 'product4': [4000, 322323]},
    {'product1': [1200, 12000, 'link'], 'product5':[2400, 30200, 'link'], 'product3': [3300, 44344, 'link'], 'product8': [6000, 722323, 'link']},
    {'product5': [1600, 17000, 'link'], 'product4':[4000, 322323,], 'product3': [3000, 34344, 'link'], 'product7': [4400, 342323, 'link']},
    ]

for i in lst:
    