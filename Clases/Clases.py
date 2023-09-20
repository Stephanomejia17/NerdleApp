import random

class Nerdle:
    pass

class Jugador:
    pass

class Ecuacion:
    def __init__(self):
        self.ecuaciones: list = []

    def generar_ecuacion(self) -> str:
        alea = random.randint(0, 780)

        # Abre el archivo Notepad
        with open('requirements/ecuaciones.txt', 'r') as archivo:
            # Lee todas las líneas del archivo y las almacena en una lista
            lineas = archivo.readlines()

        # Procesa las líneas para eliminar caracteres de nueva línea ('\n') y crea una lista
        self.ecuaciones = [linea.strip() for linea in lineas]

        ecuacion = self.ecuaciones.pop(alea)
        return ecuacion
