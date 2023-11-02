# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:32:49 2020

@author: Federico
"""

import math
import random
import string


VOCALES = 'aeiou'
CONSONANTES = 'bcdfghjklmnpqrstvwxyz'
TAMANIO_MANO = 7

VALORES_LETRAS = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'ñ': 4, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Codigo de ayuda
#

ARCHIVO_PALABRAS = "palabras.txt"

def cargar_palabras():
    """
    Retorna una lista de palabras válidas, compuestas por letras en minúscula.
    
    Dependiendo del tamaño de la lista de palabras, esta función puede tomarse su tiempo para finalizar.
    """
    
    print("Cargando lista de palabras desde el archivo...")
    # inFile: Archivo
    inFile = open(ARCHIVO_PALABRAS, 'r')
    # palabras: lista de cadenas
    palabras = []
    for palabra in inFile:
        palabras.append(palabra.strip().lower())
    print("  ", len(palabras), "palabras cargadas.")
    return palabras

def obtener_diccionario_frecuencias(secuencia):
    """
    Genera un diccionario donde las claves son los elementos de la secuencia
    y los valores son enteros, que indican la cantidad de veces que ese
    elemento está repetido en la secuencia.

    secuencia: cadena o lista
    return: diccionario {tipo_elemento -> int}
    """
    
    # frecuencias: diccionario
    frec = {}
    for x in secuencia:
        frec[x] = frec.get(x,0) + 1
    return frec
	
#
# (fin Codigo de ayuda)
# -----------------------------------

#
# Problema #2: Puntuar una palabra
#
def obtener_puntaje_palabra(palabra, n):
    """
    Obtiene el puntaje de una palabra. Asume que la palabra es una palabra válida.

    Podemos asumir que la palabra siempre será una cadena de letras 
    o la cadena vacía (""). No se puede asumir que solo contendrá letras en
    minúsculas, así que deberemos resolver también con palabras con letras en
    mayúscula y minúscula.
    
	El puntaje de una palabra es el producto de dos componentes:

	Primer componente: la suma de los puntos de las letras en la palabra.
    Segundo componente: 1 o la fórmula 
        [7 * longitud_palabra - 3 * (n - longitud_palabra)], el valor que 
    sea más grande, donde longitud_palabra es la cantidad de letras usadas 
    en la palabra y n es la cantidad de letras disponibles en la mano actual.

    Al igual que en Scrabble, cada letra tiene un puntaje.

    palabra: cadena
    n: int >= 0
    retorna: int >= 0
    """
    aux_palabra = palabra.lower()
    suma_puntos_palabra = 0
    for letra in aux_palabra:
        suma_puntos_palabra += VALORES_LETRAS[letra]
    formula = (7*len(palabra)-3*(n-len(palabra)))
    if formula > 1:
        return suma_puntos_palabra*formula
    else:
        return suma_puntos_palabra


def mostrar_mano(mano):
    """
    Muestra las letras que están en la mano del jugador.

    Por ejemplo:
       mostrar_mano({'a':1, 'x':2, 'l':3, 'e':1})
    Debería mostrar por consola lo siguiente:
       a x x l l l e
    El orden de las letras no es importante.

    mano: diccionario (string -> int)
    """
    print("Su mano es:")
    for letra in mano.keys():
        for j in range(mano[letra]):
             print(letra, end=' ')      # Muestra todas las letras en la misma linea
    print()                             # Linea vacía


def repartir_mano(n):
    """
    Genera una mano al azar con n letras en minúscula.
    techo(n/3) letras en la mano deben ser VOCALES.

    Las manos se representan como diccionarios. Las claves son letras 
    y los valores indican el número de veces que esa letra está contenida 
    en la mano.

    n: int >= 0
    Retorna: diccionario (string -> int)
    """
    
    mano={}
    cantidad_vocales = int(math.ceil(n / 3))

    for i in range(cantidad_vocales):
        if i == cantidad_vocales - 1:
            x = "*"
        else:
            x = random.choice(VOCALES)
        mano[x] = mano.get(x, 0) + 1
    
    for i in range(cantidad_vocales, n):    
        x = random.choice(CONSONANTES)
        mano[x] = mano.get(x, 0) + 1
    
    return mano

#
# Problema #3: Actualizar la mano eliminando letras.
#
def actualizar_mano(mano, palabra):
    """
    NO asumir que la mano contiene el mismo número de veces una letra 
    que las que aparece en la palabra. Las letras que están en la palabra 
    y no en la mano deben ser ignoradas. Las letras que aparecen más veces 
    en la palabra que en la mano no deben resultar en un total negativo; 
    debemos eliminar esa letra de la mano o poner su cantidad en 0.

    Actualiza la mano: usa las letras que están en la palabra y retorna 
    la nueva mano, sin esas letras.

    No debe modificar mano, sino que debe retornar un nuevo diccionario.

    palabra: string
    mano: diccionario (string -> int)    
    retorna: diccionario (string -> int)
    """
    aux_mano = mano.copy()
    aux_palabra = palabra.lower()
    for letra in aux_palabra:
        if letra in aux_mano and aux_mano[letra] > 0:
            aux_mano[letra] -= 1
    aux_mano2 = aux_mano.copy()
    for letra in aux_mano:
        if aux_mano[letra] == 0:
            del aux_mano2[letra]
    return aux_mano2

#
# Problema #4: Verificar si la palabra es válida.
#
def es_palabra_valida(palabra, mano, lista_palabras):
    """
    Devuelve True si la palabra está en lista_palabras y está compuesta
    completamente por letras en la mano. Sino, devuelve False.
    No se debe modificar ni mano ni lista_palabras.
   
    palabra: string
    mano: diccionario (string -> int)
    lista_palabras: lista de cadenas en minúsculas
    Retorna: boolean
    """
    aux_palabra = palabra.lower()
    aux_palabra_a = aux_palabra.replace("*", "a")
    aux_palabra_e = aux_palabra.replace("*", "e")
    aux_palabra_i = aux_palabra.replace("*", "i")
    aux_palabra_o = aux_palabra.replace("*", "o")
    aux_palabra_u = aux_palabra.replace("*", "u")
    if (aux_palabra in lista_palabras or aux_palabra_a in lista_palabras or aux_palabra_e in lista_palabras or aux_palabra_i in lista_palabras or aux_palabra_o in lista_palabras or aux_palabra_u in lista_palabras):
        aux_mano = mano.copy()
        for letra in aux_palabra:
            if letra in aux_mano:
                if aux_mano[letra] > 0:
                    aux_mano[letra] -= 1
                else:
                    return False
            else:
                return False
        return True
    else:
        return False

#
# Problema #5: Jugar una mano
#
def calcular_longitud_mano(mano):
    """ 
    Retorna la longitud (cantida de letras) en la mano actual.
    
    mano: diccionario (string-> int)
    retorna: integer
    """
    suma_letras = 0
    for letra in mano:
        suma_letras += mano[letra]
    return suma_letras

def jugar_mano(mano, lista_palabras):

    """
    Permite que un usuario juegue una mano, con las siguientes consideraciones:

    * Se le muestra la mano actual.
    
    * El usuario puede ingresar una palabra.

    * Cuando una palabra es ingresada (válida o inválida), utiliza letras de la mano.

    * Una palabra inválida se rechaza, mediante un mensaje que le pide al usuario
      que ingrese otra palabra.

    * Después de cada palabra válida: se muestra el puntaje de la palabra, 
      las letras restantes de la mano y se le pide al usuario que ingrese 
      otra palabra.

    * La suma de los puntajes de las palabras se presenta una vez que la mano termina.

    * La mano termina cuando no hay más letras sin usar.
      El usuario también puede terminar la mano ingresando dos signos de exclamación
      ('!!') en vez de una palabra.

      mano: diccionario (string -> int)
      lista_palabras: lista de cadenas en minúsculas.
      retorna: el puntaje total de la mano
      
    """
    
    # PSEUDO-CODIGO
    # Llevar registro del puntaje total
    
    # Mientras haya letras en la mano o el usuario no ingrese '!!':
    
        # Mostrar la mano
        
        # Pedirle al usuario que ingrese una palabra
        
        # Si la entrada son dos signos de exclamación, se termina el juego
                    
        # Sino (la entrada no son dos signos de exclamación):

            # Si la palabra es válida:

                # Mostrarle al usuario los puntos que ganó,
                # y el puntaje total de la mano hasta ese momento.

            # Sino (la palabra no es válida):
                # Rechazar palabra inválida (mostrar un mensaje)
                
            # actualizar la mano del usuario eliminando las letras 
            # que usó en la palabra (aún si la palabra era inválida)
            

    # Se terminó el juego (el usuario se quedó sin letras o ingresó '!!'),
    # se le muestra el puntaje final de la mano.

    # Retorna el puntaje final como resultado de la función.
    puntaje_mano = 0
    longitud_mano = calcular_longitud_mano(mano)
    continuar_juego = True
    while longitud_mano > 0 and continuar_juego:
        mostrar_mano(mano)
        palabra = ingresar_palabra()
        if palabra == '!!' or calcular_longitud_mano(mano) == 0:
            continuar_juego = False
        else:
            if es_palabra_valida(palabra, mano, lista_palabras):
                puntaje_palabra = obtener_puntaje_palabra(palabra, calcular_longitud_mano(mano))
                print("El puntaje de la palabra es: {}".format(puntaje_palabra))
                print()
                puntaje_mano += puntaje_palabra
            else:
                print("La palabra es invalida.")
            mano = actualizar_mano(mano, palabra)
            longitud_mano = calcular_longitud_mano(mano)
    print("El puntaje final de la mano es: {}".format(puntaje_mano))
    return puntaje_mano




def ingresar_palabra():
    """
    Permite al usuario ingresar una palabra o '!!'.
    
    retorna: string
    """
    while True:
        palabra = input("Ingrese una palabra o !! para salir: ")
        palabra = palabra.replace(" ", "")
        if not palabra == '!!':
            if any(c.isdigit() or (c in string.punctuation and not c == "*") for c in palabra):
                print("La palabra no debe contener números ni símbolos.")
                continue
            if not palabra:
                print("La palabra no puede estar vacía.")
                continue
        return palabra
    


#
# Problema #6: Jugar una partida completa
# 


#
# procedimiento para reemplazar una letra en la mano
#

def intercambiar_mano(mano, letra):
    """
    Permite al usuario reemplazar todas las copias de una letra en la mano 
    (elegida por el usuario) por una nueva letra elegida, al azar, de VOCALES 
    y CONSONANTES. La nueva letra debe ser diferente a la elegida para intercambiar, 
    y no puede ser ninguna de las letras que ya tiene en la mano.
    
    Si el usuario ingresa una letra que no está en la mano, la mano debe quedar igual.
    
    No se debe modificar la mano original.
    Por ejemplo:
        intercambiar_mano({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    puede resultar en:
        {'h':1, 'e':1, 'o':1, 'x':2} -> si la nueva letra es 'x'
    La nueva letra no debe ser 'h', 'e', 'l', u 'o' ya que esas letras ya están en 
    la mano.
    
    mano: diccionario (string -> int)
    letra: string
    retorna: diccionario (string -> int)
    """
    if letra in mano:
       cantidad_letra = mano[letra]
       letras_posibles = VOCALES + CONSONANTES
       letras_posibles = [l for l in letras_posibles if l not in mano.keys()]
       nueva_letra = random.choice(letras_posibles)
       nueva_mano = mano.copy()
       del nueva_mano[letra]
       nueva_mano[nueva_letra] = cantidad_letra
       return nueva_mano
    else:
       print("La letra ingresada no esta en la mano.")
       return mano

#
# Problema #1: Armar esqueleto del ciclo de juego
#       
    
def jugar_partida(lista_palabras):
    """
    Permitir al usuario jugar una serie de manos (partida)

    * Pedir al usuario que ingrese un número total de manos.

    * Acumular el puntaje de cada mano en un puntaje total para la partida.
 
    * Por cada mano, antes de empezar a jugar, preguntar al usuario si quiere
      intercambiar una letra por otra. Esto se puede hacer sólo una vez durante 
      el juego. Una vez que se usa esta opción, no se le debe preguntar nuevamente 
      al usuario si quiere intercambiar una letra durante el juego.
    
    * Por cada mano, preguntar al usuario si desea volver a jugar la mano.
      Si el usuario ingresa 'si', se repetirá la mano y se mantendrá el mayor
      de los dos puntajes obtenidos para esa mano. Esto se puede hacer una única vez
      durante la partida. Una vez que se utiliza la opción de volver a jugar una mano,
      no se debe volver a preguntar si desea volver a jugar futuras manos. Volver a
      jugar una mano no afecta el número de manos totales que el usuario eligió jugar.
      
            * Nota: si se vuelve a jugar una mano, no se podrá elegir reemplazar una
              letra (se debe jugar con la mano original)
      
    * Devuelve el puntaje total de la partida.

    lista_palabras: lista de cadenas en minúsculas
    """
    #Codigo de jugar_palabaras
    
    #Inicializar variables
    cantidad_manos = 0
    intercambio = False
    repeticion = False
    puntaje_total = 0
    
    #Ingresar cantidad de manos
    cantidad_manos = ingresar_cantidad_manos()
    
    #Jugar manos
    while cantidad_manos > 0:
        puntaje_mano = 0
        print("Jugando mano")
        mano = {}
        mano = repartir_mano(TAMANIO_MANO)
        
        #Verificar si hubo intercambio de letra
        if not intercambio:
            mostrar_mano(mano)
            #Verificar si quiere realizar intercambio de letra
            if (quiere_intercambiar_letra()):
                #Realizar intercambio de letra
                mano = ingresar_letra(mano)
                intercambio = True
            else:
                #NO realizar intercambio de letra
                print("--No se realiza intercambio de letra")
        puntaje_mano = jugar_mano(mano, lista_palabras)
        #Verificar si hubo repeticion de mano
        if not repeticion:
            #Verificar si se desea repetir mano
            if (quiere_repetir_mano()):
                #Repetir mano
                print("--Se va repetir mano")
                puntaje_mano_nuevo = jugar_mano(mano, lista_palabras)
                if puntaje_mano_nuevo > puntaje_mano:
                    puntaje_mano = puntaje_mano_nuevo
                else:
                    print("Nuevo puntaje menor, se va mantener el anterior.")
                repeticion = True
            else:
                #NO repetir mano
                print("--No se va repetir mano")
        #Acumular puntaje de mano actual
        puntaje_total += puntaje_mano
        print()
        cantidad_manos -= 1
    
    print("")
    #Mostrar puntaje final
    print("El puntaje total de la partida es: {}".format(puntaje_total))
    print("Fin de partida")
    #Fin codigo de jugar_palabras


def quiere_intercambiar_letra():
    """
    Permite al usuario ingresar una opcion por si desea intercambiar o no una letra.
    
    retorna: boolean 
    """
    opcion = 0
    while opcion == 0:
        try:    
            opcion = int(input("Desea intercambiar letra? 1-si/2-no :"))
            if(opcion != 1 and opcion != 2):
                print("ERROR. Las opciones permitidas son 1-si/2-no")
                opcion = 0
            elif opcion == 1:
                return True
            elif opcion == 2:
                return False
        except ValueError:
            print("ERROR. El valor ingresado debe ser un número entero. Reintente")
            opcion = 0


def quiere_repetir_mano():
    """
    Permite al usuario ingresar una opcion por si desea repetir o no una mano.
    
    retorna: boolean 
    """
    opcion = 0
    while opcion == 0:
        try:    
            opcion = int(input("Desea repetir mano? 1-si/2-no :"))
            if(opcion != 1 and opcion != 2):
                print("ERROR. Las opciones permitidas son 1-si/2-no")
                opcion = 0
            elif opcion == 1:
                return True
            elif opcion == 2:
                return False
        except ValueError:
            print("ERROR. El valor ingresado debe ser un número entero. Reintente")
            opcion = 0
            

def ingresar_cantidad_manos():
    """
    Permite al usuario ingresar la cantidad de manos a jugar.
    
    retorna: int 
    """
    cantidad_manos = 0
    while cantidad_manos == 0:
        try:    
            cantidad_manos = int(input("Ingrese la cantidad de manos a jugar: "))
        except ValueError:
            print("ERROR. El valor ingresado debe ser un número entero. Reintente")
            cantidad_manos = 0
    print("Cantidad de manos a jugar: {}".format(cantidad_manos))
    print("")
    return cantidad_manos


def ingresar_letra(mano):
    """
    Permite ingresar una letra de la mano para intercambiar.
    Si la letra se repite, se cambian todas las instancias de esta.
    
    mano: diccionario (string -> int)
    
    retorna: diccionario (string -> int) 
    """
    print("--Se va realizar un intercambio de letra")
    letra = ""
    letra_cargada = 0
    while letra_cargada == 0:
        try:    
            letra = input("Ingrese la letra a intercambiar: ")
            if (len(letra) > 1 or len(letra) == 0):
                print("ERROR. Debe ingresar solo una letra. Reintente")
                letra_cargada = 0
            elif letra.isalpha() == False:
                print("ERROR. Debe ingresar solo una letra. Reintente")
                letra_cargada = 0
            else:
                print("Su letra es: {}".format(letra))
                letra_cargada = 1
                nueva_mano = intercambiar_mano(mano, letra)
                return nueva_mano
        except ValueError:
            print("ERROR. El valor ingresado debe ser una letra. Reintente")
            letra_cargada = 0

#
# Construye las estructuras de datos necesarias para jugar la partida.
# No eliminar la condición "if __name__ == '__main__':" Este código se ejecuta
# cuando el programa se ejecuta directamente, sin usar la sentencia import.
#
if __name__ == '__main__':
    lista_palabras = cargar_palabras()
    jugar_partida(lista_palabras)