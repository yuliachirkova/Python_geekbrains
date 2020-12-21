#3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(x,y,z):
    arg_list = [x,y,z]
    max_number = max(arg_list)
    arg_list.remove(max_number)
    return max_number + max(arg_list)

print(my_func(10,-5,7))
