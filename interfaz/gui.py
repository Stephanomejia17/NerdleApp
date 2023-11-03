import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QMainWindow, QInputDialog, QMessageBox
from interfaz import consola
from Clases.Clases import Nerdle, Ecuacion
from interfaz.consola import UIConsola
from typing import Optional
from typing import Union


class MainWindowNerdle(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/MainWindow.ui", self)
        self.setFixedSize(self.size())
        self.configurar_conexion_botones()
        self.console = UIConsola()
        self.ventanaa_reglas = VentanaReglas()
        self.ventana_estadisticas = VentanaEstadisticas()
        self.ventana_ecuacion = VentanaEcuacion()

    def configurar_conexion_botones(self):
        self.iniciar_nuevo_juego.clicked.connect(self.abrir_ventana_ecuacion)
        self.mostrar_estadisticas.clicked.connect(self.abrir_ventana_estadistica)
        self.mostrar_reglas.clicked.connect(self.abrir_ventana_reglas)
        self.salir.clicked.connect(self.salir_de_juego)

    def abrir_ventana_reglas(self):
        self.ventanaa_reglas.exec()
        self.ventanaa_reglas.mostrar_reglas()

    def abrir_ventana_ecuacion(self):
        self.ventana_ecuacion.exec()

    def abrir_ventana_estadistica(self):
        self.ventana_estadisticas.exec()

    def salir_de_juego(self):
        self.close()


class VentanaReglas(QDialog):
    def __init__(self):
        super().__init__()
        self.reglas = None
        uic.loadUi("gui/Reglas.ui", self)
        self.mostrar_reglas()

    def mostrar_reglas(self):
        self.Reglas.setText(
            "Resuelve la ecuación en seis intentos\n"
            "- Componen la ecuación: números (0-9), operaciones básicas y el signo igual.\n"
            "- Tienes 6 intentos para colocarlos y llegar al resultado correcto.\n"
            "- Los colores indican lo siguiente:\n"
            "  1. Verde correcta\n"
            "  2. Amarillo existe pero está en la posición incorrecta\n"
            "  3. Rojo no pertenece a la ecuación.\n"
            "- Sigue el orden de operaciones y permite conmutabilidad en el resultado.\n"
            "- El objetivo es resolverla en el menor número de intentos posible.\n\n"
            "¡Buena suerte!\n")


class VentanaEstadisticas(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/Estadistica.ui", self)
        self.nerdle = Nerdle('')
        self.cargar_base_datos()
        self.__config()

    def __config(self):
        txt_estadisticas = ""
        for indice, valores in enumerate(self.nerdle.estadisticas, start=0):
            if valores != '':
                txt_estadisticas += f"Partidas ganadas en {indice + 1} intento: {valores}\n"
        self.Estadisticas.setText(txt_estadisticas)
        self.btn_Enviar.clicked.connect(self.enviar_email)

    def enviar_email(self):
        try:
            email = self.lbl_email.toPlainText()
            self.nerdle.send_email(email)
            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setWindowTitle('Email enviado exitosamente')
            message.setText('¡Enviamos satisfactoriamente tus estadísticas!')
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
        except:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle('ERROR :(')
            error_message.setText('No pudimos enviar tus estadísticas, vuelva a intentarlo')
            error_message.setStandardButtons(QMessageBox.Ok)
            error_message.exec_()


    def cargar_base_datos(self):
        with open("requirements/Estadísticas.txt", 'r', encoding='utf-8') as file:
            valores = (file.readline()).split(',')
        for i in range(0, 6):
            self.nerdle.estadisticas[i] = int(valores[i])


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
        self.buttons = []
        uic.loadUi("gui/Ecuacion2.ui", self)
        self.setFixedSize(self.size())
        self.__config()

    def __config(self):
        self.oKButton.clicked.connect(self.guardar_ecuacion)
        self.comparar_ecuaciones(self.nerdle.usuario.ecuacion)
        self.ecuacion.generar_ecuacion()
        # self.layouts = [self.Ecuacion1, self.Ecuacion2, self.Ecuacion3, self.Ecuacion4, self.Ecuacion5, self.Ecuacion6]
        self.buttons = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9,
                        self.btn_10, self.btn_11, self.btn_12, self.btn_13, self.btn_14, self.btn_15, self.btn_16,
                        self.btn_17, self.btn_18, self.btn_19, self.btn_20, self.btn_21, self.btn_22, self.btn_23,
                        self.btn_24, self.btn_25, self.btn_26, self.btn_27, self.btn_28, self.btn_29, self.btn_30,
                        self.btn_31, self.btn_32, self.btn_33, self.btn_34, self.btn_35, self.btn_36, self.btn_37,
                        self.btn_38, self.btn_39, self.btn_40, self.btn_41, self.btn_42, self.btn_43, self.btn_44,
                        self.btn_45, self.btn_46, self.btn_47, self.btn_48]
        print(self.consola.ecuacion_generada)

    def guardar_ecuacion(self):
        self.nerdle.usuario.ecuacion = self.txt_ecuacion.toPlainText()
        self.ecuaciones.append(self.nerdle.usuario.ecuacion)
        self.llamar_comparacion()

    def llamar_comparacion(self):
        self.comparar_ecuaciones(self.nerdle.usuario.ecuacion)
        print(self.comparar_ecuaciones)
        #self.actualizar_layouts()

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
                #print(f"ESTÁS EN EL INTENTO {self.intentos} DE 6")
                # self.nerdle = Nerdle(ecuacion_usuario=ecuacion)
                self.consola.lista_de_intentos = self.comparar_ecuaciones(self.nerdle.usuario.ecuacion)
                self.colorear_ecuacion(self.consola.lista_de_intentos, self.nerdle.usuario.ecuacion)
                self.solicitar_ecuacion()
        else:
            #print("PERDISTE")
            self.nerdle.contador_partidas_perdidas += 1

    def comparar_ecuaciones(self, ecuacion_usuario: str) -> Union[bool, list[str]]:
        if self.consola.ecuacion_generada == ecuacion_usuario:
            win_message = QMessageBox()
            win_message.setIcon(QMessageBox.Information)
            win_message.setWindowTitle('GANASTE!')
            win_message.setText('FELICIDADES, GANASTE!!')
            win_message.setStandardButtons(QMessageBox.Ok)
            win_message.exec_()

            self.nerdle.estadisticas[self.intentos - 1] += 1
            self.nerdle.contador_partidas_ganadas += 1
            self.close()
        else:
            resultado: list[str] = ['0'] * 8
            for n in range(0, 8):
                if len(self.nerdle.usuario.ecuacion) > 8:
                    if self.consola.ecuacion_generada[n] == ecuacion_usuario[n]:
                        resultado[n] = '2'  # si es igual
                    else:
                        if self.consola.ecuacion_generada[n] != ecuacion_usuario[n]:
                            if ecuacion_usuario[n] in self.consola.ecuacion_generada:
                                resultado[n] = '1'

            return resultado

    def actualizar_layouts(self):
        self.layouts[self.intentos].setText(f"{self.nerdle.usuario.ecuacion}")

        if self.intentos == 5:
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Advertencia')
            mensaje.setText('INTENTOS SUPERADOS, PERDISTE EL JUEGO')
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.exec_()
        else:
            self.intentos += 1







