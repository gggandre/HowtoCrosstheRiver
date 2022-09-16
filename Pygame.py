# A01753176-Gilberto-André García Gaytán
# A01748120-Rodrigo Hernandez de Tejada Martinez
# A01376511-Juan Carlos Flores García
# Código hecho usando PEP8 (Style Guide for Python Code)
# https://peps.python.org/pep-0008/
import sys  # Se importa la librería de sys (Parámetros y funciones
import pygame  # Se importa la librería de Pygame
# esta librería nos sirve para hacer la animación de la solucion
# del problema https://www.pygame.org/news
# específicos del sistemas) https://docs.python.org/es/3/library/sys.html
import HCRFinal  # Se importa ua librería propia creada en el HCRFinal.py

# Se cargan las imágenes y se les ajusta el tamaño
# de cada una con pygame de.trasfor.scale que encontramos
# en la documentación de pygame https://www.pygame.org/docs/
ganso = pygame.image.load("ganso.png")
ganso = pygame.transform.scale(ganso, (50, 50))
elote = pygame.image.load("elote.png")
elote = pygame.transform.scale(elote, (45, 45))
zorro = pygame.image.load("zorro.png")
zorro = pygame.transform.scale(zorro, (60, 60))
fondo = pygame.image.load("lago.png")
fondo = pygame.transform.scale(fondo, (600, 600))
# Listo es falso ya que aún no está listo nada
listo = False
# La barra espaciadora se tiene que iniciar en 0
barraespaciadora = 0
# Se crean las constantes de ganso, zorro y elote y se le da un valor
CONSTANTEGANSO = 12
CONSTANTEZORRO = 12
CONSTANTEELOTE = 12
# Título del programa
pygame.display.set_caption("TC1001S.101: How to Cross the River")


# Se hace uso de la librería de pygame para la música de la animación
def play():
    pygame.mixer.music.load('simple-life-synod-main-version-17722-03-37.wav')
    pygame.mixer.music.play()


# Se crea una función llamada solucion en donde se hace uso de
# la lobrería propia de HCR en donde se busca el path
def solucion():
    P = HCRFinal.HCRLibreria()
    while len(P) > 14:  # Si la longitu de P es mayor a 14 se reinicia
        reiniciar()
    P = HCRFinal.HCRLibreria()
    return ((P))  # regresa el valor de P
pygame.init()  # Initialize all imported pygame modules
play()  # Se llama a la función donde está la música para que se reproduzca
# junto con la animación
# Se le asigna el tamaño a la pantalla, se decidió que fuera de 600x600
# ya que creemos que es un tamaño adecuado
screen = pygame.display.set_mode([600, 600])
# Se asigna un clock para el tiempo de las animaciones
clock = pygame.time.Clock()
# Se crea una secuencia en donde hace llamado a la función de solucion
secuencia1 = solucion()


# Se creo una función llamada bajar, la cual nos ayuda
# a que los personajes se "bajen" del bote
def bajar(personaje):
    if personaje > 500:  # Si este valor es mayor que 500, entonces
        # le resta  500 a personaje
        variable = personaje - 500
    else:  # Si no suma 500 al personaje
        variable = personaje + 500
    return variable  # Te regresa el valor de la variable


# Se creo una función llamada elementoslista, la cual usa
# una lista de un rango de r elementos, y regresa los valores de
# A y B respectivamente
def elementoslista(lista):
    for r in range(0, len(lista)):
        A = lista.pop(0)
        B = lista.pop(0)
        return A, B


