# Práctica Git: desplegar solo la parte web de un repositorio grande

## Objetivo

Supongamos que tenemos un repositorio grande para un libro:

```text
mi-libro/
├── web/
│   ├── index.html
│   ├── capitulo1.html
│   ├── capitulo2.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── images/
│       ├── portada.jpg
│       └── capitulo1.jpg
│
├── latex/
│   ├── libro.tex
│   └── capitulos/
│
├── pdf/
│   └── libro.pdf
│
├── traducciones/
│   ├── en/
│   ├── fr/
│   └── de/
│
└── herramientas/
    └── build.py
```

En nuestro ordenador queremos conservar **todo el proyecto**.

Pero en el servidor de producción —por ejemplo IONOS/1&1— solo necesitamos:

```text
index.html
capitulo1.html
capitulo2.html
css/
js/
images/
```

La idea será mantener:

- `main` → proyecto completo.
- `web-prod` → únicamente los archivos publicables.

Y en el servidor clonaremos exclusivamente `web-prod`.

---

# 1. Lo importante: `git clone -b`

Una orden sencilla sería:

```bash
git clone -b web-prod git@github.com:usuario/mi-libro.git
```

La opción:

```text
-b web-prod
```

es equivalente a:

```text
--branch web-prod
```

y significa:

> Después de clonar, deja seleccionada la rama `web-prod`.

Pero hay un detalle importante.

## `-b` no significa necesariamente "descarga solamente esta rama"

Por eso, para un servidor de producción conviene utilizar:

```bash
git clone \
  --branch web-prod \
  --single-branch \
  --depth 1 \
  git@github.com:usuario/mi-libro.git
```

O en una sola línea:

```bash
git clone --branch web-prod --single-branch --depth 1 git@github.com:usuario/mi-libro.git
```

Las tres opciones significan:

| Opción | Significado |
|---|---|
| `--branch web-prod` | Selecciona `web-prod` |
| `--single-branch` | Solo descarga esa rama |
| `--depth 1` | Solo descarga el último commit |

Para un servidor web esta combinación es mucho más interesante que un `git clone` normal.

---

# 2. Tu duda: ¿una rama ligera conserva los archivos antiguos?

Sí, **si creamos una rama normal a partir de `main`**, esa rama tiene como antepasados los commits del proyecto completo.

Ejemplo:

```text
A --- B --- C --- D     main
              \
               E        web-prod
```

En `E` podríamos haber borrado:

```text
latex/
pdf/
traducciones/
```

La fotografía actual de `web-prod` sería ligera.

Pero Git sabe que el padre de `E` es `C`, y en `C` estaban todos aquellos archivos.

Por tanto, conceptualmente el historial sigue unido al repositorio grande.

## Sin embargo...

Si el servidor hace:

```bash
git clone --branch web-prod --single-branch --depth 1 ...
```

Git solo necesita el commit `E` y los objetos correspondientes a su estado actual.

Los commits anteriores quedan fuera del clon superficial.

Así que **en la práctica ya puedes ahorrar muchísimo espacio**.

---

# 3. Una solución aún más limpia: rama `orphan`

Tu idea de querer solamente "la foto final" tiene exactamente una solución Git:

```bash
git switch --orphan web-prod
```

Una rama `orphan` es una rama **sin padre**.

En vez de esto:

```text
A --- B --- C --- D       main
              \
               E          web-prod
```

tenemos:

```text
A --- B --- C --- D       main


W1 --- W2 --- W3          web-prod
```

`web-prod` tiene su propia historia.

No conoce los commits de `main`.

No sabe nada de LaTeX.

No sabe nada de los PDF.

No sabe nada de los idiomas que no publiques.

Contiene exclusivamente la web.

Esto es probablemente lo más parecido a lo que tú llamabas:

> "Quiero la foto final".

---

# 4. ¿Branch `orphan` o repositorio independiente?

Ambas soluciones son buenas.

## Opción A — rama orphan

```text
repo: mi-libro

main
 ├── HTML
 ├── LaTeX
 ├── PDF
 ├── traducciones
 └── scripts

web-prod
 ├── HTML
 ├── CSS
 ├── JS
 └── imágenes
```

Ventaja: todo sigue dentro del mismo repositorio GitHub.

## Opción B — repositorio separado

```text
mi-libro-source
├── HTML
├── LaTeX
├── PDF
├── traducciones
└── scripts

mi-libro-web
├── HTML
├── CSS
├── JS
└── imágenes
```

Es todavía más aislado, pero obliga a gestionar dos repositorios.

