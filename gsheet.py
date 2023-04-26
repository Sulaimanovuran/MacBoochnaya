import gspread
from parsing_ai import get_data_for_ai, headers
from parsing_tf import get_data_for_tf
from format import get_need_models

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


#Создаем списки нужных нам моделей

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




validated_pro = get_need_models(pro14_from_ai, pro14_from_tf, need_pro_list)
validated_air = get_need_models(air_from_ai, air_from_tf, need_air_list)

def main(): 
  """Авторизация"""
  sa = gspread.service_account()

  """Подключаемся к документу"""
  sh = sa.open("MacPython")

  """Подключаемся к странице"""
  wks = sh.worksheet('MacData')
  wks.batch_clear(["A3:C101"])

  """Обновляем записи в указанном диапазоне"""
  coll_nums = len(validated_pro) + 2

  wks.update(f'A3:C{coll_nums}', validated_pro , value_input_option='USER_ENTERED')
  coll_nums += 2

  wks.update(f'A{coll_nums}:C{coll_nums}', [["MacBook Air","AppleInsider","Tacsafon"]])

  wks.format(f'A{coll_nums}:C{coll_nums}', {
      "backgroundColor": {
        "red": 50,
        "green": 50,
        "blue": 50
      },
      "textFormat":{
       "fontSize": 12,
        "bold": True}
  })
  wks.update(f'A{coll_nums+1}:C{coll_nums + 1 + len(validated_air)+1}', validated_air, value_input_option='USER_ENTERED')
  
  """Задаем формат"""
  wks.format(f"A3:A{len(validated_pro)}", {
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
    print('Обновление записей')
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