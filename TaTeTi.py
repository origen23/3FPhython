import tkinter as tk
import random

def inicializar_tablero():
    """
    Crea e inicializa el tablero de juego con espacios vacíos.
    """
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    return tablero

def actualizar_botones(tablero):
    """
    Actualiza el texto y color de los botones en la ventana según el tablero actual.
    """
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 'O':
                botones[i][j]['text'] = 'O'
                botones[i][j]['bg'] = '#a1e9c7'  # Color verde claro para ficha O
                botones[i][j]['fg'] = '#000000'  # Texto negro para ficha O
            elif tablero[i][j] == 'X':
                botones[i][j]['text'] = 'X'
                botones[i][j]['bg'] = '#4caf50'  # Color verde para ficha X
                botones[i][j]['fg'] = '#000000'  # Texto negro para ficha X
            else:
                botones[i][j]['text'] = ' '
                botones[i][j]['bg'] = '#c8e6c9'  # Color verde claro para espacios vacíos
                botones[i][j]['fg'] = '#000000'  # Texto negro para espacios vacíos

def reiniciar_juego():
    """
    Reinicia el juego: limpia el tablero, los botones y el resultado.
    """
    global tablero
    global primero_maquina
    a_jugar=[(0,0,False)]

    tablero = inicializar_tablero()
   
    primero_maquina = random.choice([True, False])
    if primero_maquina:
       a_jugar = juega_auto(tablero)
       fila = int(a_jugar[0][0])
       columna = int(a_jugar[0][1])
       tablero[fila][columna] = 'X'
       jugador['text'] = "¡Inicia Máquina!"
    else:
       jugador['text'] = "¡Inicia Humano!"    

    actualizar_botones(tablero)
    resultado['text'] = ''
    habilitar_botones()


def jugar_humano(fila, columna):
    """
    Permite al jugador humano realizar un movimiento en el tablero.
    """
      
    if tablero[fila][columna] == ' ' and resultado['text'] == '':
        tablero[fila][columna] = 'O'
        actualizar_botones(tablero)
        if ganador(tablero, 'O'):
            resultado['text'] = "¡Has ganado!"
            deshabilitar_botones()
        elif esta_lleno(tablero):
            resultado['text'] = "Es un empate."
            deshabilitar_botones()
        else:
            jugar_maquina()

def jugar_maquina():
    a_jugar=[(0,0,False)]
    
    """
    Permite a la máquina realizar un movimiento en el tablero.
    """
    
    while True:
       
       
        a_jugar = juega_auto(tablero)
        
        fila = int(a_jugar[0][0])
        columna = int(a_jugar[0][1])

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = 'X'
            actualizar_botones(tablero)
            if ganador(tablero, 'X'):
                resultado['text'] = "¡La PC ha ganado!"
                deshabilitar_botones()
            elif esta_lleno(tablero):
                resultado['text'] = "Es un empate."
                deshabilitar_botones()
            jugador['text'] = "             "
            break

def juega_auto(aux_tablero):
    jugadas = ["H"," "," "," "," "," "," "," "," "," "]
    lineas = ([0,0,0],[1,2,3],[3,6,9],[9,8,7],[7,4,1],[1,5,9],[3,5,7],[2,5,8],[4,5,6])
    en_lineas = ([0,0,0],[1,4,5],[1,7],[1,2,6],[4,8],[5,6,7,8],[2,8],[3,4,6],[3,7],[2,3,5])    
    par_jugada = [(0,0,False)]

    aux_cargo = 0
    for i in range(3):
        for j in range(3):    
            aux_cargo += 1
            jugadas[aux_cargo]=aux_tablero[i][j]
            

    par_jugada = gano(jugadas,lineas)
    if par_jugada[0][2]: 
       return par_jugada
    else:
        par_jugada = defensa(jugadas,lineas)
        if par_jugada[0][2]:
           return par_jugada
        else:
           par_jugada = ataque(en_lineas,jugadas,lineas) 
           return par_jugada


