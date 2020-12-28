#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("hw_5_3_text.txt", 'r', encoding='utf-8') as hw_5_3_text_obj:
    new_list = []
    total_payroll = 0
    headcount = 0
    for line in hw_5_3_text_obj:
        salary_data = line.split()
        total_payroll += int(salary_data[1])
        headcount += 1
        if int(salary_data[1]) > 20000:
            new_list.append(salary_data[0])
    print(f"the following employees have salary above 20k - {new_list}")
    print(f'average salary = {total_payroll / headcount}')

