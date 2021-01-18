#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


#количество строк
with open("hw_5_2_text.txt") as hw_5_2_text_obj:
    my_list = hw_5_2_text_obj.readlines()
    print(my_list)
    print(f'количество строк равно: {len(my_list)}')

#количество слов
i = 0
with open("hw_5_2_text.txt") as hw_5_2_text_obj:
    for line in hw_5_2_text_obj:
        words = line.split()
        i = i+1
        print(f'количество слов в строке {i} равно - {len(words)}')




