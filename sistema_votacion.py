from time import sleep

print("-------SISTEMA DE VOTACION-------")

candidatos = []
numero_candidato = 1 

while True:        
    ingresar_candidato = input("Ingrese el candidato: ")

    if ingresar_candidato.isalpha():
        candidatos.append({'id':numero_candidato, 'nombre': ingresar_candidato.capitalize(), 'votos':0})

        agregar_candidato = str(input("Desea agregar más candidatos? (si/no): "))

        if agregar_candidato.lower() == "si":
            numero_candidato += 1
            continue
        
        elif agregar_candidato.lower() == "no":
            break
        
        else:
            print("Dato inválido. Intente de nuevo.")
            continue
    else:
        print("Dato invalido. Intente de nuevo")
        continue

print("")

while True:
    print("\n___MENU DE VOTACION___")
    print("\n(Si no hay mas votos por realizar, Escriba '0')")
    print("\nCandidatos a personeria")
    for _,candidato in enumerate(candidatos):
        print(f"{_+1}.{candidato['nombre']}")

    voto = int(input("Por que candidato desea votar: "))
    
    if voto == 0:
        break

    else:
        if 0 < voto <= len(candidatos):      
            for index in candidatos:           
                if voto == index['id']:
                    index['votos'] += 1
            print("Votación exitosa!!!")
            sleep(1)
            
        else:
            print("Fuera de rango. Intente de nuevo.")
            continue 

print("\n-----Votación finalizada-----")
print("\nCandidatos")
for _,candidato in enumerate(candidatos,start=1):
    print(f"{_}.{candidato['nombre']} con {candidato['votos']} votos")

print("\nEn revisión...")
sleep(1.5)


max_votos = max(candidato['votos'] for candidato in candidatos)
    
ganadores = [candidato for candidato in candidatos if candidato['votos'] == max_votos]
    
if len(ganadores) == 1:
    print(f'--¡Ganó {ganadores[0]["nombre"]} con {ganadores[0]["votos"]} votos!--')

else:
    print('¡Empate entre los siguientes candidatos:')
    for ganador in ganadores:
        print(f'{ganador["nombre"]} con un total de {ganador["votos"]} votos')
