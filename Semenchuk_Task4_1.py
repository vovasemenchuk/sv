# Створення прикладних програм на мові Python
# Лабораторна робота №4
# Семенчук Володимир, №Заліковки
print ('[1] Створення прикладних програм на мові Python, Лабораторна #4.1')
print ('[2] Семенчук Володимир, №Заліковки')
epsilon = 10E-4
n = 1
a = 1 / 3
suma = a
while a > epsilon:
	n = n + 1 
	chis = 1
	znam = -3
	for x in range(1, n+1):
		chis = chis * x**3
		znam = znam * 3 * x
	a = chis / znam
	suma += a
print('[3] При n = {},  a[n] = {} < {}, і сума всіх елементів буде рівна - {}'.format(n,a,epsilon,suma))
