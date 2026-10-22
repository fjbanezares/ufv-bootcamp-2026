"""
SOLUCIÓN 3: Comunicación Inter-Niveles con Bus de Telemetría (PASIV Device)
--------------------------------------------------------------------------
En lugar de reasignar variables primitivas mediante 'global', los niveles
se comunican compartiendo un objeto mutable (diccionario / bus de eventos).
Esto refleja cómo el maletín somnacina (PASIV) monitoriza pulsaciones,
estabilidad y sincroniza la patada musical entre soñadores.
"""

from typing import Dict, List, Any


def pasiv_dream_session():
    # Bus de telemetría compartido por referencia en todo el árbol de funciones
    telemetry: Dict[str, Any] = {
        "status": "Sedated",
        "music_playing": False,
        "logs": [],
        "architect": "Ariadne",
        "point_man": "Arthur",
        "forger": "Eames",
        "extractor": "Cobb",
    }

    def emit_signal(sender: str, message: str):
        event = f"[{sender.upper()}] -> {message}"
        telemetry["logs"].append(event)
        print(f"📡 {event}")

    def dream_level_1():
        emit_signal("Level 1 (Yusuf)", "Furgoneta bajo persecución. Lluvia torrencial.")

        def dream_level_2():
            emit_signal("Level 2 (Arthur)", "Gravedad reduciéndose. Furgoneta en el aire.")

            def dream_level_3():
                emit_signal("Level 3 (Eames)", "Asalto a la fortaleza completado. Planta la idea.")

                def limbo():
                    # Acceso directo al canal de telemetría mutable
                    emit_signal("Limbo (Cobb)", "Localizando a Fischer y Saito en la costa.")

                    # Activamos la música de aviso de la patada (Édith Piaf)
                    telemetry["music_playing"] = True
                    emit_signal("Limbo (Cobb)", "🎵 Suena 'Non, je ne regrette rien'. ¡Preparen patada!")

                    telemetry["status"] = "KICK_SYNCHRONIZED"

                dream_level_3_active = True
                limbo()

                if telemetry["music_playing"]:
                    emit_signal("Level 3 (Eames)", "Patada con explosivos en la base de la fortaleza.")

            dream_level_3()
            if telemetry["status"] == "KICK_SYNCHRONIZED":
                emit_signal("Level 2 (Arthur)", "Detonando cables del ascensor para simular caída.")

        dream_level_2()
        if telemetry["status"] == "KICK_SYNCHRONIZED":
            emit_signal("Level 1 (Yusuf)", "La furgoneta atraviesa la barandilla y cae al río.")

    print("=== INICIANDO SESIÓN PASIV ===")
    dream_level_1()

    print("\n=== REPORTE DE TELEMETRÍA FINAL ===")
    print(f"Estado de la misión: {telemetry['status']}")
    print(f"Total de señales transmitidas: {len(telemetry['logs'])}")


if __name__ == "__main__":
    pasiv_dream_session()
