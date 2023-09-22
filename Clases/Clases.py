import random


class Nerdle:
    def __init__(self):
        self.contador_intentos: int = 0
        self.contador_partidas_ganadas: int = 0
        self.contador_partidas_perdidas: int = 0

    def contador_de_intentos(self) -> bool:
        if self.contador_intentos < 7:
            self.contador_intentos += 1
            return True
        else:
            return False

    def gano_partida(self):
        if self.ecuacion.comparar_ecuaciones() is True and self.contador_de_intentos() is True:
            return True
        elif self.ecuacion.comparar_ecuaciones() is True and self.contador_de_intentos() is False:
            return False
        else:
            return False

    def contador_de_juegos(self):
        if self.gano_partida() is True:
            self.contador_partidas_ganadas += 1
        else:
            self.contador_partidas_perdidas += 1
        return

    def estadistica_de_partidas(self):
        if self.gano_partida() is True:
            self.contador_partidas_ganadas += 1
        else:
            self.contador_partidas_perdidas += 1
        return



class Jugador:
    pass


class Ecuacion:
    pass
