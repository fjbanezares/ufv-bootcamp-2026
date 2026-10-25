x = "Real World"  # This is the global variable


def dream_level_1():
    x = "Dream Level 1: Paris"  # local variable to dream_level_1

    def dream_level_2():
        x = "Dream Level 2: Hotel"  # local variable to dream_level_2

        def dream_level_3():
            x = "Dream Level 3: Snow Fortress"  # local variable to dream_level_3
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
