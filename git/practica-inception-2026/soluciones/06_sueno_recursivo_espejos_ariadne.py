"""
SOLUCIÓN 6: Sueño Fractal Recursivo - Los Espejos de Ariadne
------------------------------------------------------------
Explora la recursividad en Python como metáfora perfecta de los sueños
dentro de sueños (como el puente de espejos infinitos de Ariadne en París).
Cada llamada recursiva añade un marco a la pila de ejecución (call stack),
acumulando fragmentos de memoria hasta alcanzar el caso base (Limbo).
"""

from typing import List


def recursive_dream(
    depth: int, max_depth: int = 4, dream_memories: List[str] = None
) -> List[str]:
    """
    Función recursiva donde cada nivel de profundidad genera un nuevo
    sub-ámbito con su propia variable local, acumulando recuerdos en el retorno.
    """
    if dream_memories is None:
        dream_memories = []

    indent = "  " * depth
    level_name = f"Nivel {depth}" if depth > 0 else "Mundo Real"

    if depth == 0:
        print(f"{indent}🌐 [REALIDAD] Inicio de la inmersión recursiva.")
    else:
        print(f"{indent}🌀 [{level_name}] Profundizando en el subconsciente...")

    # Variable local a este marco específico del call stack
    current_thought = f"Pensamiento fijado en {level_name}"

    # CASO BASE: Si alcanzamos la profundidad máxima, llegamos al Limbo
    if depth >= max_depth:
        print(f"{indent}💀 [LIMBO RECURSIVO] Máxima profundidad alcanzada (Pila llena).")
        print(f"{indent}   Plantando la idea semilla en el fondo de la mente.")
        dream_memories.append("SEMILLA_IMPLANTADA: 'Mi padre quiere que sea yo mismo'")
        return dream_memories

    # LLAMADA RECURSIVA: Ir un nivel más profundo
    recursive_dream(depth + 1, max_depth, dream_memories)

    # Retorno desapilando marcos de ejecución
    print(f"{indent}↩️ [{level_name}] Despertando del nivel inferior. {current_thought}.")
    dream_memories.append(f"Recuerdo consolidado de {level_name}")

    return dream_memories


if __name__ == "__main__":
    print("=== ARIADNE DOBLA EL ESPACIO Y EL TIEMPO RECURSIVAMENTE ===")
    recuerdos = recursive_dream(depth=0, max_depth=4)

    print("\n=== RECUERDOS TRAÍDOS DE VUELTA A LA REALIDAD ===")
    for i, recuerdo in enumerate(recuerdos, 1):
        print(f" {i}. {recuerdo}")
