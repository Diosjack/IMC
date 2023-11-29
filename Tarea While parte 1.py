print("-----------------------------")
print("Programa creado por Erick 10-9")
print("-----------------------------")
print("Es un programa de loteria")
print ("Solo tienes 3 intentos buena suerte")
print("-----------------------------")
print()
#a es la variable que ocupa el while
a=1
while a <=3:
    print("Pon cualquier numero para ver si ganas la loteria")
    num = int(input())
    #Lo de las papas es un meme que encontre xD
    if num == 25:
        print("////////////////-----------------------------////////////////")
        print()
        print("Has ganado una bolsa de aire que trae papas imaginarias")
        print()
        print("////////////////-----------------------------////////////////")
        a=5
    else:
        #Algo extra para ver cuanto llevas de intentos
        print("Intenta denuevo mi amigo")
        print("Intento",a,"de 3")
        a=a+1
    if a == 4:
        print("Lo siento perdiste")
    
