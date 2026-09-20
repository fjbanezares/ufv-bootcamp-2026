# 🐧 Operación Némesis: Crónicas de un SysAdmin en Linux
### *Práctica Guiada Paso a Paso a través de las 6 Dimensiones de GNU/Linux*

---

> **Bienvenido, Agente de Sistemas.**  
> Son las 03:42 AM. Has recibido una alerta de emergencia: el administrador principal del servidor de investigación **Némesis** ha desaparecido misteriosamente. La infraestructura está encendida pero desorientada. En los registros hay intentos de intrusión, procesos en segundo plano consumiendo memoria, archivos bloqueados y configuraciones desajustadas.
>
> Tu misión es tomar el control de la terminal, investigar cada rincón del sistema de archivos, desentrañar los misterios de inodos y permisos, neutralizar anomalías y dejar desplegado un centinela automatizado.
>
> **Tu única arma:** La Shell de Linux.

---

## 💡 CÁPSULA 0: Los Secretos Ocultos de la Shell (Lo que nadie te explicó)

Antes de teclear tu primer comando, necesitas descifrar tres conceptos que verás constantemente en los scripts profesionales de Linux y que suelen confundir a los principiantes:

### 1. Los 3 Canales Estándar de UNIX (Descriptores de Archivo: 0, 1 y 2)
Cada programa que se ejecuta en Linux abre automáticamente tres canales de comunicación:
- **`0` = `stdin` (Entrada estándar):** Lo que tú escribes con el teclado.
- **`1` = `stdout` (Salida estándar):** Los resultados normales que el programa imprime en pantalla.
- **`2` = `stderr` (Salida de errores):** Los mensajes de error o advertencia que el programa emite si algo falla.

### 2. ¿Qué es `2>/dev/null`? (El "Agujero Negro" de Linux)
- En Linux, `/dev/null` es un dispositivo especial conocido como el **agujero negro** o trituradora de papel virtual. Todo lo que envías allí desaparece para siempre sin dejar rastro ni gastar disco.
- Cuando escribes **`2>/dev/null`**, le estás diciendo a la shell:
  > *"Toma el canal 2 (los errores) y envíalos a `/dev/null` para que no ensucien mi pantalla. Pero si hay un resultado normal (canal 1), muéstramelo intacto."*

### 3. Operadores Lógicos: `&&` (Y) y `||` (O)
Permiten encadenar comandos según lo que ocurra:
- **`comando_A && comando_B` (AND):** Ejecuta `comando_B` **ÚNICAMENTE SI** `comando_A` terminó con éxito (código de salida 0).
  *Ejemplo:* `mkdir mi_carpeta && cd mi_carpeta` (solo entra si se pudo crear).
- **`comando_A || comando_B` (OR):** Ejecuta `comando_B` **SOLO SI** `comando_A` falló (código de salida distinto de 0).
  *Ejemplo:* `cat archivo.txt || echo "El archivo no existe"` (si no puede leerlo, muestra el aviso alternativo).
- **`comando_A ; comando_B` (Secuencia):** Ejecuta `comando_A` y luego `comando_B` pase lo que pase, sin importar si hubo error o éxito.

---

## 🧰 Caja de Herramientas: Gestión de Paquetes en Cualquier Linux

A lo largo de esta aventura usaremos herramientas del sistema base y otras más avanzadas (como `tree`, `htop`, `netcat`, `curl`). Dependiendo de la distribución Linux en la que estés (o si usas macOS), el gestor de paquetes cambia:

| Distribución | Gestor de Paquetes | Comando de Instalación de Ejemplo |
| :--- | :--- | :--- |
| **Ubuntu / Debian / Kali / Mint** | `apt` / `apt-get` | `sudo apt update && sudo apt install -y tree htop netcat-openbsd curl` |
| **Fedora / RHEL / Rocky / AlmaLinux** | `dnf` (o `yum`) | `sudo dnf install -y tree htop nc curl` |
| **Arch Linux / Manjaro** | `pacman` | `sudo pacman -Sy tree htop gnu-netcat curl` |
| **openSUSE** | `zypper` | `sudo zypper install -y tree htop netcat-openbsd curl` |
| **macOS (Terminal zsh)** | `brew` (Homebrew) | `brew install tree htop netcat curl` |

---

