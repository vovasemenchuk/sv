# Створення прикладних програм на мові Python
# Лабораторна робота №2
# Семенчук Володимир, №Заліковки
from math import *
print ('[1] Створення прикладних програм на мові Python, Лабораторна №3')
print ('[2] Семенчук Володимир, №Заліковки')
print('[3] Введіть:')
x = float(input('	x = '))
y = float(input('	y = '))
if not (x**3-y**3) or not (1):
	print('Значення змінних виходять за область визначення функції!')
else:
	res = (1/(x**3-y**3))-sqrt(2*x)
	print('Результат обчислення = ', res)