#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("please insert revenue number: "))
costs = int(input("please insert costs number: "))

if revenue > costs:
    profit = revenue - costs
    result = f"Компания получила прибыль в размере {profit} условных единиц"
    print(result)
    margin = (profit/revenue) * 100
    print("рентабельность составляет - ", margin, "%")
    headcount = int(input("please insert headcount number: "))
    margin_per_capita = (profit/headcount) * 100
    print("прибыль в расчете на одного сотрудника - ", margin_per_capita, "%")
else:
    loss = costs - revenue
    result = f"Компания получила убыток в размере {loss} условных единиц"
    print(result)


