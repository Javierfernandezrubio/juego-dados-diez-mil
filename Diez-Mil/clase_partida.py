"""
Clase para jugar al juego de dados del DiezMil:
    Hará uso de la clase jugador.
"""
from clase_jugadores import Jugador

class Partida:
    """
    Clase que implementa la partida para el DiezMil:
        Reglas: http://www.acanomas.com/Reglamentos-Juegos-de-Dados/1235/Diez-mil.htm
    Variables de instancia:
        * __jugadores: tupla con objetos de clase Jugador (mínimo 4).
        *

    Métodos:
        * jugar: ejecuta el juego.
        * jugar_turno: ejecuta el turno.
    """

    def __init__(self, *jugadores):
        self.__jugadores
        self.__turno = 0

    def jugar(self):
        # Inicio Partida
        print("--Juego del Diez Mil--")
        print("**********************\n")

        # Turno Partida
        self.jugar_turno()

        # Imprimir puntuación


    def jugar_turno(self):
        self.__turno += 1



    def __salida_pantalla(self, salida):


n_jugadores = int(input("Introduce el número de jugadores: "))
for i in range(n_jugadores):
    p += Jugador("Jugador"[i],)
p.jugar()
print(p)