"""
SOLUCIÓN 1: Tótem de Verificación de Realidad (Spinning Top Totem)
-----------------------------------------------------------------
Añade un objeto Tótem con estado encapsulado. Al regresar de cada nivel
o entrar en el Limbo, el sujeto gira la peonza. Si las variables han sido
corrompidas o el entorno no es la realidad, el tótem revela si estamos
atrapados en una proyección subconsciente.
"""

import time


class Totem:
    def __init__(self, owner: str = "Dom Cobb"):
        self.owner = owner
        self._secret_weight = 42.0  # Solo el propietario conoce el peso real exacto

    def spin(self, reality_state: str) -> bool:
        """
        Gira el tótem.
        Retorna True si cae (estamos en el Mundo Real).
        Retorna False si sigue girando indefinidamente (estamos en un Sueño o Limbo).
        """
        print(f"\n[TÓTEM] {self.owner} hace girar su peonza metálica...")
        if "Real World" in reality_state and "altered" not in reality_state:
            print("  🌀 ... ... La peonza pierde equilibrio, se tambalea y CAE.")
            print("  ✅ Confirmado: Estamos en la REALIDAD.")
            return True
        else:
            print("  ♾️ ... La peonza gira y gira sin fricción con perfecta estabilidad.")
            print("  ⚠️ ALERTA: La realidad ha sido alterada. Sigues en un SUEÑO.")
            return False


# Variable global en el Mundo Real
reality = "Real World"
totem = Totem()


def dream_level_1():
    x = "Dream Level 1: Rainy Paris"

    def dream_level_2():
        x = "Dream Level 2: Arthur's Hotel"

        def dream_level_3():
            x = "Dream Level 3: Eames' Snow Fortress"

            def limbo():
                global reality
                print(f"\n[LIMBO] Caída al nivel más profundo.")
                print(f"[LIMBO] Vista de la realidad desde el abismo: {reality}")

                # Alteramos la realidad global
                reality = "Real World, but altered by Mal"

                nonlocal x
                print(f"[LIMBO] Nivel 3 antes de modificar: {x}")
                x = "Dream Level 3, compromised by projections"
                print(f"[LIMBO] Nivel 3 alterado: {x}")

                # Comprobación de tótem dentro de Limbo
                totem.spin(reality)

            print(f"\n[Nivel 3] En {x}. Descendiendo a Limbo...")
            limbo()
            print(f"[Nivel 3] De vuelta a {x} tras el Limbo.")

        print(f"\n[Nivel 2] En {x}. Descendiendo al Nivel 3...")
        dream_level_3()
        print(f"[Nivel 2] De vuelta a {x} tras el Nivel 3.")

    print(f"\n[Nivel 1] En {x}. Descendiendo al Nivel 2...")
    dream_level_2()
    print(f"[Nivel 1] De vuelta a {x} tras el Nivel 2.")


if __name__ == "__main__":
    print(f"=== INICIO: {reality} ===")
    totem.spin(reality)

    print("\n--- Conectando PASIV y entrando en el sueño ---")
    dream_level_1()

    print(f"\n=== REGRESO: {reality} ===")
    is_real = totem.spin(reality)
    if not is_real:
        print(">> FIN: ¿Cobb logró volver a casa o sigue atrapado?")