## 🚀 Despliegue del Laboratorio Seguro

Para no interferir con archivos personales de tu máquina, hemos preparado un laboratorio de simulación que recrea la estructura del servidor Némesis en una carpeta aislada.

Ejecuta desde la raíz del repositorio o dentro de la carpeta `linux/`:

```bash
# Si estás en la raíz del repo:
bash linux/scripts/preparar_mision_nemesis.sh

# O si ya estás dentro de la carpeta linux/:
bash scripts/preparar_mision_nemesis.sh
```

Una vez ejecutado, entra en el cuartel general de la misión:
```bash
cd laboratorio_nemesis
```

---

## 🧭 ACTO 1: ¿Qué es este Sistema? El Encuentro con el Kernel

![Parte 1: ¿Qué es un Sistema Operativo?](./linux-intro1.png)

### 📖 La Historia
Frente a ti parpadea el cursor de una pantalla negra. No hay botones, ventanas ni ratón. Solo texto esperando tus órdenes. Lo primero que debe saber cualquier SysAdmin antes de actuar es: **¿sobre qué motor estoy parado?**

El **Sistema Operativo** es el puente entre las personas y el silicio del hardware. Como muestra la infografía:
- **Kernel (Linux)**: El motor que controla CPU, memoria RAM y discos (creado por Linus Torvalds en 1991).
- **GNU**: Las herramientas, programas y compiladores libres que rodean al motor (impulsadas por Richard Stallman).
- **Shell**: El intérprete con el que estás a punto de hablar.

### 💻 Paso a Paso en la Terminal

#### 1. Identificar el Kernel y la Arquitectura
```bash
uname -a
```
* **Desglose del comando:**
  - `uname` (*Unix Name*): Pregunta al kernel sus datos de identidad.
  - Flag `-a` (*all*): Muestra toda la información disponible:
    - Nombre del kernel (ej. `Linux` o `Darwin` en macOS).
    - Nombre del equipo (*hostname*).
    - Versión exacta del kernel (ej. `6.8.0-generic`).
    - Arquitectura de la CPU (ej. `x86_64` para Intel/AMD de 64 bits, o `aarch64` / `arm64` para Apple Silicon / Raspberry Pi).

#### 2. Consultar la Distribución exacta del Sistema
En GNU/Linux existe un estándar: los detalles de la distribución (Ubuntu, Debian, Fedora, Arch) se guardan en el archivo `/etc/os-release`.

Pruébalo directamente:
```bash
cat /etc/os-release
```

**¿Qué pasa si estás en un sistema que no lo tiene (como macOS)?**
Verás un error rojo: `cat: /etc/os-release: No such file or directory`.

Para resolver esto con elegancia profesional, encadenamos alternativas con lo que aprendimos en la Cápsula 0:
```bash
cat /etc/os-release 2>/dev/null || cat /etc/issue 2>/dev/null || uname -s
```
* **Explicación didáctica paso a paso de esta sentencia:**
  1. `cat /etc/os-release 2>/dev/null`: Intenta leer `/etc/os-release`. Si falla, `2>/dev/null` traga el mensaje de error para no afear la terminal.
  2. `||`: Operador OR. Si el comando anterior falló, salta al siguiente: `cat /etc/issue 2>/dev/null`.
  3. `|| uname -s`: Si el anterior también falló (como ocurre en macOS o BSD), ejecuta como último recurso `uname -s` que siempre funciona e imprime el nombre del sistema base.

#### 3. Descubrir tu Shell actual
```bash
echo $SHELL
echo "Mi intérprete en ejecución es: $0"
```
* **Desglose:**
  - `$SHELL`: Es una variable de entorno del sistema que indica cuál es tu shell favorita predeterminada (generalmente `/bin/bash` o `/bin/zsh`).
  - `$0`: En scripts y en la terminal, `$0` almacena el nombre del comando o programa que se está ejecutando en este momento exacto.

---

## ⚔️ ACTO 2: La Terminal como Conversación Directa (Navegación y Tuberías)

![Parte 2: Terminal, Shell y Primeros Comandos](./linux-intro2.png)

