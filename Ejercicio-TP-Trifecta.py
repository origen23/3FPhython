# Ejercicio TP
import random
print("La Trifecta")

numero_ingresado = 0
palabra_ingresada = 0
cantidad_palabra = 0
num_llave = 0
es_mayor = True
es_num   = True
factorial = 0

while es_mayor and es_num:
    numero_ingresado = input(f"ingrese un numero mayor a cero para continuar:")
    es_num = numero_ingresado.isdigit()
    if es_num:
       numero_llave = int(numero_ingresado)
       if not (numero_llave) > 0:
           es_mayor = False
           print("¡¡¡ F I N del ciclo !!! ")                       
    else:
        print("¡¡¡ F I N del ciclo !!! ")    
                    

    if es_mayor and es_num:
        palabra_ingresada = input(f"ingrese una palabra o frase:")
        cantidad_palabra = len(palabra_ingresada)
        print(f"La palabra ingresada es ' {palabra_ingresada} ' ") 
        print(f"La palabra ingresada tiene {cantidad_palabra} caracteres ") 

        factorial=1
        for i in range (1,(cantidad_palabra+1),1):
                factorial = i*factorial

        print(f"El Factorial de  {cantidad_palabra} es {factorial} ")             

        es_par = False
        num_aux = 0

        num_aux = factorial / 2
        if int(num_aux) * 2 == factorial:
             es_par = True
             print(f"El Factorial {factorial} es par ")             
        else:
             print(f"El Factorial {factorial} es impar ")             
                  


             


    
    
    # if numero_ingresado == numero_secreto:
    #     print(f"¡¡¡ CORRECTO !!! Numeros iguales ... ¡¡¡ Ha ganado el juego !!!")
    #     print("¡¡¡ F I N !!! ")
    #     sigo = False
    # elif numero_ingresado < numero_secreto:
    #     print(f"¡¡¡ ERROR !!! El número ingresado es menor al numero secreto")
    # else:
    #     print(f"¡¡¡ ERROR !!! El número ingresado es mayor al numero secreto")

    # if contador == 5 and sigo:
    #     print(f"¡¡¡ FIN DEL JUEGO !!!  No hay mas intentos - Lamentablemente ha perdido")
    #     print(f"¡¡¡ EL NUMERO SECRETO ES EL {numero_secreto} ")
    # elif sigo:
    #     print(f"Tiene {(intentos-contador)} intentos mas ")
    
