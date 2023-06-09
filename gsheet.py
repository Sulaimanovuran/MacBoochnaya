import time
import gspread
from parsing_ai import get_data_for_ai, headers
from parsing_tf import get_data_for_tf
from parsing_gs import pro_from_gs, air_from_gs
from gsheet_test import get_need_data
from parsing_da import get_data_for_da, headers as head
from parsing_ref import get_data_for_ref
# from format import get_need_models, func

# Создаем списки нужных нам моделей


need_pro_list = [
    'MacBook Pro 13 M2 Pro (10-CPU 16-GPU) 16/256 Space Gray',
    'MacBook Pro 13 M2 Pro (10-CPU 16-GPU) 16/256 Silver',
    'MacBook Pro 13 M2 Pro (10-CPU 16-GPU) 16/512 Space Gray',
    'MacBook Pro 13 M2 Pro (10-CPU 16-GPU) 16/512 Silver',
    'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Space Gray',
    'MacBook Pro 14 M2 Pro (10-CPU 16-GPU) 16/512 Silver',

    'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Space Gray',
    'MacBook Pro 14 M2 Pro (12-CPU 19-GPU) 16/1TB Silver',

    'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Space Gray',
    'MacBook Pro 14 M2 Max (12-CPU 30-GPU) 32/1TB Silver',]

need_air_list = [
    'MacBook Air M2 8/256 Space Gray',
    'MacBook Air M2 8/256 Silver',
    'MacBook Air M2 8/256 Starlight',
    'MacBook Air M2 8/256 Midnight',
    'MacBook Air M2 16/256 Space Gray',
    'MacBook Air M2 16/256 Silver',
    'MacBook Air M2 16/512 Space Gray',
    'MacBook Air M2 16/512 Silver',
    'MacBook Air M2 24/512 Space Gray',
    'MacBook Air M2 24/512 Silver',
    'MacBook Air M2 24/256 Space Gray',
    'MacBook Air M2 24/256 Silver',
]



ai_pro = 'https://prices.appleinsider.com/macbook-pro-14-inch-2023'
ai_pro_16 = "https://prices.appleinsider.com/macbook-pro-16-inch-2023"
ai_pro_13 = "https://prices.appleinsider.com/macbook-pro-13-inch-2022"
ai_air = 'https://prices.appleinsider.com/macbook-air-2022'

pro_from_ai = get_data_for_ai(ai_pro, headers)
pro_13_from_ai = get_data_for_ai(ai_pro_13, headers)
# pro_16_from_ai = get_data_for_ai(ai_pro_16, headers)
air_from_ai = get_data_for_ai(ai_air, headers)


tf_pro = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-14"
tf_pro_16 = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-16"
tf_pro_13 = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-13"
tf_air = 'https://tacsafon.ru/magazin/folder/apple-macbook-air'

pro_from_tf = get_data_for_tf(tf_pro)
pro_13_from_tf = get_data_for_tf(tf_pro_13)
# pro_16_from_tf = get_data_for_tf(tf_pro_16)
air_from_tf = get_data_for_tf(tf_air)


da_pro = 'https://prod.danawa.com/list/?cate=11336467'
da_air = 'https://prod.danawa.com/list/?cate=11336468'

pro_from_da = get_data_for_da(da_pro, headres=head)
air_from_da = get_data_for_da(da_air, headres=head)


ref = "https://www.apple.com/shop/refurbished/mac/13-inch-macbook-air"

pro_from_ref = get_data_for_ref(ref, need_pro_list, 'MacBook Pro')
air_from_ref = get_data_for_ref(ref, need_air_list, 'MacBook Air')





validated_pro = get_need_data([pro_from_ai, pro_13_from_ai,pro_from_da, pro_from_ref,pro_from_tf, pro_13_from_tf,
                     pro_from_gs], need_pro_list)
validated_air = get_need_data([air_from_ai, air_from_da, air_from_ref,air_from_tf,
                     air_from_gs],need_air_list)



def main():
    """Авторизация"""
    sa = gspread.service_account()

    """Подключаемся к документу"""
    sh = sa.open("MacPython")

    """Подключаемся к странице"""
    wks = sh.worksheet('TestData2')
    wks.batch_clear(["A3:K101"])

    """Обновляем записи в указанном диапазоне"""
    coll_nums = len(validated_pro) + 2

    wks.update(f'A3:K{coll_nums}', validated_pro,
               value_input_option='USER_ENTERED')
    coll_nums += 2

    wks.merge_cells(f'B{coll_nums}:C{coll_nums}')
    wks.update(f'B{coll_nums}:C{coll_nums}', 'Apple Insider')

    wks.merge_cells(f'D{coll_nums}:E{coll_nums}')
    wks.update(f'D{coll_nums}:E{coll_nums}', 'Danawa')

    wks.merge_cells(f'F{coll_nums}:G{coll_nums}')
    wks.update(f'F{coll_nums}:G{coll_nums}', 'Apple Refurbished')

    wks.merge_cells(f'H{coll_nums}:I{coll_nums}')
    wks.update(f'H{coll_nums}:I{coll_nums}', 'TacSafon')

    wks.merge_cells(f'J{coll_nums}:K{coll_nums}')
    wks.update(f'J{coll_nums}:K{coll_nums}', 'Google Sheet')


    wks.format(f'A{coll_nums}:K{coll_nums}', {
        "backgroundColor": {
            "red": 50,
            "green": 50,
            "blue": 50
        },
        "textFormat": {
            "fontSize": 12,
            "bold": True}
    })
    wks.update(f'A{coll_nums+1}:K{coll_nums + 1 + len(validated_air)+1}',
               validated_air, value_input_option='USER_ENTERED')

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


if __name__ == '__main__':
    main()
    print('Обновление записей')
    # while True:
    #     # time.sleep(5)
    #     main()
    #     print('Обновление записей')
