#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —

#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('HW_5_6_text.txt', 'r', encoding="utf-8") as study_f:

    for line in study_f:
        i = 0
        sum_line = 0
        new_line = line.replace(":", "").replace("(л)", "").replace("(пр)", "").replace("(лаб).", "").replace("—", "").replace("(лаб)", "")
        new_line = new_line.split()
        for i in new_line[1:len(new_line)]:
            sum_line += int(i)

        study_dict = {new_line[0]:sum_line}
        print(study_dict)

#почему то результат как три словаря, надо как-то объединить в один..