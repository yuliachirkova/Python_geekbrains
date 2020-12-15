#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Please insert the month number from 1 to 12: "))

season_dict = {
   1: "winter",
   2: "winter",
   12: "winter",
    3: "spring",
    4: "spring",
    5: "spring",
    6: "summer",
    7: "summer",
    8: "summer",
    9: "autumn",
    10: "autumn",
    11: "autumn" }

season_list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"]

print(f'For month number {month} the season is {season_dict.get(month)}')
print(f'for month number {month} the season is {season_list[month-1]}')




