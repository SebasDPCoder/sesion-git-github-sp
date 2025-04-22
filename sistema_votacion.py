
candidatos = []

def ingresar_candidatos():  
    num = 1 
    while True:        
        ingresar_candidato = input("Ingrese el candidato: ")
        candidatos.append({'id':num, 'nombre': ingresar_candidato.capitalize(), 'votos':0})
        agregar_candidato = str(input("Desea agregar más candidatos? (si/no): "))
        
        if agregar_candidato.lower() == "si":
            num += 1
            continue
        
        elif agregar_candidato.lower() == "no":
            break
        
        else:
            print("Dato inválido. Intente de nuevo.")
            continue
                
    print("")
    return candidatos

ingresar_candidatos()

while True:
    print("\n___MENU DE VOTACION___")
    print("\nCandidatos")
    for _,candidato in enumerate(candidatos):
        print(f"{_+1}.{candidato['nombre']}")

    voto = int(input("Por que candidato desea votar: "))
    
    if 0 < voto <= len(candidatos):      
        for index in candidatos:           
            if voto == index['id']:
                index['votos'] += 1

        continuar_votos = str(input("Desea seguir votando? (si/no): "))
        
        if continuar_votos.lower() == "si":
            continue

        elif continuar_votos.lower() == "no":
            print("\nVotación finalizada")
            print("\nCandidatos")
            for _,candidato in enumerate(candidatos):
                print(f"{_+1}.{candidato['nombre']} con {candidato['votos']} votos")
            break
        
        else:
            print("Dato inválido. Intente de nuevo.")
            continue
        
    else:
        print("Fuera de rango. Intente de nuevo.")
        continue 

def validate_votes(candidates):
    for candidate in candidates:
        for candidate_2 in candidates:
            if candidate['votos'] > candidate_2['votos']:
                print(f'ganó {candidate}')
            
validate_votes(candidatos)           
        