import time
import gspread
from parsing_ai import get_data_for_ai, headers
from parsing_tf import get_data_for_tf
from parsing_gs import pro_from_gs, air_from_gs
from format import get_need_models, func

ai_pro14 = 'https://prices.appleinsider.com/macbook-pro-14-inch-2023'
ai_air = 'https://prices.appleinsider.com/macbook-air-2022'

tf_pro14 = "https://tacsafon.ru/magazin/folder/apple-macbook-pro-14"
tf_air = 'https://tacsafon.ru/magazin/folder/apple-macbook-air'

# ai_urls = [ai_pro14, ai_air]
# tf_urls = [tf_pro14, tf_air]

pro14_from_ai = get_data_for_ai(ai_pro14, headers)
air_from_ai = get_data_for_ai(ai_air, headers)


pro14_from_tf = get_data_for_tf(tf_pro14)
air_from_tf = get_data_for_tf(tf_air)


# Создаем списки нужных нам моделей

need_pro_list = [
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
]


validated_pro = func(pro14_from_ai, pro14_from_tf,
                     list3=pro_from_gs, item_names=need_pro_list)
validated_air = func(air_from_ai, air_from_tf,
                     list3=air_from_gs, item_names=need_air_list)


def main():
    """Авторизация"""
    sa = gspread.service_account()

    """Подключаемся к документу"""
    sh = sa.open("MacPython")

    """Подключаемся к странице"""
    wks = sh.worksheet('MacData')
    wks.batch_clear(["A3:D101"])

    """Обновляем записи в указанном диапазоне"""
    coll_nums = len(validated_pro) + 2

    wks.update(f'A3:D{coll_nums}', validated_pro,
               value_input_option='USER_ENTERED')
    coll_nums += 2

    wks.update(f'A{coll_nums}:D{coll_nums}', [
               ["MacBook Air", "AppleInsider", "Tacsafon", "GSheet"]])

    wks.format(f'A{coll_nums}:D{coll_nums}', {
        "backgroundColor": {
            "red": 50,
            "green": 50,
            "blue": 50
        },
        "textFormat": {
            "fontSize": 12,
            "bold": True}
    })
    wks.update(f'A{coll_nums+1}:D{coll_nums + 1 + len(validated_air)+1}',
               validated_air, value_input_option='USER_ENTERED')

    """Задаем формат"""
    wks.format(f"A3:A{len(validated_pro)}", {
        "backgroundColor": {
            "red": 1,
            "green": 1,
            "blue": 1
        },
        "horizontalAlignment": "LEFT",
        "verticalAlignment": "TOP",
        "wrapStrategy": "WRAP",
        "textFormat": {
            "foregroundColor": {
                "red": 0,
                "green": 0,
                "blue": 0
            },
            "fontSize": 10,
            "bold": False
        }
    })


if __name__ == '__main__':
    main()
    print('Обновление записей')
    # while True:
    #     # time.sleep(5)
    #     main()
    #     print('Обновление записей')
