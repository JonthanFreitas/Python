dia = int(input("Digite quantos dias: "))
hora = int(input("Digite quantos horas: "))
minuto = int(input("Digite quantos minutos: "))
segundo = int(input("Digite quantos segundos: "))

seg = (dia * 24 * 60 * 60) + (hora * 60 * 60) + (minuto * 60) + segundo

print(f'O total de segundos são {seg:}')