### 📖 La Historia
Ahora que conoces el terreno, necesitas moverte por el servidor. Te han informado de que el antiguo administrador dejó un archivo de registro (*log*) con pistas antes de marcharse. Debes encontrarlo, examinarlo sin sobrecargar la pantalla y extraer únicamente los eventos críticos usando **tuberías (`|`)** y **redirecciones (`>`, `>>`)**.

### 💻 Paso a Paso en la Terminal

#### 1. ¿Dónde estoy parado?
```bash
pwd
```
* **Desglose:** `pwd` (*Print Working Directory*). Muestra la ruta absoluta desde la raíz `/` hasta la carpeta donde te encuentras. Debes ver algo como `/.../laboratorio_nemesis`.

#### 2. Inspeccionar el entorno con diferentes opciones (flags)
Prueba estos tres comandos uno tras otro y fíjate en cómo cambia la información:
```bash
# 1. Modo simple (solo nombres)
ls

# 2. Modo detallado / largo
ls -l

# 3. Modo detallado incluyendo archivos ocultos
ls -la
```
* **Desglose de las opciones:**
  - `-l` (*long format*): Muestra columnas con: permisos (`drwxr-xr-x`), número de enlaces, usuario propietario, grupo, tamaño en bytes y fecha de modificación.
  - `-a` (*all*): Muestra los archivos ocultos (los que comienzan por un punto `.`).
  - **¿Qué son `.` y `..`?**:
    - `.` representa **el directorio actual**.
    - `..` representa **el directorio padre** (un nivel arriba).

#### 3. Viajar por la jerarquía
```bash
cd var/log
pwd
cd ../..
pwd
```
* **Desglose:** `cd` (*Change Directory*).
  - `cd var/log`: Ruta relativa hacia adelante.
  - `cd ../..`: Subimos dos escalones en la jerarquía (de `log/` a `var/` y de `var/` a la raíz del laboratorio).

#### 4. Investigar el Log con Tuberías y Filtros
El archivo `var/log/sistema.log` contiene el registro de actividad.
Si haces `cat var/log/sistema.log` verás todas las líneas de golpe. Pero como SysAdmin, tú solo buscas los incidentes graves.

Vamos a conectar comandos con la **tubería (`|`)**:
```bash
cat var/log/sistema.log | grep "SECURITY"
```
* **¿Qué hace la tubería `|`?**:
  Toma la salida estándar de `cat` (el texto del archivo) y se la pasa directamente como entrada al comando `grep` (que busca y filtra solo las líneas que coincidan con la palabra `"SECURITY"`).

Ahora un truco más limpio: `grep` puede leer archivos directamente sin necesidad de usar `cat`:
```bash
grep -i -n -E "ALERT|CRITICAL" var/log/sistema.log
```
* **Desglose de cada flag de `grep`:**
  - `-i` (*ignore case*): No distingue entre mayúsculas y minúsculas (encuentra `alert`, `Alert` o `ALERT`).
  - `-n` (*number*): Muestra el número de línea exacto donde ocurrió el incidente.
  - `-E` (*extended regex*): Permite usar expresiones regulares como el símbolo `|` (OR) para buscar "ALERT" o "CRITICAL" al mismo tiempo.

#### 5. Redirecciones: Crear un informe de incidentes
Vamos a guardar estos hallazgos en un archivo nuevo usando los operadores de redirección:

```bash
# Operador '>' : Crea el archivo (o lo sobrescribe si ya existía)
grep "SECURITY" var/log/sistema.log > informe_amenazas.txt

# Operador '>>' : Añade contenido AL FINAL del archivo sin borrar lo anterior
grep -E "ALERT|CRITICAL" var/log/sistema.log >> informe_amenazas.txt

# Comprobamos el archivo final
cat informe_amenazas.txt
```

#### 6. Atajos ninja de productividad en la terminal
Pruébalos ahora mismo en tu teclado:
- **Autocompletado con `Tab`**: Escribe `cd ho` y presiona la tecla `Tab`. La shell adivinará y completará `home/` al instante.
- **Búsqueda interactiva en el historial (`Ctrl + R`)**: Pulsa `Ctrl + R` y teclea `informe`. La shell buscará el último comando donde usaste esa palabra. Presiona Enter para ejecutarlo.
- **Repetir último comando con `!!`**: Escribe `!!` y presiona Enter. Repetirá la última orden ejecutada (muy útil cuando olvidas poner `sudo` al principio: `sudo !!`).