Para un proyecto personal, **yo empezaría por una rama orphan `web-prod`**.

---

# 5. Práctica completa desde cero

Vamos a simular todo el proceso.

## 5.1 Crear el proyecto de prueba

```bash
mkdir demo-libro
cd demo-libro
git init
```

Creamos las carpetas:

```bash
mkdir -p web/css web/js web/images latex pdf traducciones/en herramientas
```

Creamos archivos web:

```bash
echo "<h1>Mi libro</h1>" > web/index.html
echo "<h1>Capítulo 1</h1>" > web/capitulo1.html
echo "body { font-family: sans-serif; }" > web/css/style.css
echo "console.log('Libro cargado');" > web/js/app.js
echo "imagen simulada" > web/images/portada.jpg
```

Creamos archivos que NO queremos en producción:

```bash
echo "\\documentclass{book}" > latex/libro.tex
echo "PDF simulado" > pdf/libro.pdf
echo "<h1>My book</h1>" > traducciones/en/index.html
echo "print('build')" > herramientas/build.py
```

---

## 5.2 Crear el primer commit

```bash
git add .
git commit -m "Proyecto completo del libro"
git branch -M main
```

> **Nota sobre `-M`**: `-m` significa `--move` (renombrar rama). La `-M` en mayúscula equivale a `--move --force`. Fuerza el renombrado de la rama actual a `main` (por si Git la creó por defecto con el nombre antiguo `master`), evitando cualquier error si ya existiera una rama llamada `main`.

Ahora tenemos:

```text
main
└── proyecto completo
```

---

## 5.3 Crear el repositorio en GitHub

En GitHub:

```text
New repository
```

Nombre:

```text
demo-libro
```

Es mejor no marcar:

```text
Add README
Add .gitignore
Add license
```

porque nuestro repositorio local ya existe.

GitHub nos dará dos tipos de URL:
- **HTTPS (Recomendada si no tienes claves SSH configuradas)**: `https://github.com/TU_USUARIO/demo-libro.git`
- **SSH (Requiere clave pública en GitHub)**: `git@github.com:TU_USUARIO/demo-libro.git`

Añadimos el remoto (ejemplo con HTTPS):

```bash
git remote add origin https://github.com/TU_USUARIO/demo-libro.git
```

*(O si prefieres SSH: `git remote add origin git@github.com:TU_USUARIO/demo-libro.git`)*

Subimos `main`:

```bash
git push -u origin main
```

> **Aviso sobre permisos**: Aunque el repositorio sea público, GitHub **siempre exige autenticación para `git push`** para verificar que eres el propietario. Si usas SSH y no has subido tu clave pública a GitHub, recibirás un error `Permission denied (publickey)`. En ese caso, utiliza la URL HTTPS o configura tu clave SSH como se explica a continuación.

---

# 6. Dar permisos con SSH

Comprobamos si tenemos una clave:

```bash
ls ~/.ssh
```

Por ejemplo:

```text
id_ed25519
id_ed25519.pub
```

Si no existe:

```bash
ssh-keygen -t ed25519
```

Mostramos la clave pública:

```bash
cat ~/.ssh/id_ed25519.pub
```

En GitHub:

```text
Settings
→ SSH and GPG keys
→ New SSH key
```

Pegamos la clave pública y probamos:

```bash
ssh -T git@github.com
```

---

# 7. Crear nuestra "foto web" con una rama orphan

Antes de cambiar de rama, guardamos una copia temporal de la web:

```bash
rm -rf /tmp/web-deploy
mkdir /tmp/web-deploy
cp -R web/* /tmp/web-deploy/
```

Ahora:

```bash
git switch --orphan web-prod
```

Borramos del índice y del working tree lo heredado:

```bash
git rm -rf .
```

Restauramos solo la web:

```bash
cp -R /tmp/web-deploy/* .
```

Ahora la raíz debe quedar así:

```text
index.html
capitulo1.html
css/
js/
images/
```

Añadimos y hacemos commit:

```bash
git add .
git commit -m "Snapshot web inicial"
```

Subimos la rama:

```bash
git push -u origin web-prod
```

---

# 8. Qué significa realmente `orphan`

En `main` tenemos:

```text
A --- B --- C --- D
```

Y en `web-prod`:

```text
W1
```

No hay línea entre ambos historiales.

Eso quiere decir que `web-prod` **no tiene como padre al proyecto completo**.

Es literalmente una historia independiente.

---

# 9. Clonar solo la web en IONOS / 1&1

