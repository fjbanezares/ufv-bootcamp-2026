# ==============================================================================
# ALUMNA: María Rozas Casero
# REFLEXIÓN DE SCOPES:
# El programa de Python va a buscar los nombres siguiendo el orden LEGB establecido.
# Se entiende por LEGB Local, Enclosing de funciones envolventes, Global y Built-in de nombres incorporados.
#
# En la función limbo(), la instrucción global x indica que la variable x pertenece al ámbito del módulo.
# Por eso se modifica la realidad global, mientras que las variables x de París, Hotel y 
# Fortaleza conservan sus valores reales/iniciales.
#
# nonlocal_real_world_x es una variable local de la función limbo(). Dicho nombre
# no equivale a utilizar la instrucción nonlocal. Recibe el valor de
# la x global y reasignarla no modifica la x de la Fortaleza.
# Por lo tanto, de este modo los comentarios originales que indican que esa variable
# modifica el nivel 3 no describen lo que realmente hace el código.
#
# Si utilizáramos nonlocal x en lugar de global x, se podría modificar
# la x de la función envolvente más cercana que la tenga definida:
# en este caso sería dream_level_3(). La variable global no cambiaría.
#
# Modificar variables globales puede crear efectos secundarios/colaterales y
# dificultar las pruebas. Utilizar parámetros y devolver resultados
# suele facilitar la comprensión y el mantenimiento de nuestro programa.
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
