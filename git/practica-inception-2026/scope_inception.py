
# ALUMNO: [Adrián García Fontanet]
# PRACTICA: EL DESAFIO INCEPTION - GIT Y PYTHON SCOPES
#
# Reflexion:
# La palabra clave global permite modificar una variable definida
# fuera de todas las funciones.
# La palabra clave nonlocal permite modificar una variable definida
# en una funcion exterior, pero no global.
# El orden de busqueda de variables en Python es LEGB:
# Local, Enclosing, Global y Built-in.


x = "Real World"  # Variable global


def dream_level_1():
    x = "Dream Level 1: Paris"

    def dream_level_2():
        x = "Dream Level 2: Hotel"

        def dream_level_3():
            dream_level_3_x = "Dream Level 3: Snow Fortress"

            def limbo():
                global x
                nonlocal dream_level_3_x

                print(f"In Limbo, reality is: {x}")

                # Modificamos la variable global.
                x = "Real World, but altered"

                print(
                    f"In Limbo, the Dream Level 3 is: "
                    f"{dream_level_3_x}"
                )

                # Modificamos la variable del nivel exterior.
                dream_level_3_x = "Dream Level 3, but altered"

            print(
                f"In {dream_level_3_x}, starting to go deeper..."
            )
            limbo()
            print(f"Back in {dream_level_3_x}, after Limbo.")

        print(f"In {x}, starting to go deeper...")
        dream_level_3()
        print(f"Back in {x}, after Dream Level 3.")

    print(f"In {x}, starting to go deeper...")
    dream_level_2()
    print(f"Back in {x}, after Dream Level 2.")


print(f"In the {x}, starting to dream...")
dream_level_1()
print(f"Back in the {x}.")
