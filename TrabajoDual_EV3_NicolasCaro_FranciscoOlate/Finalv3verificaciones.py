import os
import pyfiglet
from datetime import datetime

fecha_actual = datetime.now()
fecha_formateada = fecha_actual.strftime("%d-%m-%Y")

productos_txt = 'productos.txt'
ventas_txt = 'ventas.txt'

productos=[]
ventas=[]

def buscar_producto(id):
    for producto in productos:
        if producto[0] == id:
            return producto
    return -1

def leer_datos_productos_txt(productos_txt):
    lista_productos = []
    with open(productos_txt, 'r') as file:
        for linea in file:
            datos = linea.strip().split(',')
            lista_productos.append(datos)
    return lista_productos

def listar_productos():
    for producto in productos:
        print(", ".join(map(str, producto)))

def imprimir_productos(lista_productos):
    for producto in lista_productos:
        print(", ".join(map(str,producto)))

def agregar_producto(id, tipo, marca, nombre, conexion, stock, precio):
    productos.append([id, tipo, marca, nombre, conexion, stock, precio])

def modificar(id, nuevo_tipo, nueva_marca, nuevo_nombre, nueva_conexion, nuevo_stock, nuevo_precio):
    for producto in productos:
        if producto[0] == id:
            producto[1] = nuevo_tipo
            producto[2] = nueva_marca
            producto[3] = nuevo_nombre
            producto[4] = nueva_conexion
            producto[5] = nuevo_stock
            producto[6] = nuevo_precio
            return True
    return False

def eliminar(id):
    for producto in productos:
        if producto[0] == id:
            productos.remove(producto)
            return True
    return False

def guardar_venta(folio, fecha, id_producto, cantidad, total):
    ventas.append([folio, fecha, id_producto, cantidad, total])

def leer_datos_ventas_txt(ventas_txt):
    lista_ventas = []
    with open(ventas_txt, 'r') as file:
        for linea in file:
            datos = linea.strip().split(',')
            lista_ventas.append(datos)
    return lista_ventas

def imprimir_ventas(lista_ventas):
    for venta in lista_ventas:
        print(", ".join(map(str,venta)))

def restar_stock(id_a_modificar, nuevo_stock):
    for producto in productos:
        if producto[0] == id_a_modificar:
            producto[5] = nuevo_stock
            return True
    return False

def respaldar_datos():
    with open(productos_txt, 'w') as file:
        for producto in productos:
            file.write(','.join(map(str, producto)) + '\n')

    with open(ventas_txt, 'w') as file:
        for venta in ventas:
            file.write(','.join(map(str, venta)) + '\n')

def validar_fecha(fecha):
    if len(fecha) != 10:
        return -1
    try:
        datetime.strptime(fecha, "%d-%m-%Y")
    except ValueError:
        return -1
    dia, mes, anio = map(int, fecha.split('-'))
    
    if dia<1 or dia>31:
        return -1
    
    if mes<1 or mes<12:
        return -1
    
    if anio<2000:
        return -1

    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            if dia<1 or dia>29:
                return -1
        else:
            if dia<1 or dia>28:
                return -1   
    return 1

def validar_largo_id(id):
    if len(id) != 5:
        return -1
    return 1

def validar_id_unico(id, lista_productos):
    for producto in lista_productos:
        if producto[0] == id:
            return -1
    return 1

def validar_campo_no_vacio(texto):
    if not texto.strip():  
        return -1
    return 1

def validar_stock(stock):
    try:
        stock = int(stock)
        if stock < 0:
            return -1
    except ValueError:
        return -1
    return 1

def validar_precio(precio):
    try:
        precio = int(precio)
        if precio < 0:
            return -1
    except:
        return -1
    return 1

op = 0

os.system("cls")
from pyfiglet import Figlet
f = pyfiglet.figlet_format("CompuPC Factory", font="epic", justify="left", width=130)
print(f)
print("Intregantes: Nicolas Caro, Francisco Olate")
os.system("pause")

