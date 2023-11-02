import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QMainWindow, QInputDialog, QMessageBox
from interfaz import consola
from Clases.Clases import Nerdle, Ecuacion
from interfaz.consola import UIConsola
from typing import Optional


class MainWindowNerdle(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/MainWindow.ui", self)
        self.setFixedSize(self.size())
        self.configurar_conexion_botones()
        self.ventanaa_reglas = VentanaReglas()
        self.ventana_estadisticas = VentanaEstadisticas()
        self.ventana_ecuacion = VentanaEcuacion()

    def configurar_conexion_botones(self):
        self.iniciar_nuevo_juego.clicked.connect(self.abrir_ventana_ecuacion)
        self.mostrar_estadisticas.clicked.connect(self.abrir_ventana_estadistica)
        self.mostrar_reglas.clicked.connect(self.abrir_ventana_reglas)

    def abrir_ventana_reglas(self):
        self.ventanaa_reglas.exec()
        self.ventanaa_reglas.mostrar_reglas()

    def abrir_ventana_ecuacion(self):
        self.ventana_ecuacion.exec()

    def abrir_ventana_estadistica(self):
        self.ventana_estadisticas.exec()


class VentanaReglas(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/Reglas.ui", self)

    def mostrar_reglas(self):
        print("Ok")


class VentanaEstadisticas(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/Estadistica.ui", self)


class VentanaEcuacion(QDialog):
    def __init__(self):
        super().__init__()
        self.nerdle: Optional[Nerdle] = Nerdle('')
        self.ecuacion = Ecuacion()
        self.consola = UIConsola()
        self.consola.ecuacion_generada = self.nerdle.iniciar_nuevo_juego()
        self.intentos = 0
        self.ecuaciones = []
        self.layouts = []
        uic.loadUi("gui/Ecuacion.ui", self)
        self.setFixedSize(self.size())
        self.__config()

    def __config(self):
        self.oKButton.clicked.connect(self.guardar_ecuacion)
        self.ecuacion.generar_ecuacion()
        self.layouts = [self.Ecuacion1, self.Ecuacion2, self.Ecuacion3, self.Ecuacion4, self.Ecuacion5, self.Ecuacion6]

    def guardar_ecuacion(self):
        self.nerdle.usuario.ecuacion = self.txtEcuacion.toPlainText()
        self.ecuaciones.append(self.nerdle.usuario.ecuacion)
        self.llamar_comparacion()

    def llamar_comparacion(self):
        self.consola.comparar_ecuaciones(self.nerdle.usuario.ecuacion)
        self.actualizar_layouts()

    def comprobacion_de_intentos(self):
        if self.intentos != 6:
            separador = self.nerdle.usuario.ecuacion.split(sep='=')
            operados = eval(separador[0])
            resultado = int(separador[1])
            if (len(self.nerdle.usuario.ecuacion) > 8 or len(self.nerdle.usuario.ecuacion) < 8) or (operados != resultado):
                mensaje = QMessageBox()
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setWindowTitle('Advertencia')
                mensaje.setText('NÚMERO DE DÍGITOS SUPERADO')
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.exec_()
            else:
                self.intentos = self.nerdle.contador_de_intentos(self.intentos)
                print(f"ESTÁS EN EL INTENTO {self.intentos} DE 6")
                # self.nerdle = Nerdle(ecuacion_usuario=ecuacion)
                self.consola.lista_de_intentos = self.comparar_ecuaciones(self.nerdle.usuario.ecuacion)
                self.colorear_ecuacion(self.consola.lista_de_intentos, self.nerdle.usuario.ecuacion)
                self.solicitar_ecuacion()
        else:
            print("PERDISTE")
            self.nerdle.contador_partidas_perdidas += 1

    def actualizar_layouts(self):
        self.layouts[self.intentos].setText(f"{self.nerdle.usuario.ecuacion}")

        if self.intentos == 5:
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Advertencia')
            mensaje.setText('INTENTOS SUPERADOS')
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.exec_()
        else:
            self.intentos += 1







