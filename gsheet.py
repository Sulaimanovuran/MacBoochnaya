import time
import gspread
from parsing_ai import get_data_for_ai, headers, get_data_for_ai_mac_mini
from parsing_tf import get_data_for_tf, get_data_for_tf_mini
# from parsing_gs import pro_from_gs, air_from_gs
from parsing_edu import pro_from_edu, air_from_edu, mini_from_edu
from gsheet_test import get_need_data, header_row_writer
from parsing_da import get_data_for_da, headers as head, get_data_for_da_mac_mini
from parsing_ref import get_data_for_ref


# Создаем списки нужных нам моделей


need_pro_list = [

    'MacBook Pro 14 M1 Pro (8-CPU 14-GPU) 16/512 Silver',
    'MacBook Pro 14 M1 Pro (8-CPU 14-GPU) 16/512 Space Gray',

    'MacBook Pro 14 M1 Pro (8-CPU 14-GPU) 16/1TB Silver',
    'MacBook Pro 14 M1 Pro (8-CPU 14-GPU) 16/1TB Space Gray',

    'MacBook Pro 14 M1 Pro (10-CPU 16-GPU) 16/1TB Silver',
    'MacBook Pro 14 M1 Pro (10-CPU 16-GPU) 16/1TB Space Gray',

    'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Space Gray',
    'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Silver',

    'MacBook Pro 16 M1 Pro (10-CPU 16-GPU) 16/512 Silver',
    'MacBook Pro 16 M1 Pro (10-CPU 16-GPU) 16/512 Space Gray',

    ]



need_air_list = [
    'MacBook Air M2 8-GPU 8/256 Space Gray',
    'MacBook Air M2 8-GPU 8/256 Silver',
    'MacBook Air M2 8-GPU 8/256 Starlight',
    'MacBook Air M2 8-GPU 8/256 Midnight',

    'MacBook Air M2 8-GPU 16/256 Space Gray',
    'MacBook Air M2 8-GPU 16/256 Silver',
    'MacBook Air M2 8-GPU 16/256 Starlight',
    'MacBook Air M2 8-GPU 16/256 Midnight',

    'MacBook Air M2 8-GPU 16/512 Space Gray',
    'MacBook Air M2 8-GPU 16/512 Silver',
    'MacBook Air M2 8-GPU 16/512 Starlight',
    'MacBook Air M2 8-GPU 16/512 Midnight',
]


need_mini_list = [
    'Mini M1 8-GPU 8/256',
    'Mini M1 8-GPU 16/512',
    'Mini M2 10-GPU 8/256',
    'Mini M2 10-GPU 16/256',
    'Mini M2 10-GPU 24/256',
    'Mini M2 10-GPU 16/512',
    'Mini M2 Pro 16-GPU 16/512',
]




'''             Apple Insider           '''

"""MacBooks"""
ai_pro = 'https://prices.appleinsider.com/macbook-pro-14-inch-2023'
ai_pro_16 = "https://prices.appleinsider.com/macbook-pro-16-inch-2021"
# ai_pro_13 = "https://prices.appleinsider.com/macbook-pro-13-inch-2022"
ai_pro_14_m1 = 'https://prices.appleinsider.com/macbook-pro-14-inch-2021'
ai_air = 'https://prices.appleinsider.com/macbook-air-2022'

pro_from_ai = get_data_for_ai(ai_pro, headers)
pro_m1_from_ai = get_data_for_ai(ai_pro_14_m1, headers)
# pro_13_from_ai = get_data_for_ai(ai_pro_13, headers)
pro_16_from_ai = get_data_for_ai(ai_pro_16, headers)
air_from_ai = get_data_for_ai(ai_air, headers)

pro_from_ai.update(pro_m1_from_ai)
pro_from_ai.update(pro_16_from_ai)

"""Mac mini"""

mini_m1_ai = 'https://prices.appleinsider.com/mac-mini-late-2020'
mini_m2_ai = 'https://prices.appleinsider.com/mac-mini-2023'

mini_from_ai = get_data_for_ai_mac_mini(mini_m1_ai, headers=headers)
mini_from_ai.update(get_data_for_ai_mac_mini(mini_m2_ai, headers=headers))


'''             Tacsafon                '''

"""MacBooks"""
tf_pro = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-14"
tf_pro_16 = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-16"
# tf_pro_13 = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-13"
tf_air = 'https://tacsafon.ru/magazin/folder/apple-macbook-air'

pro_from_tf = get_data_for_tf(tf_pro)
# pro_13_from_tf = get_data_for_tf(tf_pro_13)
pro_16_from_tf = get_data_for_tf(tf_pro_16)
air_from_tf = get_data_for_tf(tf_air)

pro_from_tf.update(pro_16_from_tf)

"""Mac mini"""

