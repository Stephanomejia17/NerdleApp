import sys
from typing import ClassVar, Optional, Union
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

        self.nerdle: Optional[Nerdle] = Nerdle('')
        self.cargar_base_Estadisticas()
        self.opciones = {
            "1": self.iniciar_nuevo_juego,
            "2": self.imprimir_reglas,
            "3": self.mostrar_estadisticas,
            "4": self.salir
        }
        self.lista_de_intentos: list[str] = []
        self.ecuacion_generada: str = ''
        self.intentos: int = 0

    @staticmethod
    def mostrar_menu():
        titulo = " Nerdle "
        print(f"\n{titulo:_^30}")
        print("1. Iniciar nuevo juego")
        print("2. Mostrar reglas")
        print("3. Mostrar estadisticas")
        print("4. Salir")
        print(f"{'_':_^30}")

    @staticmethod
    def imprimir_reglas():

        print("Nerdle:\n\n"
              "------------------------------------------------------------------------------\n"
              "Resuelve la ecuación en seis intentos\n"
              "- Componen la ecuación: números (0-9), operaciones básicas y el signo igual.\n"
              "- Tienes 6 intentos para colocarlos y llegar al resultado correcto.\n"
              f"- Los colores indican lo siguiente:\n"
              f"  1. {color_verde}Verde{resetear_color} correcta\n"
              f"  2. {color_amarillo} Amarillo {resetear_color} existe pero está en la posición incorrecta\n"
              f"  3. {color_rojo} Rojo {resetear_color} no pertenece a la ecuación.\n"
              "- Sigue el orden de operaciones y permite conmutabilidad en el resultado.\n"
              "- El objetivo es resolverla en el menor número de intentos posible.\n\n"
              "¡Buena suerte!\n"
              "_______________________________________________________________________________")

    def solicitar_ecuacion(self):
        if self.intentos != 6:
            ecuacion = input("Ingrese su ecuacion: ")
            separador = ecuacion.split(sep='=')
            operados = eval(separador[0])
            resultado = int(separador[1])
            if (len(ecuacion) > 8 or len(ecuacion) < 8) or (operados != resultado):
                print(f"La {ecuacion} no es permitida")
                self.solicitar_ecuacion()
            else:
                self.intentos = self.nerdle.contador_de_intentos(self.intentos)
                print(f"ESTÁS EN EL INTENTO {self.intentos} DE 6")
                #self.nerdle = Nerdle(ecuacion_usuario=ecuacion)
                self.lista_de_intentos = self.comparar_ecuaciones(ecuacion)
                self.colorear_ecuacion(self.lista_de_intentos, ecuacion)
                self.solicitar_ecuacion()
        else:
            print("PERDISTE")
            self.nerdle.contador_partidas_perdidas += 1


    def iniciar_nuevo_juego(self):
        self.intentos = 0
        #self.nerdle.ecuacion.generar_ecuacion()
        self.ecuacion_generada = self.nerdle.iniciar_nuevo_juego()
        self.solicitar_ecuacion()

    def mostrar_estadisticas(self):

        estadisticas = self.nerdle.estadisticas

        for indice, valores in enumerate(estadisticas, start=0):
            if valores != '':
                print(f"Partidas ganadas en {indice+1} intento: {valores}")

        while True:
            respuesta = input("Desearía que le mandemos las estadísticas a su correo electrónico? S/N: ")
            if respuesta == 'S':
                while True:
                    correo = input("Ingrese su correo electrónico: ")
                    comprobacion = input(f"El correo {correo} ingresado es correcto? S/N: ")
                    if comprobacion == 'S':
                        break

                self.nerdle.send_email(correo)
                break
            elif respuesta == 'N':
                break

    def cargar_base_Estadisticas(self):
        with open("requirements/Estadísticas.txt", 'r', encoding='utf-8') as file:
            valores = (file.readline()).split(',')
        for i in range(0, 6):
            self.nerdle.estadisticas[i] = int(valores[i])

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

    def comparar_ecuaciones(self, ecuacion_usuario: str) -> Union[bool, list[str]]:
        if self.ecuacion_generada == ecuacion_usuario:
            print("FELICIDADES, GANASTE!!")
            self.nerdle.estadisticas[self.intentos - 1] += 1
            self.nerdle.contador_partidas_ganadas += 1
            self.ejecutar_app()
        else:
            resultado: list[str] = ['0'] * 8
            for n in range(0, 8):
                if self.ecuacion_generada[n] == ecuacion_usuario[n]:
                    resultado[n] = '2'  # si es igual
                else:
                    if self.ecuacion_generada[n] != ecuacion_usuario[n]:
                        if ecuacion_usuario[n] in self.ecuacion_generada:
                            resultado[n] = '1'

            return resultado

    def colorear_ecuacion(self, listado_de_colores: list[str], ecuacion_usuario: str):
        ecuacion_coloreada = ""
        for valor in range(len(listado_de_colores)):
            if listado_de_colores[valor] == '2':
                ecuacion_coloreada += (color_verde + ecuacion_usuario[valor] + resetear_color)
            elif listado_de_colores[valor] == '1':
                ecuacion_coloreada += (color_amarillo + ecuacion_usuario[valor] + resetear_color)
            else:
                ecuacion_coloreada += (color_rojo + ecuacion_usuario[valor] + resetear_color)

        self.lista_de_intentos.clear()
        print(ecuacion_coloreada)


    def actualizar_base_Estadisticas(self):
        with open("requirements/Estadísticas.txt", 'w', encoding='utf-8') as file:
            res = ""
            for i in range(0, 6):
                res += f"{self.nerdle.estadisticas[i]},"

            file.write(res)


    def salir(self):
        self.actualizar_base_Estadisticas()
        print("\nGRACIAS POR JUGAR NERDLE. VUELVA PRONTO")
        sys.exit(0)

