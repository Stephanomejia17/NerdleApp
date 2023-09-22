# Crear el tablero con dimensiones 6x8
tablero = [[' ' for _ in range(8)] for _ in range(6)]

# Imprimir el tablero
for fila in tablero:
    print('|'.join(fila))
    print('-' * 17)