---

## 🏛️ ACTO 3: La Gran Biblioteca del Sistema de Archivos y los Enlaces

![Parte 3: Sistema de Archivos de Linux](./linux-intro3.png)

### 📖 La Historia
En Linux existe una máxima legendaria: **«En UNIX, todo es un archivo»** (programas, documentos, discos e incluso las conexiones de red). Toda esta inmensa biblioteca cuelga de un único punto de origen: la raíz `/`.

Dentro de `home/agente/`, el antiguo SysAdmin preparó un paquete de datos llamado `transmision.dat`. Pero observas dos archivos similares: `transmision_respaldo.dat` y `acceso_directo_transmision.lnk`. ¿Son copias independientes que ocupan el doble de espacio o son enlaces?

### 💻 Paso a Paso en la Terminal

#### 1. Conocer las carpetas sagradas del sistema raíz (`/`)
Repasa para qué sirve cada una según la infografía:
- `/etc`: Archivos de configuración del sistema (como `servidor.conf` o `passwd`).
- `/var`: Datos variables en constante crecimiento (como `/var/log`).
- `/home`: Espacio personal de cada usuario humano.
- `/tmp`: Archivos temporales (se vacían al reiniciar).
- `/bin`: Binarios y comandos ejecutables esenciales (`ls`, `cp`, `bash`).
- `/dev`: Representación como archivos de dispositivos de hardware (`/dev/null`, discos).

#### 2. Enlaces Duros (*Hard Links*) vs Enlaces Simbólicos (*Symlinks*)
Ve a la carpeta del agente y fíjate en el número de inodo de cada archivo con `ls -li`:
```bash
cd home/agente
ls -li
```
* **Observa con atención las columnas:**
  - La **primera columna numérica** es el número de **inodo** (el identificador físico en el disco).
  - Fíjate: `transmision.dat` y `transmision_respaldo.dat` **tienen exactamente el mismo número de inodo**.
  - **¿Qué significa esto?**: Que no son dos copias duplicadas. Son **dos nombres que apuntan a la misma habitación física de datos**. No ocupan el doble de espacio.
  - En cambio, `acceso_directo_transmision.lnk` tiene un inodo distinto y una flecha `->`. Es un **enlace simbólico** (*soft link*): un archivo ligero que solo contiene la ruta hacia otro archivo (como un acceso directo de escritorio).

#### 3. El Experimento de la Destrucción (¿Qué pasa al borrar?)
Vamos a comprobar la diferencia real entre ambos enlaces:

```bash
# 1. Leemos primero a través del enlace blando
cat acceso_directo_transmision.lnk

# 2. Borramos el archivo original
rm transmision.dat

# 3. ¿Sobrevivió el hard link?
cat transmision_respaldo.dat

# 4. ¿Qué le pasó al enlace simbólico?
cat acceso_directo_transmision.lnk
```

* **Explicación técnica del resultado:**
  - `transmision_respaldo.dat` **sigue intacto**: En Linux, el contenido físico de un archivo solo se libera cuando **todos** los hard links que apuntan a su inodo han sido eliminados (contador de enlaces llega a 0).
  - `acceso_directo_transmision.lnk` **se rompe** (*Dangling Symlink*): Devuelve un error `No such file or directory` porque el archivo al que apuntaba por ruta ya no existe.

Regresemos a la base:
```bash
cd ../..
```

---

## 🔬 ACTO 4: Rayos X al Disco: Inodos, Bloques y Tamaños Fantasma

![Parte 4: ¿Cómo se guarda un archivo por dentro?](./linux-intro4.png)

### 📖 La Historia
El hardware no entiende de nombres de archivos simpáticos; entiende de **bloques de almacenamiento de 4 KB** y de números de catálogo llamados **inodes (nodos-índice)**.
Un inodo guarda:
1. Quién es el dueño (`UID`, `GID`).
2. Qué permisos tiene (`rwxr-xr-x`).
3. Cuánto mide en bytes.
4. Fechas de acceso, modificación y cambio (`atime`, `mtime`, `ctime`).
5. Dónde están los bloques en los que se dividió el contenido.

**Curiosidad clave:** El inodo **NO guarda el nombre del archivo**. El nombre solo vive en el directorio, asociando un texto a un número de inodo.

