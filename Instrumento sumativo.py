for i in range(3):
    #Bienvenida
    print("........................................")
    print("Bienvenido al Club de viajes Erick")
    print("........................................")
    print ("Me podrias decir tu nombre para empezar")
    nombre = input()
    print("Bienvenido",nombre,"Podrias decirme tu edad")
    edad = int(input())
    #ERROR de edad
    if(edad < 18):
        print ("///////////////////ERROR////////////////////")
        print("Lo siento no tienes la edad suficiente")
        print("Para usar esta herramienta")
        print ("///////////////////ERROR////////////////////")
    #Destino y Horas
    else:
        #Destino
        print (nombre,"Podrias decirme cual es tu destino?")
        destino =input()
        #Horas
        print (nombre,"Cuantas horas vas a viajar")
        horas = int(input())
        #Cantidad de tickets
        print(nombre,"cuantos tickets ocupas?")
        print("(Cantidad de personas que viajan)")
        ticket = int(input())
        #Seleccion de transporte
        print("Ahora puedes eligir el modo de viaje")
        print ("por ahora contamos con 2 tipos de transporte")
        print("-------------------------------------")
        print ("1. Bus, costo por hora ₡3000 + iva") 
        print("2. Tren, costo por hora ₡10000 + iva")
        print("-------------------------------------")
        #Total pagar bus
        pagoticketb = 3000 * ticket
        subtotalb =  pagoticketb * horas
        ivab = subtotalb * 0.13
        pagototal1 = subtotalb + ivab
        #Total pagar tren 
        pagotickett = 10000 * ticket
        subtotalt =  pagotickett * horas
        ivat =  subtotalt * 0.13
        pagototal2 = subtotalt + ivat
        #Selecion de transporte
        transporte = int(input())
        if(transporte == 1):
            print("-----------------------------------")
            print("Eligiste el bus para viajar")
            print("-----------------------------------")
            print("Usuario:",nombre)
            print("Destino:",destino)
            print("Tickets totales:",ticket)
            print("Pago tickets: ₡",pagoticketb)
            print("Pago por hora: ₡ 3000")
            print("Horas de viaje:",horas)
            print("IVA: ₡",ivab)
            print ("Subtotal: ₡",subtotalb)
            print("Total a pagar: ₡",pagototal1)
        elif (transporte == 2):
            print("-----------------------------------")
            print("Eligiste el tren para viajar")
            print("-----------------------------------")
            print("Usuario:",nombre)
            print("Destino:",destino)
            print("Tickets totales:",ticket)
            print("Pago tickets: ₡",pagotickett)
            print("Pago por hora: ₡ 10000")
            print("Horas de viaje:",horas)
            print("IVA: ₡",ivat)
            print ("Subtotal: ₡",subtotalt)
            print("Total a pagar: ₡",pagototal2)
        else: 
            print("Lo siento el numero que elijiste no existe entre los transportes")
