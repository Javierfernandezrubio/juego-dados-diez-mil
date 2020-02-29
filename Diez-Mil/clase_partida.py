"""
Clase para jugar al juego de dados del DiezMil:
    Hará uso de la clase jugador.
"""
from Clase_jugadores import Clase_jugadores
import Clase_jugadores

class Partida:
    """
    Clase que implementa la partida para el DiezMil:
        Reglas: http://www.acanomas.com/Reglamentos-Juegos-de-Dados/1235/Diez-mil.htm

    Métodos:
        * jugar: ejecuta el juego.
        * jugar_turno: ejecuta el turno.
    """

    def __init__(self, *jugadores):
        self.__jugadores = jugadores


    def jugar(self):
        # Inicio Partida
        print("--Juego del Diez Mil--")
        print("**********************\n")

        # Turno Partida
        self.jugar_turno()
        
    def jugar_ronda(self):
        pass

    def jugar_turno(self):
        bool = True
        while bool:
            Clase_jugadores.reset()
            jugar_turno_jugador()
            if Jugador.puntos_acumulados == 10000:
                print(f"Felicidades {Clase_jugadores} has ganado.")
                self.__salida_pantalla(marcador)
                break
            if Jugador.puntos_acumulados > 10000:
                print(f"Lo siento {Clase_jugadores} has perdido.")
                self.__salida_pantalla(marcador)
                break
            n = raw_input("Quieres seguir tirando (s/n):")
            if n.strip() == 'n':
                bool = False

        pass

    def jugar_turno_jugador(self):
        j.comprobar_puntos()
        self.__salida_pantalla(Partida.salida_tirada(j))
        pass

    def salida_tirada(j):
        print("Ha salido: ")
        for i in Clase_jugadores.dados:
            print(Clase_jugadores.dados)
        print(f"Tienes {Clase_jugadores.puntos_turno()}.")
        print(f"Tus puntos totales son: {Clase_jugadores.puntos_acumulados()}.")



    def __salida_pantalla(self, salida):
        self.__salida[self.turno] += salida + "\n"

    def marcador(self):
        print("--Marcador--")
        print(f"Jugador 1: {p[0]}")
        print(f"Jugador 2: {p[1]}")
        print(f"Jugador 3: {p[2]}")
        print(f"Jugador 4: {p[3]}")


p = Partida(Clase_jugadores("Jugador1"), Clase_jugadores("Jugador2"), Clase_jugadores("Jugador3"), Clase_jugadores("Jugador4"))

p.jugar()


