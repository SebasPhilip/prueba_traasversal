productos = {'8475HD':['HP',15.6,'8GB','DD','IT','Intel Core i5', 'Nvidia GTX1050'],
             '2175HD':['Lenovo',14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'NvidiaGTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB' 'Intel COre i7', 'Nvidia RTX2080Ti']
}

stock={'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD':[424990,1] }


def stock_marca(marca):
    stock_disponible=[]
    if marca in productos:
        stock_disponible.append(marca)

        





def busqueda_precio (p_min, p_max):
    try: 
        p_min=int(input("Ingrese un rango de precio (Límite inferior): "))
        p_max=int(input("Ingrese un rango de precio (Límite superior): "))
    except ValueError:
        print ("Rango de precios no válido")


    coincidencias=[]
    for modelo, precio in stock.items():
        if p_min <= precio <= p_max: 
            if modelo in stock:
                marca=productos[modelo][0]
                coincidencias.append((marca,modelo))

    coincidencias.sort()

    if coincidencias:
        print(f"Los modelos encontrados entre el rango de precios comprendido entre {p_min} y {p_max} son {coincidencias}")
    else:
        print ("No hay notebooks en ese rango de precios")

def actualizar_precio(modelo, p):

    if modelo in stock:
        stock[modelo][0]=p


        print (f"El nuevo precio de {modelo} es {p}")
    else:
        print (f"Sin existencias de {modelo} en nuestros datos")
    return

print ("Bienvenido a Pybooks")
while True:
    print ("Menú Principal")
    print("1. Stock Marca")
    print("2.Busuqueda por precio")
    print ("3. Actualizar Precio")
    print ("4. Salir")
    try:
        opt=int(input("Ingrese una opción: "))
    except ValueError:
        print("Opción No Puede ser un número")
    else:
        if opt==1:
            marca=input("Ingrese la marca que busca: ").upper().strip()
            stock_marca(marca)
        elif opt ==2:
            p_min=0
            p_max=0
            busqueda_precio(p_min, p_max)
        elif opt ==3:
            while True:
                try:
                    modelo=input("Ingrese modelo al que quiera actualizar su precio: ").upper().strip()
                    p=int(input(f"Ingrese el nuevo precio de {modelo}: "))
                except ValueError:
                    print ("Valor inválido")
                else:
                    actualizar_precio(modelo, p)
                    decision=input("Deseas realizar algún otro cambio? s/n ")

                    if decision == "s":
                        actualizar_precio(modelo, p)
                    elif decision == "n":
                        break
                    else:
                        print ("Opción no válida")

        elif opt==4:
            print ("Terminando Programa... Gracias por usar Pybooks.")
            break
        else:
            print("Ingrese una opción válida (1-4)")