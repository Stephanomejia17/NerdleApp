import random
from typing import ClassVar, Optional, Union

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operadores = ['+', '-', '*', '/']


class Ecuacion:

    def __init__(self):
        self.ecuacion: str = ""
        self.ecuaciones: list = []
        self.ecuacion_alea: str = ""

    def __str__(self) -> str:
        return f"{self.ecuacion_alea}"

    def generar_ecuacion(self) -> str:
        pos_operador = random.randint(1, 3)
        self.ecuacion_alea: str = ""
        for i in range(0, 4):

            if i == pos_operador:
                opr_alea = operadores[random.randint(0, len(operadores) - 1)]
                self.ecuacion_alea += opr_alea

            indice_ecuacion = len(self.ecuacion_alea) - 1

            if (len(self.ecuacion_alea) == 0) or (self.ecuacion_alea[indice_ecuacion] in operadores):
                num_alea = numeros[random.randint(1, len(numeros) - 1)]

            else:
                num_alea = numeros[random.randint(0, len(numeros) - 1)]

            self.ecuacion_alea += num_alea

        evaluacion: Union[float, int] = eval(self.ecuacion_alea)
        if isinstance(eval(self.ecuacion_alea), int):
            self.ecuacion_alea += '='
            self.ecuacion_alea += f'{evaluacion}'
        elif isinstance(eval(self.ecuacion_alea), float):
            if evaluacion.is_integer():
                self.ecuacion_alea += '='
                self.ecuacion_alea += f'{int(evaluacion)}'

        if len(self.ecuacion_alea) != 8:
            self.generar_ecuacion()

        return self.ecuacion_alea



class Jugador:
    def __init__(self, ecuacion: str):
        self.ecuacion: str = ecuacion



class Nerdle:
    def __init__(self, ecuacion_usuario: str):
        self.ecuacion: Ecuacion = Ecuacion()
        self.usuario: Jugador = Jugador(ecuacion_usuario)
        self.contador_partidas_ganadas: int = 0
        self.contador_partidas_perdidas: int = 0

    def contador_de_intentos(self, contador_intentos: int) -> int:
        if contador_intentos < 7:
            contador_intentos += 1
            return contador_intentos

        else:
            return -1
    def iniciar_nuevo_juego(self):
        return self.ecuacion.generar_ecuacion()


