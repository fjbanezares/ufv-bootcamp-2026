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

> [!NOTE]
> ### 🔍 ¿Qué significa la opción `-M` en `git branch -M main`?
> * **`-m`** viene de `--move` (renombrar una rama).
> * **`-M`** (en mayúscula) equivale a `--move --force` (**renombrado forzado**).
> 
> Al ejecutar `git init`, dependiendo de tu versión o configuración de Git, la rama inicial puede crearse con el nombre histórico `master`. Con `git branch -M main` renombras la rama en la que te encuentras a `main`. Si ya existiese una rama llamada `main`, la mayúscula **`-M` fuerza la sobrescritura** sin interrumpirte con un error de conflicto de nombres.

Configura el remoto usando **HTTPS** (recomendado para evitar errores de claves SSH):

```bash
git remote add origin https://github.com/TU_USUARIO/demo-libro.git
git push -u origin main
```

> [!IMPORTANT]
> **¿Por qué HTTPS y por qué me pide credenciales si el repo es público?**
> * **Repositorio público**: Cualquiera en Internet puede *leer y clonar* libremente sin autenticarse.
> * **Hacer `git push`**: Para *escribir o publicar cambios*, GitHub **siempre exige autenticación** (mediante tu usuario/token o `gh auth login`). De lo contrario, cualquiera podría sobreescribir tu repositorio.
> * Usando la URL **HTTPS** (`https://github.com/...`) no necesitas tener generadas ni vinculadas claves criptográficas SSH en tu Mac (`~/.ssh/id_ed25519`). Si usas la URL de SSH (`git@github.com:...`) sin haber configurado tu clave pública en GitHub, recibirás el error `Permission denied (publickey)`.

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

## Paso 4: Subir `main`, `web-prod` y el tag a GitHub

### ¿Cómo subir ambas ramas si estás en `web-prod`?
Si creaste la rama `web-prod` sin haber hecho push previo de `main`, puedes alternar fácilmente entre ellas:

```bash
# 1. Cambiar a main y subir el taller completo
git switch main
git push -u origin main

# 2. Regresar a la rama de producción
git switch web-prod

# 3. Subir la rama web-prod
git push -u origin web-prod

# 4. Subir la etiqueta (tag)
git push origin v1.0.0-web

# (O subir todos los tags existentes de una vez con: git push origin --tags)
```

---

## Paso 5: Despliegue en el servidor (Clon Selectivo)

En tu servidor de producción (IONOS / 1&1, VPS, etc.), ejecuta el comando de clonación selectiva en la carpeta de destino (`public_html` o similar).

### Opción A: Clonar SOLO la rama `web-prod`
```bash
git clone --branch web-prod --single-branch --depth 1 https://github.com/TU_USUARIO/demo-libro.git public_html
```

### Opción B: Clonar SOLO el Tag concreto (`v1.0.0-web`)
En Git, el parámetro `--branch` acepta tanto nombres de ramas como de **tags**:
```bash
git clone --branch v1.0.0-web --single-branch --depth 1 https://github.com/TU_USUARIO/demo-libro.git public_html
```

*(Si tu servidor tiene configurada autenticación SSH, puedes usar `git@github.com:TU_USUARIO/demo-libro.git` en lugar de la URL HTTPS).*

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

## Paso 8: Alternativa en el proyecto grande (Rama podada vs. Rama Orphan)

¿Qué pasa si en lugar de una rama huérfana (`orphan`), creas una rama normal a partir de `main` y simplemente borras los archivos sobrantes?

```bash
# 1. Crear una rama normal desde main:
git switch -c web-release

# 2. Eliminar del seguimiento todo lo que no pertenezca a la web:
git rm -r latex pdf traducciones herramientas
git commit -m "chore: podar archivos internos para release web"
```

### La diferencia crucial:
* **En la rama podada normal**: La fotografía actual solo tiene los archivos de la web, **pero el commit tiene como padre a `main`**. Los archivos grandes (PDF, LaTeX) siguen existiendo en los commits anteriores del árbol genealógico. Si alguien clona esa rama sin opciones especiales, **Git descargará a toda la familia histórica**.
* **En la rama `orphan`**: El commit **no tiene padre** (`parent = null`). Es una nueva raíz. No arrastra ni un solo byte del pasado.

