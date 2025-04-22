productos = {
    'manzana': {'precio': 1500, 'cantidad': 65},
    'plátano': {'precio': 1200, 'cantidad': 80},
    'naranja': {'precio': 800, 'cantidad': 100},
    'papa': {'precio': 1000 , 'cantidad': 90},
    'pan': {'precio': 2000, 'cantidad': 55},
    'pollo': {'precio': 12000, 'cantidad': 20},
    'gaseosa': {'precio': 4000, 'cantidad': 40}
}


def añadir_producto():
        while True:
            try:
                producto = input("Ingresar nombre del producto: ")
                if producto.isalpha():
                    precio = float(input("Ingresar precio del producto: "))
                    cantidad = int(input("Ingresar cantidad del producto: "))
                else:
                    print("Valores invalidos")
                    continue
                break
            except ValueError:
                print("Valores invalidos")
    
        return producto,precio,cantidad
    
while True:
    try:
        opcion = int(input("Ingrese una de las 4 opciones (1/2/3/4): "))
        break
    except ValueError:
        print("Error. Ingrese una opcion valida")
        continue
    