Supongamos que queremos desplegar en:

```text
/home/usuario/public_html
```

Desde su directorio padre:

```bash
cd /home/usuario
```

Clonamos:

```bash
git clone \
  --branch web-prod \
  --single-branch \
  --depth 1 \
  git@github.com:TU_USUARIO/demo-libro.git \
  public_html
```

En una sola línea:

```bash
git clone --branch web-prod --single-branch --depth 1 git@github.com:TU_USUARIO/demo-libro.git public_html
```

El servidor recibe únicamente:

```text
index.html
capitulo1.html
css/
js/
images/
```

No recibe:

```text
latex/
pdf/
traducciones/
herramientas/
```

---

# 10. Comprobar que el clon es superficial

Dentro del servidor:

```bash
cd public_html
git log --oneline
```

Debería aparecer solo el commit web más reciente.

Podemos verificar además:

```bash
git rev-parse --is-shallow-repository
```

Resultado esperado:

```text
true
```

---

# 11. Actualizar la web en el futuro

Trabajamos normalmente en `main`:

```bash
git switch main
```

Actualizamos por ejemplo:

```text
web/capitulo1.html
web/images/nueva.jpg
```

Commit:

```bash
git add .
git commit -m "Actualizado capítulo 1"
git push
```

Después regeneramos el snapshot web:

```bash
rm -rf /tmp/web-deploy
mkdir /tmp/web-deploy
cp -R web/* /tmp/web-deploy/
```

Cambiamos a producción:

```bash
git switch web-prod
```

Limpiamos:

```bash
git rm -rf .
```

Copiamos la nueva versión:

```bash
cp -R /tmp/web-deploy/* .
```

Publicamos:

```bash
git add .
git commit -m "Publicación web actualizada"
git push
```

---

# 12. Actualizar IONOS

En el servidor:

```bash
cd /home/usuario/public_html
git pull --ff-only
```

Y listo.

El servidor solo descarga los cambios de `web-prod`.

---

# 13. Flujo visual

```text
┌──────────────────────────────┐
│            main              │
│                              │
│ HTML                         │
│ LaTeX                        │
│ PDF                          │
│ traducciones                 │
│ scripts                      │
└──────────────┬───────────────┘
               │
               │ extraer web terminada
               ▼
┌──────────────────────────────┐
│         web-prod             │
│         (orphan)             │
│                              │
│ HTML                         │
│ CSS                          │
│ JS                           │
│ imágenes                     │
└──────────────┬───────────────┘
               │
            git push
               ▼
        ┌─────────────┐
        │   GitHub    │
        └──────┬──────┘
               │
 git clone --single-branch
          --depth 1
               │
               ▼
┌──────────────────────────────┐
│         IONOS / 1&1          │
│                              │
│ index.html                   │
│ css/                         │
│ js/                          │
│ images/                      │
└──────────────────────────────┘
```

---

# 14. La combinación realmente potente

No es solo:

```bash
git clone -b web-prod
```

sino:

```bash
git clone --branch web-prod --single-branch --depth 1 ...
```

Porque:

- `--branch web-prod` selecciona la rama correcta.
- `--single-branch` evita traer otras ramas.
- `--depth 1` evita traer todo el historial.
- `web-prod` como `orphan` evita incluso tener parentesco histórico con `main`.

---

# 15. Rama normal vs orphan vs repo separado

| Solución | Historia unida a `main` | Fácil | Aislamiento |
|---|---:|---:|---:|
| Rama normal | Sí | Muy fácil | Medio |
| Rama orphan | No | Fácil | Alto |
| Repo separado | No | Algo más de gestión | Máximo |

Para este caso, **rama orphan + clone shallow** es una solución muy elegante.

---

# 16. Qué usaría yo

Para un libro con:

```text
HTML
LaTeX
PDF
multidioma
fuentes
scripts
recursos
```

y un servidor que solo necesita:

```text
HTML
CSS
JS
images
```

usaría:

```text
main
    proyecto completo

web-prod
    rama orphan
    solo resultado web
```

Y en IONOS:

```bash
git clone --branch web-prod --single-branch --depth 1 git@github.com:USUARIO/REPO.git public_html
```

Después, en cada despliegue:

```bash
cd public_html
git pull --ff-only
```

---

# 17. Idea clave

> **`main` contiene cómo se construye el libro; `web-prod` contiene únicamente lo que debe ver Internet.**

`main` es **el taller**.

`web-prod` es **el escaparate**.

Y 1&1 solo necesita el escaparate.
