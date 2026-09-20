"""
SOLUCIÓN 4: 'The Kick' con Generadores y Corrutinas (Yield & Send)
-----------------------------------------------------------------
Utiliza generadores (`yield`) para suspender la ejecución de cada nivel de sueño.
Cada nivel queda 'dormido' hasta que el nivel más profundo envía 'The Kick'
(la caída o impacto simultáneo) que propaga el despertar en cascada.
"""


def level_3_generator():
    print("      [Nivel 3: Fortaleza] Iniciado. Esperando que Limbo termine...")
    kick_data = yield "Level 3 Sedated"
    print(f"      [Nivel 3: Fortaleza] 💥 KICK RECIBIDO: '{kick_data}'")
    print("      [Nivel 3: Fortaleza] Detonación de la fortaleza. Despertando a Nivel 2...")
    return "Inception Completed"


def level_2_generator():
    print("    [Nivel 2: Hotel] Iniciado. Vigilando durmientes...")
    kick_data = yield "Level 2 Sedated"
    print(f"    [Nivel 2: Hotel] 💥 KICK RECIBIDO: '{kick_data}'")
    print("    [Nivel 2: Hotel] Impacto del ascensor. Despertando a Nivel 1...")
    return "Hotel Cleared"


def level_1_generator():
    print("  [Nivel 1: Furgoneta] Yusuf conduciendo bajo la lluvia...")
    kick_data = yield "Level 1 Sedated"
    print(f"  [Nivel 1: Furgoneta] 💥 KICK RECIBIDO: '{kick_data}'")
    print("  [Nivel 1: Furgoneta] Furgoneta golpea el agua. ¡Despertar en el avión!")
    return "All extraction targets awake"


def orchestrate_mission():
    print("=== ACTIVANDO MÁQUINA DE SUEÑOS (GENERADORES SUSPENDIDOS) ===")
    g1 = level_1_generator()
    g2 = level_2_generator()
    g3 = level_3_generator()

    # Cada nivel entra en suspensión profunda
    next(g1)
    next(g2)
    next(g3)

    print("\n>>> [LIMBO] Cobb y Saito se encuentran. La idea está implantada.")
    the_kick = "🎵 Édith Piaf: Non, je ne regrette rien"
    print(f">>> [LIMBO] Disparando patada sincronizada: {the_kick}\n")

    # Despertamos de abajo hacia arriba enviando el kick
    try:
        g3.send(the_kick)
    except StopIteration as e:
        res3 = e.value

    try:
        g2.send(the_kick)
    except StopIteration as e:
        res2 = e.value

    try:
        g1.send(the_kick)
    except StopIteration as e:
        res1 = e.value

    print("\n=== TODOS DESPIERTOS EN EL BOEING 747 ===")
    print(f"Resultados: Nivel 3: '{res3}', Nivel 2: '{res2}', Nivel 1: '{res1}'")


if __name__ == "__main__":
    orchestrate_mission()
