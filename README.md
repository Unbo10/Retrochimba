# Retrochimba
1. Integrantes:
   
		- Juan Esteban Huertas Serrano

		- Juan Pablo Ospina Santos

		- Samuel David Luna Salazar

		- Santiago Rocha Pachón

2. Lenguaje de programación
   
		Python

3. Nombre del proyecto
   
		Retrochimba
4. ¿En qué consiste?

Se propone en una aplicación que emule una consola retro en la cual se van a poder elegir 4 diferentes juegos:

		Tetris
En esta opción se va a poder acceder al clásico juego “Tetris” pero esta no va a ser la parte principal de este segmento del proyecto sino que el juego se usaría para una especie de base de datos que se base en la temática del juego, ya que la opción permitiría sacar un promedio del puntaje de las partidas jugadas por el usuario, comparar sus mejores puntajes con los records del mundo de diferentes años, leer datos curiosos del juego, que el usuario pueda ver si su rendimiento mejora o hasta comentarios graciosos relacionados con el juego y otras funciones encaminadas a usar los conceptos de listas, funciones, condicionales e.t.c vistos en clase.

Para esta parte del proyecto se usaría como se mencionó anteriormente, los conceptos y herramientas de Python vistas en clase, específicamente, listas, librerías, condicionales y funciones. Aparte de eso, se utilizarán diferentes librerías (como Pygame) orientadas a juegos que permitirán el desarrollo del juego.

		Conecta 4
Se propone hacer un juego, multijugador local, conocido como Conecta 4 en el que dos jugadores intentarán conectar 4 puntos de su color en la misma línea o diagonal, para así logré la victoria, este será programado gráficamente con Pygame, herramienta con la que se traducirá la decisión del jugador (detectará el cursor para así escoger dónde quedará cada pieza o el teclado) y se diseñará la interfaz física. También usará una matriz, para así almacenar los datos de cada jugada y analizará estás matrices cada turno para detectar si hay alguna victoria de el jugador. Se harán dos métodos de detección de victoria: una a partir de álgebra modular y otra basándose en lectura de matrices con ciclos.

Cada jugador podrá escoger tanto color, forma y como quiere ver el tablero. También se implementará un modo a tres jugadores en el que se ampliará el tablero y ropuest arriesgada (un modo para un solo jugar contra un bot con diferentes dificultades).

		Galaga
Se propone hacer un juego parecido al conocido en la época antigua llamado galaga. Este juego va a consistir en una nave que tiene que superar obstáculos o destruirlos. Estos van a ir cayendo con el tiempo. A medida que el jugador va aumentando de puntuación la dificultad va a ser mayor. Se pretende que sea un ambiente espacial, para dar al jugador una experiencia agradable.

Habría que utilizar Pygame para la visualización de los obstáculos, su comportamiento y la acción que estos tengan sobre la nave del jugador; listas para el registro de las puntutaciones pasadas y la actual, funciones para interpretar el input de teclado y/o mouse del jugador, condicionales para el funcionamiento del juego, y librerías que ayudarán con los cálculos matemáticos de la física o matemática utilizada para los movimientos de los obstáculos.

		Formula 1 2D
Juego inspirado en la Fórmula 1 que consistirá esencialmente en una vista 2D de un carro recorriendo diferentes pistas (3 idealmente). Se buscará imitar lo más cercano a la realidad la aceleración y desaceleración de un Fórmula 1, haciendo especial hincapié en la necesidad de la aplicación del freno y la regulación del acelerador para no salirse de la pista, parámetros que variarían según las ruedas (compuestos blandos, medios o duros) y la fuerza aerodinámica de la configuración (alta, media o baja). Si ello sucede, el usuario será devuelto al centro de la pista con velocidad 0, haciendo que pierda tiempo. El objetivo último del juego es superar el mejor tiempo de la pista, llevando en consecuencia registros de los intentos del jugador. Adicionalmente, podría pensarse en hacerlo multijugador de modo que los jugadores compitan por llegar primero (habría entonces que añadirle una funcionalidad para que, en caso de colisiones o salidas de la pista, el jugador rezagado sea restablecido a una velocidad similar al jugador líder para mantener el nivel de zoom en la pista, a menos que se cree una pantalla dividida).

Los conceptos a utilizar serán las listas (para almacenar los tiempos de los jugadores, tanto por sectores como total y por un número n de vueltas, y las características del carro), funciones (para las acciones del usuario, sensibilidad en la aceleración y el freno del carro de acuerdo al carro escogido, y la aplicación de reglas como penalizaciones de tiempo y banderas amarillas), condicionales (para controlar las salidas de la pista y los rezagos si se hace multijugador), y librerías (como math). Se tendrá que buscar información acerca de librerías de física y matemáticas (para las curvas de la pista y el cálculo de la trayectoria central), Pymath de nuevo para la interfaz y la funcionalidad del juego, ciertos conceptos avanzados de fuerzas aerodinámicas, estadísticas sobre cada uno de los compuestos de ruedas en cada uno de los circuitos, y controladores condicionales que limiten al usuario en ocasiones de bandera amarilla, penalizaciones, etc.
