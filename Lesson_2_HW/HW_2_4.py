#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

some_string = input("Please insert a few words using letter space: ")
print(some_string)
for ind, el in enumerate(some_string.split(" "), 1):
    print(ind,el[:10])
