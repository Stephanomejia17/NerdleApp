class UIConsola:
    def __init__(self):
        self.nerdle: Optional[Nerdle] = None
        self.opciones = {
            "1": self.iniciar_nuevo_juego,
            "2": self.mostrar_reglas,
            "3": self.mostrar_estadisticas,
            "4": self.salir
        }
    @staticmethod
    def mostrar_menu():
        titulo = " Nerdle "
        print(f"\n{titulo:_^30}")
        print("1. Iniciar nuevo juego")
        print("2. Mostrar reglas")
        print("3. Mostrar estadisticas")
        print("4. Salir")
        print(f"{'_':_^30}")
    mostrar_menu()
