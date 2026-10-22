"""
SOLUCIÓN 5: Context Managers - El Compuesto Sedante de Yusuf
------------------------------------------------------------
Utiliza gestores de contexto de Python (`with dream_layer(...)`) para
administrar la entrada y salida de los niveles de sueño, calculando
automáticamente la dilatación del tiempo (x20 por nivel) y asegurando
la limpieza de recursos y estabilización de signos vitales.
"""

from contextlib import contextmanager
import time


class DreamSession:
    current_depth = 0
    time_factor = 1  # 1 seg en la realidad = 20 seg en nivel 1, 400 seg en nivel 2...


@contextmanager
def dream_layer(name: str, architect: str):
    DreamSession.current_depth += 1
    DreamSession.time_factor *= 20
    indent = "  " * DreamSession.current_depth

    print(f"{indent}💤 [ENTRANDO] {name} (Diseñado por: {architect})")
    print(f"{indent}   ⏱️ Dilatación temporal: x{DreamSession.time_factor} relativo a la realidad")

    layer_state = {"name": name, "depth": DreamSession.current_depth, "stable": True}

    try:
        yield layer_state
    except Exception as e:
        print(f"{indent}   🚨 INESTABILIDAD DETECTADA en {name}: {e}")
        layer_state["stable"] = False
        raise
    finally:
        print(f"{indent}🔔 [DESPERTANDO / KICK] Saliendo de {name}...")
        DreamSession.time_factor //= 20
        DreamSession.current_depth -= 1


def run_compound_heist():
    print("=== COMIENZA EL VUELO: SIDNEY -> LOS ÁNGELES ===")

    with dream_layer("Nivel 1: Calles de Lluvia", architect="Ariadne") as l1:
        with dream_layer("Nivel 2: Hotel Elegante", architect="Arthur") as l2:
            with dream_layer("Nivel 3: Fortaleza Alpina", architect="Eames") as l3:
                print(f"      🎯 En la cámara acorazada del Nivel 3.")
                print(f"      🎯 Profundidad actual: {l3['depth']}. Sembrando el testamento.")
                print(f"      🎯 Tiempo corriendo a x{DreamSession.time_factor} velocidad.")

    print("\n=== FIN DEL SUEÑO: Despertar sereno en primera clase ===")


if __name__ == "__main__":
    run_compound_heist()
