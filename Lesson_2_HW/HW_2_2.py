#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = list(input("Пожалуйста введите X любых значений:"))
print(my_list)
for el in range((len(my_list))//2):
    my_list[el], my_list[el+1] = my_list[el+1], my_list[el]
    el = el + 2
print(my_list)

#очень странно работает в итоге код.. меняет местами элементы,но не все соседние..




