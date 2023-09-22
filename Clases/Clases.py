import random

class Nerdle:
    def __init__(self):
        self.tablero = self.crear_tablero()

    def crear_tablero(self):
        filas = 6
        columnas = 8
        tablero = [[None] * columnas for _ in range(filas)]
        return tablero

    def mostrar_tablero(self):
        for fila in self.tablero:
            print(fila)

    pass

class Jugador:
    pass

class Ecuacion:
    pass




