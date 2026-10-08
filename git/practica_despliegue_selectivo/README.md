# Práctica: Despliegue Selectivo y Clon Ligero en Git

Este directorio contiene todo el material para aprender a separar el código fuente de desarrollo ("el taller") del código publicable en servidores de producción ("el escaparate") usando ramas `orphan`, `tags` y clones selectivos superficiales (`--single-branch --depth 1`).

---

## Contenido de la práctica

1. **[Guía Rápida Paso a Paso (Directa al grano)](./DESPLIEGUE_SELECTIVO_PASO_A_PASO.md)**:
   - Flujo rápido de comandos: inicialización, creación de rama `orphan`, etiquetado con `tag`, subida a GitHub, clonación selectiva y verificación.
2. **[Manual Extendido de la Práctica](./practica_git_branch_web_prod_orphan.md)**:
   - Explicación conceptual en profundidad sobre ramas normales vs. ramas huérfanas, árboles de commits, configuración SSH y despliegue en IONOS / 1&1.
3. **[Estructura del Proyecto Demo (`proyecto-demo/`)](./proyecto-demo/)**:
   - Subcarpeta con la estructura realista de archivos (`web/`, `latex/`, `pdf/`, `traducciones/`, `herramientas/`) lista para probar la práctica de inmediato.
4. **[Infografía explicativa](./Despliegue%20web%20ligero%20en%201%261.png)**:
   - Esquema visual del flujo de trabajo y arquitectura de ramas.

---

## Infografía

![Infografía: Despliegue web ligero en 1&1](./Despliegue%20web%20ligero%20en%201%261.png)
