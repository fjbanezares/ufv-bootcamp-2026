# 🎬 Práctica de Git: El Desafío Inception (Ramas y Merge)

Esta práctica combina el aprendizaje de **Git (flujo de ramas, commits y merge)** con la resolución/mejora de código en **Python (variables globales, ámbito léxico y `nonlocal`)**.

---

## 🎯 Objetivo de la Práctica
1. Trabajar en una rama secundaria independiente sin tocar directamente `main`.
2. Mejorar o refactorizar el código de [`scope_inception.py`](./scope_inception.py).
3. Confirmar los cambios con commits limpios.
4. Integrar (mergear) la rama en `main`.
5. Subir los cambios a GitHub (`git push`).

---

## 📜 El Código Base: Metáfora de Inception
El script simula los niveles de sueño de la película *Inception*:
- **Real World** (`global reality / x`)
- **Nivel 1: París** (ámbito local de `dream_level_1`)
- **Nivel 2: Hotel** (ámbito local de `dream_level_2`)
- **Nivel 3: Fortaleza de Nieve** (ámbito local de `dream_level_3`)
- **Limbo**: Nivel más profundo que intenta alterar la realidad global y niveles intermedios mediante `global` y `nonlocal`.

---

## 🛠️ Guía Paso a Paso para el Alumno

### Paso 1: Asegurarte de estar en la rama `main` actualizada
```bash
git checkout main
git pull origin main
```

### Paso 2: Crear y cambiar a una rama de trabajo
Crea tu propia rama con tu nombre o el identificador de tu equipo:
```bash
git checkout -b feature/mejora-inception-tu-nombre
# o si usas la sintaxis moderna:
git switch -c feature/mejora-inception-tu-nombre
```

### Paso 3: Probar y modificar el código
1. Ejecuta el script base para entender la salida actual:
   ```bash
   python3 git/practica-inception/scope_inception.py
   ```
2. Realiza tu mejora en el código. Ideas de mejora:
   - Añadir un tótem o comprobación de si sigue en un sueño.
   - Refactorizar las alteraciones de variables para que sigan un orden lógico.
   - Añadir tipado estático, docstrings o tests unitarios.

### Paso 4: Confirmar tus cambios en la rama
```bash
git status
git add git/practica-inception/scope_inception.py
git commit -m "feat(inception): mejorar manejo de niveles de sueño y variables de scope"
```

### Paso 5: Mergear la rama a `main`
Una vez completada la mejora, regresa a `main` e integra tu trabajo:
```bash
# 1. Volver a la rama principal
git checkout main

# 2. Fusionar la rama con tus mejoras
git merge feature/mejora-inception-tu-nombre
```

### Paso 6: Subir los cambios a GitHub
```bash
git push origin main
```

### Paso 7: (Opcional) Eliminar la rama local una vez integrada
```bash
git branch -d feature/mejora-inception-tu-nombre
```