# Se creo una función llamada siesentero, la cual verifica si
# el valor de n es entero y te regresa Falso
def siesentero(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


# Se creo una función llamada secuencia, la cual tiene
# una lista vacía y despúes se usa un for de la lista
# junto con una serie de condiciones para acomodar los personajes
# en donde se les dió el valor del 1 al 4
def secuencia(List):
    secuencia = []
    for i in List:
        if i == 'Ganzo':
            secuencia.append(1)
        elif i == 'Zorro':
            secuencia.append(2)
        elif i == 'Maiz':
            secuencia.append(3)
        elif i == 'Granjero':
            secuencia.append(4)
    return secuencia  # regresa la secuencia
# Se nombra la constante variable y se dice que es  = secuencia
SEC = secuencia(secuencia1)

# Se establecen los ejes para que se posicisionen los personajes
# en los lugares establecidos en los ejes x,y
fotoxb = 200
fotoyb = 500
fotox_a = 200
imageY_A = 450
fotox_b = 300
imageY_B = 450

# Se asignan las velocidades de los
# elementos que se van a mover
velx_bote = -15
velx_a = -15
velx_b = -15

# Se suben las imágenes de granjero, vacio y bote, ya que son las que
# tienen movimiento
# en la animación y se escalan respectivamente
granjero = pygame.image.load("granjero.png")
granjero = pygame.transform.scale(granjero, (100, 100))
IMAGENVACIA = pygame.image.load("vacio.png")
IMAGENVACIA = pygame.transform.scale(IMAGENVACIA, (100, 100))
bote = pygame.image.load("bote.png")
bote = pygame.transform.scale(bote, (300, 100))
# EL movimiento se iguala con la imagen vacia
MOVIMIENTO = IMAGENVACIA

# Se crea un while con el número 2
while 2:
    clock.tick(50)  # Se usa el clock para el movimiento
    pygame.display.flip()  # Actualiza la superficie de visualización completa a la pantalla
    for event in pygame.event.get():  # procesar internamente los
        # controladores de eventos de pygame
        fotox_a -= 2  # Se le da los valores a los personajes
        fotox_b -= 2
        fotoxb -= 2
        fotox_a += velx_a
        fotoxb += velx_bote
        fotox_b += velx_b
        if event.type == pygame.QUIT:  # Si se acaba el path se sale
            listo = True  # Se termina
            pygame.quit()  # Se quita la animación
            sys.exit()  # Se quita lo de sys
        if event.type == pygame.KEYDOWN:  # Si se aprita la barra espaciadora
            if SEC:
                # EN esta condición hace los movimientos necesarios
                # para animar la solución del problema how to cross the river
                R, W = elementoslista(SEC)
                for i in range(0, 1):
                    barraespaciadora += 1
                    alto = barraespaciadora / 2
                    if siesentero(alto):  # Se detiene
                        velx_a *= -1
                        velx_b *= -1
                        velx_bote *= -1
                    else:  # si no sigue
                        velx_a *= -1
                        velx_b *= -1
                        velx_bote *= -1
                    if R == 4 and W == 1:  # Para que los personajes se bajen
                        MOVIMIENTO = ganso
                        CONSTANTEGANSO = bajar(CONSTANTEGANSO)
                    elif R == 4 and W == 2:
                        MOVIMIENTO = zorro
                        CONSTANTEZORRO = bajar(CONSTANTEZORRO)
                    elif R == 4 and W == 3:
                        MOVIMIENTO = elote
                        CONSTANTEELOTE = bajar(CONSTANTEELOTE)
                    else:
                        MOVIMIENTO = IMAGENVACIA
            else:
                pygame.quit()  # se quita la animación
                sys.exit()  # Acaba el sys
    if (fotox_a > 600 and fotox_a < 0):
            velx_a *= 0  # Los valores de las velocidades son menor que
            # las fotos, entonces velocidad = 0
    if (fotox_b > 600 and fotox_b < 0):
            velx_bote *= 0
    if (fotoxb > 600 and fotox_b < 0):
           velx_b *= 0
    # Se usa screen.blit El objeto de pantalla representa la pantalla del juego
    # Es un envoltorio delgado alrededor de una superficie de Pygame que le
    # permite dibujar fácilmente imágenes en la pantalla y de todos los
    # personajes
    screen.blit(fondo, (0, 0))
    screen.blit(granjero, (fotox_a, imageY_A, 80, 80))
    screen.blit(MOVIMIENTO, (fotox_b, imageY_B, 80, 80))
    screen.blit(ganso, (CONSTANTEGANSO, 100))
    screen.blit(zorro, (CONSTANTEZORRO, 200))
    screen.blit(elote, (CONSTANTEELOTE, 300))
    screen.blit(bote, (fotoxb, fotoyb, 80, 80))
    pygame.display.update()  # Inicializar el módulo de visualización
