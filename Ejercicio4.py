N = int(input('Inserte un numero: '))
print('El número insertado es: ',N,' se mostrara su tabla de multiplicar del 1 al 10')

for i in range (N):
    if i%5==0:
        print('Se salteara el numero')
        continue                             # Salta el print de abajo y vuelve al inicio del for
    print(i)
