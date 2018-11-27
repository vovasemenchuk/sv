# Створення прикладних програм на мові Python
# Лабораторна робота 7
# Семенчук Володимир, 14
print ('Створення прикладних програм на мові Python, Лабораторна 7')
print ('Семенчук Володимир, 14')

tyr = 0
price = 1

def showSpisok (**sp):
    for x in sp:
        print ('{} - тираж: {}, ціна: {}$'.format(x, sp[x][tyr], sp[x][price]) )

def SerPrice (*sp):
    aprice = 0
    k = 0
    average = 0
    for x in A:
        if A[x][tyr] < 10000:
            aprice += A[x][price]
            k += 1
            average = aprice / k
    return average
    

A = {
    'Журнал1': [443,5],
    'Журнал2': [22342,12],
    'Журнал3': [11100,20],
    'Журнал4': [9999,18.5],
    'Журнал5': [17340,28],
    }

showSpisok(**A)
print('Середня вартість журналів,тираж менше 10 000: ',SerPrice(*A))
