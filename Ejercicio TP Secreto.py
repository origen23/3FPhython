# Ejercicio TP
import random
print("JUEGO - ADIVINE EL NÚMERO SECRETO")

numero_maximo = 50
numero_minimo = 1
numero_secreto = random.randint(numero_minimo,numero_maximo)
numero_ingresado = 0
intentos = 5
contador = 0
sigo = True

# print(f"El numero secreto es {numero_secreto}  ")

while sigo and contador < intentos:
    numero_ingresado = int(input(f"ingrese un numero entre {numero_minimo} y {numero_maximo}: "))
    contador +=1
    if numero_ingresado == numero_secreto:
        print(f"¡¡¡ CORRECTO !!! Numeros iguales ... ¡¡¡ Ha ganado el juego !!!")
        print("¡¡¡ F I N !!! ")
        sigo = False
    elif numero_ingresado < numero_secreto:
        print(f"¡¡¡ ERROR !!! El número ingresado es menor al numero secreto")
    else:
        print(f"¡¡¡ ERROR !!! El número ingresado es mayor al numero secreto")

    if contador == 5 and sigo:
        print(f"¡¡¡ FIN DEL JUEGO !!!  No hay mas intentos - Lamentablemente ha perdido")
        print(f"¡¡¡ EL NUMERO SECRETO ES EL {numero_secreto} ")
    elif sigo:
        print(f"Tiene {(intentos-contador)} intentos mas ")
    
