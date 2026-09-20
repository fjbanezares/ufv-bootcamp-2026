def is_even(number: int) -> bool:
    """
    return true if the input integer is even
    Explanation: Lets take a look at the following decimal to binary conversions
    2 => 10
    14 => 1110
    100 => 1100100
    3 => 11
    13 => 1101
    101 => 1100101
    from the above examples we can observe that
    for all the odd integers there is always 1 set bit at the end
    also, 1 in binary can be represented as 001, 00001, or 0000001
    so for any odd integer n => n&1 is always equals 1 else the integer is even

    >>> is_even(1)
    False
    >>> is_even(4)
    True
    >>> is_even(9)
    False
    >>> is_even(15)
    False
    >>> is_even(40)
    True
    >>> is_even(100)
    True
    >>> is_even(101)
    False
    """

    # La operación & 1 (AND binario con 1) aísla ese último bit.
    return number & 1 == 0


# Ejecuta el siguiente bloque de código solo si este fichero(is_even.py) se está ejecutando directamente desde la terminal (ej: python is_even.py)".
# Si este fichero es importado por otro script(ej: import is_even), este bloque de código no se ejecutará.
# Esto es lo que permite que el fichero sirva como una biblioteca reutilizable y como un script ejecutable.

if __name__ == "__main__":
    import doctest

# Este comando le dice al módulo doctest: "Busca en todo este fichero (.testmod()) cualquier docstring, encuentra todos los ejemplos >>> que contenga y ejecútalos como pruebas".
    doctest.testmod()


# Los >> >): Estos son los doctests. Son ejemplos de uso que también funcionan como pruebas automáticas.
#     >> > is_even(1) es el código que se ejecutará.
#     False (en la línea siguiente) es el resultado esperado.
