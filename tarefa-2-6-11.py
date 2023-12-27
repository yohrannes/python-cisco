from datetime import time
while True:
    horainicio=input("Digite a hora inicial: ")
    minutoinicio=input("Digite o minuto inicial: ")
    horainicio=int(horainicio)
    minutoinicio=int(minutoinicio)

    if horainicio <= 24 and minutoinicio <=60:
        
        minutoduracao=input("Digite a duração em minutos: ")
        minutoduracao=int(minutoduracao)
        
        horaduracao=int(minutoduracao / 60)
        minutoduracao=int(minutoduracao % 60)
        
        horafinal = horainicio + horaduracao
        minutofinal = minutoinicio + minutoduracao
        
        if minutofinal >= 60:
            minutofinal = minutofinal - 60
            horafinal = horafinal + 1
            
        while True:
            if horafinal >= 24:
                horafinal = horafinal - 24
                diastotais = 0
                diastotais = diastotais + 1
            else:
                break
        
        print("Duração de", diastotais, "dias,", horaduracao, "horas e", minutoduracao, "minutos")
        print("Será finalizado às ", horafinal, ":", minutofinal)
        break
    else:
        print ("Hora e/ou minuto inicial inválido!")