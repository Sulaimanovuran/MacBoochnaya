import gspread
from format import format_description_pro, format_description_air
from CHGPT import format_description_air as fda
import requests
import re

currency = round(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['USD'].get('Value'),4)


"""Подключаемся к таблице и собираем данные"""
sa = gspread.service_account()
sh2 = sa.open_by_url("https://docs.google.com/spreadsheets/d/1cZ4-asy3-YgId4S0Ijd8NQqK8EiTrXDm39AgdcBEUbk/edit#gid=0")

wks2 = sh2.sheet1
all_MBs_data_GS_pro, all_MBs_data_GS_air = wks2.batch_get(["A2:B7", "A17:B18"])

"""Форматируем описание"""

# pro_from_gs = [[format_description_pro(mac[0], 1), mac[1]] for mac in all_MBs_data_GS_pro]
# air_from_gs = [[format_description_air(mac[0], 1), mac[1]] for mac in all_MBs_data_GS_air]


def format_for_dict(mac_array):
    all_MBs_data_GS = {}
    for mac in mac_array:
        if 'Air' in mac[0]:
            description = fda(mac[0], 1)
        else:
            pattern = r'(\d+)\"'
            match = re.search(pattern, mac[0])
            if match:
                numbers = match.group(1)
                desc_dict = format_description_pro(mac[0], 1)
                if numbers == '13':
                    if desc_dict['chip'] == 'M1':
                        description = f'MacBook Pro {numbers} {desc_dict["chip"]} (8-CPU 8-GPU) {desc_dict["memory"]} {desc_dict["color"]}'
                    elif desc_dict['chip'] == 'M2':
                        description = f'MacBook Pro {numbers} {desc_dict["chip"]} (8-CPU 10-GPU) {desc_dict["memory"]} {desc_dict["color"]}'
                elif numbers == '16':
                    if desc_dict['chip'] == 'M1':
                        description = f'MacBook Pro {numbers} {desc_dict["chip"]} {desc_dict["chip_version"]} {desc_dict["cgpu"]} {desc_dict["memory"]} {desc_dict["color"]}'
                    elif desc_dict['chip'] == 'M2':
                        description = f'MacBook Pro {numbers} {desc_dict["chip"]} {desc_dict["chip_version"]} {desc_dict["cgpu"]} {desc_dict["memory"]} {desc_dict["color"]}'
                else:
                    description = f'MacBook Pro {numbers} {desc_dict["chip"]} {desc_dict["chip_version"]} {desc_dict["cgpu"]} {desc_dict["memory"]} {desc_dict["color"]}'
        price = re.sub(r"[^\w\s\.\\xa0]", "", mac[1]).replace('\xa0', '')
        price_rub = round((int(price) * currency )* 1.045, 2)
        all_MBs_data_GS[description] = [price, price_rub]

    return all_MBs_data_GS

pro_from_gs = format_for_dict(all_MBs_data_GS_pro)
air_from_gs = format_for_dict(all_MBs_data_GS_air)




# print(pro_from_gs)
#Pro 14" M2 Pro 10-CPU 16-GPU 512GB Silver