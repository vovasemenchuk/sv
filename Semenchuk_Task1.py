cours_name = 'Створення прикладних програм на мові Python'
lab_num = 1
print ('[1] ' + cours_name, lab_num, sep = ', ')

name = 'Volodymyr'
surname = 'Semenchuk'
var_num = 'NUM-14(2)'
print ('[2] ' + name + ' ' + surname, var_num, sep = ', ')

teacher = 'Ivan Yaroslavovich'
result = '[3] '
for i in range(45):
	if i == 0:
		result += teacher
	else:
		result += ', ' + teacher
print (result)

x = ((123-23.1)*(2*2*2+2.2)/(127.24-21.1))-3.2
print('[4] x = ', x)
