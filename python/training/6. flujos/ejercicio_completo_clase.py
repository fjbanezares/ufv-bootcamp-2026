# Clase Perro: Permite la creación de un perro con nombre, peso y altura.
# Si el peso del perro es mayor que el peso ideal + 111, creamos un perro especial "Entrenador".
# Se utilizan los métodos __new__, __init__, __str__ y __add__ para manejar la creación, inicialización, y presentación del objeto.

class Perro:
    peso_ideal = 20  # Peso ideal en kg para los perros. Valor compartido por toda la clase.

    def __new__(cls, name, peso, height):
        """
        Método __new__ para la creación del objeto.
        Si el peso del perro es mayor que el peso ideal + 111, creamos un perro especial "Entrenador".
        """
        if peso > cls.peso_ideal + 111:  # Condición para crear el "Entrenador"
            print(f"Creando un entrenador especial debido al sobrepeso extremo de {name}.")
            # Creamos una nueva instancia del perro y usamos 'Entrenador' como nombre temporal
            instance = super(Perro, cls).__new__(cls)
            instance.es_entrenador = True  # Marcamos que esta instancia es un "Entrenador"
            return instance  # Devolvemos la instancia de "Entrenador"
        else:
            # Si no tiene sobrepeso extremo, se crea un perro normal
            instance = super(Perro, cls).__new__(cls)
            instance.es_entrenador = False  # No es entrenador
            return instance


    def __init__(self, name, peso, height):
        """
        Método __init__ para inicializar los atributos del perro.
        Si el perro es "Entrenador", usamos el peso ideal pero conservamos el nombre original.
        """
        if self.es_entrenador:
            # Si es un entrenador, usamos el peso ideal pero mantenemos el nombre que pasamos
            self.name = "Entrenador"  # Asignamos "Entrenador" como nombre visible
            self.peso = Perro.peso_ideal  # Peso ideal para el entrenador
            self.height = height  # Conservamos la altura original
            self.nombre_original = name  # Guardamos el nombre original (Firulais, por ejemplo)
        else:
            # Si es un perro normal, inicializamos los valores pasados
            self.name = name
            self.peso = peso
            self.height = height

    def ladrar(self):
        """
        Método que permite que el perro ladre mostrando su nombre.
        """
        print(f"{self.name} dice: ¡Guau guau!")

    def evaluar_sobrepeso(self):
        """
        Evalúa si el perro tiene sobrepeso comparando su peso con el peso ideal de la clase.
        """
        if self.peso > Perro.peso_ideal:
            print(f"{self.name} tiene sobrepeso, ¡A entrenar!")  # Si tiene sobrepeso
        else:
            print(f"{self.name} está en forma, ¡Bien hecho!")  # Si está en forma

    def __add__(self, val2):
        """
        Permite sumar dos perros combinando sus pesos.
        Devuelve un nuevo perro con el mismo nombre y altura del primer perro, pero con la suma de sus pesos.
        """
        return Perro(self.name, self.peso + val2.peso, self.height)

    # def __str__(self):
    #     """
    #     Método especial __str__ que devuelve una representación en forma de cadena de un objeto Perro.
    #     Esto es útil cuando queremos imprimir información del perro o ver el resultado de una suma de perros.
    #     """
    #     return f"Perro: {self.name}, Peso: {self.peso} kg, Altura: {self.height} cm"

    def __bool__(self):
        """
        Devuelve True si el perro está en forma (peso menor o igual al ideal)
        y False si tiene sobrepeso.
        """
        return self.peso <= Perro.peso_ideal


# Ejemplo de uso:

# Firulais tiene un peso muy superior al ideal, se debería crear un entrenador

perro1 = Perro("Firulais", 150, 25)  
print(perro1)
# Max está en forma, así que se crea normalmente
perro2 = Perro("Max", 18, 18)

# En este caso, Firulais será reemplazado por un entrenador
perro1.ladrar()  # El entrenador ladra

# Evaluamos si Firulais (o el entrenador) tiene sobrepeso
perro1.evaluar_sobrepeso()

# Max ladra
perro2.ladrar()

# Evaluamos si Max tiene sobrepeso (debería estar en forma)
perro2.evaluar_sobrepeso()

# Verificamos si Max está en forma utilizando el método __bool__
if perro2:
    print(f"{perro2.name} está en buena forma.")
else:
    print(f"{perro2.name} tiene sobrepeso.")

# Verificamos si el entrenador (Firulais reemplazado) está en forma
if perro1:
    print(f"{perro1.name} está en buena forma.")  # El entrenador siempre está en forma
else:
    print(f"{perro1.name} tiene sobrepeso.")  # No debería pasar, ya que el entrenador tiene el peso ideal

# Ahora mostramos la suma de dos perros con el método __add__ y el uso de __str__ para visualizar el resultado
nuevo_perro = perro1 + perro2  # Sumamos los pesos de Firulais (entrenador) y Max
print(nuevo_perro)  # Gracias al método __str__, mostramos el resultado de la suma


if hasattr(perro1, 'nombre_original'):
    print(f"El nombre original de {perro1.name} es: {perro1.nombre_original}")
else:
    print(f"El nombre de {perro1.name} es: {perro1.name}")

# Para el segundo perro, no es entrenador, así que simplemente mostramos su nombre
print(f"El nombre de {perro2.name} es: {perro2.name}")


# Explota? ---> AttributeError: 'Perro' object has no attribute 'nombre_original'
print(f"El nombre original de {perro2.name} es: {perro2.nombre_original}")


''' If __new__ detects a weight that exceeds a threshold, 
it can return a special object (like a "Trainer") 
instead of the standard dog object.'''
