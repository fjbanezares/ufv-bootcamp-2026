
# ==============================================================================
# ALUMNO: Guillermo López-Quiroga Lizarraga
# REFLEXION DE SCOPES:
#
# Los niveles 1, 2 y 3 tienen su propia variable local x, mientras que el Limbo utiliza la variable global x.
# Python busca las variables siguiendo la regla LEGB.
#
# Al utilizar 'global x' dentro del Limbo, podemos modificar la variable
# de la realidad, aunque estemos dentro de varias funciones anidadas.
#
# Por otro lado, 'nonlocal' permite modificar una variable que pertenece
# a una funcion exterior, sin tener que cambiar una variable global.
#
# En este codigo, 'nonlocal_real_world_x' es solo un nombre de variable,
# no una instruccion 'nonlocal'.
#
# Considero que abusar de 'global' puede provocar errores dificiles de
# detectar, porque una funcion puede modificar datos utilizados por otras.
# Por eso, es preferible controlar donde se modifican las variables.
# ==============================================================================


# ALUMNO: Alejandro Arias Sanjuán

# REFLEXIÓN:
# En este programa hay varias funciones dentro de otras, y cada una tiene su propia variable x,
# que representa un nivel diferente de sueño.
# Al utilizar global x dentro de limbo(), podemos modificar la variable x del mundo real, aunque estemos dentro de varias
# funciones.
# Por otro lado, nonlocal permite modificar una variable de una función exterior que contiene a la función actual, 
# sin modificar la variable global.
# Utilizar muchas variables globales puede provocar errores, porque una función puede cambiar valores que también
# utilizan otras funciones.


x = "Real World"  # This is the global variable

def dream_level_1():
    x = "Dream Level 1: Paris"  # local variable to dream_level_1

    def dream_level_2():
        x = "Dream Level 2: Hotel"  # local variable to dream_level_2

        def dream_level_3():
            x = "Dream Level 3: Snow Fortress"  # local variable to dream_level_3

            # ==============================================================================
            # ALUMNO: Elba Pérez de Cortabitarte 
            # REFLEXIÓN DE SCOPES:
            # Hola profe. En este ejemplo, 'global' permite cambiar la variable x que se definió
            # al principio del programa, aunque estemos dentro de varias funciones.
            # Es como si desde el último nivel del sueño pudiéramos modificar
            # directamente lo que ocurre en la realidad.
            # En cambio, 'nonlocal' sirve para modificar una variable de una función
            # superior, sin llegar a cambiar la variable global.
            # Esto me ayuda a entender por qué es importante saber dónde se define
            # una variable y qué partes del programa pueden modificarla.
            # ==============================================================================

            
            # ============================================================
            # ALUMNA: Nirvana Falcón Puebla
            # REFLEXIÓN DE SCOPES:
            # 'global x' permite acceder a la variable x definida en el
            # ámbito global y modificar la realidad exterior desde limbo.
            # 'nonlocal' permite modificar una variable de una función
            # envolvente, sin cambiar la variable global.
            # En este ejemplo, nonlocal x dentro de limbo permitiría
            # modificar la x de dream_level_3, mientras que global x
            # modifica la x global. Son ámbitos distintos.
            # En producción, abusar de global puede generar efectos
            # secundarios difíciles de detectar y mantener.
            # ============================================================


            # ======================================================================
            # ALUMNO: Ignacio Camarena Gómez
            # REFLEXIÓN DE SCOPES:
            # En limbo(), `global x` hace que la lectura y la asignación de x
            # apunten a la variable del módulo, saltándose los x locales de los
            # niveles anteriores. Por eso, al despertar, la realidad queda alterada.
            # La asignación `nonlocal_real_world_x = x` de este ejemplo no usa la
            # palabra clave `nonlocal`: crea otra variable local y no modifica el x
            # de Snow Fortress. Con `nonlocal`, una función anidada puede modificar
            # una variable de su función envolvente; no puede declararse `global x`
            # y `nonlocal x` a la vez en el mismo ámbito. En producción, abusar de
            # `global` dificulta rastrear cambios de estado y puede causar efectos
            # secundarios inesperados.
            # ======================================================================


            def limbo():
                global x  # Declare global first before using the name x in any way.
                print(f"In Limbo, reality is: {x}")
                x = "Real World, but altered"  # modifying global reality
                # Aunque su nombre contiene "nonlocal", esta es una variable local de limbo().
                # Guarda el valor de la x global porque arriba se ha declarado "global x".
                # Cambiar nonlocal_real_world_x no modifica la x de dream_level_3().
                # Para modificar esa x exterior se necesitaría otro enfoque con "nonlocal x".
                nonlocal_real_world_x = x # Copia el valor de la x global
                print(
                    f"In Limbo, after altering reality, the Dream Level 3 is: {nonlocal_real_world_x}"
                )
                nonlocal_real_world_x = (
                    "Dream Level 3, but altered"  # Cambia solo la variable local; no modifica la x de dream_level_3().
                )

            print(f"In {x}, starting to go deeper...")
            limbo()
            print(f"Back in {x}, after Limbo.")

        print(f"In {x}, starting to go deeper...")
        dream_level_3()
        print(f"Back in {x}, after Dream Level 3.")

    print(f"In {x}, starting to go deeper...")
    dream_level_2()
    print(f"Back in {x}, after Dream Level 2.")


print(f"In the {x}, starting to dream...")
dream_level_1()
print(f"Back in the {x}.")