---

## Paso 9: Secretos Internos de Git: ¿Por qué existe `shallow` y qué pasa en un `clone`?

> *"Llevo 15 años usando Git y no conocía este comportamiento. ¿Por qué no se enseña más a menudo?"*

### 1. ¿Qué descarga realmente un `git clone` por defecto?
Por defecto, Git es un sistema **distribuido puro (DVCS)**:
```bash
git clone https://github.com/usuario/repo.git
```
Este comando se descarga **TODO el Grafo Acíclico Dirigido (DAG)**:
* Todos los commits de la historia.
* Todas las ramas remotas (`origin/main`, `origin/dev`, etc.) y todos los tags.
* Todos los árboles (*trees*) y todos los archivos (*blobs*) que hayan existido alguna vez.
En tu carpeta de trabajo (*working tree*) solo ves los archivos de la rama por defecto, pero dentro de `.git/objects/` tienes la base de datos íntegra.

### 2. ¿En qué se basa poder bajar una rama independiente (`--single-branch`)?
Git mapea los remotos con una regla llamada *refspec*:
* Por defecto: `+refs/heads/*:refs/remotes/origin/*` (descarga todas las ramas).
* Con `--single-branch --branch web-prod`: Git configura el *refspec* para rastrear **únicamente** `refs/heads/web-prod`. El servidor omite enviar las referencias y objetos exclusivos de las otras ramas.

### 3. La trampa de los diferenciales ("La familia")
Git almacena sus datos en paquetes comprimidos llamados **Packfiles**. Los objetos se comprimen por delta (diferencias respecto a versiones previas).
Si una rama normal tiene 200 commits, para que tu cliente Git pueda reconstruir el archivo y validar su suma criptográfica SHA, el servidor te enviaría **toda la cadena de padres** hasta el commit inicial del proyecto ("toda la familia").

### 4. La magia de `--depth 1` (*Shallow Clone*)
Aquí entra la opción clave:
```bash
git clone --branch web-prod --single-branch --depth 1 ...
```
1. El servidor corta el árbol y genera en tu cliente un archivo especial llamado `.git/shallow`.
2. Ese archivo contiene el SHA del commit descargado y le dice a Git: **"Trata este commit como si fuera la raíz absoluta; no intentes buscar a sus padres"**.
3. El servidor empaqueta **exclusivamente** los blobs del árbol actual y te los envía.
4. **Resultado**: Reducción drástica del peso (en nuestra demo, de 220 KB a 72 KB; en proyectos reales, de gigabytes a unos pocos megabytes).

### 5. ¿Por qué no se enseña más a menudo?
* **Filosofía de desarrollo vs. despliegue**: A los desarrolladores se les enseña a tener el historial completo para poder trabajar sin conexión, usar `git log`, `git blame` o `git bisect`. Un clon superficial no permite ver el historial antiguo ni hacer ciertas operaciones de rebase complejo.
* **El estándar en la nube y CI/CD**: Aunque rara vez se explica en cursos básicos, **es el estándar indiscutible en producción**. Plataformas como GitHub Actions, GitLab CI, Vercel y Docker usan internamente `fetch-depth: 1` para no malgastar ancho de banda ni tiempo de CPU.

---

## Paso 10: Un Git dentro de otro Git (Ciclos de vida y dependencias)

Durante esta práctica hemos creado un repositorio `proyecto-demo` dentro del repositorio general del curso. ¿Cómo conviven y cómo se sincronizan?

### 1. Ciclos de vida independientes
Cada carpeta que contiene un directorio `.git` es un universo autónomo:
* `proyecto-demo` tiene su propio `origin` en GitHub (`demo-libro.git`), sus propias ramas (`main`, `web-prod`) y sus propios tags.
* El repositorio superior tiene su propio `origin` y su propia historia.

