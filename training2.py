# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PASOS DEL PROGRAMA:
# 1.Mostrar un menu con 4 opciones para gestionar calificaciones.
# 2.Validar la entrada del usuario para evitar caracteres no validos.
# 3.Implementar una opción para ver el estado de aprobación de una calificación individual.
# 4.Implementar una opción para calcular el promedio de un conjunto de calificaciones.
# 5.Implementar una opción para contar cuantas calificaciones son mayores a un valor especificado.
# 6.Implementar una opción para contar cuantas veces aparece una calificación especifica.
# 7.Permitir que el usuario salga del programa escribiendo 'salir' en cualquier momento.
# 8.Validar que las calificaciones ingresadas esten en un rango valido (0-100).
# 9.Gestionar excepciones para entradas no validas, como caracteres o números fuera de rango.
# 10.Mostrar los resultados de las operaciones seleccionadas de manera clara y detallada.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


from time import sleep
import os
os.system('clear') # Limpiar la consola

# Funcion para mostrar el titulo de mejor manera
def title(message):
    print("="*70)
    print(f"{message:^70}")
    print("="*70)

# Presentamos el menu al usuario
def menu():

    title("GESTION DE CALIFICACIONES")
    print("""\nMENU
1.ESTADO DE APROBACION DE NOTA INDIVIDUAL
2.PROMEDIO NOTAS
3.CONTEO DE NOTAS MAYORES A UN VALOR
4.CONTEO NOTA ESPECIFICA
(PARA FINALIZAR EL PROGRAMA. ESCRIBA 'salir') 
""")

# Función para gestionar la entrada del usuario por si desea salir
def user_input(message):
    while True:
        user_entry = input(message)  # Solicita una entrada
        if user_entry.lower() == "salir":  # Si el usuario escribe 'salir', termina el programa
            print("Saliendo del programa...")
            exit()  # Salir completamente del programa
        return user_entry  # Si no se escribe 'salir', devuelve lo que el usuario ingreso
    
# Función para mostrar un mensaje especifico
def message():
    print("Volviendo al menu...")
    sleep(2)
    
# Función para obtener las calificaciones del usuario y validarlas
def get_grades():
    while True:
        try:
            # Solicita las calificaciones al usuario (separadas por comas)
            grades_input = user_input("Ingrese sus calificaciones (separadas por ','): ")
            grades = []

            # Procesa cada calificación ingresada
            for grade in grades_input.split(","):
                grade = grade.strip()  # Elimina espacios adicionales
                
                try:
                    grade = float(grade)  # Convierte la calificación a tipo float
                    if 0 <= grade <= 100: # Verifica si la calificación esta en el rango valido
                        grades.append(grade)  # Si es valida, la agrega a la lista

                    else:
                        print("No esta en el rango permitido. Intente de nuevo.")  # Si no esta en el rango, muestra un error
                        break  # Sale del bucle y pide las calificaciones nuevamente
                    
                except ValueError:
                    # Si no se puede convertir la calificación a float, muestra un error
                    print("Ingresar un valor numerico.")
                    break  # Sale del bucle y pide las calificaciones nuevamente
                
            else:
                return grades  # Si las calificaciones son validas, Retorna las calificaciones y rompe el bucle para continuar
               
            
        except ValueError:
            # Si ocurre algún error al ingresar las calificaciones, muestra un mensaje y sigue pidiendo las calificaciones
            print("Hubo un error. Por favor, intente de nuevo.")
            continue
        
        