def gano(jugadas_g,lista_lineas):
    mejores = [0,0,0,0,0,0,0,0,0]
    indice3 = 0
    mejor_fila = 0
    opciones = []
    respuesta_g = [(0,0,False)]
    elegida = 0
    

    for i in range(len(lista_lineas)):
        cuento_x = 0
        cuento_o = 0          
        indice2 = i
        indice = 0

        for x in range(3):
            indice = lista_lineas[indice2][x]   
            if jugadas_g[indice] == "X":
                cuento_x += 1
            elif jugadas_g[indice] == "O":        
                cuento_o += 1
                  
        mejores[i] = cuento_x - cuento_o
   
    indice3 = 0

    
    valor_mejor_fila = max(mejores)
    
    if valor_mejor_fila == 2:
      # Busco la posición de 2X
        for i in range(len(mejores)):
           if mejores[i] == 2:
              opciones.append(i)
        
        elegida = random.choice(opciones)

        for x in range(len(lista_lineas[i])):
                indice3 = lista_lineas[elegida][x]
                if jugadas_g[indice3] == " ":
    
                   return convierto(indice3) 
                
    return respuesta_g

def defensa(jugadas_g,lista_lineas):
    mejores = [0,0,0,0,0,0,0,0,0]
    indice3 = 0
    mejor_fila = 0
    respuesta_g = [(0,0,False)]
    opciones = []
    elegida = 0

    # Recorro todas las filas , son ocho para saber si hay peligro. 
    for i in range(len(lista_lineas)):
        cuento_x = 0
        cuento_o = 0          
        indice2 = i
        indice = 0
        
        # Recorro la tupla de cada fila, son ocho filas con una tupla de 3 cada una
        for x in range(3):
                # indice toma el valor de cada integrante de la linea, que es una casilla
                indice = lista_lineas[indice2][x]   
                       
                if jugadas_g[indice] == "X":
                    cuento_x += 1
                elif jugadas_g[indice] == "O":        
                    cuento_o += 1                             
        mejores[i] = cuento_o - cuento_x
   
    indice3 = 0
    valor_mejor_fila = max(mejores)
    if valor_mejor_fila == 2:

        for i in range(len(mejores)):
           if mejores[i] == 2:             
              opciones.append(i)
      
        #   Encuentro al puntaje peligroso y lo busco en la tupla de 3
        elegida = random.choice(opciones)

        for x in range(len(lista_lineas[i])):
                indice3 = lista_lineas[elegida][x]
                #  Encuentro la casilla peligrosa y la regreso
                if jugadas_g[indice3] == " ":
    
                   return convierto(indice3) 
      
    return respuesta_g

def ataque(casillas_en,jugadas_g,lista_lineas):
    mejores = [0,0,0,0,0,0,0,0,0,0]
    maximo_puntaje = 0
    opciones = []
    elegida = 0

    # Recorro las casilla del 1 al 9 dándoles puntaje para el ataque    
    for i in range(len(casillas_en)):
      if jugadas_g[i] == " ":           
         indice_de_fila = 0
         indice_9 = i
            
         # Recorro Dentro cada tupla de la casilla de turno las líneas en las que participa - Recorro las 2, 3 o 4
         if jugadas_g [5] == " ":
            return convierto(5)         
         
         for x in range(len(casillas_en[indice_9])):
            indice_de_fila = casillas_en[indice_9][x]
         
            cant_vacios = 0
            cant_dexs = 0
            cant_deos = 0 
                  
            # Voy a las filas y las analizo, de acuerdo al contenido de cada casilla de cada línea - Son 3
            for k in range(len(lista_lineas[indice_de_fila])):
               if k >= 1: 
                  indice_8 = lista_lineas[indice_de_fila][k]  
                  
                  if indice_9 != lista_lineas[indice_de_fila][k]:
                        
                     if jugadas_g[indice_8] == " ":
                        cant_vacios += 1

                     if jugadas_g[indice_8] == "X":
                        cant_dexs   += 1
                     if jugadas_g[indice_8] == "O":
                        cant_deos   += 1

            if cant_deos == 1:
                 mejores[indice_9] += 0
            elif cant_dexs == 1:
                 mejores[indice_9] += 1               
            elif cant_vacios >= 1:
                 mejores[indice_9] += 2               
            
            
                 
   
    maximo_puntaje = max(mejores) 
   
   
    for i in range(len(mejores)):
        if mejores[i] == maximo_puntaje:                          
            opciones.append(i)
    
    elegida = random.choice(opciones)
   
    return convierto(elegida)
    