### 💻 Paso a Paso en la Terminal

#### 1. Inspeccionar las entrañas de un archivo con `stat`
```bash
stat etc/servidor.conf
```
* **¿Qué datos estás viendo?**:
  - `Inode`: El número único de carnet de identidad del archivo en el sistema de ficheros.
  - `Links`: Cuántos nombres apuntan a este inodo.
  - `Blocks`: Cuántos bloques físicos de disco tiene asignados.
  - `Access / Modify / Change`:
    - *Access (atime)*: Última vez que alguien leyó su contenido.
    - *Modify (mtime)*: Última vez que se modificó su contenido.
    - *Change (ctime)*: Última vez que cambiaron sus metadatos (como sus permisos o su dueño).

#### 2. Tamaño Lógico vs Espacio Real Ocupado (`ls` vs `du`)
Crea un archivo diminuto de solo 15 caracteres:
```bash
echo "Hola SysAdmin" > mini.txt
ls -lh mini.txt
du -h mini.txt
```
* **Explicación didáctica del misterio:**
  - `ls -lh` (*human-readable*) reporta **14 bytes** (tamaño lógico real del texto).
  - `du -h` (*Disk Usage*) reporta **4.0 KB**.
  - **¿Por qué?**: Porque el sistema de archivos divide el disco en bloques indivisibles de **4 KB (4096 bytes)**. Si tu archivo mide 14 bytes, el sistema le asigna un bloque entero, dejando los 4082 bytes restantes sin usar dentro de ese bloque. ¡No se puede reservar medio bloque!

#### 3. Magia Técnica: Creando un Archivo Disperso (*Sparse File*) de 1 GB que ocupa 0 Bytes
¿Es posible crear un archivo que aparente medir 1 Gigabyte pero no gaste nada de espacio en tu disco? Sí, se llama *Sparse File*.

Vamos a crearlo paso a paso:
```bash
dd if=/dev/zero of=archivo_fantasma.img bs=1M count=0 seek=1024
```
* **Desglose parámetro por parámetro del comando `dd`:**
  - `dd`: Herramienta clásica de bajo nivel para copiar y convertir datos bloque a bloque.
  - `if=/dev/zero`: *Input File* (fichero de entrada). `/dev/zero` es un generador infinito de ceros binarios del kernel.
  - `of=archivo_fantasma.img`: *Output File* (fichero de destino a crear).
  - `bs=1M`: *Block Size* (tamaño del bloque: 1 Megabyte).
  - `count=0`: Le decimos: "No leas ni escribas ningún bloque todavía".
  - `seek=1024`: Salta el puntero de escritura directamente a la posición 1024 (1 GB) sin escribir nada en el medio.

Ahora comparemos cómo lo ven los dos comandos:
```bash
ls -lh archivo_fantasma.img
du -h archivo_fantasma.img
```
* **La revelación:**
  - `ls -lh` reporta **1.0G** (para cualquier programa, el archivo mide 1 GB).
  - `du -h` reporta **0B** (cero bytes físicos ocupados en tu disco duro).
  - Linux solo asigna bloques físicos reales cuando un programa escribe datos de verdad sobre los huecos.

Limpia los archivos de prueba para dejar el laboratorio impecable:
```bash
rm -f mini.txt archivo_fantasma.img
```

---

## 🛡️ ACTO 5: Usuarios, Permisos Especiales y la Caza del Proceso Fantasma

![Parte 5: Usuarios, Permisos y Procesos](./linux-intro5.png)

### 📖 La Historia
Revisando los registros descubriste una alarma crítica: alguien intentó acceder a `srv/backup/clave_secreta.txt`, y además hay un proceso sospechoso corriendo en segundo plano que podría estar enviando datos fuera. Tienes que auditar los permisos, proteger el archivo confidencial y neutralizar el proceso.

### 💻 Paso a Paso en la Terminal

#### 1. ¿Quién soy y qué permisos tengo?
```bash
whoami
id
```
* **Desglose:**
  - `whoami`: Te dice el nombre de tu usuario activo.
  - `id`: Te muestra tu identificador numérico (`uid`), tu grupo principal (`gid`) y todos los grupos secundarios a los que perteneces.
  - En Linux, el superusuario con poder absoluto es **`root`**, cuyo `uid` es siempre **0**.