mini_tf = 'https://tacsafon.ru/magazin/folder/apple-mac-mini'

mini_from_tf = get_data_for_tf_mini(mini_tf)

'''             Danawa              '''

"""MacBooks"""
da_pro = 'https://search.danawa.com/dsearch.php?query=Macbook+pro+14+M2'
da_pro_m1 = 'https://search.danawa.com/dsearch.php?query=Macbook+pro+14+M1'
da_pro_16 = 'https://search.danawa.com/dsearch.php?k1=Macbook+pro+16+M1'
# da_pro_13 = 'https://search.danawa.com/dsearch.php?query=Macbook+pro+13+m2'
da_air_m1 = 'https://search.danawa.com/dsearch.php?query=MacBook+Air+m1'
da_air_m2 = 'https://search.danawa.com/dsearch.php?query=MacBook+Air+2022'

pro_from_da = get_data_for_da(da_pro, headres=head)
pro_m1_from_da = get_data_for_da(da_pro_m1, headres=head)
pro_16_from_da = get_data_for_da(da_pro_16, headres=head)
# pro_13_from_da = get_data_for_da(da_pro_13, headres=head)
air_from_da = get_data_for_da(da_air_m1, headres=head)
air_from_da_2 = get_data_for_da(da_air_m2, headres=head)

air_from_da.update(air_from_da_2)
pro_from_da.update(pro_m1_from_da)
pro_from_da.update(pro_16_from_da)

"""Mac mini"""

mini_da = 'https://search.danawa.com/dsearch.php?k1=macmini&module=goods&act=dispMain'

mini_from_da = get_data_for_da_mac_mini(mini_da, head)



'''             Apple Refurb                '''

"""MacBooks"""
ref = "https://www.apple.com/shop/refurbished/mac/13-inch-macbook-air"

pro_from_ref = get_data_for_ref(ref, 'MacBook Pro', need_pro_list)
air_from_refurb = get_data_for_ref(ref, 'Air', need_air_list)

"""MacMini"""

mini_from_ref = get_data_for_ref(ref, 'Mac mini', need_mini_list)

"""Фильтрация по нужным моделям из списка"""

validated_pro = get_need_data([pro_from_ref, pro_from_ai, pro_from_da, pro_from_tf, pro_from_edu], need_pro_list, row_count=3)

validated_air = get_need_data([air_from_refurb, air_from_ai, air_from_da, air_from_tf, air_from_edu ], need_air_list, row_count=len(validated_pro)+5)

validated_mini = get_need_data([mini_from_ref, mini_from_ai, mini_from_da, mini_from_tf, mini_from_edu], need_mini_list, row_count=len(validated_air)+len(validated_pro)+7)


"""Запись в Google Sheets"""

def main():
    """Авторизация"""
    sa = gspread.service_account()

    """Подключаемся к документу"""
    sh = sa.open("MacPython")

    """Подключаемся к странице и очищаем её"""
    wks = sh.worksheet('TestData2')
    wks.batch_clear(["A2:M50"])
    


    """Обновляем записи в указанном диапазоне"""
    coll_nums = len(validated_pro) + 2  #Отслеживание каретки

    '''MacBook Pro'''
    header_row_writer(wks, coll_num=1, product_name='MacBook Pro')

    wks.update(f'A3:F{coll_nums}', validated_pro,
               value_input_option='USER_ENTERED')
    coll_nums += 2


    '''MacBook Air'''
    header_row_writer(wks, coll_num=coll_nums, product_name='MacBook Air')

    wks.update(f'A{coll_nums+1}:K{coll_nums + 1 + len(validated_air)+1}',
               validated_air, value_input_option='USER_ENTERED')

    
    coll_nums += 1 + len(validated_air)+1

    '''Mac Mini'''
    header_row_writer(wks, coll_num=coll_nums, product_name='Mac Mini')

    wks.update(f'A{coll_nums+1}:K{coll_nums + 1 + len(validated_mini)+1}',
               validated_mini, value_input_option='USER_ENTERED')




if __name__ == '__main__':
    main()
    print('Обновление записей')
    # while True:
    #     # time.sleep(5)
    #     main()
    #     print('Обновление записей')




"""Примеры форматирования"""

    # """Задаем формат"""
    # wks.format(f"A3:A{len(validated_pro)}", {
    #     "backgroundColor": {
    #         "red": 1,
    #         "green": 1,
    #         "blue": 1
    #     },
    #     "horizontalAlignment": "LEFT",
    #     "verticalAlignment": "TOP",
    #     "wrapStrategy": "WRAP",
    #     "textFormat": {
    #         "foregroundColor": {
    #             "red": 0,
    #             "green": 0,
    #             "blue": 0
    #         },
    #         "fontSize": 10,
    #         "bold": False
    #     }
    # })