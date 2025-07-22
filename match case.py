lista_ventas=[]
suma=0
while True:
    print("MENÚ DE OPCIONES")
    print("1.Ingresar lista de ventas")
    print("2.MOstrar ventas ingresadas")
    print("3.Calcular la venta mas alta y la mas baja")
    print("4.Calcular promedio de ventas")
    print("5.Contar cuantos días superaron los Q.100")
    print ("6.Clasificar cada venta (alta/media(baja):")
    print("7.Salir")
    opcion= input("Ingrese una opcion:")

    match opcion :
        case "1":
            cantidad_datos = int(input("Cuantos datos desea agregar?:"))
            if cantidad_datos < 0:
                print("Dato no valido, no pude ser negativo")
            else:
                while True:
                    for i in range(cantidad_datos):
                        dato=int(input("Ingrese dato que desea agregar:"))
                        if dato < 0:
                            print("CDato no valido, debe ser un entero positivo.")
                        else:
                            lista_ventas.append(dato)
                            suma += dato
                    break
        case "2":
            for mostrar in lista_ventas:
                print(f"VENTAS INGRESADA: {mostrar}")
        case "3":
            print("CALCULO DE VENTAS ALTAS Y BAJAS")
            if lista_ventas:
                maximo_ventas=lista_ventas[0]
                minimo_ventas=lista_ventas[0]
                for venta in lista_ventas:
                    if venta > maximo_ventas:
                        maximo_ventas= venta
                    elif venta < minimo_ventas:
                        minimo_ventas = venta
                print(f"La venta mas alta es:{maximo_ventas}")
                print(f"La venta mas bja es:{minimo_ventas}")


        case "4":
            print("PROMEDIO DE VENTAS")
            promedio= (suma /cantidad_datos)
            print(f"El promedio de ventas es de:{promedio}")

        case "5":
            print("CUANTOS DÍAS SUPERARON LOS 100")

        case "6":
            print("CLASIFICACIÓN DE VENTAS")

        case "7":
            print("Saliendo del programa...")


        case _:
            print("No existe opcion")