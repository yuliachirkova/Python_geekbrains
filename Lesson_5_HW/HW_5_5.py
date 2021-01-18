#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('hw_5_5_text.txt', "w", encoding="utf-8") as numbers_file:

    sum_numbers = 0

    numbers = input('please insert some numbers with split \n: ')
    numbers_file.writelines(numbers)
    numbers_list = numbers.split()
    for i in numbers_list:
        sum_numbers += int(i)
    print(sum_numbers)
