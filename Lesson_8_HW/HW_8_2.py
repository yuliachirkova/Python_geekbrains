#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class DivisionException:

    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    @staticmethod
    def zero_division(dividend, divisor):
        try:
            return dividend / divisor
        except:
            return f"На ноль делить нельзя"


my_division = DivisionException(0, 0)
print(my_division)
print(my_division.zero_division(500, 0))
print(my_division.zero_division(400, 0.5))