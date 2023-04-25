import gspread
from parsing_ai import get_data_for_ai, url as url1, headers
from parsing_tf import get_data_for_tf, url as url2
all_MBs_data_AI = get_data_for_ai(url1, headers)
all_MBs_data_TF = get_data_for_tf(url2)

# Создаем пустой словарь для хранения товаров и цен
products = {}

# Проходим по первому списку и добавляем товары и цены в словарь
for product in all_MBs_data_AI:
    products[product[0]] = [product[1], 'n/a']

# Проходим по второму списку и добавляем цены к существующим товарам или создаем новые
for product in all_MBs_data_TF:
    if product[0] in products:
        products[product[0]].pop()
        products[product[0]].append(product[1])
        # products[product[0]].append('n/a')
    else:
        products[product[0]] = ['n/a',product[1]]

result  = [[k] + [j for j in v] for k, v in products.items()]



def main(): 
  """Авторизация"""
  sa = gspread.service_account()

  """Подключаемся к документу"""
  sh = sa.open("MacPython")

  """Подключаемся к странице"""
  wks = sh.worksheet('MacData')
  wks.batch_clear(["A3:C101"])
#   wks.update('F19:H25', res)
  """Обновляем записи в указанном диапазоне"""
#   wks.update('A3:D101',  result)
  wks.update('A3:C101', result, value_input_option='USER_ENTERED')
  wks.update('E1:I101', all_MBs_data_AI,value_input_option='USER_ENTERED')
  
#   wks.update_acell('E84', '=HYPERLINK("https://prices.appleinsider.com/product/macbook-pro-14-inch-2023/Z17G002K8";"$6049.0")')
  
  """Задаем формат"""
  wks.format("A3:A101", {
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
    main()
    # while True:
    #     # time.sleep(5)
    #     main()
    #     print('Обновление записей')


'''Help on method update in module gspread.worksheet:

update(range_name, values=None, **kwargs) method of gspread.worksheet.Worksheet instance
    Sets values in a cell range of the sheet.
    
    :param str range_name: The A1 notation of the values
        to update.
    :param list values: The data to be written.
    
    :param bool raw: The values will not be parsed by Sheets API and will
        be stored as-is. For example, formulas will be rendered as plain
        strings. Defaults to ``True``. This is a shortcut for
        the ``value_input_option`` parameter.
    
    :param str major_dimension: (optional) The major dimension of the
        values. Either ``ROWS`` or ``COLUMNS``.
    
    :param str value_input_option: (optional) How the input data should be
        interpreted. Possible values are:
    
        ``ValueInputOption.raw``
            The values the user has entered will not be parsed and will be
            stored as-is.
    
        ``ValueInputOption.user_entered``
            The values will be parsed as if the user typed them into the
            UI. Numbers will stay as numbers, but strings may be converted
            to numbers, dates, etc. following the same rules that are
            applied when entering text into a cell via
            the Google Sheets UI.
    
    :type value_input_option: :namedtuple:`~gspread.utils.ValueInputOption`
    
    :param response_value_render_option: (optional) Determines how values should
        be rendered in the output. See `ValueRenderOption`_ in
        the Sheets API.
    
        Possible values are:
    
        ``ValueRenderOption.formatted``
            (default) Values will be calculated and formatted according
            to the cell's formatting. Formatting is based on the
            spreadsheet's locale, not the requesting user's locale.
    ``ValueRenderOption.unformatted``
            Values will be calculated, but not formatted in the reply.
            For example, if A1 is 1.23 and A2 is =A1 and formatted as
            currency, then A2 would return the number 1.23.
    
        ``ValueRenderOption.formula``
            Values will not be calculated. The reply will include
            the formulas. For example, if A1 is 1.23 and A2 is =A1 and
            formatted as currency, then A2 would return "=A1".
    
        .. _ValueRenderOption: https://developers.google.com/sheets/api/reference/rest/v4/ValueRenderOption
    
    :type response_value_render_option: :namedtuple:`~gspread.utils.ValueRenderOption`
    
    :param str response_date_time_render_option: (optional) How dates, times, and
        durations should be represented in the output.
    
        Possible values are:
    
        ``DateTimeOption.serial_number``
            (default) Instructs date, time, datetime, and duration fields
            to be output as doubles in "serial number" format,
            as popularized by Lotus 1-2-3.
    
        ``DateTimeOption.formated_string``
            Instructs date, time, datetime, and duration fields to be output
            as strings in their given number format
            (which depends on the spreadsheet locale).
    
        .. note::
    
            This is ignored if ``value_render_option`` is ``ValueRenderOption.formatted``.
    
        The default ``date_time_render_option`` is ``DateTimeOption.serial_number``.
    :type date_time_render_option: :namedtuple:`~gspread.utils.DateTimeOption`
    
    Examples::
    
        # Sets 'Hello world' in 'A2' cell
        worksheet.update('A2', 'Hello world')
        
        # Updates cells A1, B1, C1 with values 42, 43, 44 respectively
        worksheet.update([42, 43, 44])
    
        # Updates A2 and A3 with values 42 and 43
        # Note that update range can be bigger than values array
        worksheet.update('A2:B4', [[42], [43]])
    
        # Add a formula
        worksheet.update('A5', '=SUM(A1:A4)', raw=False)
    
        # Update 'my_range' named range with values 42 and 43
        worksheet.update('my_range', [[42], [43]])
    
        # Note: named ranges are defined in the scope of
        # a spreadsheet, so even if `my_range` does not belong to
        # this sheet it is still updated'''