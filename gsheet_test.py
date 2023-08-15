from format import krwusd, rubkgs, kgsusd

def get_need_data(lst, need_list, row_count=None):
    result = {}
    c = 0
    for dictionary in lst:
        c += 1
        for product in need_list:
            if product in dictionary:
                row_count+=1
                pre_prices = dictionary[product]
                
                if len(pre_prices) == 3 and c == 2:
                    won_to_usd = round(float(int(pre_prices[0])*krwusd), 2)
                    prices = [f'=ГИПЕРССЫЛКА("{pre_prices[2]}";"${won_to_usd}")']
                    
                elif len(pre_prices) == 3:
                    prices = [f'=ГИПЕРССЫЛКА("{pre_prices[2]}";"{pre_prices[0]}")']

                else:
                    prices = [pre_prices[0]]
                if len(prices) == 1:
                    result.setdefault(product, []).extend(prices)
                else:
                    result.setdefault(product, []).extend(['n/a',])
            else:
                result.setdefault(product, []).extend(['n/a'])

    for_gsheet = [[k] + v for k, v in result.items()]
    return for_gsheet


def header_row_writer(wks, coll_num, product_name):
    wks.update(f'B{coll_num}', 'Apple Insider')
    wks.update(f'C{coll_num}', 'Danawa')
    wks.update(f'D{coll_num}', 'Apple Refurbished')
    wks.update(f'E{coll_num}', 'TacSafon')
    wks.update(f'F{coll_num}', 'Apple Education')
    wks.update(f'A{coll_num}', product_name)

    wks.format(f'A{coll_num}:F{coll_num}', {
        "backgroundColor": {
            "red": 50,
            "green": 50,
            "blue": 50
        },
        "textFormat": {
            "fontSize": 12,
            "bold": True}
    })





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