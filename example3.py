per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Money = "))
values = list(per_cent.values())
New_values = [(i*money)//100 for i in values]
print('Deposit = ',New_values)
print()
Max = max(New_values)
print(Max)
