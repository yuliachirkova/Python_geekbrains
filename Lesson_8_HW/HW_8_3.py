#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
#Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class Error_in_list:
    def __init__(self, *args):
        self.my_list = []

    @property
    def my_input(self):

        global value

        while True:
            try:
                value = int(input('Insert your value and push Enter - '))
                self.my_list.append(value)
                print(f'Current list is {self.my_list} \n ')
            except:
                if value == "stop": #не понятно, но почему-то этот кусок кода не работает. Ввожу stop но ничего не происходит, сообщение о завершении списка не выходит.
                    return f'список закончен'
                else:
                    print(f"Not a number, please try again")


my_value = Error_in_list(1)
print(my_value.my_input)