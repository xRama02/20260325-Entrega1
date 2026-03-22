lista_palabras = []
palabra = 'x'
while palabra != 'z':
    palabra = input('Inserte una palabra: ')
    if (len(palabra)>3):
        palabra+=' '
        lista_palabras.append(palabra)
for elemento in lista_palabras:
    print(elemento)
