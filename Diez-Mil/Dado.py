
import random

Class Dado:
    """
    Esta clase simula el comportamiento de un dado
    """
    def __init__(self,*valores):
        """"
        Crea el objeto que simula un dado.
        :param valores: tupla (no es una lista) de valores de las caras del dado.
        """
        self.__caras = valores
        self.__cara = random.choice(valores)

    @property
    def cara(self):
        return self.__cara

    @property
        def caras(self):
            return self.__caras


    def tirada(self):
        self.__cara = random.choice(self.__caras)
        return self.__cara