### 2. ¿Cómo se gestiona la dependencia al hacer `git pull`?
Hay dos formas profesionales de gestionarlo:

#### Enfoque A: Repositorio independiente ignorado (Sandbox / Práctica)
Si añades `proyecto-demo/` al `.gitignore` del repositorio padre:
* El padre se desentiende de él.
* Tú trabajas y haces `git pull` y `git push` dentro de `proyecto-demo` como un proyecto independiente.

#### Enfoque B: Git Submodule (`git submodule`)
Si el proyecto padre necesita formalmente al proyecto hijo como dependencia:
1. Se registra como submódulo:
   ```bash
   git submodule add https://github.com/TU_USUARIO/demo-libro.git submodulos/demo-libro
   ```
2. El repositorio padre **no guarda los archivos del hijo**, solo guarda un archivo `.gitmodules` y un **puntero (el SHA del commit del hijo)**.
3. **¿Cómo se hace el `git pull` coordinado?**:
   ```bash
   # Opción 1 (Directa): Actualizar el repo padre y todos sus submódulos a la vez:
   git pull --recurse-submodules
   git submodule update --remote --merge

   # Opción 2 (Paso a paso):
   # 1. Entras en el submódulo y traes sus novedades:
   cd submodulos/demo-libro
   git pull origin main

   # 2. Vuelves al repo padre y registras el nuevo puntero:
   cd ../..
   git add submodulos/demo-libro
   git commit -m "build: actualizar submódulo demo-libro a último commit"
   git push origin main
   ```

---

## Paso 11: Chuleta Estándar — Libro Multiformato (Web vs. Kindle KDP vs. LaTeX)

En un proyecto editorial completo sueles generar 3 salidas muy diferentes:
1. **Salida Web (HTML, CSS, JS, imágenes)**: Para lectura online, documentación o web del libro. Debe alojarse en **IONOS / 1&1**.
2. **Salida eBook (EPUB)**: Para Amazon Kindle (**KDP - Kindle Direct Publishing**) y lectores de libros digitales.
3. **Salida Impresa (LaTeX $\rightarrow$ PDF de alta resolución 300 DPI)**: Para impresión bajo demanda en Amazon KDP Print (tapa blanda/dura).

> [!WARNING]
> Si subes todo el repositorio con PDFs de imprenta, fuentes LaTeX y borradores al servidor de hosting, **superarás fácilmente 1 GB de peso inútil**, consumiendo ancho de banda, espacio en disco y ralentizando cualquier despliegue.

---

### ¿Cuál es la mejor estrategia para gestionar EPUB y LaTeX sin ensuciar IONOS?

| Canal | Destino | Dónde se guarda en Git | Estrategia recomendada |
|---|---|---|---|
| **Web** | Servidor IONOS | Rama `orphan` (`web-prod`) | Tag `edicion-1-web` $\rightarrow$ Clon shallow (`--single-branch --depth 1`) |
| **eBook (EPUB)** | Amazon KDP | Código fuente en `main` | Binario `.epub` subido como **Asset en GitHub Releases** |
| **Impreso (PDF)** | Amazon KDP Print | Fuentes `.tex` en `main` | Binario `.pdf` (300 DPI) subido como **Asset en GitHub Releases** |

#### Regla de oro para EPUB y LaTeX/PDF:
* **En `main` se versionan las fuentes**, no los binarios generados pesados:
  Añade a tu `.gitignore` los archivos compilados:
  ```gitignore
  *.pdf
  *.epub
  *.aux
  *.log
  *.out
  ```
* **Para entregar a Amazon KDP**:
  Cuando cierres una versión editorial, creas un tag en `main` y publicas una **GitHub Release**:
  ```bash
  git tag -a edicion-1-kdp -m "Archivos maestros para Amazon KDP - 1ª Edición"
  git push origin edicion-1-kdp
  ```
  Desde la interfaz de GitHub (o con `gh release create edicion-1-kdp libro.epub libro-interior.pdf portada.pdf`), adjuntas los binarios finales. De esta forma tienes los archivos listos para descargar y subir a KDP **sin inflar el repositorio Git ni tu servidor IONOS**.

