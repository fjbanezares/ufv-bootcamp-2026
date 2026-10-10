# 🧭 Guía Definitiva de `git reset`: El Control del Tiempo en Git

> Una explicación profunda, visual y desde los primeros principios, sin dar nada por sabido.

---

## 🎨 Las 3 Infografías del Módulo

Esta guía acompaña y profundiza en las tres infografías de referencia incluidas en este directorio:

| 1. Las Tres Versiones | 2. Tres Formas de Volver Atrás | 3. Los 7 Usos Clave |
|---|---|---|
| [![Las tres versiones de Git](./Git%20reset_%20las%20tres%20versiones-1.png)](./Git%20reset_%20las%20tres%20versiones-1.png) | [![Tres formas de volver atrás](./Git%20reset_%20tres%20formas%20de%20volver%20atr%C3%A1s-2.png)](./Git%20reset_%20tres%20formas%20de%20volver%20atr%C3%A1s-2.png) | [![Los 7 usos de git reset](./Los%207%20usos%20de%20git%20reset-3.png)](./Los%207%20usos%20de%20git%20reset-3.png) |

---

## 1. Fundamentos Clave: Sin dar nada por sabido

Para entender `git reset` sin memorizar comandos mágicos, primero debemos comprender cómo piensa Git.

### 1.1 ¿Qué es un Commit?
Un commit **NO es una lista de diferencias (diffs)** guardada en un fichero; un commit es una **fotografía instantánea (*snapshot*)** completa de todo tu proyecto en un segundo concreto.

Cada commit contiene:
1. Un identificador único criptográfico (el hash SHA, ej: `8a3f12c`).
2. El árbol con la foto de todos los archivos (*Tree* y *Blobs*).
3. Un puntero al **commit anterior (su padre)**.

### 1.2 ¿Qué es una Rama (*Branch*)?
En Git, una rama **no es un contenedor de archivos**. Una rama es simplemente un **puntero móvil (un archivo de texto de 41 bytes)** que guarda el hash del último commit de esa línea temporal.

```text
[Commit A] <--- [Commit B] <--- [Commit C]
                                     ▲
                                   main  (solo una etiqueta que apunta a C)
```

### 1.3 ¿Qué es `HEAD`?
`HEAD` es el puntero que le dice a Git: **"Tú estás aquí ahora mismo"**.
Generalmente, `HEAD` apunta a la rama en la que estás trabajando:
$$\text{HEAD} \longrightarrow \text{main} \longrightarrow \text{Commit C}$$

---

## 2. Descifrando la Sintaxis Relativa: `HEAD~` vs `HEAD^`

Cuando queremos viajar en el tiempo, le decimos a Git a qué commit queremos regresar. Podemos usar su identificador hash (`git reset 8a3f12c`) o usar **referencias relativas respecto a `HEAD`**.

Aquí es donde mucha gente se confunde: ¿qué diferencia hay entre la virgulilla `~` (*tilde*) y el circunflejo `^` (*caret*)?

### 2.1 La virgulilla `~` (Saltos generacionales hacia atrás)
La virgulilla `~` significa **"retrocede $N$ generaciones hacia el pasado en línea directa"**:
* `HEAD~1` (o simplemente `HEAD~`): El **padre** inmediato del commit actual (1 paso atrás).
* `HEAD~2`: El **abuelo** (2 pasos atrás).
* `HEAD~3`: El **bisabuelo** (3 pasos atrás).

```text
Commit A <--- Commit B <--- Commit C (HEAD)
 HEAD~2        HEAD~1         HEAD
(abuelo)       (padre)       (actual)
```

### 2.2 El circunflejo `^` (Selección de padres en bifurcaciones y merges)
El circunflejo `^` tiene dos funciones según lleve número o no:

1. **Sin número o `^1`**: Significa exactamente lo mismo que `~1` (el primer padre).
   * `HEAD^` = `HEAD^1` = `HEAD~1` (el commit inmediatamente anterior).
   * `HEAD^^` = retrocede 2 pasos = `HEAD~2`.
2. **Con un número mayor a 1 (`HEAD^2`, `HEAD^3`)**: Se utiliza en **commits de fusión (*merge commits*)**, donde un commit tiene **más de un padre**:
   * `HEAD^1`: El commit padre de la **rama principal** donde se hizo el merge.
   * `HEAD^2`: El commit padre de la **rama secundaria** que fue fusionada.

```text
         Commit B (rama feature)
        /        \
Commit A          Commit M (Merge commit - HEAD)
        \        /
         Commit C (rama main)

HEAD~1  ó  HEAD^1  --> Commit C (primer padre, línea main)
           HEAD^2  --> Commit B (segundo padre, línea feature)
```

