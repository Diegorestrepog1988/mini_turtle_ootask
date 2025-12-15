# mini_turtle_ootask

Descripción del Proyecto
Este proyecto es una implementación simple de una simulación de tortuga en Python utilizando programación orientada a objetos (POO). El objetivo es demostrar conceptos básicos de POO como clases, objetos, encapsulamiento y métodos.

Funcionalidades
Clase Tortuga: Representa una tortuga que puede moverse en una línea horizontal.
Método avanzar: Permite a la tortuga avanzar un número determinado de pasos, actualizando su posición y dibujando su representación gráfica en la consola.
Encapsulamiento: La posición de la tortuga se mantiene como un atributo privado dentro de la clase.
Código de la Clase Tortuga
class Tortuga:
    
    def __init__(self):
        # El único atributo de estado necesario para el dibujo de escalera
        self.paso_actual = 0  
        
    # --- Método: Dibuja la parte Horizontal del Escalón (Adelante) ---
    
    def adelante(self, n):
        # La sangría se calcula con el valor fijo 5
        espaciosIzquierda = " " * 5 * self.paso_actual
        
        # Imprime el segmento horizontal
        print(espaciosIzquierda + "-" * n + ">")

    # --- Método: Dibuja la parte Vertical y aumenta la Sangría (Abajo) ---
    
    def abajo(self, n):
        # La sangría se calcula con el valor fijo 5
        espaciosIzquierda = " " * 5 * self.paso_actual
        
        # El patrón vertical usa el valor fijo 5
        patron_vertical = espaciosIzquierda + (" " * 5 + "|\n")
        
        # Imprime la bajada y el marcador 'V'
        print(patron_vertical * n + (espaciosIzquierda + " " * 5 + "V"))
        
        # Incrementa el estado del dibujo para el siguiente escalón
        self.paso_actual += 1 

    # --- Método: Reinicia el Contador ---

    def reiniciar(self):
        self.paso_actual = 0
Estructura del Proyecto
mini_turtle__oo_taks/
├── main.py                    # Script principal que demuestra el uso de la clase Tortuga
├── README.md                  # Este archivo de documentación
├── LICENSE                    # Licencia del proyecto
└── mini_turtle_oo/            # Paquete Python
    ├── __init__.py            # Inicialización del paquete
    ├── turtle_class.py        # Definición de la clase Tortuga
    └── __pycache__/           # Archivos compilados de Python (generados automáticamente)
Instalación y Uso
Requisitos: Python 3.x instalado en el sistema.

Ejecución:

Navega al directorio del proyecto.
Ejecuta el script principal: python main.py
Ejemplo de Salida
Al ejecutar main.py, verás una simulación donde dos tortugas dibujan escaleras en la consola, con segmentos horizontales (---->) y verticales (|) terminando en V.

Ejemplo:

--- Escalera de T1 con adelante/abajo ---
---->
     |
     |
     |
     V
     ---->
          |
          |
          |
          V

--- Escalera de T2 con adelante/abajo ------
---->
     |
     |
     |
     V
     ---->
          |
          |
          |
          V

--- Reiniciando T1 ---
---->
     |
     |
     |
     V

--- reiniciar ---
---->
     |
     |
     |
     V
Conceptos de POO Demostrados
Clase: Tortuga define el blueprint para crear objetos tortuga.
Objeto: Instancias como t1 y t2 son objetos creados a partir de la clase.
Método: avanzar(pasos) es un método que modifica el estado del objeto.
Atributo: posicion_x es un atributo que almacena el estado interno.
Encapsulamiento: El atributo posicion_x no se accede directamente desde fuera de la clase.
Contribución
Si deseas contribuir, por favor crea un fork del repositorio y envía un pull request con tus mejoras.
