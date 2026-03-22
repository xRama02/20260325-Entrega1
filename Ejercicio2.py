cantidad_segundos = 0
horas = 0
minutos = 0
segundos = 0
cantidad_segundos = float(input('Introduzca la cantidad de segudos: '))
horas = cantidad_segundos//3600
print('se imprimiran las horas:',horas)
if (cantidad_segundos%3600 == 0):
    print(cantidad_segundos,'de segundos se corresponde a: ',horas,'horas')
else:
    minutos=cantidad_segundos%3600//60
    if ((cantidad_segundos%3600)/60 == 0):
        print(cantidad_segundos,'de segundos se corresponde a: ',horas,'horas',' y ',minutos,'minutos')
    else:
        segundos=(cantidad_segundos%3600)%60
        print(cantidad_segundos,'de segundos se corresponde a: ',horas,'horas',' y ',minutos,'minutos y ',segundos,' segundos')
