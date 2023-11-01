import random
from typing import ClassVar, Optional, Union
import smtplib
from email.message import EmailMessage

NUMEROS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
OPERADORES = ['+', '-', '/', '*']

 # 20 * 3 = 60
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
                opr_alea = OPERADORES[random.randint(0, len(OPERADORES) - 1)]
                self.ecuacion_alea += opr_alea

            indice_ecuacion = len(self.ecuacion_alea) - 1

            if (len(self.ecuacion_alea) == 0) or (self.ecuacion_alea[indice_ecuacion] in OPERADORES):
                num_alea = NUMEROS[random.randint(1, len(NUMEROS) - 1)]

            else:
                num_alea = NUMEROS[random.randint(0, len(NUMEROS) - 1)]

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

        print(self.ecuacion_alea)

        return self.ecuacion_alea



class Jugador:
    def __init__(self, ecuacion: str):
        self.ecuacion: str = ecuacion



class Nerdle:
    def __init__(self, ecuacion_usuario: str):
        self.message = EmailMessage()
        self.receiver_email: Optional[str] = None
        self.ecuacion: Ecuacion = Ecuacion()
        self.usuario: Jugador = Jugador(ecuacion_usuario)
        self.contador_partidas_ganadas: int = 0
        self.contador_partidas_perdidas: int = 0
        self.estadisticas = [0, 0, 0, 0, 0, 0]


    def contador_de_intentos(self, contador_intentos: int) -> int:
        if contador_intentos < 7:
            contador_intentos += 1
            return contador_intentos

        else:
            return -1
    def iniciar_nuevo_juego(self):
        return self.ecuacion.generar_ecuacion()

    def send_email(self, receiver_email):
        # Creando objeto email message
        self.message = EmailMessage()
        email_subject = "Tus estadísticas de Nerdle App ya están aquí!"
        sender_email_address = "pysenderemailspython@gmail.com"
        email_password = "ryhz rcso bypn jelw"
        receiver_email_address = f"{receiver_email}"

        # Configurando los encabezados del email
        self.message['Subject'] = email_subject
        self.message['From'] = sender_email_address
        self.message['To'] = receiver_email_address

        # Setteando el contenido del email
        self.message.set_content(f"ESTADÍSTICAS:\n\n"
                                 f"Partidas ganadas en 1 intento: {self.estadisticas[0]}\n"
                                 f"Partidas ganadas en 2 intento: {self.estadisticas[1]}\n"
                                 f"Partidas ganadas en 3 intento: {self.estadisticas[2]}\n"
                                 f"Partidas ganadas en 4 intento: {self.estadisticas[3]}\n"
                                 f"Partidas ganadas en 5 intento: {self.estadisticas[4]}\n"
                                 f"Partidas ganadas en 6 intento: {self.estadisticas[5]}"
                                 f"\n\nGRACIAS POR JUGAR NERDLE APP!")

        # Setteando el servidor y puerto
        email_smtp = "smtp.gmail.com"
        server = smtplib.SMTP(email_smtp, 587)

        # indentificar el cliente para el servidor SMTP
        server.ehlo()

        # Estableciendo una conexión segura con SMTP
        server.starttls()

        # Login de la cuenta
        server.login(sender_email_address, email_password)

        # Enviando mensaje
        server.send_message(self.message)

        #Cerrando coneccion con el servidor
        server.quit()