# Bucle principal para el menu de opciones
while True:
    try:
        menu()
        option = int(user_input("Ingrese una de las 4 opciones (1/2/3/4): ")) # Solicita la opción del usuario y la convierte a entero

    except ValueError:
        # Si el usuario no ingresa un número valido, muestra un mensaje de error y vuelve a pedir la opción
        print("Error. Ingrese una opción valida.")
        continue

    # Opcion 1: Ver el estado de aprobación de una calificación individual
    if option == 1:
        os.system('clear')
        title("ESTADO DE APROBACION DE NOTA INDIVIDUAL")
        while True:
            try:
                # Solicita al usuario ingresar una calificación
                approval_grade = float(user_input("Ingresa tu calificación (0-100): "))
                
                # Verifica si la calificación esta en el rango de aprobación
                if 60 <= approval_grade <= 100:
                    print("\nEstado -- Aprobado ✅\n")  # Si esta en el rango de aprobado
                    message()
                    break

                elif 0 <= approval_grade < 60:
                    print("\nEstado -- Reprobado ❌\n")  # Si esta en el rango de reprobado
                    message()
                    break

                else:
                    # Si la calificación no esta en el rango 0-100, pide que ingrese un valor valido
                    print("Debes ingresar un número de 0 a 100.")
                    continue

            except ValueError:
                # Si se ingresa un valor no numerico, muestra un error y vuelve a pedir la calificación
                print("Valor invalido.")
                continue


    # Opcion 2: Calcular el promedio de una serie de calificaciones
    elif option == 2:
        os.system('clear')
        title("PROMEDIO NOTAS")

        grades = get_grades()  # Llama a la funcion previamente definida para pedir las calificaciones
        
        # Calcula el promedio de las calificaciones ingresadas
        average = sum(grades) / len(grades)

        # Muestra las calificaciones y el promedio
        print(f"\nCalificaciones -- {grades}")
        print(f"\nPromedio  -- {average:.2f}")

        # Verifica si el promedio es aprobado o reprobado
        if 60 <= average <= 100:
            print("-- Aprobaste ✅ --\n")
            message()
            
        elif 0 <= average < 60:
            print("-- Reprobaste ❌ --\n")
            message()
            

    # Opcion 3: Contar las calificaciones mayores a un valor especifico
    elif option == 3:
        os.system('clear')
        title("CONTEO DE NOTAS MAYORES A UN VALOR")
        
        grades = get_grades()
        
        while True:
            try:
                count = 0  # Inicializa el contador de calificaciones mayores
                index = 0  # Indice mediante el cual se van a ir comparando calificaciones
                value = int(user_input("Ingrese un valor para contar las calificaciones mayores a este: "))
                
                if 100 >= value >= 0:  # Verifica que el valor ingresado este en el rango permitido
                    while index < len(grades):
                        if grades[index] > value:
                            count += 1  # Cuenta las calificaciones mayores al valor ingresado
                        index += 1
                        
                    print(f"\nCantidad de calificaciones mayores a {value} -- {count}\n")
                    message()                    
                    break

                else:
                    print("Digite valor de 0-100")  # Si el valor no esta en el rango, muestra un mensaje de error

            except ValueError:
                # Si ocurre un error al ingresar el valor, muestra un mensaje de error
                print("Valor Invalido")
                continue


    # Opcion 4: Contar cuantas veces aparece una calificación especifica
    elif option == 4:
        os.system('clear')
        title("CONTEO DE NOTA ESPECIFICA")
        
        grades = get_grades()
        
        while True:
            try:
                count = 0
                specific_grade = float(user_input("Ingrese la calificación a contar: "))

                # Verifica que la calificación esté en el rango de 0-100
                if 100 >= specific_grade >= 0:
                    
                    for grade in grades:
                        if grade == specific_grade:
                            count += 1  # Cuenta las veces que aparece la calificación
                            
                    if count:
                        print(f"\nLa calificación {specific_grade} se encontro -- {count} {'vez' if count == 1 else 'veces'}\n")
                        message()                        
                        break

                    else:
                        print(f"\nLa calificación {specific_grade} no se encontro\n")
                        message()
                        break
                        
                else:
                    print(f"Digite valor de 0-100")  # Si la calificación no esta en el rango, muestra un error

            except ValueError:
                # Si ocurre un error al ingresar la calificación, muestra un mensaje de error
                print("Valor Invalido")
                continue
    else:
        print("Opcion Invalida")
