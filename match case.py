lista_ventas=[]
suma=0
contador= 0
numero_datos=0
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
                numero_datos += cantidad_datos
                while True:
                    for i in range(cantidad_datos):
                        valor=int(input("Ingrese valor de venta que desea agregar:"))
                        if valor < 0:
                            print("CDato no valido, debe ser un entero positivo.")
                        else:
                            lista_ventas.append(valor)
                            suma += valor
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
            if numero_datos > 0:
                promedio= (suma /numero_datos)
                print(f"El promedio de ventas es de:{promedio}")
            else:
                print("No hay ventas ingresadas para calcular promedio")

        case "5":
            print("CUANTOS DÍAS SUPERARON LOS 100")
            for ventas in lista_ventas:
                if ventas > 1000:
                    contador +=1
            print(f"Hay {contador} día/s que superaron los Q1000")


        case "6":
            print("CLASIFICACIÓN DE VENTAS")
            for ventas_comp in lista_ventas:
                if ventas_comp > 1000:
                    print(f"{ventas_comp} es venta alta")
                elif ventas_comp >=500 and ventas_comp <=1000:
                    print(f"{ventas_comp} es una venta media")
                else:
                    print(f"{ventas_comp} es un venta baja")


        case "7":
            print("Saliendo del programa...")


        case _:
            print("No existe opcion")