while op <= 4:
    os.system("cls")
    print("""       Menu de componentes de PC
                                fecha:{}
                                version:011b
          1.- Comprar productos
          2.- Reportes de ventas
          3.- Mantenedores
          4.- Administracion
          5.- Salir

          """.format(fecha_formateada))

    op = int(input("Ingrese una opcion entre 1 y 5: "))

    if op == 5:
        print("Saliendo del Menú...")
        os.system("pause")
        os.system("cls")
        break
    elif op < 1 or op > 5:
        print("Error, debe ingresar una opción válida")
        op = 0
        os.system("pause")

    match op:
        case 1:
            os.system("cls")
            op = 0

            while True:
                os.system("cls")
                print("Comprar productos")
                print("\n")
                id = input("Ingrese id a buscar: ")
                lista = buscar_producto(id)
                if len(id)==5:
                    if productos and ventas != -1:
                        if lista != -1:
                            print("Producto encontrado")
                            print(lista)
                            cantidad = int(input("Ingrese cantidad: "))
                            if cantidad <= int(lista[5]) and cantidad>0:
                                total = cantidad * int(lista[6])
                                print("Total a pagar: ", total)
                                confirmar = input("¿Confirmar la compra? si/no: ")
                                if confirmar.lower() == "si":
                                    folio += 1
                                    guardar_venta(folio, fecha_formateada, lista[0], cantidad, total)
                                    resta=int(lista[5])-cantidad
                                    nuevo_stock=resta
                                    dato_final=restar_stock(id,nuevo_stock)
                                    print("Venta confirmada")
                                    print(lista[0]," ",lista[1]," ",lista[2]," ",cantidad," ",total)
                                    os.system("pause")
                                    break
                                elif confirmar.lower()== "no":
                                    print("No se confirmó la venta")
                                    os.system("pause")
                                    break
                                else:
                                    print("Error, escriba una respuesta válida")
                                    os.system("pause")                                   
                            elif cantidad>int(lista[5]):
                                print("Error, no hay suficiente stock")
                                os.system("pause")
                            elif cantidad<=0:
                                print("Error, ingrese una cantidad mayor a 0")
                                os.system("pause")
                        else:
                            print("Error, id no existe en la base de datos")
                            os.system("pause")
                else:
                    print("Error, el id debe tener 5 caracteres")
                    os.system("pause")

        case 2:
            opr = 0
            while opr <= 4:
                os.system("cls")
                print("""
                                REPORTES
                      ---------------------------------
                      1.- General de ventas
                      2.- Ventas por fecha especifica
                      3.- Ventas por rango de fecha
                      4.- Salir al menu principal

                      """)
                opr = int(input("Ingrese una opción entre 1 y 4: "))

                if opr == 4:
                    print("Saliendo del Menú...")
                    os.system("pause")
                    os.system("cls")
                    break
                elif opr < 1 or opr > 4:
                    print("Error, debe ingresar una opción válida")
                    opr = 0
                    os.system("pause")

                match opr:
                    case 1:
                        os.system("cls")
                        print("General de Ventas")
                        print("\n")
                        if len(ventas)>0:
                            imprimir_ventas(ventas)
                            os.system("pause")
                        else:
                            print("No hay datos que mostrar")
                            os.system("pause")

                    case 2:
                        os.system("cls")
                        print("Buscar venta por fecha")
                        print("\n")
                        fecha_a_buscar = input("Ingrese la fecha a buscar en el formato: Dia-Mes-Año: ")

                        if validar_fecha(fecha_a_buscar) == -1:
                            print("Fecha ingresada no válida.")
                            os.system("pause")

                        elif validar_fecha(fecha_a_buscar) == 1:
                            ventas_encontradas = []

                            for venta in ventas:
                                if venta[1] == fecha_a_buscar:
                                    ventas_encontradas.append(venta)

                            if ventas_encontradas:
                                imprimir_ventas(ventas_encontradas)
                            else:
                                print("No se encontraron ventas en la fecha solicitada.")
                            os.system("pause")

                    case 3:
                        os.system("cls")
                        print("Buscar ventas por rango de fechas\n")
                        fecha_inicio = input("Ingrese fecha de inicio (dia-mes-año): ")
                        if validar_fecha(fecha_inicio) == -1:
                            print("Fecha de inicio no válida.")
                            os.system("pause")
                        elif validar_fecha(fecha_inicio) == 1:
                            fecha_fin = input("Ingrese fecha de fin (dia-mes-año): ")                            
                            
                            if validar_fecha(fecha_fin) == -1:
                                print("Fecha de fin no válida.")
                                os.system("pause")
                            elif validar_fecha(fecha_fin) == 1:
                                ventas_encontradas = []
                                fecha_inicio_dt = datetime.strptime(fecha_inicio, "%d-%m-%Y")
                                fecha_fin_dt = datetime.strptime(fecha_fin, "%d-%m-%Y")

                                ventas_rango = []

                                for venta in ventas:
                                    fecha_venta_dt = datetime.strptime(venta[1], "%d-%m-%Y")
                                    if fecha_inicio_dt <= fecha_venta_dt <= fecha_fin_dt:
                                        ventas_rango.append(venta)

                                if ventas_rango:
                                    imprimir_ventas(ventas_rango)
                                else:
                                    print("No se encontraron ventas en el rango de fechas indicado")
                                os.system("pause")

        case 3:
            opcion = 0
            while opcion <= 6:
                os.system("cls")                               
                print("""
                        Mantenedor de productos

                      1.- Agregar
                      2.- Buscar
                      3.- Eliminar
                      4.- Modificar
                      5.- Listar
                      6.- Salir al menu principal

                      """)
                opcion = int(input("Ingrese una opcion entre 1 y 6: "))
                match opcion:
                    case 1:
                        os.system("cls")
                        print("Agregar")
                        print("\n")
                        while True:
                            os.system("cls")
                            id = input("Ingrese el id: ")
                            if validar_largo_id(id)==-1:
                                print("Error, el id debe tener 5 caracteres")
                                os.system("pause")
                                continue
                            if validar_id_unico(id, productos)==-1:
                                print("Error, el id ingresado ya existe")
                                os.system("pause")
                                continue
                            break
                        while True:
                            os.system("cls")
                            tipo = input("Ingrese el tipo de componente: ")
                            if validar_campo_no_vacio(tipo)==-1:
                                print("Error, el campo no puede estar vacío.")
                                os.system("pause")
                                continue
                            break
                        while True:
                            os.system("cls")
                            marca = input("Ingrese la marca del producto: ")
                            if validar_campo_no_vacio(marca)==-1:
                                print("Error, el campo no puede estar vacío")
                                os.system("pause")
                                continue
                            break
                        while True:   
                            os.system("cls")
                            nombre = input("Ingrese el nombre del producto: ")
                            if validar_campo_no_vacio(nombre)==-1:
                                print("Error, el campo no puede estar vacío.")
                                os.system("pause")
                                continue
                            break
                        while True:
                            os.system("cls")
                            conexion = input("Ingrese el tipo de conexión: ")
                            if validar_campo_no_vacio(conexion)==-1:
                                print("Error, el campo no puede estar vacío.")
                                os.system("pause")
                                continue
                            break
                        while True:   
                            os.system("cls")
                            stock = input("Ingrese el stock: ")
                            if validar_stock(stock)==-1:
                                print("Error, el stock debe ser mayor o igual a 0")
                                os.system("pause")
                                continue
                            break
                        while True:
                            os.system("cls")
                            try:
                                precio = int(input("Ingrese el precio en números: "))
                                if validar_precio(precio)==-1:
                                    print("Error, el precio debe ser mayor o igual a 0")
                                    os.system("pause")
                                    continue
                            except:
                                print("Error, el campo no puede estar vacío.")
                                os.system("pause")
                                continue
                            break

                        lista=agregar_producto(id, tipo, marca, nombre, conexion, stock, precio)
                        os.system("cls")
                        print("\n")
                        print("Componente agregado: ", marca, nombre)
                        os.system("pause")

                    case 2:
                        os.system("cls")
                        print("Ingrese la id: ")
                        print("\n")
                        while True:
                            os.system("cls")
                            id = input("Ingrese id a buscar: ")
                            if validar_largo_id(id)==-1:
                                    print("Error, el id debe tener 5 caracteres")
                                    os.system("pause")
                                    continue
                            break
                        lista = buscar_producto(id)
                        if lista != -1:
                            print(lista)
                        else:
                            print("Error, id no existe en la base de datos")
                        os.system("pause")

                    case 3:
                        os.system("cls")
                        print("Eliminar producto")
                        print("\n")
                        while True:
                            id = input("Ingrese id del producto a eliminar: ")
                            if validar_largo_id(id)==-1:
                                    print("Error, el id debe tener 5 caracteres")
                                    os.system("pause")
                                    continue
                            break
                        lista = eliminar(id)

                        if lista != -1:
                            print("Producto eliminado")
                        else:
                            print("Error, id no existe en la base de datos")

                        os.system("pause")

                    case 4:
                        os.system("cls")
                        print("Modificar datos producto")
                        print("\n")
                        while True:
                            os.system("cls")
                            id = input("Ingrese id a buscar: ")
                            if validar_largo_id(id)==-1:
                                    print("Error, el id debe tener 5 caracteres")
                                    os.system("pause")
                                    continue
                            break
                        lista = buscar_producto(id)
                        
                        if lista != -1:
                            print("Producto encontrado")
                            print(lista[0]," ",lista[1]," ",lista[2]," ",lista[3]," ",lista[4]," ",lista[5]," ",lista[6])
                            os.system("pause")
                            while True:
                                os.system("cls")
                                tipo = input("Ingrese nuevo tipo: ")
                                if validar_campo_no_vacio(tipo)==-1:
                                    print("Error, el campo no puede estar vacío.")
                                    os.system("pause")
                                    continue
                                break
                            while True:
                                os.system("cls")
                                marca = input("Ingrese nueva marca: ")
                                if validar_campo_no_vacio(marca)==-1:
                                    print("Error, el campo no puede estar vacío")
                                    os.system("pause")
                                    continue
                                break
                            while True:
                                os.system("cls")
                                nombre = input("Ingrese nuevo nombre: ")
                                if validar_campo_no_vacio(nombre)==-1:
                                    print("Error, el campo no puede estar vacío.")
                                    os.system("pause")
                                    continue
                                break
                            
                            while True:
                                os.system("cls")
                                conexion = input("Ingrese nueva conexion: ")
                                if validar_campo_no_vacio(conexion)==-1:
                                    print("Error, el campo no puede estar vacío.")
                                    os.system("pause")
                                    continue
                                break
                            while True:
                                os.system("cls")
                                try:
                                    stock = int(input("Ingrese nuevo stock: "))
                                    if validar_stock(stock)==-1:
                                        print("Error, el stock debe ser mayor o igual a 0")
                                        os.system("pause")
                                        continue
                                except:
                                    print("Error, el campo no puede estar vacío.")
                                    os.system("pause")
                                    continue
                                break
                            while True:
                                os.system("cls")
                                try:
                                    precio = int(input("Ingrese nuevo precio en números: "))
                                    if validar_precio(precio)==-1:
                                        print("Error, el precio debe ser mayor o igual a 0")
                                        os.system("pause")
                                        continue
                                except:
                                    print("Error, el campo no puede estar vacío.")
                                    os.system("pause")
                                    continue
                                break

                            dato_final=modificar(id,tipo,marca,nombre,conexion,stock,precio)
                            print("Datos modificados por: ",id,tipo,marca,nombre,conexion,stock,precio)
                        else:
                            print("Error, id no existe en la base de datos")

                        os.system("pause")

                    case 5:
                        os.system("cls")
                        print("Listar productos")
                        print("\n")                        
                        imprimir_productos(productos)
                        os.system("pause")
                if opcion == 6:
                    print("Regresando al Menú Principal...")
                    os.system("pause")
                    break
                elif opcion < 1 or opcion > 6:
                    print("Error, debe ingresar una opción válida")
                    opcion = 0
                    os.system("pause")

        case 4:
            opt = 0
            while opt <= 2:
                os.system("cls")
                print("""
                                    Mantenedor de productos
                            
                                    1.- Cargar Datos
                                    2.- Respaldar Datos
                                    3.- Salir

                      """)
                opt = int(input("Ingrese una opcion entre 1 y 3: "))

                match opt:
                    case 1:
                        productos = leer_datos_productos_txt(productos_txt)
                        imprimir_productos(productos)
                        ventas = leer_datos_ventas_txt(ventas_txt)
                        print("\n----------------------\n")
                        imprimir_ventas(ventas)
                        folio = int(ventas[-1][0])
                        print("----------Datos Cargados----------")
                        os.system("pause")
                    case 2:
                        respaldar_datos()
                        print("Datos guardados correctamente")
                        os.system("pause")
                    case 3:
                        if opt == 3:
                            print("Saliendo del Menú...")
                            os.system("pause")
                            os.system("cls")
                            break
                        elif opt < 1 or opt > 3:
                            print("Error, debe ingresar una opción válida")
                            opt = 0
                            os.system("pause")