> [!TIP]
> **Regla nemotécnica rápida:**
> * Si quieres retroceder en el tiempo en una rama normal, usa siempre **`HEAD~N`** (ejemplo: `HEAD~1` para 1 commit atrás, `HEAD~3` para 3 atrás).
> * Solo necesitas `HEAD^2` cuando quieras viajar al padre secundario de un merge.

---

## 3. Las Tres Versiones de Git (Infografía 1)

Git gestiona tu proyecto a través de tres árboles o áreas de trabajo. `git reset` actúa directamente sobre ellas:

```text
┌───────────────────────┐      git add       ┌───────────────────────┐     git commit     ┌───────────────────────┐
│   WORKING DIRECTORY   │ ─────────────────> │         INDEX         │ ─────────────────> │      REPOSITORY       │
│  (Directorio local)   │                    │     (Staging Area)    │                    │        (HEAD)         │
│                       │ <───────────────── │                       │ <───────────────── │                       │
│ Archivos reales que   │     git checkout   │ El borrador listo     │     git reset      │ La cámara acorazada;  │
│ ves y editas en tu    │     git restore    │ para el commit        │                    │ el historial          │
│ editor (disco)        │                    │                       │                    │ confirmado            │
└───────────────────────┘                    └───────────────────────┘                    └───────────────────────┘
```

1. **Working Directory (Directorio de trabajo)**: Son los archivos físicos de tu disco que abres en VS Code. Aquí trabajas, creas funciones y guardas cambios.
2. **Index / Staging Area**: La antesala. Es una zona intermedia donde seleccionas cuidadosamente qué cambios formarán parte del próximo commit mediante `git add`.
3. **Repository (HEAD)**: El historial definitivo. Cuando haces `git commit`, la foto del Staging Area se almacena para siempre en la base de datos de Git y `HEAD` se mueve a esa nueva foto.

---

## 4. Las Tres Formas de Volver Atrás: `--soft`, `--mixed` y `--hard` (Infografía 2)

¿Qué hace en realidad `git reset <commit>`?
> **`git reset` mueve la rama actual y `HEAD` hacia un commit del pasado.**

La diferencia entre `--soft`, `--mixed` y `--hard` es **qué hace con el Staging Area y con tus archivos del disco al retroceder**.

```text
                             git reset HEAD~1
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
     --soft                      --mixed                     --hard
  (El suave)                  (El estándar)               (El destructor)
        │                           │                           │
  Solo mueve HEAD             Mueve HEAD y                Mueve HEAD,
  Conserva Staging            vacía el Staging.           vacía Staging y
  Conserva Disco              Conserva Disco              SOBREESCRIBE DISCO
        │                           │                           │
  Tus cambios quedan          Tus cambios quedan          Tus cambios
  listos para commit          como "no preparados"        SE PIERDEN
```

### Tabla Comparativa de Impacto

| Bandera | Mueve `HEAD` | ¿Qué pasa con el Staging (Index)? | ¿Qué pasa con el Disco (Working Dir)? | Nivel de Riesgo |
|---|:---:|:---:|:---:|:---:|
| **`git reset --soft`** | ✅ Sí | 🟢 **Se mantiene intacto** (los cambios siguen en verde). | 🟢 **No se toca nada**. | 🟢 Cero riesgo |
| **`git reset --mixed`** *(por defecto)* | ✅ Sí | 🟡 **Se vacía** (los cambios salen del staging). | 🟢 **No se toca nada** (quedan como modificaciones en disco). | 🟢 Cero riesgo |
| **`git reset --hard`** | ✅ Sí | 🔴 **Se vacía**. | 🔴 **Se borra todo**: los archivos vuelven al estado exacto del commit anterior. | 🔴 **Peligro de pérdida** |

---

## 5. Laboratorio Práctico: Experimenta los 3 modos en tu terminal

Vamos a crear un directorio temporal seguro para probar cada uno de los comandos y ver en directo qué ocurre en cada área.

### 5.0 Preparar el laboratorio
Abre una terminal y ejecuta:

```bash
# 1. Crear carpeta de pruebas
mkdir /tmp/laboratorio-reset && cd /tmp/laboratorio-reset
git init

# 2. Primer commit base
echo "Línea base v1" > app.txt
git add app.txt
git commit -m "feat: commit 1 (base)"

# 3. Segundo commit
echo "Nueva característica v2" >> app.txt
git add app.txt
git commit -m "feat: commit 2 (cambios que queremos revisar)"
```

Comprueba el historial:
```bash
git log --oneline
```
Verás dos commits: el `commit 1` y el `commit 2 (HEAD)`.

---

### Práctica 1: `git reset --soft HEAD~1` (Rehacer el commit)

