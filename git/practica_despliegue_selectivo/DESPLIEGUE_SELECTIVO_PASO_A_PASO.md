# Guía Rápida: Despliegue Selectivo y Clon Ligero en Git

Esta guía va **directo al grano**. Aprenderás a tener un repositorio con todo tu proyecto ("el taller") y desplegar en el servidor de producción (IONOS, VPS, hosting) **únicamente los archivos necesarios** mediante una rama `orphan` o un `tag` específico con un **clon superficial y selectivo**.

![Infografía: Despliegue web ligero en 1&1](./Despliegue%20web%20ligero%20en%201%261.png)

---

## Estructura del Proyecto Demo

En la subcarpeta [`proyecto-demo/`](./proyecto-demo/) tienes la estructura real lista para usar:

```text
proyecto-demo/
├── web/                   <-- LO ÚNICO QUE VA A PRODUCCIÓN
│   ├── index.html
│   ├── capitulo1.html
│   ├── css/style.css
│   ├── js/app.js
│   └── images/portada.svg
├── latex/                 <-- Fuentes pesadas (se quedan fuera)
│   ├── libro.tex
│   └── capitulos/cap1.tex
├── pdf/libro.pdf          <-- Binario pesado (se queda fuera)
├── traducciones/en/       <-- Borradores (se quedan fuera)
├── herramientas/build.py  <-- Scripts internos (se quedan fuera)
└── README.md
```

---

## Paso 1: Inicializar y subir la rama principal (`main`)

Entra en la carpeta del proyecto o en una copia de trabajo:

```bash
cd proyecto-demo
git init
git add .
git commit -m "feat: proyecto completo del libro (taller de trabajo)"
git branch -M main
```

*(Opcional si vas a subirlo a GitHub)*:
```bash
git remote add origin git@github.com:TU_USUARIO/demo-libro.git
git push -u origin main
```

---

## Paso 2: Crear la rama huérfana (`orphan`) para producción

Una rama `orphan` no hereda historial ni ancestros de `main`. Solo contendrá los archivos web listos para servir:

```bash
# 1. Guardar temporalmente el contenido de la web
rm -rf /tmp/web-deploy && mkdir /tmp/web-deploy
cp -R web/* /tmp/web-deploy/

# 2. Crear y cambiar a la rama huérfana
git switch --orphan web-prod

# 3. Vaciar el índice de los archivos heredados de main
git rm -rf .

# 4. Colocar los archivos web en la raíz de esta rama
cp -R /tmp/web-deploy/* .

# 5. Crear el commit limpio de producción
git add .
git commit -m "deploy: snapshot web v1.0.0"
```

---

## Paso 3: Crear un Tag específico para congelar la versión

Poner una etiqueta (*tag*) en esta rama te permite clonar exactamente una versión concreta e inmutable:

```bash
git tag -a v1.0.0-web -m "Release v1.0.0 web de producción"
```

---

## Paso 4: Subir la rama y el tag a GitHub

```bash
# Subir la rama de producción
git push -u origin web-prod

# Subir el tag específico
git push origin v1.0.0-web

# O subir todos los tags de una vez:
# git push origin --tags
```

---

## Paso 5: Despliegue en el servidor (Clon Selectivo)

En tu servidor de producción (IONOS / 1&1, VPS, etc.), ejecuta el comando de clonación selectiva en la carpeta de destino (`public_html` o similar).

### Opción A: Clonar SOLO la rama `web-prod`
```bash
git clone --branch web-prod --single-branch --depth 1 git@github.com:TU_USUARIO/demo-libro.git public_html
```

### Opción B: Clonar SOLO el Tag concreto (`v1.0.0-web`)
En Git, el parámetro `--branch` acepta tanto nombres de ramas como de **tags**:
```bash
git clone --branch v1.0.0-web --single-branch --depth 1 git@github.com:TU_USUARIO/demo-libro.git public_html
```

### ¿Qué hace cada bandera?
| Parámetro | Función |
|---|---|
| `--branch <rama o tag>` | Selecciona la rama o tag exacto que quieres desplegar. |
| `--single-branch` | Descarga **únicamente** esa referencia (ignora `main` y las demás ramas). |
| `--depth 1` | Descarga solo el **último commit** (sin historial antiguo ni objetos huérfanos). |

---

## Paso 6: Verificación empírica en el servidor

Comprueba que el servidor está limpio y ultraligero:

```bash
cd public_html

# 1. Solo existen los archivos de la web en la raíz:
ls -la
# Salida: index.html, capitulo1.html, css/, js/, images/
# (latex/, pdf/, traducciones/ NO existen)

# 2. Solo existe la rama clonada:
git branch -a

# 3. El historial tiene exactamente un commit:
git log --oneline

# 4. Confirmar que el repositorio es superficial:
git rev-parse --is-shallow-repository
# Salida: true

# 5. El directorio .git pesa kilobytes, no megabytes ni gigabytes:
du -sh .git
```

---

## Paso 7: Actualizaciones posteriores

### Si despliegas siguiendo la rama `web-prod`:
En local actualizas la web, haces commit en `web-prod` y `git push`. En el servidor basta con:
```bash
cd public_html
git pull --ff-only
```

### Si despliegas por Tags (recomendado para versiones fijas):
Cuando crees `v1.1.0-web` en local y lo subas:
```bash
cd public_html
git fetch --tags --depth 1
git checkout tags/v1.1.0-web
```

---

## Resumen Express de comandos

```bash
# EN TU MÁQUINA LOCAL:
git switch --orphan web-prod
git rm -rf .
cp -R /tmp/web-deploy/* .
git add . && git commit -m "v1.0.0 web"
git tag -a v1.0.0-web -m "v1.0.0"
git push origin web-prod --tags

# EN EL SERVIDOR (IONOS / VPS):
git clone --branch v1.0.0-web --single-branch --depth 1 <URL_REPO> public_html
```
