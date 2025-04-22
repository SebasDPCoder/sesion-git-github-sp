print("BIENVENIDO\nADMINISTRADOR DE TAREAS\n")

print("""MENU
1.Hacer lista de tareas
2.Ver lista de tareas
3.Marcar tareas como completadas
4.Salir\n""")

tareas = []  
estado_tareas = []  

def ingresar_tareas():    
    while True:
        ingresar_tarea = input("Ingrese la tarea: ")
        tareas.append(ingresar_tarea)
        estado_tareas.append(False) 
        agregar_tarea = str(input("Desea agregar más tareas? (si/no): "))
        if agregar_tarea.lower() == "si":
            continue
        elif agregar_tarea.lower() == "no":
            break
        else:
            print("Dato inválido. Intente de nuevo.")
            continue
    return tareas

def ver_lista():
    if not tareas:
        print("No hay tareas por realizar")
    else:
        print("\nLista de Tareas")
        num = 0
        for tarea, estado in zip(tareas, estado_tareas):
            num += 1
            estado_texto = "Completada" if estado else "Pendiente"
            print(f"{num}. {tarea.capitalize()} - {estado_texto}")
        print("")

    
def marcar_tareas():
    if not tareas:
        print("No hay tareas para marcar ")
    else:
        while True:
                tarea_numero = int(input("Ingrese el número de la tarea que ha completado: "))
                if 1 <= tarea_numero <= len(tareas):
                    estado_tareas[tarea_numero - 1] = True
                    print(f"Tarea '{tareas[tarea_numero - 1]}' marcada como completada.")
                    break
                else:
                    print("Número de tarea no válido. Intente de nuevo.")

def salir():
    print("Hasta luego")
    exit()

while True:
    try:
        opcion = int(input("Ingrese una de las 4 opciones (1/2/3/4): "))
    except ValueError:
        print("Error. Ingrese una opcion valida.")
        continue
    
    if opcion == 1:
        ingresar_tareas()
    elif opcion == 2:
        ver_lista()
    elif opcion == 3:
        marcar_tareas()
    elif opcion == 4:
        salir()
    else:
        print("Dato invalido")
        
    