#### 2. Entender los permisos `rwx` y el valor octal
Observa la tabla de la infografía:
- **r** (Read / Lectura) = **4**
- **w** (Write / Escritura) = **2**
- **x** (Execute / Ejecución) = **1**

Cada archivo tiene 3 grupos de permisos: `[Dueño][Grupo][Otros]`

| Permiso Octal | Cálculo | Notación Simbólica | Significado en la vida real |
| :---: | :---: | :---: | :--- |
| **`755`** | `(4+2+1)(4+0+1)(4+0+1)` | `rwxr-xr-x` | El dueño puede hacer todo; grupo y resto solo leer y ejecutar (ideal para programas). |
| **`644`** | `(4+2+0)(4+0+0)(4+0+0)` | `rw-r--r--` | El dueño lee y modifica; el resto del mundo solo puede leer (ideal para documentos públicos). |
| **`600`** | `(4+2+0)(0+0+0)(0+0+0)` | `rw-------` | **Máxima privacidad**: Solo el dueño puede leer y modificar; nadie más puede tocarlo. |

#### 3. Blindar el archivo secreto
Verifiquemos cómo está el archivo confidencial:
```bash
ls -l srv/backup/clave_secreta.txt
```
Si estuviera legible por otros usuarios, lo blindamos a modo confidencial:
```bash
chmod 600 srv/backup/clave_secreta.txt
ls -l srv/backup/clave_secreta.txt
```
* `chmod 600` le quita todo permiso al grupo y a otros usuarios, asegurando la clave.

#### 4. Permisos Especiales: El Sticky Bit (`+t`)
¿Por qué en carpetas públicas compartidas como `/tmp` cualquier usuario puede crear archivos pero nadie puede borrar los archivos de los demás? Gracias al **Sticky Bit**:
```bash
mkdir -p carpeta_compartida
chmod 1777 carpeta_compartida
ls -ld carpeta_compartida
```
* **Fíjate en el resultado:** Aparece una **`t`** al final: `drwxrwxrwt`.
* El `1` delante de `777` activa el **Sticky Bit**, impidiendo que un usuario borre o renombre los archivos creados por otro usuario en esa carpeta.

Limpia la carpeta de prueba:
```bash
rmdir carpeta_compartida
```

#### 5. Caza del Proceso Fantasma
Lanza el proceso sospechoso en segundo plano colocando un ampersand **`&`** al final del comando:
```bash
./bin/proceso_fantasma.sh &
```
* **¿Qué significa el `&`?**: Le dice a la shell: "Inicia este programa pero no bloquees mi terminal; devuélveme el control de inmediato". La terminal te devolverá el número de trabajo y su **PID** (Identificador de Proceso, ej. `[1] 12345`).

Ahora busquemos el proceso en ejecución:
```bash
ps aux | grep "proceso_fantasma" | grep -v grep
```
* **Desglose de cada pieza de esta tubería:**
  1. `ps aux`:
     - `a`: Muestra procesos de todos los usuarios.
     - `u`: Formato detallado con usuario, consumo de %CPU y %MEM.
     - `x`: Incluye procesos que no dependen de una terminal (servicios en segundo plano).
  2. `| grep "proceso_fantasma"`: Filtra la lista para mostrar solo las líneas que mencionan al script.
  3. `| grep -v grep`: El propio comando `grep` que busca es un proceso que también aparecería en la lista. El flag `-v` (*invert match*) le dice: "Muestra todo **EXCEPTO** la línea del propio grep".

También puedes usar la herramienta moderna especializada `pgrep`:
```bash
pgrep -l -f "proceso_fantasma"
```
* `-l` muestra el nombre del proceso y `-f` busca en la línea de comando completa.

#### 6. Neutralizar el proceso: SIGTERM (-15) vs SIGKILL (-9)
Un buen SysAdmin jamás dispara a matar a la primera. Linux utiliza **señales** para comunicarse con los procesos:

1. **Paso 1: Petición educada (SIGTERM / señal 15)**: Le pide al proceso que termine ordenadamente, guarde datos abiertos y cierre conexiones de red:
   ```bash
   pkill -15 -f "proceso_fantasma"
   ```
2. **Paso 2: Comprobar si respondió:**
   ```bash
   pgrep -f "proceso_fantasma"
   ```