---

### Chuleta Paso a Paso: Desde Local hasta la Terminal SSH de IONOS

Usa estos nombres genéricos sustituyendo las variables en mayúsculas:

#### A. En tu máquina local (Crear instantánea web y etiquetar edición):

```bash
# 1. Asegurar que main está al día
git switch main
git push origin main

# 2. Extraer solo los archivos web finales a una carpeta temporal
rm -rf /tmp/web-deploy && mkdir /tmp/web-deploy
cp -R ruta/a/salida-html/* /tmp/web-deploy/

# 3. Crear rama orphan para la web (o switch si ya existe)
git switch --orphan web-prod
git rm -rf .
cp -R /tmp/web-deploy/* .
git add .
git commit -m "build: compilación web para primera edición"

# 4. Etiquetar con la edición correspondiente
git tag -a edicion-1-web -m "Primera edición web del libro"

# 5. Subir rama y tag a GitHub
git push -u origin web-prod
git push origin edicion-1-web
```

> **Para la Segunda Edición en el futuro:**
> Repites el proceso en la rama `web-prod`, haces commit de los nuevos archivos y creas el tag:
> `git tag -a edicion-2-web -m "Segunda edición web del libro"` y `git push origin edicion-2-web`.

---

#### B. En la Terminal SSH de IONOS / 1&1 (Clon Selectivo Shallow):

Conéctate a tu servidor IONOS mediante SSH:

```bash
ssh USUARIO_SSH@DOMINIO_O_IP
# Ejemplo: ssh u12345678@home123456789.1and1-data.host
```

Una vez dentro de la terminal de IONOS:

```bash
# 1. Ir al directorio donde apunta el dominio web
cd /homepages/xx/u123456789/htdocs
# (o la ruta de tu carpeta: cd ~/public_html o cd ~/mi-sitio-web)

# 2. CLON SELECTIVO ULTRALIGERO del tag exacto (1ª Edición):
git clone \
  --branch edicion-1-web \
  --single-branch \
  --depth 1 \
  https://github.com/TU_USUARIO/TU_REPOSITORIO.git \
  .
```

*(El punto `.` al final clona los archivos directamente en el directorio actual sin crear una subcarpeta).*

```bash
# 3. Comprobación instantánea de ligereza:
ls -la
# Verás ÚNICAMENTE index.html, css/, js/ (nada de LaTeX, EPUB ni PDFs pesados)

du -sh .git
# Ocupa apenas unos kilobytes en lugar de cientos de megabytes
```

---

#### C. Actualizar IONOS cuando publiques la Segunda Edición (`edicion-2-web`):

Desde la terminal SSH de IONOS, sin tener que borrar ni volver a clonar todo:

```bash
# 1. Descargar solo la información del nuevo tag
git fetch --tags --depth 1 origin edicion-2-web

# 2. Cambiar a los archivos de la segunda edición
git checkout tags/edicion-2-web
```

---

## Paso 12: Arquitectura de Imágenes y Assets Compartidos (Web, EPUB y LaTeX)

En un libro real surge una duda habitual: **¿Qué pasa con las imágenes que se usan a la vez en la Web, en el PDF (LaTeX) y en el EPUB?**

### 1. La fuente de la verdad en `main` (El Taller)
Las imágenes maestras deben vivir en un único lugar dentro del repositorio de desarrollo (`main`):

```text
mi-libro/ (rama main)
├── recursos/imagenes/        <-- FUENTE ÚNICA (Alta resolución)
│   ├── diagrama1.png
│   └── portada.png
├── latex/                    <-- Las incluye: \includegraphics{../recursos/imagenes/diagrama1.png}
├── epub/                     <-- El script de Pandoc/eBook las enlaza desde recursos/imagenes/
└── web/                      <-- Contiene las versiones optimizadas para navegador
    └── images/
```

