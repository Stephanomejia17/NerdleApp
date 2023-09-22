import random

class Nerdle:
    pass


class Ecuacion:
    ecuaciones: list = []
    ecuacion_alea: str
    def __init__(self):
        self.ecuacion: list[str] = []

    def generar_ecuacion(self) -> str:
        alea = random.randint(0, 780)

        # Abre el archivo Notepad
        with open('requirements/ecuaciones.txt', 'r') as archivo:
            # Lee todas las líneas del archivo y las almacena en una lista
            lineas = archivo.readlines()

        # Procesa las líneas para eliminar caracteres de nueva línea ('\n') y crea una lista
        self.ecuaciones = [linea.strip() for linea in lineas]

        ecuacion_aleatoria = self.ecuaciones.pop(alea)
        return ecuacion_aleatoria

    def comparar_ecuaciones(self, ecuacion_usuario: str) -> bool | list[str]:
        if self.ecuacion_alea == ecuacion_usuario:
            return True
        else:
            resultado: list[str] = ['0'] * 8
            for n in range(0, 8):
                if self.ecuacion_alea[n] == ecuacion_usuario[n]:
                    resultado[n] = '2'  # si es igual
                else:
                    if self.ecuacion_alea[n] != ecuacion_usuario[n]:
                        if ecuacion_usuario[n] in self.ecuacion_alea:
                            resultado[n] = '1'
        return resultado


class Jugador:
    def __int__(self):
        self.ecuacion: Ecuacion = None
