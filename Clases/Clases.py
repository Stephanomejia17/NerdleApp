import random
from typing import ClassVar, Optional, Union


class Ecuacion:

    def __init__(self):
        self.ecuacion: str = ""
        self.ecuaciones: list = []
        self.ecuacion_alea: str = ""

    def __str__(self) -> str:
        return f"{self.ecuacion_alea}"

    def generar_ecuacion(self) -> str:
        alea = random.randint(0, 780)

        # Abre el archivo Notepad
        with open('requirements/ecuaciones.txt', 'r') as archivo:
            # Lee todas las líneas del archivo y las almacena en una lista
            lineas = archivo.readlines()

        # Procesa las líneas para eliminar caracteres de nueva línea ('\n') y crea una lista
        self.ecuaciones = [linea.strip() for linea in lineas]

        self.ecuacion_alea = self.ecuaciones.pop(alea)
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


