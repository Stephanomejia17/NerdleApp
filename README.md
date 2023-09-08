# Descripción Nerdle
Nerdle es un juego de secuencias matemáticas en el que el jugador debe adivinar, en un número
limitado de intentos, una secuencia matemática que consta de números entre 0 y 9, operaciones
matemáticas básicas y el signo de igualdad. El juego proporciona retroalimentación después de
cada intento, lo que permite al jugador deducir la secuencia correcta.
Reglas del juego:
1. Secuencia Objetivo: En cada ronda, el juego selecciona cuidadosamente una secuencia de 8
elementos. Estos elementos pueden ser números del 0 al 9, operaciones matemáticas (+, -, *,
/) y el signo de igualdad (=).
2. Intentos Limitados: El jugador tiene un número máximo de intentos para adivinar la secuencia
de 8 elementos correcta. Generalmente se asigna un máximo de 6 intentos, pero este número
puede variar según la implementación del juego.
3. Adivinanzas: En cada intento, el jugador propone una secuencia de 8 elementos que cree que
coincide con la secuencia objetivo. Por ejemplo, una adivinanza podría ser "3 + 7 * 2 = 17".
4. Retroalimentación: Después de cada intento, el juego proporciona retroalimentación precisa
en tres categorías:
• Elemento correcto en la posición correcta: Indica cuántos elementos están en la
secuencia y en la posición correcta (marcadas en verde).
• Elemento correcto en la posición incorrecta: Muestra cuántos elementos están en la
secuencia, pero en la posición incorrecta (marcadas en amarillo).
• Elemento incorrecto: Informa cuántos elementos no están en la secuencia objetivo
(marcadas en gris).
5. Intentos restantes: El juego muestra el número de intentos restantes para motivar al jugador a
adivinar la secuencia antes de agotar los intentos disponibles.
6. Victoria o derrota: El jugador gana el juego si adivina la secuencia oculta dentro de los intentos
asignados. En caso contrario, si se agotan todos los intentos sin adivinar correctamente la
secuencia, se considera una derrota. En este último caso, el juego muestra cual era la
secuencia correcta.
Al finalizar, el jugador tiene la opción de iniciar un nuevo juego.
En cualquier momento, el jugador podrá ver las instrucciones del juego. Además, también deberá
tener la opción de ver las estadísticas del juego donde se le mostrará un gráfico con la distribución
de sus los intentos en cada juego realizado. El gráfico se debe poder enviar por correo electrónico.