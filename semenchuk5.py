N = int(input ('Введіть число:'))
proste = N
k = 0
while  k < 5:
	x = 0
	for j in range(1,proste+1):
		if proste % j == 0:
			x += j
	if x-1 == proste:
		k += 1
		print(proste, end = ' ')
	proste += 1