# main.py

# 1. Importa la función específica desde tu otro fichero
from is_even import is_even

# 2. Ahora puedes usar la función como si estuviera definida aquí
numero_usuario = 101

if is_even(numero_usuario):
    print(f"El número {numero_usuario} es PAR.")
else:
    print(f"El número {numero_usuario} es IMPAR.")

# Probemos con otro número
print(f"¿Es 20 par? {is_even(20)}")
