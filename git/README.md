# Módulo Git & Control de Versiones

Espacio dedicado al aprendizaje y consulta de flujos de trabajo con Git y plataformas como GitHub.

## Flujo Básico de Trabajo
1. **Estado y cambios**:
   ```bash
   git status
   git diff
   ```
2. **Añadir y confirmar**:
   ```bash
   git add .
   git commit -m "feat: descripción del cambio"
   ```
3. **Sincronización remota**:
   ```bash
   git fetch origin
   git pull origin main
   git push origin main
   ```

## Ramas y Colaboración
- Crear y cambiar de rama: `git checkout -b feature/nueva-funcionalidad` (o `git switch -c ...`)
- Listar ramas: `git branch -a`
- Fusionar rama: `git merge feature/nueva-funcionalidad`
- Descartar cambios locales no guardados: `git restore <archivo>`
