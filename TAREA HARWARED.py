import pygame
import threading
import time

#inicializamos pygame
pygame.init()

#definimos dimenciones de la ventana
ancho = 800
alto = 600

#creamos la ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Laberinto")

# Carga los datos en matriz
laberinto = [[[0 for _ in range(5)] for _ in range(50)] for _ in range(30)]

with open("laberintoEdificio.txt", 'r') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        piso, columna, fila, construccion = linea.strip().split(',')
        piso = int(piso)
        columna = int(columna)
        fila = int(fila)
        laberinto[piso][columna][fila] = construccion

def recorrer_laberinto(clon, fila, columna, piso, rutaActual):
    # Verificar si la posición actual es la salida (ventana)
    if laberinto[piso][columna][fila] == 'V':
        print(f"Ruta encontrada por clon {clon}: {rutaActual}")
        return

    # Verificar si la posición actual es un muro (X) o si ya fue visitada
    if laberinto[piso][columna][fila] == 'X' or laberinto[piso][columna][fila] == '-':
        return

    # Marcar la posición actual como visitada por el clon
    laberinto[piso][columna][fila] = '-'

    # Simular el movimiento visualmente
    r, g, b = 255, 255, 255
    pygame.draw.rect(ventana, [r, g, b], (columna * 10 + 150, fila * 10 + 150, 10, 10))
    pygame.display.update()
    time.sleep(0.1)

    # Explorar las posibles direcciones de movimiento: derecha, izquierda, arriba y abajo
    derecha(clon, fila, columna, piso, rutaActual)
    izquierda(clon, fila, columna, piso, rutaActual)
    arriba(clon, fila, columna, piso, rutaActual)
    abajo(clon, fila, columna, piso, rutaActual)

    # Restaurar la posición para evitar conflictos entre clones
    laberinto[piso][columna][fila] = '.'

def derecha(x,y,r,g,b):
    global matriz
    i = x
    while(i <= 49) and (matriz[i][y] == "."):
        matriz[i][y] = "-"
        time.sleep(2)
        pygame.draw.rect(ventana,[r,g,b],( (i*10 + 150, y*10 + 150,10,10) ))
        pygame.display.update()

        if(y > 0) and (matriz[i][y-1] == "-"):
            arriba(i,y-1,255,255,255)
        if(y < 29) and (matriz[i][y+1] == "-"):
            abajo(i,y+1,255,255,255)
        i += 1
    if(i<50) and (matriz[i][y] == "V")
        print('salida encontrada en posicion(',x,',',y,')')
        exit

def izquierda(x,y,r,g,b):
    global matriz
    i = x
    while(i >= 0) and (matriz[i][y] == "."):
        matriz[i][y] = "-"
        time.sleep(2)
        pygame.draw.rect(ventana,[r,g,b],( (i*10 + 150, y*10 + 150,10,10) ))
        pygame.display.update()

        if(y > 0) and (matriz[i][y-1] == "-"):
            arriba(i,y-1,255,255,255)
        if(y < 29) and (matriz[i][y+1] == "-"):
            abajo(i,y+1,255,255,255)
        i -= 1
    if(i>=0) and (matriz[i][y] == "V"):
        print('salida encontrada en posicion(',x,',',y,')')
        exit

def arriba(x,y,r,g,b):
    global matriz
    i = y
    while(i >= 0) and (matriz[x][y] == "."):
        matriz[x][i] = "-"
        time.sleep(2)
        pygame.draw.rect(ventana,[r,g,b],( (x*10 + 150, i*10 + 150,10,10) ))
        pygame.display.update()

        if (x > 0) and (matriz[x-1][i-1] == "-"):
            izquierda(x-1,i,255,255,255)
        if (x < 29) and (matriz[x+1][i] == "-"):
            derecha(x+1,i,255,255,255)
        i -= 1
    if (i >= 0) and (matriz[x][i] == "V"):
        print('salida encontrada en posicion(',x,',',y,')')
        exit

def abajo(x,y,r,g,b):
    global matriz
    i = y
    while(i <= 29) and (matriz[x][y] == "."):
        matriz[x][i] = "-"
        time.sleep(2)
        pygame.draw.rect(ventana,[r,g,b],( (x*10 + 150, i*10 + 150,10,10) ))
        pygame.display.update()

        if (x > 0) and (matriz[x-1][i] == "-"):
            izquierda(x-1,i,255,255,255)
        if (x < 49) and (matriz[x+1][i+1] == "-"):
            derecha(x+1,i,255,255,255)
        i += 1
    if (i < 30) and (matriz[x][i] == "V"):
        print('salida encontrada en posicion(',x,',',y,')')
        exit

# Defino la matriz y la inicializo con "."
matriz=[]
for i in range(5):
   piso=[]
   for j in range(50):
      vector=[]
      for k in range(30):
          vector.append('.')
      piso.append(vector)
   matriz.append(piso)
  
#importamos el laberinto
fd = open("c:\Users\Camil\OneDrive\Escritorio\laberinto.txt","r")
datos = fd.readlines()
for dato in datos:
   pos = dato.split(',')
   matriz[int(pos[2])][int(pos[1])][int(pos[0])] = pos[3][0:1]
   print(pos[2] + ',' + pos[1] + ',' + pos[0] + ' = ' + pos[3][0:1])

def iniciarRecorrido():
    clon = threading.current_thread().getName()
    recorrer_laberinto(clon, 0, 0, 0, "")
    print(f"El clon {clon} ha terminado de recorrer el laberinto")

cantClones = 3
hebras = []

for i in range(cantClones):
    hebra = threading.Thread(target=iniciarRecorrido, name = f"Clon {i+1}")
    hebras.append(hebra)

for hebra in hebras:
    hebra.start()

for hebra in hebras:
    hebra.join()

pygame.quit()