**Objetivo:** Nos hemos equivocado en el mensaje del commit o queremos agruparlo. Queremos deshacer el commit pero **mantener los cambios listos en stage**.

```bash
git reset --soft HEAD~1
```

Ahora ejecuta:
```bash
git status
```
**Resultado observado:**
* Git te dice: `Changes to be committed: modified: app.txt` (en color verde).
* El commit 2 ha desaparecido del historial, pero tus cambios siguen preparados en el Staging Area.
* Puedes modificar lo que quieras, cambiar el mensaje y volver a hacer commit:
  ```bash
  git commit -m "feat: commit 2 con mejor descripción"
  ```

---

### Práctica 2: `git reset --mixed HEAD~1` (El modo por defecto)

**Objetivo:** Queremos deshacer el commit y además **sacar los archivos de la zona de preparación**, pero sin perder ni una sola línea de código escrita en el disco.

*(Hagamos un commit rápido para probarlo)*:
```bash
echo "Cambio extra para mixed" >> app.txt
git add app.txt
git commit -m "feat: commit 3 para prueba mixed"
```

Ahora ejecuta el reset por defecto:
```bash
git reset HEAD~1
# (equivale exactamente a: git reset --mixed HEAD~1)
```

Comprueba el estado:
```bash
git status
```
**Resultado observado:**
* Git te dice: `Changes not staged for commit: modified: app.txt` (en color rojo).
* El commit se deshizo.
* El Staging Area se vació.
* **Tus líneas de código siguen intactas en el archivo `app.txt` de tu disco.** Puedes revisarlas con `git diff`.

---

### Práctica 3: `git reset --hard HEAD~1` (El botón de reinicio nuclear)

**Objetivo:** Hicimos un experimento fallido, no sirve para nada y queremos destruir todo rastro de ese commit y volver al estado exacto del pasado.

*(Preparamos un commit experimental)*:
```bash
echo "CÓDIGO BASURA ROTO" >> app.txt
git add app.txt
git commit -m "experimento fallido que rompe todo"
```

Comprueba el contenido del archivo antes del reset:
```bash
cat app.txt
```

Ahora ejecutamos el reset duro:
```bash
git reset --hard HEAD~1
```

Comprueba el archivo y el estado:
```bash
cat app.txt
git status
```
**Resultado observado:**
* La línea `"CÓDIGO BASURA ROTO"` ha desaparecido por completo del disco.
* El commit ha desaparecido del historial.
* El working directory está limpio (`working tree clean`).

---

### Práctica 4: El salvavidas de oro: ¿Cómo resucitar un commit borrado con `--hard`?

> *"¡Acabo de hacer `git reset --hard` por error y he borrado un commit valioso! ¿Está perdido para siempre?"*

**No.** En Git, casi nada se destruye de inmediato. Git conserva un registro interno de cada movimiento de `HEAD` llamado **`reflog`**.

Pruébalo ahora mismo:
```bash
git reflog
```

Verás una salida similar a esta:
```text
8a3f12c HEAD@{0}: reset: moving to HEAD~1
b4e991a HEAD@{1}: commit: experimento fallido que rompe todo
8a3f12c HEAD@{2}: commit: feat: commit 2
```

Fíjate en el hash del commit que creías destruido (`b4e991a`). ¡Sigue vivo en la base de datos de Git!

Para resucitarlo y volver al estado previo al reset hard:
```bash
git reset --hard HEAD@{1}
# (o directamente: git reset --hard b4e991a)
```

Comprueba de nuevo tu archivo:
```bash
cat app.txt
```
¡Tu código y tu commit han resucitado intactos!

---

## 6. Los 7 Usos Clave de `git reset` (Infografía 3)

| Uso | Comando | Escenario real |
|---|---|---|
| **1. Deshacer un `git add`** | `git reset <archivo>` *(o `git restore --staged <archivo>`)* | Añadiste por error un archivo con contraseñas o un fichero temporal al stage y quieres sacarlo sin borrar tu trabajo. |
| **2. Rehacer el último commit** | `git reset --soft HEAD~1` | Hiciste commit demasiado rápido, olvidaste incluir un archivo o quieres cambiar el mensaje. |
| **3. Fusionar varios commits en uno (*Squash*)** | `git reset --soft HEAD~3` seguido de `git commit -m "feat: todo junto"` | Hiciste 3 commits pequeños locales ("wip", "arreglo typo", "ahora sí") y quieres empaquetarlos en un solo commit limpio antes de subir a GitHub. |
| **4. Descartar cambios locales no deseados** | `git reset --hard HEAD` | Modificaste varios archivos locales, las pruebas fallaron y quieres descartar todo para volver al último commit limpio. |
| **5. Borrar los últimos commits erróneos** | `git reset --hard HEAD~2` | Los dos últimos commits no sirven y quieres que la rama vuelva al estado de hace dos versiones. |
| **6. Abortar un merge conflictivo** | `git reset --hard HEAD` *(o `git merge --abort`)* | Intentaste un merge, aparecieron 40 conflictos inmanejables y quieres cancelar el intento volviendo al estado previo. |
| **7. Rescatar un archivo de un commit antiguo** | `git reset <commit_antiguo> -- ruta/al/archivo` | Quieres restaurar únicamente un archivo concreto a cómo estaba hace tres semanas sin alterar el resto del proyecto. |

