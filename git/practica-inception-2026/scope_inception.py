# ==========================================================
# ALUMNO: Arturo Santiago Santos García
# REFLEXIÓN DE SCOPES:
#
# Python busca los nombres siguiendo el orden LEGB:
# local, funciones exteriores, global e incorporados.
#
# En limbo(), global x permite acceder a la x del archivo.
# Al cambiar su valor, se modifica la realidad global,
# pero no las variables x propias de los otros sueños.
#
# nonlocal x permitiría modificar la x de la función
# exterior más cercana que la tenga definida.
#
# En este código, nonlocal_real_world_x es una variable
# local: su nombre no equivale a usar la palabra nonlocal
# y asignarle un valor no modifica la x del nivel 3.
#
# Usar muchas variables globales puede dificultar entender
# qué función ha cambiado un dato y provocar errores.
# ==========================================================
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
