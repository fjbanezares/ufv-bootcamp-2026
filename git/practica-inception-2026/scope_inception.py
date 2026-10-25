# ALUMNO: Alejandro Arias Sanjuán

# REFLEXIÓN:
# En este programa hay varias funciones dentro de otras, y cada una tiene su propia variable x, que representa un nivel diferente de sueño.
# Al utilizar global x dentro de limbo(), podemos modificar la variable x del mundo real, aunque estemos dentro de varias funciones.
# Por otro lado, nonlocal permite modificar una variable de una función exterior que contiene a la función actual, sin modificar la variable global.
# Utilizar muchas variables globales puede provocar errores, porque una función puede cambiar valores que también utilizan otras funciones.

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
