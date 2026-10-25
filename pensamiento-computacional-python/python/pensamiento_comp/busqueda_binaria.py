objetivo = int(input('escoge un numero '))
epsilot = 0.01
bajo = 0.0
alto = max(1.0, objetivo )
respuesta = alto + bajo / 2

while abs(respuesta**2 - objetivo) >= epsilot:   #mientras el margen sea mayor a epsilot:
    if respuesta**2 < objetivo:                  #si la mitad de (alto+bajo)^2 < input:    
        bajo = respuesta                         #se actualiza el valor de bajo
    else: 
        alto = respuesta                         #se actualiza alto  

    respuesta = (alto + bajo) / 2

print(f'la raiz cuadrada de {objetivo} es  {respuesta}')
         