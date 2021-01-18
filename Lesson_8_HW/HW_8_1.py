# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def define_date(cls, date):
        format_date = []

        for i in date.split():
            if i != '-': format_date.append(i)

        return int(format_date[0]), int(format_date[1]), int(format_date[2])

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Дата определена корректно'
                else:
                    return f'Неправильно указан год'
            else:
                return f'Неправильный указан месяц'
        else:
            return f'Неправильный указан день'

    def __str__(self):
        return f'Дата {Data.define_date(self.date)}'


the_date = Data('14 - 1 - 2021')
print(the_date)
print(the_date.validation(31, 13, 2009))
print(the_date.define_date('14 - 02 - 2021'))
print(the_date.validation(14, 1, 2021))