#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


#после урока модифицировала свое решение потому что поняла, что не поняла задание
# кстати, код с разбора на вебинаре не работает, в последней строке не хватает 4 пробела у Вас :).
with open("text_f.txt", "w", encoding='utf-8') as text_f:
    str_list = []
    while True:
        user_input = input()
        if not user_input: #вот эта история в коде с урока не понятно как работает, но без нее почему-то не работает код :)
            break
        str_list.append(user_input)
        text_f.writelines(str_list) #непонятно почему в итоге записывает в файл одной строкой а не построчно
    #text_f.read() - непонятно почему, но такой вывод на чтение в этом коде не работает.
print(str_list)






