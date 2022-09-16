# A01753176-Gilberto-André García Gaytán
# A01748120-Rodrigo Hernandez de Tejada Martinez
# A01376511-Juan Carlos Flores García
# Código hecho usando PEP8 (Style Guide for Python Code)
# https://peps.python.org/pep-0008/
import random  # Se importa la librería random que
# se utiliza para generar números aleatorios
LadoA = ['Granjero', 'Ganzo', 'Maiz', 'Zorro']  # Se definen los diccionarios
LadoB = []  # Se crea un dicciionario vacío ya que
# de ese lado no hay personajes
Path = []  # El path vacío


# Se tiene que validar el estado como se vio en clase
def validaestado(L):
    if 'Zorro' in L and 'Ganzo' in L and len(L) == 2:
        return False  # Si zorro y ganzo son igual a 2, regresa Falso
    elif 'Ganzo' in L and 'Maiz' in L and len(L) == 2:
        return False  # Si gazo y maíz son igual a 2, regresa Falso
    return True  # Si estás dos no se cumplen regresa Verdadero


# Si no lo valida tiene que reiniciar
def reiniciar():
    global LadoA, LadoB, Path  # Se declaran las variables globales
    # Las variables globales son Las variables que se crean fuera
    # de una función se le conocen como variables globales
    LadoA = ['Granjero', 'Ganzo', 'Maiz', 'Zorro']  # Diccionario de
    # los personajes que estan del lado izquierdo (LadoA)
    LadoB = []   # Diccionario de
    # los personajes que estan del lado derecho, como no hay nadie
    # se pone vacío (LadoB)
    Path = []  # El path vacío


def jugada(Z, W):  # Se creo una función jugada en la que
    # se hace uso de la librería random para mover al personaje
    if len(Z) != 0:  # Si la longitud es != no igual
        # al operador, devuelve verdadero si los operandos no son iguales
        # enrtre sí y si son iguales devuelve falso
        J1 = random.choice(Z)  # Devuelve un valor aleatorio
        # extraído de la secuencia pasada como argumento
        if J1 != 'Granjero':  # Si granjero es !=
            Z.remove(J1)  # Remove elmina el primer elemento
            # que es pasado como argumento de una lista o tupla
            W.append(J1)  # Append es un método de python para agregar
            # un solo elemento
        if 'Granjero' in Z:  # Si granjero está en Z
            Z.remove('Granjero')  # Remove elmina el primer elemento
            # que es pasado como argumento de una lista o tupla
            W.append('Granjero')  # Append es un método de python para agregar
            # un solo elemento
    else:  # Si no
        J1 = ''  # Vacío
    return ('Granjero', J1)  # Regresa el valor


def HCRLibreria():  # Se crea una función de HCR
    # que se usará en el main (Pygame.py)
  n = 0  # Nombramos las variables a usar
  m = 0
  F = LadoA
  D = LadoB
  a = 1
  while len(LadoB) != 4:  # El ciclo while se usa para
      # iterar el bloque de código siempre y cuando sea
      # verdadero
    J1, J2 = jugada(F, D)
    if validaestado(F) and validaestado(D) and a <= 7:  # Si la función
        # vaida estado en F y en D el valor de a es menor o igual a 7
        F, D = D, F
        Path.append(J1)  # agrega J1
        Path.append(J2)  # agrega J2
        m += 1
        a += 1
    else:  # si no
        n += 1
        m += 1
        a = 1
        reiniciar()  # Se usa la función reiniciar
        F = LadoA
        D = LadoB
  return (Path)  # Regresa el path
