# 🐙 Git Desde Cero: El Manual Definitivo de Control de Versiones
### *Curso Profundo, Visual y 100% Práctico con Mini-Prácticas Flash en Terminal*

---

> **¿Por qué este curso es diferente?**  
> Muchas personas intentan aprender Git memorizando comandos como si fueran conjuros mágicos (`git add .`, `git commit -m "fix"`, `git push origin main`), rezando para no ver un error en rojo. Cuando aparece un conflicto o un mensaje de *Detached HEAD*, cunde el pánico y terminan borrando la carpeta para clonarla de nuevo.
>
> Este manual existe para que eso **no te vuelva a pasar jamás**.  
> A través de **10 láminas visuales**, explicaciones de arquitectura interna y **mini-prácticas flash paso a paso**, entenderás exactamente cómo piensa Git. Cuando entiendes el modelo mental de Git, cualquier problema se vuelve predecible, fácil y resoluble.

---

## 🧭 Índice del Curso

1. [Módulo 1: Por qué existe Git y qué problema resuelve](#módulo-1-por-qué-existe-git-y-qué-problema-resuelve)
2. [Módulo 2: Git Internals: Blobs, Trees, Commits y el DAG](#módulo-2-git-internals-blobs-trees-commits-y-el-dag)
3. [Módulo 3: El Flujo Diario: Working Directory, Stage y Repository](#módulo-3-el-flujo-diario-working-directory-stage-y-repository)
4. [Módulo 4: Stage vs Stash: Guardar sin perder el hilo](#módulo-4-stage-vs-stash-guardar-sin-perder-el-hilo)
5. [Módulo 5: Ramas (Branches), Merge y Resolución de Conflictos](#módulo-5-ramas-branches-merge-y-resolución-de-conflictos)
6. [Módulo 6: Repositorios Remotos y Colaboración en Equipo](#módulo-6-repositorios-remotos-y-colaboración-en-equipo)
7. [Módulo 7: Estrategias de Merge Avanzadas: Fast-Forward, No-FF, Squash y Octopus](#módulo-7-estrategias-de-merge-avanzadas-fast-forward-no-ff-squash-y-octopus)
8. [Módulo 8: HEAD, Detached HEAD y Viajar en el Tiempo](#módulo-8-head-detached-head-y-viajar-en-el-tiempo)
9. [Módulo 9: Rebase y Rebase Interactivo (`git rebase -i`)](#módulo-9-rebase-y-rebase-interactivo-git-rebase--i)
10. [Módulo 10: Seguridad, Flujos Profesionales y Hábitos de Oro](#módulo-10-seguridad-flujos-profesionales-y-hábitos-de-oro)

---

## Módulo 1: Por qué existe Git y qué problema resuelve

![Parte 1: Por qué existe Git y qué es](./git%20crash%20course/git1.png)

### 🎯 La Idea en Humano
Todos hemos pasado por esto: guardas un trabajo como `informe.doc`, luego `informe_final.doc`, luego `informe_final_revisado.doc`, y terminas con `informe_definitivo_v2_este_si_que_si.doc`.
- ¿Qué cambió entre la versión 2 y la 3? Nadie lo sabe.
- Si un compañero sobreescribe tu archivo, tu trabajo se pierde para siempre.

**Git es una máquina del tiempo colaborativa.** En lugar de duplicar archivos con nombres raros, Git mantiene un **único archivo** con un libro de registro invisible (la carpeta `.git`) donde cada cambio significativo queda sellado con fecha, autor y explicación.

### 🔬 Conceptos Mínimos Indispensables
1. **Repositorio (Repo):** Una carpeta ordinaria en tu disco duro a la que Git le ha añadido superpoderes de seguimiento.
2. **Commit:** Una foto instantánea (*snapshot*) del estado de tus archivos en un momento dado, acompañada de un mensaje descriptivo.
3. **Branch (Rama):** Una línea de trabajo independiente. Te permite probar ideas locas sin poner en riesgo la versión estable.
4. **Merge:** La acción de fusionar dos líneas de trabajo en una sola.
5. **Remote:** Una copia del repositorio alojada en la nube o en un servidor (como GitHub, GitLab o Bitbucket).

---

### ⚡ Mini-Práctica Flash 1: Tu Primer Repositorio en 60 Segundos

Abre tu terminal y ejecuta los siguientes comandos para crear un laboratorio de pruebas:

```bash
# 1. Creamos una carpeta vacía para experimentar y entramos en ella
mkdir sandbox_git && cd sandbox_git

# 2. Convertimos esta carpeta en un repositorio oficial de Git
git init

# 3. Observa lo que ha ocurrido tras bambalinas
ls -la
```
* **¿Qué acaba de pasar?**: Verás una carpeta oculta llamada `.git/`. Esa carpeta es el cerebro de Git. Mientras exista esa carpeta, cada cambio que ocurra aquí dentro podrá ser recordado para siempre.

---

## Módulo 2: Git Internals: Blobs, Trees, Commits y el DAG

![Parte 2: Internals: cómo guarda Git la información](./git%20crash%20course/git2.png)

### 🎯 La Idea en Humano
Mucha gente cree que Git guarda "diferencias entre líneas" (*diffs*). **Falso.**  
Git es en realidad un **almacén de contenido direccionable por clave-valor**:
- Toma el contenido de un archivo.
- Calcula su huella digital criptográfica única usando el algoritmo **SHA-1** (un código de 40 caracteres hexadecimales como `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`).
- Si dos archivos en carpetas distintas tienen exactamente el mismo contenido, Git **solo guarda una copia** y le asigna el mismo hash.

### 🔬 Los 4 Objetos Sagrados de Git
1. **Blob (*Binary Large Object*):** Guarda únicamente los bytes del contenido de un archivo (no guarda su nombre ni sus permisos).
2. **Tree:** Representa un directorio. Contiene una lista de punteros a *Blobs* (con sus nombres de archivo reales) y a otros *Trees* (subdirectorios).
3. **Commit:** Contiene un puntero al *Tree* raíz de tu proyecto, los metadatos (quién eres, fecha, hora), el mensaje del commit y un puntero al **commit padre**.
4. **Tag:** Una etiqueta fija que apunta a un commit específico (usualmente para marcar versiones: `v1.0.0`).

### 🕸️ El DAG (*Directed Acyclic Graph*)
Los commits forman un **Grafo Acíclico Dirigido**:
- **Dirigido:** Cada commit sabe quién es su padre (la flecha apunta hacia el pasado).
- **Acíclico:** Es imposible viajar hacia el pasado y convertirte en el padre de tu propio abuelo (no hay bucles infinitos).

---

### ⚡ Mini-Práctica Flash 2: Hackeando las Entrañas de `.git`

Vamos a mirar por el agujero de la cerradura de la base de datos de Git:

```bash
# 1. Escribimos una frase en un archivo
echo "Git no es magia, es estructura de datos" > frase.txt

# 2. Lo agregamos al escenario
git add frase.txt

# 3. ¿Dónde guardó Git ese contenido? Usemos la herramienta interna cat-file
# Primero buscamos el hash del archivo en el index:
git ls-files -s
```
Verás una línea parecida a:
`100644 4c8c0f... 0 frase.txt`

Copia los primeros caracteres de ese hash (por ejemplo `4c8c0f`) y pregúntale a Git qué tipo de objeto es y qué contiene:
```bash
# Preguntar el tipo de objeto (-t)
git cat-file -t 4c8c0f

# Leer el contenido exacto almacenado (-p de pretty-print)
git cat-file -p 4c8c0f
```
* **¡Sorpresa!**: `git cat-file -t` te responderá `blob`, y `git cat-file -p` imprimirá exactamente tu texto. Has leído directamente la base de datos interna de Git sin intermediarios.

---

## Módulo 3: El Flujo Diario: Working Directory, Stage y Repository

![Parte 3: Flujo diario: working directory, stage y commit](./git%20crash%20course/git3.png)

### 🎯 La Idea en Humano
Para guardar un archivo en Git no basta con pulsar `Ctrl + S`. Tu código pasa por **3 estados o habitaciones**:

```
[ 1. Working Directory ]  ➔ (git add) ➔  [ 2. Staging Area ]  ➔ (git commit) ➔  [ 3. Repository ]
  (Tu mesa de trabajo)                    (La caja de mudanza)                    (El camión sellado)
```

1. **Working Directory (Directorio de Trabajo):** Son los archivos físicos que ves y editas en tu editor (VS Code, terminal, etc.). Aquí los cambios están "en sucio".
2. **Staging Area / Index (Área de Preparación):** Es la caja de mudanzas. Aquí eliges con pinzas **qué cambios específicos** formarán parte del próximo paquete.
3. **Repository (Historial Local):** Cuando haces `git commit`, la caja se sella con cera caliente, se le asigna un número de serie (hash) y se guarda en el historial permanente.

### 🏆 La Regla de Oro del Buen Commit (Commits Atómicos)
Un mal commit mezcla 5 cosas no relacionadas: *"Cambié el botón de login, arreglé un bug de la base de datos y cambié el color del fondo"*. Si luego el login falla, ¿cómo reviertes solo esa parte?
- **Un commit debe resolver UNA sola cosa.**
- Debe ser pequeño, coherente y tener un mensaje que explique **el porqué**, no solo el qué.

---

### ⚡ Mini-Práctica Flash 3: Dominando el Trío `status`, `diff` y `commit`

```bash
# 1. Creamos dos archivos
echo "print('Hola Mundo')" > app.py
echo "SECRET_KEY=12345" > config.env

# 2. Preguntamos el estado del proyecto
git status
```
*Observa:* Ambos archivos aparecen en rojo bajo "Untracked files" (fuera del escenario).

```bash
# 3. Añadimos SOLO el archivo de código, dejando fuera el archivo de claves
git add app.py
git status
```
*Observa:* `app.py` está en verde ("Changes to be committed"), mientras que `config.env` sigue en rojo. ¡Tú tienes el control total de lo que entra al commit!

```bash
# 4. Modificamos app.py para ver qué hace git diff
echo "print('Hola Mundo Bienvenidos al Bootcamp')" > app.py

# Comparamos el área de trabajo con el staging area:
git diff

# Comparamos lo que ya está en staging con el último commit:
git diff --staged

# 5. Sellamos el commit
git add app.py
git commit -m "feat: añadir saludo inicial en app.py"

# 6. Inspeccionamos el árbol de historia
git log --oneline
```

---

## Módulo 4: Stage vs Stash: Guardar sin perder el hilo

![Parte 4: Stage vs Stash: guardar sin perder el hilo](./git%20crash%20course/git4.png)

### 🎯 La Idea en Humano
Imagina que estás en mitad de una tarea compleja modificando 4 archivos a la vez. De repente, entra tu jefe o profesor por la puerta:  
> *"¡Emergencia! Hay un error crítico en producción y tienes que arreglarlo ahora mismo en otra rama."*

- Tu código actual está a medio escribir, no compila y no quieres hacer un commit chapucero como `"wip asdf no compila"`.
- Tampoco puedes cambiar de rama porque Git te impedirá moverte si hay cambios sucios sin guardar.

**La solución es `git stash` (El cajón de sastre):**  
`git stash` coge todos tus cambios a medio hacer, los mete en un cajón temporal y deja tu directorio de trabajo completamente limpio. Haces el arreglo urgente, y cuando termines, abres el cajón y recuperas exactamente donde te habías quedado.

### 🛠️ Comandos Esenciales de Stash
- `git stash`: Guarda los cambios sucios en el cajón.
- `git stash list`: Lista todo lo que tienes guardado en el cajón.
- `git stash apply`: Aplica los cambios guardados pero los mantiene en el cajón.
- `git stash pop`: Aplica los cambios y **los elimina del cajón** (la opción más común).
- `git stash push -m "mensaje"`: Guarda en el cajón con una etiqueta descriptiva (ej. `"trabajo en UI botones"`).

---

### ⚡ Mini-Práctica Flash 4: El Simulacro de la Emergencia

```bash
# 1. Empezamos a modificar app.py pero dejamos el código a medias
echo "def funcion_incompleta():" >> app.py
echo "    # falta programar todo" >> app.py
git status

# 2. ¡Llega la urgencia! Guardamos en el cajón con mensaje descriptivo
git stash push -m "WIP: desarrollo de nueva función"

# 3. Comprobamos cómo quedó el archivo
cat app.py
git status
```
*¡Magia!*: El archivo volvió al estado del último commit. El código roto ha desaparecido de la vista.

```bash
# 4. Miramos dentro del cajón
git stash list

# 5. Pasó la emergencia: recuperamos nuestro trabajo intacto
git stash pop
cat app.py
```
Tus líneas incompletas han vuelto a tu editor exactamente como las dejaste. Limpiamos descartando los cambios con:
```bash
git restore app.py
```

---

## Módulo 5: Ramas (Branches), Merge y Resolución de Conflictos

![Parte 5: Branches, merge y conflictos](./git%20crash%20course/git5.png)

### 🎯 La Idea en Humano
Una **rama (branch)** en Git no es una carpeta duplicada ni una copia pesada de tu disco duro.  
En las entrañas de Git, una rama es simplemente **un archivo de texto de 41 bytes que contiene el hash del último commit**. ¡Crear una rama cuesta menos de un milisegundo!

Las ramas te dan la libertad de equivocarte sin consecuencias:
- La rama `main` guarda el código estable y funcional.
- Creas una rama `feature/login` para desarrollar una novedad.
- Si la idea no funciona, borras la rama y `main` sigue virgen e impecable.
- Si funciona, haces un **`merge`** para unir los caminos.

### 💥 ¿Qué es un Conflicto y por qué no debes temerlo?
Un conflicto ocurre cuando dos ramas han modificado **las mismas líneas exactas del mismo archivo** con contenidos distintos, y le pides a Git que las una.  
Git no puede adivinar cuál de las dos versiones es la correcta. En lugar de tirar una moneda al aire, Git se detiene, marca el archivo con banderas de conflicto y te dice con humildad:  
> *"Humano: he unido todo lo demás automáticamente, pero aquí tenéis dos ideas contradictorias. Elige tú cuál se queda."*

---

### ⚡ Mini-Práctica Flash 5: Provocando y Resolviendo un Conflicto Real

Vamos a provocar un conflicto a propósito para perderle el miedo para siempre:

```bash
# 1. Aseguramos un commit inicial en main
echo "Color de fondo: Blanco" > diseno.txt
git add diseno.txt
git commit -m "chore: diseno inicial blanco"

# 2. Creamos una rama llamada 'modo-oscuro' y nos cambiamos a ella
git switch -c modo-oscuro

# 3. En esta rama cambiamos el color a Negro y confirmamos
echo "Color de fondo: Negro Medianoche" > diseno.txt
git commit -am "feat: cambiar diseno a negro medianoche"

# 4. Regresamos a la rama main
git switch main

# 5. En main alguien decide cambiar el color a Azul Marino y confirma
echo "Color de fondo: Azul Marino" > diseno.txt
git commit -am "fix: cambiar diseno a azul marino"

# 6. ¡Llega el momento de la verdad! Intentamos fusionar modo-oscuro en main
git merge modo-oscuro
```

Verás este mensaje de Git:
`CONFLICT (content): Merge conflict in diseno.txt`  
`Automatic merge failed; fix conflicts and then commit the result.`

#### ¿Cómo se resuelve?
Abre `diseno.txt` con `cat diseno.txt`. Verás las marcas del conflicto:

```text
<<<<<<< HEAD
Color de fondo: Azul Marino
=======
Color de fondo: Negro Medianoche
>>>>>>> modo-oscuro
```
- Lo que está entre `<<<<<<< HEAD` y `=======` es lo que había en tu rama actual (`main`).
- Lo que está entre `=======` y `>>>>>>> modo-oscuro` es lo que viene de la otra rama.

```bash
# 7. Editamos el archivo para dejar la decisión final limpia (por ejemplo, nos quedamos con ambos o uno)
echo "Color de fondo: Negro Medianoche con acentos en Azul Marino" > diseno.txt

# 8. Le decimos a Git que el conflicto está resuelto haciendo add y cerrando el commit
git add diseno.txt
git commit -m "merge: resolver conflicto de diseno combinando negro y azul"

# 9. Comprobamos el árbol resultante
git log --oneline --graph
```
*¡Enhorabuena!*: Has resuelto tu primer conflicto con criterio técnico.

---

## Módulo 6: Repositorios Remotos y Colaboración en Equipo

![Parte 6: Remotos y colaboración](./git%20crash%20course/git6.png)

### 🎯 La Idea en Humano
Git es un sistema **distribuido**. Esto significa que tu ordenador tiene el 100% de la historia del proyecto; no necesita conexión a internet para hacer commits, ver logs ni crear ramas.  
Los servidores remotos (como GitHub) actúan como el punto de encuentro del equipo.

La regla mnemotécnica de los 3 verbos remotos:
> 👁️ **`git fetch` es MIRAR:** Consulta qué cambios hay en el servidor remoto y los descarga a tu máquina, pero **NO toca tus archivos locales**.  
> 🔄 **`git pull` es ACTUALIZAR:** Es un `fetch` seguido de un `merge`. Trae los cambios remotos y los fusiona directamente en tu rama actual.  
> 🚀 **`git push` es COMPARTIR:** Envía tus commits locales al servidor remoto para que tus compañeros puedan verlos.

### 🚫 El Clásico Error: «[rejected - non-fast-forward]»
Intentas hacer `git push` y GitHub te escupe un error:  
`! [rejected] main -> main (fetch first)`  
`error: failed to push some refs...`

**¿Por qué pasa esto?** Porque un compañero de equipo subió commits antes que tú. El remoto está por delante. Git no permitirá que sobreescribas el trabajo de tu compañero a ciegas.  
**Solución:** Primero haces `git pull` (o `git pull --rebase`), integras sus cambios en local, y luego vuelves a hacer `git push`.

---

### ⚡ Mini-Práctica Flash 6: Simulación de Trabajo en Pareja (2 Clones Locales)

¿Sabías que puedes simular un GitHub remoto en tu propio disco duro usando dos carpetas?

```bash
# 1. Salimos de sandbox_git y creamos una carpeta para que actúe de servidor remoto "central"
cd ..
git init --bare servidor_central.git

# 2. Entramos en nuestro repo original y lo vinculamos a ese "servidor"
cd sandbox_git
git remote add origin ../servidor_central.git

# 3. Subimos nuestro código
git push -u origin main

# 4. Ahora simulamos a una compañera de equipo (Sofía) clonando el repo en otra carpeta
cd ..
git clone servidor_central.git repo_sofia
cd repo_sofia

# 5. Sofía hace un cambio y lo sube al servidor
echo "Función creada por Sofía" >> sofia.txt
git add sofia.txt && git commit -m "feat: aportación de Sofía"
git push origin main

# 6. Regresamos a nuestro propio repositorio
cd ../sandbox_git

# Usamos fetch para inspeccionar qué hizo Sofía sin alterar nuestros archivos
git fetch origin
git log --oneline origin/main

# Ahora sí, actualizamos nuestro directorio con pull
git pull origin main
ls -la
```
*Observa:* `sofia.txt` ya está en tu carpeta. ¡Has completado un ciclo colaborativo profesional completo!

---

## Módulo 7: Estrategias de Merge Avanzadas: Fast-Forward, No-FF, Squash y Octopus

![Parte 7: Merges avanzados: no-ff, squash y octopus](./git%20crash%20course/git7.png)

### 🎯 La Idea en Humano
Cuando fusionas ramas, tienes varias formas de escribir la historia. No hay una "mejor" que otra; cada una responde a una necesidad del equipo:

| Estrategia | Comando | Qué ocurre con los commits | Cuándo usarlo |
| :--- | :--- | :--- | :--- |
| **Fast-Forward (FF)** | `git merge rama` | La rama destino solo mueve su puntero en línea recta. No se crea ningún commit nuevo. | Tareas pequeñas donde nadie avanzó en `main` mientras trabajabas. |
| **No Fast-Forward** | `git merge --no-ff rama` | **Fuerza la creación de un commit de merge**, dejando dibujada la burbuja/curva de la rama en el gráfico. | En proyectos grandes donde quieres que quede constancia explícita de que una *feature* existió como rama. |
| **Squash Merge** | `git merge --squash rama` | Toma 15 commits ruidosos de tu rama (*"arreglo typo"*, *"probando"*, *"ahora sí"*) y los aplasta en **UN SOLO commit limpio** en `main`. | Pull Requests donde el historial interno de la rama era caótico y solo importa el resultado final. |
| **Octopus Merge** | `git merge ramaA ramaB ramaC` | Fusiona tres o más ramas simultáneamente en un solo commit. | Casos donde varias sub-ramas compatibles se integran al mismo tiempo. |

---

### ⚡ Mini-Práctica Flash 7: Probando el Squash Merge

```bash
# 1. Creamos una rama para una funcionalidad ruidosa
git switch -c feature/calculadora

# 2. Hacemos 3 commits pequeños y desordenados
echo "def suma(a, b): return a + b" >> calc.py && git add calc.py && git commit -m "wip: funcion suma"
echo "def resta(a, b): return a - b" >> calc.py && git add calc.py && git commit -m "fix: anadir resta"
echo "# Documentacion calculada" >> calc.py && git add calc.py && git commit -m "docs: anadir comentario"

# Comprobamos los 3 commits
git log --oneline -n 3

# 3. Regresamos a main y aplicamos SQUASH
git switch main
git merge --squash feature/calculadora

# 4. Fíjate en git status: los cambios están en Staging listos para un único commit maestro
git status
git commit -m "feat: implementar modulo completo de calculadora"

# 5. Comprobamos el log de main
git log --oneline -n 2
```
*El resultado:* En `main` no hay rastro del ruido ni de los commits intermedios; solo hay un único commit limpio y atómico.

---

## Módulo 8: HEAD, Detached HEAD y Viajar en el Tiempo

![Parte 8: HEAD, detached HEAD y viajar en el tiempo](./git%20crash%20course/git8.png)

### 🎯 La Idea en Humano
¿Qué es exactamente **HEAD**?  
Piensa en una cinta de cassette o en la aguja de un tocadiscos: **HEAD es el cabezal de lectura que indica en qué punto exacto del historial estás situado ahora mismo.**
- Normalmente, HEAD apunta al nombre de una rama (ej. `HEAD -> main`), y la rama apunta al último commit.
- Cuando haces un commit nuevo, la rama avanza y HEAD se mueve con ella.

### 👻 El Gran Miedo: ¿Qué es el *Detached HEAD*?
Si le dices a Git: `git checkout <hash_antiguo>`, el cabezal HEAD se despega de la rama y se coloca directamente sobre un commit del pasado.  
La terminal te soltará una advertencia intimidante:  
`You are in 'detached HEAD' state...`

**No te asustes:** No has roto nada. Estás en **modo espectador**:
- Puedes mirar los archivos como eran en ese commit histórico.
- Puedes compilar y probar si un bug ya existía en esa versión.
- **¿Cómo sales de ahí?**  
  - Si solo estabas mirando y quieres volver al presente:  
    `git switch main`
  - Si hiciste cambios en ese pasado y quieres conservarlos en una rama nueva:  
    `git switch -c rescate-de-ideas`

### 🧭 Navegación Relativa: Tildes y Sombreros (`~` y `^`)
- `HEAD~1`: El padre directo del commit actual (un commit atrás).
- `HEAD~2`: El abuelo (dos commits atrás).
- `HEAD~3`: Tres commits atrás.
- `HEAD^`: El primer padre. En un commit de merge (que tiene 2 padres), `HEAD^2` te lleva al segundo padre.

---

### ⚡ Mini-Práctica Flash 8: Entrar y Salir del Modo Espectador

```bash
# 1. Miramos el historial para copiar el hash del commit más antiguo
git log --oneline

# 2. Supongamos que el primer commit tiene el hash 'a1b2c3d' (usa tu propio hash del log)
PRIMER_HASH=$(git rev-list --max-parents=0 HEAD)

# 3. Viajamos en el tiempo hacia ese commit
git checkout $PRIMER_HASH
```
Lee con atención el mensaje que emite Git: estás en *detached HEAD*. Comprueba tus archivos con `ls`: los archivos que creaste después han desaparecido temporalmente.

```bash
# 4. Comprobamos dónde apunta HEAD
git status

# 5. Volver al presente sano y salvo con un solo comando:
git switch main
ls
```
Todos tus archivos del presente están de vuelta inmediatamente.

---

## Módulo 9: Rebase y Rebase Interactivo (`git rebase -i`)

![Parte 9: Rebase e interactive rebase](./git%20crash%20course/git9.png)

### 🎯 La Idea en Humano
Tanto `merge` como `rebase` sirven para integrar cambios entre ramas, pero con filosofías opuestas:
- **`merge` conserva la historia real y la topología:** Muestra con orgullo cuándo se bifurcaron las ramas y cuándo se unieron, creando un commit de merge.
- **`rebase` reescribe la historia para que sea lineal:** Coge tus commits, los levanta del árbol y los vuelve a plantar encima del último commit de la otra rama, como si hubieras empezado a programar hoy mismo.

### 🪄 El Superpoder: Rebase Interactivo (`git rebase -i`)
Es el procesador de textos del historial de Git. Te permite tomar los últimos commits que hiciste en local y limpiarlos antes de compartirlos con el equipo:
- **`reword` (r):** Cambiar el mensaje de un commit antiguo para corregir una errata.
- **`squash` (s):** Fundir este commit con el anterior combinando sus mensajes.
- **`fixup` (f):** Fundir este commit con el anterior descartando el mensaje secundario.
- **`drop` (d):** Borrar por completo un commit erróneo de la historia.
- **Reordenar:** Cambiar el orden de las líneas en el editor para cambiar el orden cronológico de los commits.

> ⚠️ **La Regla de Oro del Rebase:**  
> **NUNCA hagas rebase sobre commits que ya hayas subido (`push`) a una rama pública compartida por otras personas.** Reescribirás la historia y provocarás que tus compañeros tengan hashes incompatibles. Úsalo solo en tus ramas locales antes de hacer push.

---

### ⚡ Mini-Práctica Flash 9: Editando el Pasado con Rebase Interactivo

```bash
# 1. Creamos 3 commits para practicar la cirugía de historial
echo "Paso 1" >> notas.txt && git add notas.txt && git commit -m "feat: paso 1"
echo "Paso 2 con errata" >> notas.txt && git add notas.txt && git commit -m "feat: pasooo 2 con errata"
echo "Paso 3" >> notas.txt && git add notas.txt && git commit -m "feat: paso 3"

# 2. Lanzamos el rebase interactivo sobre los últimos 3 commits
# (Nota: Se abrirá tu editor por defecto, como nano o vim)
git rebase -i HEAD~3
```

En la pantalla del editor verás algo así:
```text
pick 1a2b3c feat: paso 1
pick 4d5e6f feat: pasooo 2 con errata
pick 7g8h9i feat: paso 3
```
- Cambia la palabra `pick` del segundo commit por **`reword`** (o simplemente `r`).
- Guarda y cierra el editor.
- Git se detendrá en ese commit y te abrirá una nueva ventana para corregir el texto: cambia `pasooo 2 con errata` por `feat: paso 2 corregido`.
- Guarda y listo:
```bash
git log --oneline -n 3
```
El historial ha quedado corregido limpiamente.

---

## Módulo 10: Seguridad, Flujos Profesionales y Hábitos de Oro

![Parte 10: Seguridad, trabajo real y temas avanzados](./git%20crash%20course/git10.png)

### 🎯 La Idea en Humano
Llegar a nivel profesional en Git no es saberse 100 comandos oscuros; es **saber proteger el código y a las personas del equipo**:

### 1. `git commit --amend` (El botón de deshacer inmediato)
¿Acabas de hacer un commit y te diste cuenta de que olvidaste incluir un archivo o escribiste mal el mensaje?
```bash
git add archivo_olvidado.py
git commit --amend --no-edit
```
Git incorporará el cambio **dentro del último commit**, sin crear un commit extra innecesario.

### 2. `push --force` vs `push --force-with-lease`
Si alguna vez reescribes tu historial local y necesitas forzar la subida a tu rama remota:
- ❌ **`git push --force` (El bulldozer ciego):** Sobrescribe el remoto sin importar si un compañero de equipo subió código hace 5 minutos. Puedes destruir trabajo ajeno para siempre.
- ✅ **`git push --force-with-lease` (El profesional precavido):** Solo forzará la subida si nadie ha modificado la rama remota desde tu última lectura. Si alguien subió algo, el comando abortará para protegerlo.

### 3. Git Hooks: Automatización previa
En `.git/hooks/` residen scripts ejecutables que saltan automáticamente ante eventos de Git. El más famoso es el hook **`pre-commit`**, que puede ejecutar linters de estilo o baterías de tests automáticas impidiendo el commit si el código tiene fallos de sintaxis.

---

### 🏆 Los 10 Hábitos de Oro del Desarrollador Profesional

1. **Commits pequeños y frecuentes:** Es diez veces más fácil revisar o revertir 5 commits pequeños que uno gigantesco de 1.000 líneas.
2. **Mensajes claros y con intención:** Usa convenciones como *Conventional Commits* (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`).
3. **Ramas cortas:** No dejes una rama abierta durante tres semanas; intégrala pronto para minimizar conflictos.
4. **`git fetch` frecuente:** Entérate de lo que hace tu equipo antes de que sea tarde.
5. **Revisar antes de empujar:** Haz `git status` y `git diff` antes de cada commit y push.
6. **Resolver conflictos con calma:** No borres código de tus compañeros sin preguntarles si tienes dudas.
7. **No reescribir ramas públicas:** Rebase en local, merge al compartir.
8. **Verificar antes de hacer force:** Usa siempre `--force-with-lease`.
9. **Branch Protection:** En GitHub, activa la protección de la rama `main` para exigir que todo cambio pase por una Pull Request revisada.
10. **Aprender leyendo el historial:** Acostúmbrate a usar `git log --graph --oneline --all` para ver la evolución arquitectónica de tus proyectos.

---

## 🧹 Limpieza del Laboratorio de Prácticas
Cuando hayas terminado todas las mini-prácticas y quieras dejar tu terminal limpia:
```bash
cd ..
rm -rf sandbox_git servidor_central.git repo_sofia
```