3. **Paso 3 (Solo si sigue vivo rebelde): Fuerza bruta (SIGKILL / señal 9)**: El kernel fulmina el proceso instantáneamente sin darle oportunidad de despedirse:
   ```bash
   pkill -9 -f "proceso_fantasma"
   ```

---

## 🌐 ACTO 6: Redes, Sockets, Firewall y el Script Centinela

![Parte 6: Red, Scripting y Visión Final](./linux-intro6.png)

### 📖 La Historia
El servidor está a salvo internamente, pero un servidor que no se comunica con el mundo exterior no sirve de nada. Debes inspeccionar las interfaces de red, comprobar si el puerto de servicio `8080` está escuchando conexiones, y automatizar un **Script Centinela en Bash** con control de señales para que audite el sistema periódicamente.

### 💻 Paso a Paso en la Terminal

#### 1. Auditoría de red e interfaces
Históricamente en Linux se usaba el comando `ifconfig`. Hoy en día el estándar oficial es el paquete `iproute2` con el comando `ip`:
```bash
# Comando moderno en GNU/Linux:
ip addr show
```
*(Si estás en macOS o un UNIX clásico donde `ip` no viene instalado, usa `ifconfig`).*

#### 2. Puertos y Sockets en escucha
¿Qué puertos y servicios tiene abiertos este equipo esperando conexiones?
```bash
# El comando moderno oficial: ss (Socket Statistics)
ss -tuln
```
*(Si `ss` no estuviera disponible, su equivalente clásico es `netstat -tuln`).*

* **Desglose de los flags `-tuln`:**
  - `-t` (*TCP*): Muestra conexiones TCP (orientadas a conexión, fiables, como HTTP o SSH).
  - `-u` (*UDP*): Muestra conexiones UDP (rápidas, sin conexión previa, como streaming o DNS).
  - `-l` (*Listening*): Muestra solo los sockets que están en espera de recibir clientes.
  - `-n` (*Numeric*): Muestra números de puertos directamente (ej. `:8080` o `:22`) sin perder tiempo intentando resolver nombres por DNS.

#### 3. Cortafuegos (Firewall): El guardián Netfilter
El kernel de Linux integra en sus entrañas un subsistema llamado **Netfilter**. Herramientas como `iptables`, `nftables` o `ufw` permiten definir reglas sobre 3 cadenas principales:
- **INPUT**: Paquetes de red que vienen de internet hacia este servidor.
- **OUTPUT**: Paquetes de red generados por este servidor hacia internet.
- **FORWARD**: Paquetes que solo pasan a través de este equipo (cuando actúa como router).

*Ejemplo de regla en `iptables` para permitir tráfico entrante en puerto 2222:*
```bash
# sudo iptables -A INPUT -p tcp --dport 2222 -j ACCEPT
```
- `-A INPUT`: Añade (*Append*) a la cadena de entrada.
- `-p tcp`: Protocolo TCP.
- `--dport 2222`: Puerto de destino 2222.
- `-j ACCEPT`: Acción (*Jump*): Aceptar el paquete.

---

## 🤖 DESAFÍO FINAL: Desarrollar el Script Centinela de Némesis

Como coronación de tu misión, crearás un script en Bash en `bin/centinela.sh`.
Antes de escribirlo, examinemos los conceptos avanzados que contendrá:

1. **`#!/usr/bin/env bash` (Shebang)**: La primera línea indispensable que le indica al kernel qué programa debe interpretar este archivo.
2. **`trap '...' SIGINT`**: Un "gancho" que intercepta la señal de `Ctrl + C` para que, si el operador cancela el script a mitad, este se despida amigablemente en lugar de abortar feamente.
3. **`awk '{print $1}'`**: Utilidad de procesamiento de texto que divide cada línea por espacios en blanco y extrae la columna número 1 (la columna de permisos `rwxr-xr-x`).
4. **`$?`**: Variable especial de la shell que contiene el código numérico de salida del último comando ejecutado (0 = éxito, cualquier otro número = error).

Crea el archivo `bin/centinela.sh`:

