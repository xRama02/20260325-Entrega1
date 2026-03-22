N = int(input('Inserte un numero: '))

multiplos_cinco = []
no_multiplos_cinco = []

for i in range (N):
    if i%5==0:
        print('Se agregara el numero:',i,' a la lista: multiplos_cinco')
        multiplos_cinco.append(i)
        continue    
    else:
        print('Se agregara el numero:',i,' a la lista: no_multiplos_cinco')                        
        no_multiplos_cinco.append(i)

print('Se imprimira la lista de multiplos de 5: ')
for elemento in multiplos_cinco:
    print(elemento)

print('Se imprimira la lista de no multiplos de 5: ')
for elemento in no_multiplos_cinco:
    print(elemento)

print('Finaliza el proceso')