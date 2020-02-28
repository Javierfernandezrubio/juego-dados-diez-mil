import Dado


class Clase_jugadores:
    """
    Clase jugadores del juego de los dados Diez Mil, cuyas reglas están definidas aquí:
    http://www.acanomas.com/Reglamentos-Juegos-de-Dados/1235/Diez-mil.htm

    Variables de instancia de cada objeto jugador:
        * __nombre: nombre del jugador.
        * __contador_dados: array con las caras de los 6 dados
        * __puntos_acumulados: puntuación acumulada.
        * __puntos_turno: puntuación tirada actual.
    Métodos:
        * comprobar_puntos.
        * reset: resetea el puntaje por turno
    """

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__contador_dados = [0, 0, 0, 0, 0, 0]
        self.__puntos_acumulados = 0
        self.__puntos_turno = 0

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def dados(self):
        return self.__contador_dados

    @dados.setter
    def dados(self, value):
        self.__contador_dados = value

    @property
    def puntos_acumulados(self):
        return self.__puntos_acumulados

    @puntos_acumulados.setter
    def puntos_acumulados(self, value):
        self.__puntos_acumulados = value

    @property
    def puntos_turno(self):
        return self.__puntos_turno

    @puntos_turno.setter
    def puntos_turno(self, value):
        self.__puntos_turno = value

    # Métodos:

    def comprobar_puntos(self):
        """
        Método que inicializa las tirada de los 6 dados, comprueba la caras ganadoras de los 6 dados
        y los acumula en un array. Por último va sumando todos los untos de cada turno de cada jugador.
        """
        dados = [Dado.tirada(), Dado.tirada(), Dado.tirada(), Dado.tirada(), Dado.tirada(), Dado.tirada()]
        caras = self.__contador_dados
        dados_reusables = 0

        # Comprobamos los resultados de los 6 dados
        for i in dados:
            if dados[i] == 1:
                caras[0] += 1
            if dados[i] == 2:
                caras[1] += 1
            if dados[i] == 3:
                caras[2] += 1
            if dados[i] == 4:
                caras[3] += 1
            if dados[i] == 5:
                caras[4] += 1
            if dados[i] == 6:
                caras[5] += 1

        # Sumamos puntos
        if caras == [1, 1, 1, 1, 1, 1]:
            self.__puntos_turno += 1500
        else:
            if caras[0] == 1 or 2:
                self.__puntos_turno += 100*caras[0]
            if caras[0] >= 3:
                self.__puntos_turno += 1000+100*caras[0]

            if caras[4] == 1 or 2:
                self.__puntos_turno += 50*caras[4]
            if caras[4] >= 3:
                self.__puntos_turno += 500+100*caras[4]

            if caras[1] >= 3:
                self.__puntos_turno += 200+100*caras[1]
            else:
                dados_reusables += 1

            if caras[2] >= 3:
                self.__puntos_turno += 300+100*caras[2]
            else:
                dados_reusables += 1

            if caras[3] >= 3:
                self.__puntos_turno += 400+100*caras[3]
            else:
                dados_reusables += 1

            if caras[5] >= 3:
                self.__puntos_turno += 600+100*caras[5]
            else:
                dados_reusables += 1
        return self.__puntos_turno

    def reset(self):
        """
        Método que pasa los puntos por turno de cada jugador a sus puntos totales o acumulados,
        luego resetea los puntos por turno a 0 para el siguiente turno
        """
        self.__puntos_acumulados += self.__puntos_turno
        self.__puntos_turno = 0
        return self.__puntos_acumulados
