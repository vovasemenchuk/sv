def f(*x, **y):
	if max(x) > min(y.values()):
		res = 0
		n = 1
		for val in x:
			res += val**n
			n += 1
		return res
	else:
		m = len(y.values())
		res = list(y.values())[-1]**m
		sp = list(y.values())[-2::-1]
		for val in range(len(sp)):
		 	m -= 1
		 	res -= val**m 
		return res

x = [-2, 1,0,3,4]
y = { str(i):i for i in range(5,8)}

print(x)
print(list(y.values()))
print(f(*x,**y))
