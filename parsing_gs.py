import gspread
from format import format_description_pro, format_description_air

"""Подключаемся к таблице и собираем данные"""
sa = gspread.service_account()
sh2 = sa.open_by_url("https://docs.google.com/spreadsheets/d/1cZ4-asy3-YgId4S0Ijd8NQqK8EiTrXDm39AgdcBEUbk/edit#gid=0")

wks2 = sh2.sheet1
all_MBs_data_GS_pro, all_MBs_data_GS_air = wks2.batch_get(["A2:B7", "A17:B18"])

"""Форматируем описание"""

pro_from_gs = [[format_description_pro(mac[0], 1), mac[1]] for mac in all_MBs_data_GS_pro]
air_from_gs = [[format_description_air(mac[0], 1), mac[1]] for mac in all_MBs_data_GS_air]


