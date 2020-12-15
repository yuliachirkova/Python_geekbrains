#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds_input = int(input("Введите время в секундах: "))

if seconds_input >= 3600:
    hours = seconds_input//3600
    minutes = (seconds_input - hours*3600)//60
    seconds = seconds_input - hours*3600 - minutes*60;
elif seconds_input < 3600 and seconds_input >= 60:
    hours = "00"
    minutes = seconds_input//60
    seconds = seconds_input - minutes*60
else:
    hours = "00"
    minutes = "00"
    seconds = seconds_input

time = f"{hours}:{minutes}:{seconds}"
print(time)
