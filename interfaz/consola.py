class UIConsola:
    @staticmethod
    def imprimir_reglas():

        print("Nerdle:\n\n"
              "------------------------------------------------------------------------------\n"
              "Resuelve la ecuación en seis intentos\n"
              "- Componen la ecuación: números (0-9), operaciones básicas y el signo igual.\n"
              "- Tienes 6 intentos para colocarlos y llegar al resultado correcto.\n"
              f"- Los colores indican lo siguiente:\n"
              f"  1. {color_verde}Verde{color_reset} correcta\n"
              f"  2. {color_amarillo} Amarillo {color_reset} existe pero está en la posición incorrecta\n"
              f"  3. {color_rojo} Rojo {color_reset} no pertenece a la ecuación.\n"
              "- Sigue el orden de operaciones y permite conmutabilidad en el resultado.\n"
              "- El objetivo es resolverla en el menor número de intentos posible.\n\n"
              "¡Buena suerte!\n"
              "_______________________________________________________________________________")