def convierto(ubicacion):
    
    if ubicacion == 1:
       return [(0,0,True)]
    if ubicacion == 2:
       return [(0,1,True)]
    if ubicacion == 3:
       return [(0,2,True)]
    if ubicacion == 4:
       return [(1,0,True)]
    if ubicacion == 5:
       return [(1,1,True)]
    if ubicacion == 6:
       return [(1,2,True)]
    if ubicacion == 7:
       return [(2,0,True)]
    if ubicacion == 8:
       return [(2,1,True)]
    if ubicacion == 9:
       return [(2,2,True)]



def ganador(tablero, simbolo):
    """
    Verifica si el jugador con el símbolo dado ha ganado.
    """
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == simbolo for j in range(3)) or all(tablero[j][i] == simbolo for j in range(3)):
            return True

    # Verificar diagonales
    if tablero[0][0] == simbolo and tablero[1][1] == simbolo and tablero[2][2] == simbolo:
        return True
    if tablero[0][2] == simbolo and tablero[1][1] == simbolo and tablero[2][0] == simbolo:
        return True
    return False

def esta_lleno(tablero):
    """
    Verifica si el tablero está lleno.
    """
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

def deshabilitar_botones():
    """
    Deshabilita todos los botones del tablero.
    """
    for i in range(3):
        for j in range(3):
            botones[i][j]['command'] = None

def habilitar_botones():
    """
    Habilita todos los botones del tablero.
    """
    # juega_pc = True
    
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                botones[i][j]['command'] = lambda i=i, j=j: jugar_humano(i, j)

# Inicializar la GUI
ventana = tk.Tk()
ventana.title('TaTeTi')
primero_maquina = False

jugador = tk.Label(ventana, text='', font=('Helvetica', 20))
jugador.grid(row=6, column=0, columnspan=3)

# Definir estilos de colores verdes
color_fondo_botones = '#c8e6c9'  # Fondo verde claro para los botones
color_texto_botones = '#000000'  # Texto negro para los botones

tablero = inicializar_tablero()

botones = [[tk.Button(ventana, text=' ', width=10, height=3,
                      bg=color_fondo_botones, fg=color_texto_botones,
                      command=lambda i=i, j=j: jugar_humano(i, j))
                      for j in range(3)] for i in range(3)]
                     


for i in range(3):
    for j in range(3):
        botones[i][j].grid(row=i, column=j)

primero_maquina = random.choice([True, False])
if primero_maquina:
   a_jugar = juega_auto(tablero)
   fila = int(a_jugar[0][0])
   columna = int(a_jugar[0][1])
   tablero[fila][columna] = 'X' 
  
   botones[fila][columna]['text'] = 'X'
   botones[fila][columna]['bg'] = '#4caf50'  # Color verde para ficha X
   botones[fila][columna]['fg'] = '#000000'  # Texto negro para ficha X    
   jugador['text'] = "¡Inicia Máquina!"
else:
   jugador['text'] = "¡Inicia Humano!"    


resultado = tk.Label(ventana, text='', font=('Helvetica', 20))
resultado.grid(row=3, column=0, columnspan=3)


boton_reiniciar = tk.Button(ventana, text="Reiniciar juego", command=reiniciar_juego)
boton_reiniciar.grid(row=4, column=0, columnspan=3)

ventana.mainloop()