### 2. Flujo abstracto hacia la rama `orphan`
No quieres subir a IONOS imágenes TIFF o PNG de imprenta a 300 DPI (eso inflaría la web a cientos de megabytes). Por tanto:
1. En el script o proceso de build en local, las imágenes necesarias para la web se copian (u optimizan a WebP/JPG ligero) dentro de la carpeta `web/images/`.
2. Al generar la instantánea para `web-prod`, la carpeta `images/` viaja a la raíz de la rama huérfana:
   ```text
   web-prod/ (rama orphan en GitHub y en IONOS)
   ├── index.html
   ├── css/
   ├── js/
   └── images/                <-- Solo las imágenes que la web necesita para renderizar
   ```
3. **Resultado**: LaTeX y KDP usan las imágenes de alta resolución en `main`, mientras que el servidor IONOS solo recibe las imágenes optimizadas para la web dentro de su rama huérfana.

---

## Paso 13: El mito de "borrar y volver a copiar" — ¿Por qué Git SÍ aprovecha los Deltas?

> *"Si para la versión 2 borramos todo con `git rm -rf .` y copiamos desde `/tmp` lo nuevo... ¿no lo verá Git como archivos totalmente nuevos perdiendo el ahorro de deltas?"*

**Rotundamente NO.** Aquí es donde se aprecia la genialidad del diseño interno de Git.

### 1. Git no almacena archivos; almacena contenido (*Blobs*)
Git es un **sistema de almacenamiento direccionable por contenido** (*Content-Addressable Storage*):
* A Git **no le importan los inodos del disco, ni la fecha de creación, ni si el archivo fue copiado desde `/tmp`**.
* Git calcula el hash criptográfico SHA (SHA-1 o SHA-256) del **contenido** exacto de cada archivo.

### 2. Qué ocurre por dentro al hacer `git add .` en la 2ª edición:
Imagina que de 50 archivos de tu libro web, en la 2ª edición solo modificas 3 capítulos:

| Archivo | Qué hace Git internamente | Espacio añadido en Git |
|---|---|---|
| **47 archivos sin cambios** (imágenes, CSS, JS, etc.) | El hash SHA es **idéntico al de la 1ª edición**. Git no almacena nada nuevo; simplemente reutiliza el puntero existente en el árbol (*Tree*). | **0 bytes** (reutilización total). |
| **3 capítulos modificados** | Git detecta que la ruta es la misma (`capitulo1.html`). Al empaquetar, el motor de Git calcula un **delta** (diferencias de líneas) entre el contenido viejo y el nuevo. | **Solo los bytes de las palabras modificadas**. |
| **Páginas que eliminaste en la 2ª edición** | Git detecta que ya no están presentes y registra la eliminación en el commit. | **0 bytes**. |

### 3. ¿Por qué usamos entonces `git rm -rf .` y `cp`?
Hacemos `git rm -rf .` antes de copiar lo nuevo por un único motivo: **detectar archivos borrados**.  
Si en la 2ª edición eliminaste una página antigua o renombraste un archivo, vaciar el índice antes de restaurar garantiza que los archivos obsoletos no se queden flotando como basura huérfana en tu servidor web.

**En resumen**: Aunque vacíes y copies desde `/tmp`, Git reconoce instantáneamente todo el contenido previo idéntico y calcula deltas mínimos para el texto modificado.

---

## Resumen Express de comandos

```bash
# EN TU MÁQUINA LOCAL:
# 1. Taller principal (main)
git branch -M main
git remote add origin https://github.com/TU_USUARIO/demo-libro.git
git push -u origin main

# 2. Escaparate de producción (web-prod con tag de edición)
git switch --orphan web-prod
git rm -rf .
cp -R /tmp/web-deploy/* .
git add . && git commit -m "v1.0.0 web"
git tag -a edicion-1-web -m "Primera edición web"
git push -u origin web-prod --tags

# EN LA TERMINAL SSH DE IONOS / VPS:
ssh USUARIO_SSH@SERVIDOR_IONOS
cd ~/public_html
git clone --branch edicion-1-web --single-branch --depth 1 https://github.com/TU_USUARIO/demo-libro.git .
```

