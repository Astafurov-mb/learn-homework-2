"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime
nowtime = datetime.datetime.now()
nowdate = datetime.datetime.now().date()
dttm_string = '01/01/20 12:10:03.234567'
def print_days():
    print(nowdate, ' Сейчас\n', nowdate-datetime.timedelta(days=1), 'было вчера\n', nowdate-datetime.timedelta(days=30), 'было 30 дней назад' )
    


def str_2_datetime(date_string):
    print(datetime.datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f"))

if __name__ == "__main__":
    print_days()
    print(str_2_datetime(dttm_string))
