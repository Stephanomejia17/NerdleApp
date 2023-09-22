resetear_color = "\033[0m"  # Restablecer el color y otros atributos de formato
color_verde = "\033[32m"
color_amarillo = "\033[33m" # Texto amarillo
color_gris = "\033[37m"  # Texto gris
color_rojo = "\033[31m"
from Clases.Clases import Nerdle
from typing import Optional
import time
class UIConsola:
    def __init__(self):
        self.nerdle: Optional[Nerdle] = None
        self.opciones = {
            "a": self.iniciar_nuevo_juego,
            "b": self.mostrar_reglas,
            "c": self.mostrar_estadisticas,
            "d": self.salir
        }
    @staticmethod
    def mostrar_menu():
        pass

    def solicitar_ecuacion(self):
        pass


    def mostrar_ecuacion(self):
        pass
    def iniciar_nuevo_juego(self):
        self.solicitar_ecuacion()
        self.nerdle.iniciar_nuevo_juego()
        datos: bool | list[str] = self.nerdle.ecuacion.comparar_ecuaciones(self.nerdle.usuario.ecuacion)
        print(self.nerdle.ecuacion.ecuacion_alea)
        for i in range(0,6):
            if datos == True:
                print("¡¡¡GANASTE!!!")
                time.sleep(2)
                self.ejecutar_app()
            else:
                self.colorear_ecuacion(datos, self.nerdle.usuario.ecuacion)




    def mostrar_reglas(self):
        pass

    def mostrar_estadisticas(self):
        pass
    def salir(self):
        pass
    def ejecutar_app(self):
        print("\nBIENVENIDO A NERDLE")
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if opcion in self.opciones.keys():
                accion()
            else:
                print(f"{opcion} no es una opción válida")
    def colorear_ecuacion(self, listado_de_colores: list[str], ecuacion_usuario: str):
        ecuacion_coloreada = ""
        for valor in range(len(listado_de_colores)):
            if listado_de_colores[valor] == '2':
                ecuacion_coloreada += (color_verde + ecuacion_usuario[valor] + resetear_color)
            elif listado_de_colores[valor] == '1':
                ecuacion_coloreada += (color_amarillo + ecuacion_usuario[valor] + resetear_color)
            else:
                ecuacion_coloreada += (color_rojo + ecuacion_usuario[valor] + resetear_color)
        print(ecuacion_coloreada)






