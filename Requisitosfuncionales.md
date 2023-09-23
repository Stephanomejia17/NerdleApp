## NERDLE: Requisitos Funcionales

### R1 - Iniciar Juego

**Resumen:** El sistema debe ser iniciado.

**Entradas:**
- El usuario ingresa al juego

**Resultado:**
1. El sistema genera la operación que el jugador debe adivinar.
2. El sistema muestra un tablero de 6 x 8 para el juego.

| Pasos           | Métodos                     | Responsable |
|-----------------|-----------------------------|-------------|
| Iniciar juego   | `iniciar_nuevo_juego()`    | Nerdle      |
| Crear ecuación  | `generar_ecuacion()`       | Ecuación    |

### R2 – Hacer Jugada

**Resumen:** El jugador ingresa la ecuación a adivinar y el sistema la verifica. Si el jugador adivina la ecuación generada por el sistema, gana; de lo contrario, continúa jugando durante los próximos 6 turnos para intentar ganar.

**Entradas:**
- El jugador ingresa la ecuación.

**Resultado:**
1. El jugador ingresa la ecuación.
2. Se verifica si el usuario ingresó "2"; de ser así, se llama a R5.
3. Se verifica si la ecuación ingresada es lógica.
4. Se inicia el conteo de intentos hasta un máximo de 6; en caso de superar el número máximo de intentos, se llama a R3.
5. Si la ecuación ingresada es la misma generada por el sistema, se llama a R3.
6. Si la ecuación ingresada no es la misma que la generada por el sistema, se verifica que el jugador no haya alcanzado el número máximo de intentos y se realiza la siguiente revisión:
   - a) Los elementos que se encuentran en la posición correcta se marcan en verde.
   - b) Los elementos en la posición incorrecta pero pertenecientes a la ecuación se marcan en amarillo.
   - c) Los elementos que no pertenecen a la ecuación se marcan en gris.
7. Se llama a R2 para continuar el juego.

| Pasos                                      | Métodos                                             | Responsable  |
|--------------------------------------------|-----------------------------------------------------|--------------|
| Se ingresa ecuación y verifica si es lógica | `solicitar_ecuacion()`                              | UIConsola    |
| Conteo de intentos                          | `contador_de_intentos(contador_intentos: int)`      | Nerdle       |
| Ingresa y verifica la ecuación             | `comparar_ecuaciones(ecuacion_usuario: str)`        | UIConsola    |

### R3 – Finalizar Juego

**Resumen:** Las estadísticas se actualizan y se llama al menú.

**Entradas:**
- N/A

**Resultado:**
1. Guarda las estadísticas de la partida.
2. Se llama a R4.

| Pasos                               | Métodos                           | Responsable |
|-------------------------------------|-----------------------------------|-------------|
| Guardar estadística                | `guardar_estadisticas()`         | UIConsola   |
| Terminar partida y cerrar juego     | `salir()`                         | UIConsola   |

### R4 – Seleccionar Opciones del Menú

**Resumen:** El jugador podrá seleccionar alguna opción presentada en el menú.

**Entradas:**
- Selección del usuario.

**Resultado:**
1. Se carga el archivo de estadísticas de juegos pasados.
2. Se muestra el menú con las opciones.
3. Si el jugador selecciona la opción "Estadísticas", se llama a R6.
4. Si el jugador selecciona la opción para ver las reglas, se llama a R5.
5. Si el jugador selecciona la opción de continuar jugando, se llama a R1.

| Pasos                           | Métodos                    | Responsable |
|---------------------------------|----------------------------|-------------|
| Cargar estadística              | `cargar_estadistica()`     | UIConsola   |
| Mostrar menú con opciones       | `mostrar_menu()`           | UIConsola   |

### R5 – Ver Reglas

**Resumen:** Si el usuario ingresó "2" (R2) o seleccionó la opción en el menú (R4), se imprimirán las reglas del juego.

**Entradas:**
- N/A

**Resultado:**
1. Se imprimen las reglas de juego.
2. Se llama a R2.

| Pasos                  | Métodos                   | Responsable |
|------------------------|---------------------------|-------------|
| Mostrar reglas         | `imprimir_reglas()`       | UIConsola   |

### R6 – Ver Estadística

**Resumen:** El jugador visualizará su estadística.

**Entradas:**
- N/A

**Resultado:**
1. Se muestra:
   1.1. Juegos totales
   1.2. Número de aciertos:
        - Cantidad de aciertos por número de intentos.
   1.3. Número de desaciertos.

| Pasos                  | Métodos                      | Responsable |
|------------------------|------------------------------|-------------|
| Mostrar estadística    | `mostrar_estadisticas()`    | UIConsola   |

