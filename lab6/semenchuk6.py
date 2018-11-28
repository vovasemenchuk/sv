sp =  [int(x) for x in input('Числа через пробіл: ').split()]
for x in range(sp.count(0)):
	sp.remove(0)
	sp.append(0)
print(sp)
