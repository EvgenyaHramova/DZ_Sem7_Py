def inp_mod():
    mod = input('Введите режим работы (букву и для импорта данных; букву э для экспорта данных): ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname

def view_import (result):
    print(*result, sep='\n') 

def inp_export():
    name = input('Введите имя: ')
    sec_name = input('Введите отчество: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите телефона: ')
    comment = input('Ведите признак телефона (домашний, рабочий): ')
    return '\n', name,  sec_name, surname, phone, comment


def view_import_no ():
    print(f'Данные не найдены')