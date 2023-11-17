venta = dict() # Diccionario principal
codigo = 0 # Claves autoincrementables

while True: # Ciclo para hacer menús
    print("1.- Añadir una nueva venta \n2.- Consultar una venta \n3.- Salir")
    opcion = int(input("Elige la opcion deseada: "))
    print()
    if opcion == 1:
        print(f"Ticket {codigo}")
        print()
        almacen = list() # Lista de los elementos de cada producto (Un producto es una lista)
        # Cuando es una venta individual, todo se mete a almacen
        articulo = list() # Lista de productos (Lista de productos)
        nombre = input("Producto: ")
        precio = float(input("Precio unitario: ")) # Float al momento de multiplicar o dividir pueden quedar decimales
        cantidad = int(input("Cantidad: "))
        total = precio * cantidad # Calculo del monto total
        almacen.append(nombre) # Lista de elementos de cada producto (Agrego el nombre)
        almacen.append(cantidad) # Lista de elementos de cada producto (Agrego la cantidad)
        almacen.append(precio) # Lista de elementos de cada producto (Agrego el precio)
        almacen.append(total) # Lista de elementos de cada producto (Agrego el total)
        articulo.append(almacen) # La lista resultante se mete a la lista principal
        print(f"El monto total es: ${total}") # Imprime el total
        print()
        print("El articulo se añadio exitosamente")
        pregunta = input("Presiona A para agregar otro articulo, o cualquier otra tecla para continuar: ")
        # Pregunta si quieres agregar otro articulo a la misma venta
        while pregunta == "A" or pregunta == "a": # Mientras pregunta == A o a vas a hacer esto
            print()
            lista = list() # Cuando es una venta colectiva, todo se mete a lista
            nombre = input("Producto: ")
            precio = float(input("Precio unitario: "))
            cantidad = int(input("Cantidad: "))
            total = precio * cantidad
            print(f"El monto total es: ${total}")
            print()
            print("El articulo se añadio exitosamente")
            pregunta = input("Presiona A para agregar otro articulo, o cualquier otra tecla para continuar: ")
            # Vuelvo a preguntar si quieres agregar un nuevo articulo
            print()
            # Asignacion de elementos de un producto
            lista.append(nombre)
            lista.append(cantidad)
            lista.append(precio)
            lista.append(total)
            # Los articulos resultantes se meten a la lista principal
            articulo.append(lista)
        venta[codigo] = articulo # Se mete la listas de listas al diccionario
        codigo += 1 # Se le agrega uno al contador para incrementar la llave del diccionario
        print()
    if opcion == 2:
        llave = int(input("Introduce la clave del ticket de venta a consultar: "))
        print()
        for elemento in venta.keys(): # Recorrer el diccionario por llaves
            if elemento == llave: # Igualar la llave del diccionario a la llave introducida
                print(f"Ticket {llave}") # Imprimir codigo de ticket
                print("-" * 25)
                for i in venta[llave]: #Recorrer el contenido de cada una de las claves
                    # Formato de ticket
                    print(f"Producto: {i[0]} \nCantidad: {i[1]} piezas \nPrecio unitario: ${i[2]} \nMonto total: ${i[2]}")
                    print("-" * 25)
                    print()
        else:
             print("No se encontro la venta con el codigo ingresado")
    if opcion == 3:
        print("EJECUCION FINALIZADA")
        break # Rompe el ciclo principal