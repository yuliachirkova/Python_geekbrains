#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(name = input("name: "), surname = input("surname: "), year_of_birth = input("year of birth: "), town = input("town: "), email = input("email: "), phone_number = input("phone number: ")):
    return f'User data is: {name} {surname}, {year_of_birth} г.р., {town}, email: {email}'

print(my_func())
