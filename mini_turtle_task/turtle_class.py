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
