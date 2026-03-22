total = 0

print('Se iniciara la caja registradora: ')

while True:
    precio = float(input('Inserte un precio: '))
    if (precio<0):
        print('el numero no puede ser negativo')
        continue
    if(precio==0):
        print('Se ingreso el 0, por lo que se cerrara la caja')
        break
    total+=precio

print('El total acumulado es: ',total)