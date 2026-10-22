# 💡 Catálogo de Soluciones - Desafío Inception Scope

Esta carpeta contiene 6 implementaciones avanzadas que amplían el código original de Inception demostrando diferentes conceptos arquitectónicos y de lenguaje en Python:

---

### 1. [`01_totem_verification.py`](./01_totem_verification.py) — El Tótem de Cobb
- **Concepto**: Encapsulación de estado con clases (`Totem`).
- **Mecánica**: Gira la peonza de metal en cada nivel y al regresar. Si la variable global de la realidad fue alterada o seguimos en un sueño, la peonza gira indefinidamente sin fricción; si es el Mundo Real, cae.

---

### 2. [`02_cuarto_nivel_subconsciente.py`](./02_cuarto_nivel_subconsciente.py) — 4º Nivel de Profundidad
- **Concepto**: Ámbitos léxicos de múltiples capas y `nonlocal` jerárquico.
- **Mecánica**: Añade un 4º nivel ("Ciudad derrumbándose en la costa") antes del Limbo. Desde el Limbo se modifican variables intermedias de varios niveles superiores usando `nonlocal` simultáneo.

---

### 3. [`03_comunicacion_senales_telemetria.py`](./03_comunicacion_senales_telemetria.py) — Telemetría PASIV (Bus de Señales)
- **Concepto**: Paso por referencia de estructuras mutables (diccionario de estado).
- **Mecánica**: Los niveles no sobreescriben variables primitivas arbitrariamente, sino que emiten eventos a un canal central compartido (`telemetry`). Permite que el aviso musical de la patada ("Non, je ne regrette rien") se sincronice entre todos los soñadores.

---

### 4. [`04_the_kick_generadores_yield.py`](./04_the_kick_generadores_yield.py) — "The Kick" con Generadores y Corrutinas
- **Concepto**: Generadores de Python (`yield` y método `.send()`).
- **Mecánica**: Cada nivel de sueño queda suspendido en un `yield` esperando la patada. El Limbo dispara la música y cada generador despierta recibiendo el valor y devolviendo su estado con `return`.

---

### 5. [`05_context_managers_sedante_yusuf.py`](./05_context_managers_sedante_yusuf.py) — Compuesto Sedante (Context Managers)
- **Concepto**: Gestores de contexto (`@contextmanager` y sintaxis `with`).
- **Mecánica**: Gestiona la entrada (`__enter__`) y salida (`__exit__`) limpia de cada nivel de sueño. Calcula en tiempo real la dilatación temporal exponencial ($20^N$) y garantiza la restauración de variables aunque ocurra un error.

---

### 6. [`06_sueno_recursivo_espejos_ariadne.py`](./06_sueno_recursivo_espejos_ariadne.py) — Recursividad Fractal (Los Espejos de Ariadne)
- **Concepto**: Pila de ejecución de llamadas (*Call Stack*) y recursividad funcional.
- **Mecánica**: La profundidad de sueño no está codificada a fuego, sino que se genera recursivamente como espejos enfrentados. Al alcanzar la profundidad límite (Limbo / caso base), se planta la semilla y los recuerdos se acumulan al desapilar la pila de llamadas.
