x = "Real World"


def dream_level_1():
    x = "Dream Level 1: Paris"

    def dream_level_2():
        x = "Dream Level 2: Hotel"

        def dream_level_3():
            x = "Dream Level 3: Snow Fortress"

            # Guardamos la realidad del tercer nivel
            dream_level_3_reality = x

            def limbo():
                global x
                nonlocal dream_level_3_reality

                # Mostramos la realidad original
                print(f"In Limbo, reality is: {x}")

                # Modificamos la variable global
                x = "Real World, but altered"

                # Modificamos la realidad del tercer nivel
                dream_level_3_reality = (
                    "Dream Level 3: Snow Fortress altered"
                )

                print(
                    f"In Limbo, Dream Level 3 is: "
                    f"{dream_level_3_reality}"
                )

            print(f"In {x}, starting to go deeper...")
            limbo()

            print(
                f"Back in {dream_level_3_reality}, "
                f"after Limbo."
            )

        print(f"In {x}, starting to go deeper...")
        dream_level_3()
        print(f"Back in {x}, after Dream Level 3.")

    print(f"In {x}, starting to go deeper...")
    dream_level_2()
    print(f"Back in {x}, after Dream Level 2.")


print(f"In the {x}, starting to dream...")
dream_level_1()
print(f"Back in the {x}.")
