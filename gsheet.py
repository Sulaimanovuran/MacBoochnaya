import gspread
from parsing_ai import get_data_for_ai, url as url1, headers
from parsing_tf import get_data_for_tf, url as url2
all_MBs_data_AI = get_data_for_ai(url1, headers)
all_MBs_data_TF = get_data_for_tf(url2)

def main():
  """Авторизация"""
  sa = gspread.service_account()

  """Подключаемся к документу"""
  sh = sa.open("MacPython")

  """Подключаемся к странице"""
  wks = sh.worksheet('MacData')

  """Обновляем записи в указанном диапазоне"""
  wks.update('A3:C101',  all_MBs_data_AI)
  wks.update('F3:G17', all_MBs_data_TF)
  print(all_MBs_data_AI[0:21])
  """Задаем формат"""
  wks.format("A3:C101", {
      "backgroundColor": {
        "red": 1,
        "green": 1,
        "blue": 1
      },
      "horizontalAlignment": "LEFT",
      "verticalAlignment" : "TOP",
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

  wks.format("F3:G17", {
      "backgroundColor": {
        "red": 1,
        "green": 1,
        "blue": 1
      },
      "horizontalAlignment": "LEFT",
      "verticalAlignment" : "TOP",
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

import time

if __name__ == '__main__':
    while True:
        time.sleep(5)
        main()
        print('Обновление записей')