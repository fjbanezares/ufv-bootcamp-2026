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
x = "Real World"  # This is the global variable


def dream_level_1():
    x = "Dream Level 1: Paris"  # local variable to dream_level_1

    def dream_level_2():
        x = "Dream Level 2: Hotel"  # local variable to dream_level_2

        def dream_level_3():
            x = "Dream Level 3: Snow Fortress"  # local variable to dream_level_3

            def limbo():
                global x  # Declare global first before using the name x in any way.
                print(f"In Limbo, reality is: {x}")
                x = "Real World, but altered"  # modifying global reality

                nonlocal_real_world_x = x  # This refers to Dream Level 3's x
                print(
                    f"In Limbo, after altering reality, the Dream Level 3 is: {nonlocal_real_world_x}"
                )
                nonlocal_real_world_x = (
                    "Dream Level 3, but altered"  # modifying the dream level 3 reality
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
