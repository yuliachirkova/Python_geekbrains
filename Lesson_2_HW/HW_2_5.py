#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


my_list = [8, 9, 3, 3, 2, 6]
print(my_list)

#Var 1 (была идея сделать так 1)добавить элемент в конец списка, затем отсортировать)
my_list = [8, 9, 3, 3, 2, 6]
new_el = int(input("please insert your number: "))
new_list = my_list.append(new_el)

#Var 2 (отчаявшись что апенд выдает None повторила решение по схеме другой группы, тоже провал)
new_el = int(input("please insert your number: "))
i = 0
for el in my_list:
    if new_el <= el:
        i = i + 1
new_list = my_list.insert(i, new_el)
print(new_list)

#Тут какая-то фигня почему-то элемент не добавляется
# в список функией append выдает результат None... extend тоже не работает и
# этот вариант из подсказки в видео другой группы почему то Insert тоже возвращает None



