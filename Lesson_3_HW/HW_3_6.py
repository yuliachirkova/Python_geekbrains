#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

#Первая часть
def int_func():
    word = input('введите слово из маленьких латинских букв: ')
    word_new = input('введите слова разделенные пробелом: ')
    return word.capitalize(), word_new.title()
print(int_func())