```bash
cat << 'EOF' > bin/centinela.sh
#!/usr/bin/env bash
# ==============================================================================
# CENTINELA NÉMESIS v1.0 - Monitor de Integridad del Sistema
# ==============================================================================

# Capturar señal de interrupción (SIGINT / Ctrl+C) con trap
trap 'echo -e "\n🛑 [CENTINELA] Interrupción manual recibida. Cerrando patrulla con honor."; exit 0' SIGINT

NOMBRE_HOST=$(hostname)
FECHA=$(date "+%Y-%m-%d %H:%M:%S")

echo "========================================================"
echo "🛡️  PATRULLA CENTINELA ACTIVADA EN: ${NOMBRE_HOST}"
echo "📅  Fecha: ${FECHA}"
echo "👤  Operador: $(whoami)"
echo "========================================================"

# 1. Comprobación de argumentos recibidos por línea de comandos ($# = total, $1 = primero)
if [ $# -gt 0 ]; then
    echo "ℹ️  Modo de patrulla recibido: $1"
fi

# 2. Análisis de incidentes en el log
ARCHIVO_LOG="var/log/sistema.log"
if [ -f "$ARCHIVO_LOG" ]; then
    # grep -c cuenta el número de líneas coincidentes
    TOTAL_ALERTAS=$(grep -c -E "ALERT|CRITICAL|SECURITY" "$ARCHIVO_LOG")
    echo "🔍 Análisis de logs ($ARCHIVO_LOG):"
    echo "   ⚠️ Incidentes críticos detectados: ${TOTAL_ALERTAS}"
    
    if [ "$TOTAL_ALERTAS" -gt 0 ]; then
        echo "   🚨 Eventos prioritarios encontrados en el log:"
        grep -n -E "ALERT|CRITICAL" "$ARCHIVO_LOG" | head -n 3
    else
        echo "   ✅ Sin anomalías registradas."
    fi
else
    echo "⚠️ Archivo de log no encontrado en $ARCHIVO_LOG"
fi

# 3. Comprobación de seguridad en la clave confidencial
ARCHIVO_CLAVE="srv/backup/clave_secreta.txt"
if [ -f "$ARCHIVO_CLAVE" ]; then
    # Usamos awk para quedarnos solo con la columna 1 (los permisos)
    PERMISOS=$(ls -l "$ARCHIVO_CLAVE" | awk '{print $1}')
    echo "🔐 Estado de clave confidencial ($ARCHIVO_CLAVE):"
    echo "   Permisos actuales: $PERMISOS"
    if [ "$PERMISOS" == "-rw-------" ]; then
        echo "   ✅ BLINDADO: Solo el propietario tiene lectura y escritura."
    else
        echo "   ⚠️ VULNERABLE: Corregir permisos inmediatamente con 'chmod 600 $ARCHIVO_CLAVE'."
    fi
fi

echo "========================================================"
echo "🏆 [MISIÓN CUMPLIDA] El servidor Némesis está bajo control."
echo "========================================================"
EOF
```

Dale permisos de ejecución con `chmod +x` y pruébalo:
```bash
chmod +x bin/centinela.sh
./bin/centinela.sh "Inspección de Seguridad 2026"
```

---

## 🏆 Resumen de los 10 Mandamientos del SysAdmin Linux

1. **Linux te da control y libertad**: Lo que tú ordenas, el kernel lo ejecuta sin rechistar.
2. **La terminal te da precisión**: Con pipes y filtros puedes procesar millones de líneas en segundos.
3. **El sistema de archivos es un árbol**: Todo empieza en `/`, no hay letras de unidad tipo `C:\`.
4. **El inodo es el verdadero archivo**: El nombre es solo una etiqueta que apunta a él.
5. **Los permisos te protegen**: `chmod 600` para secretos, `755` para programas, `644` para lectura general.
6. **Todo proceso tiene un PID**: Monitorea con `ps`, `top/htop` y mata primero con `kill -15`.
7. **Linux se conecta al mundo**: Domina `ss`, `ip`, `curl` y los estados de sockets.
8. **Los scripts automatizan tu vida**: Un buen SysAdmin escribe scripts para no repetir trabajo.
9. **El firewall es tu muralla**: Netfilter vigila la frontera de paquetes.
10. **Aprender terminal te da superpoderes**: El conocimiento que adquieras hoy en Linux te servirá en servidores, contenedores Docker, nubes AWS/GCP/Azure y sistemas embebidos durante décadas.