---

## 7. Comparativa a fondo: `git reset` vs `git rebase` vs `git revert`

Los tres comandos sirven para alterar el historial o deshacer cambios, pero sus propósitos y mecánicas son completamente diferentes:

```text
┌─────────────────┬──────────────────────────────────────────┬────────────────────────────────────────┐
│     Comando     │               ¿Qué hace?                 │              ¿Cuándo usarlo?           │
├─────────────────┼──────────────────────────────────────────┼────────────────────────────────────────┤
│   git reset     │ Mueve la rama actual HACIA ATRÁS         │ Exclusivamente en COMMITS LOCALES      │
│                 │ reescribiendo el historial local.        │ que aún NO has subido a GitHub.        │
├─────────────────┼──────────────────────────────────────────┼────────────────────────────────────────┤
│   git rebase    │ Mueve la BASE de una rama y REAPLICA     │ Para integrar cambios de main en tu    │
│                 │ sus commits encima de otra línea.        │ feature branch sin crear merge commits.│
├─────────────────┼──────────────────────────────────────────┼────────────────────────────────────────┤
│   git revert    │ Crea un NUEVO commit que aplica          │ Para deshacer cambios en RAMAS         │
│                 │ exactamente el cambio inverso.           │ PÚBLICAS / COMPARTIDAS (main).         │
└─────────────────┴──────────────────────────────────────────┴────────────────────────────────────────┘
```

### 7.1 `reset` vs `rebase`: Las diferencias fundamentales

#### ¿En qué se parecen?
Ambos **reescriben el historial**. Al alterar commits, cambian los hashes SHA de los commits afectados.

#### ¿En qué se diferencian?
* **`git reset` es un viaje en el tiempo hacia atrás**:
  Mueve el puntero de tu rama actual a un commit anterior. Los commits posteriores desaparecen de la rama actual (aunque sigan temporalmente flotando en `reflog`).
* **`git rebase` es una reubicación de base hacia adelante**:
  Toma los commits exclusivos de tu rama `feature`, los "despega" temporalmente, adelanta la base al commit más reciente de `main`, y vuelve a aplicar tus commits uno a uno encima de la nueva base.

```text
SITUACIÓN INICIAL:
          D --- E   (feature)
         /
A --- B --- C       (main)

CON GIT REBASE (en rama feature: git rebase main):
A --- B --- C       (main)
             \
              D' --- E' (feature linealizada, sin merge commit)

CON GIT RESET (en rama feature: git reset --hard HEAD~1):
          D         (feature - el commit E se ha descartado)
         /
A --- B --- C       (main)
```

### 7.2 La Regla de Oro Sagrada de Git

> [!CAUTION]
> ### 🚨 NUNCA hagas `git reset` ni `git rebase` sobre commits que ya hayas subido a un repositorio remoto compartido (`main`, ramas de equipo).

**¿Por qué?**
Si haces `git reset` de un commit que tu compañero ya se ha descargado con `git pull`, tu repositorio local y el de tu compañero tendrán historias divergentes. Cuando intentes hacer `git push`, GitHub lo rechazará. Si fuerzas con `git push --force`, **romperás el historial del equipo**.

* **Para commits locales (solo en tu máquina)**: Usa `git reset` o `git rebase` con total libertad para limpiar tu historial antes de compartirlo.
* **Para commits públicos (ya en GitHub / producción)**: Usa siempre **`git revert <commit>`**. `git revert` no borra el pasado: crea un nuevo commit hacia adelante que deshace los cambios de forma segura y colaborativa.

---

## 8. Chuleta Resumen Express

```bash
# 1. Sacar un archivo del área de preparación (stage)
git reset app.py

# 2. Deshacer el último commit conservando todo en Stage (para rehacer el commit)
git reset --soft HEAD~1

# 3. Deshacer el último commit conservando los cambios en disco (sin stage)
git reset HEAD~1

# 4. Destruir el último commit y borrar todos los cambios del disco
git reset --hard HEAD~1

# 5. Salvar la vida tras un reset accidental
git reflog
git reset --hard HEAD@{1}

# 6. Deshacer en producción sin reescribir historia
git revert <hash_del_commit>
```
