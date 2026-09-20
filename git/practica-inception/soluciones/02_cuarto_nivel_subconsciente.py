"""
SOLUCIÓN 2: Cuarto Nivel de Sueño - El Abismo Subconsciente
----------------------------------------------------------
Añade un nivel adicional de profundidad ("Dream Level 4: Collapsing Beach"),
demostrando la jerarquía de 'nonlocal' cruzando múltiples capas anidadas.
"""

reality = "Real World (Boeing 747 First Class)"


def dream_level_1():
    rain = "Heavy Rain in Los Angeles"

    def dream_level_2():
        gravity = "Zero Gravity in Hotel Corridor"

        def dream_level_3():
            fortress_state = "Snow Mountain Fortress intact"

            def dream_level_4():
                # Cuarto nivel antes de Limbo
                city_coast = "Decaying Modernist City on the Shore"

                def limbo():
                    global reality
                    nonlocal fortress_state, gravity, city_coast

                    print(">>> [LIMBO] Te encuentras con Saito envejecido 50 años.")
                    print(f"    Realidad original desde Limbo: {reality}")

                    # Modificamos la realidad global
                    reality = "Real World (Landing in Los Angeles, mission completed)"

                    # Modificamos variables de diferentes niveles de sueño (nonlocal multinivel)
                    fortress_state = "Fortress detonated with C4"
                    gravity = "Gravity stabilized after elevator plunge"
                    city_coast = "Buildings crumbling into the sea"

                    print(f"    [Limbo] Desencadenando cambios hacia arriba:")
                    print(f"    - Nivel 4 alterado: {city_coast}")
                    print(f"    - Nivel 3 alterado: {fortress_state}")
                    print(f"    - Nivel 2 alterado: {gravity}")

                print(f"  [Nivel 4: Costa] {city_coast}. Saltando al abismo...")
                limbo()
                print(f"  [Nivel 4: Costa] Despertando en Nivel 4. Estado: {city_coast}")

            print(f" [Nivel 3: Fortaleza] {fortress_state}. Sedante fuerte...")
            dream_level_4()
            print(f" [Nivel 3: Fortaleza] Despertando en Nivel 3. Estado: {fortress_state}")

        print(f"[Nivel 2: Hotel] {gravity}. Vigilando la furgoneta...")
        dream_level_3()
        print(f"[Nivel 2: Hotel] Despertando en Nivel 2. Estado: {gravity}")

    print(f"[Nivel 1: Furgoneta] {rain}. Yusuf conduce hacia el puente...")
    dream_level_2()
    print(f"[Nivel 1: Furgoneta] Despertando en Nivel 1. La furgoneta impacta el agua.")


if __name__ == "__main__":
    print(f"=== ESTADO INICIAL: {reality} ===")
    dream_level_1()
    print(f"=== ESTADO FINAL: {reality} ===")
