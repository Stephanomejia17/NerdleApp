import random

class Nerdle:
    contador: int = 0

    def contador_de_juegos(self):
        pass



    def numero_de_aciertos(self):
        pass


    def numero_de_desaciertos(self):
        pass

class Jugador:
    pass

class Ecuacion:

    def comparar_ecuaciones(self, ecuacion_usuario: str) -> list:
        resultado = ['0'] * 8
        for n in range(0, 8):
            if self.ecuacion[n] == ecuacion_usuario[n]:
                resultado[n] = '2' # si es igual
        for n in range(0, 8):
            if self.ecuacion[n] != ecuacion_usuario[n]:
                for m in range(0, 8):
                    if (m != n) and (self.ecuaciones[n] == ecuacion_usuario[m]) and (resultado[m] == '0'):
                        resultado[m] = '1'
                        break
        return resultado
    pass




