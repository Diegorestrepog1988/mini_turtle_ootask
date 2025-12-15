# Suponiendo que __init__.py expone la clase:
from mini_turtle_oo.turtle_class import Tortuga 

# Crea dos tortugas dibujantes independientes
t1 = Tortuga()
t2 = Tortuga()

print("--- Escalera de T1 con adelante/abajo ---")
t1.adelante(4)
t1.abajo(3)
t1.adelante(4)
t1.abajo(3)

print("\n--- Escalera de T2 con adelante/abajo ------")
t2.adelante(4)
t2.abajo(3)
t2.adelante(4)
t2.abajo(3)

print("\n--- Reiniciando T1 ---")
t1.reiniciar()
t1.adelante(4)
t1.abajo(3)
print("\n--- reiniciar ---")
t2.reiniciar()
t2.adelante(4)
t2.abajo(3)
