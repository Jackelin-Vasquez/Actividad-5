lista_ventas=[]
while True:
    print("MENÚ DE OPCIONES")
    print("1.Ingresar lista de ventas")
    print("2.MOstrar ventas ingresadas")
    print("3.Calcular la venta mas alta y la mas baja")
    print("4.Calcular promedio de ventas")
    print("5.Contar cuantos días superaron los Q.100")
    print("6.Buscar si una venta especifica existe en una lista")
    print ("7.Clasificar cada venta (alta/media(baja):")
    print("8.Salir")
    opcion= input("Ingrese una opcion:")

    match opcion :
        case "1":
            cantidad_datos = int(input("Cuantos datos desea agregar?:"))
            if cantidad_datos < 0:
                print("Dato no valido, no pude ser negativo")
            else:
                for i in range(cantidad_datos):
                    dato=int(input("Ingrese dato que desea agregar:"))
                    if dato < 0:
                        print("CDato no valido")
                    else:
                        lista_ventas.append(dato)
        case "2":
            for mostrar in lista_ventas:
                print(f"VENTAS INGRESADA: {mostrar}")
        case "3":
            print("CALCULO DE VENTAS ALTAS Y BAJAS")


        case "4":
            print("")
        case "5":
            print("CUANTOS DÍAS SUPERARON LOS 100")
        case "6":
            venta= int(input("Ingrese venta a buscar:"))
            if venta in lista_ventas:
                print(venta)
            else:
                print("Venta no encontrada...")
        case "7":
            print("CLASIFICACIÓN VENTAS:")


        case "8":
            print("Saliendo del sistema...")

        case _:
            print("No existe opcion")