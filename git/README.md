# 🐙 Módulo Git & Control de Versiones - UFV Bootcamp 2026

Bienvenido al espacio de **Control de Versiones con Git y GitHub**. Aquí encontrarás un curso completo estructurado a partir de 10 infografías temáticas, mini-prácticas flash para la terminal y proyectos prácticos colaborativos.

---

## 📚 Materiales Principales

### 1. 📖 [Curso Profundo: Git Desde Cero (Manual Interactivo)](./CURSO_GIT_DESDE_CERO.md)
Guía extensa y didáctica dividida en 10 módulos con explicaciones internas (*blobs, trees, commits, DAG*) y **mini-prácticas flash paso a paso** para ejecutar directamente en la terminal.

### 2. 🎨 [Serie Visual: Git Desde Cero (11 Láminas Infográficas)](./git%20crash%20course/)
Colección completa de láminas visuales en alta resolución que condensan cada concepto:
- **[Evolución Histórica](./git%20crash%20course/git_remotos_svn_vs_git.png)**: Arquitectura Distribuida (Git) vs Centralizada (Subversion / SVN) y Colaboración Remota.
1. **[Parte 1](./git%20crash%20course/git1.png)**: ¿Por qué existe Git y qué problema resuelve?
2. **[Parte 2](./git%20crash%20course/git2.png)**: Git Internals: cómo guarda la información (Blobs, Trees, Commits y DAG).
3. **[Parte 3](./git%20crash%20course/git3.png)**: Flujo diario: Working Directory, Staging Area, Repository y `.gitignore`.
4. **[Parte 4](./git%20crash%20course/git4.png)**: Stage vs Stash: guardar sin perder el hilo.
5. **[Parte 5](./git%20crash%20course/git5.png)**: Ramas (branches), merges y resolución de conflictos.
6. **[Parte 6](./git%20crash%20course/git6.png)**: Remotos, GitHub paso a paso, autenticación SSH/gh y colaboración.
7. **[Parte 7](./git%20crash%20course/git7.png)**: Merges avanzados (Fast-forward, no-ff, squash y octopus).
8. **[Parte 8](./git%20crash%20course/git8.png)**: HEAD, detached HEAD y viajar en el tiempo.
9. **[Parte 9](./git%20crash%20course/git9.png)**: Rebase y rebase interactivo (`git rebase -i`).
10. **[Parte 10](./git%20crash%20course/git10.png)**: Seguridad, trabajo en producción y los 10 hábitos de oro.

### 3. 🎬 [Práctica Colaborativa: El Desafío Inception Scope](./practica-inception/README.md)
Ejercicio guiado de trabajo en ramas donde los alumnos aplican el flujo real de creación de ramas (`feature/...`), mejora de scripts en Python con niveles de sueño, resolución de merge y push a GitHub.

---

## ⚡ Chuleta Rápida de Comandos

```bash
# 1. Estado y diferencias
git status
git diff

# 2. Guardar cambios con intención
git add .
git commit -m "feat: descripción breve y clara"

# 3. Ramas y movimientos
git switch -c feature/nueva-idea   # Crear y cambiar de rama
git switch main                    # Volver a main
git merge feature/nueva-idea       # Fusionar

# 4. Sincronización remota
git fetch origin                   # Mirar cambios remotos
git pull origin main               # Actualizar e integrar
git push origin main               # Compartir cambios
```
