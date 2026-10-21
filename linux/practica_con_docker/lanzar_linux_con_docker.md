# Guía de Laboratorio: Introducción a Linux y Codificación de Caracteres con Docker

## 1. Conceptos Previos: ¿Qué es Docker y cómo funciona?

Antes de escribir nuestro primer comando en Linux, necesitamos un entorno limpio y seguro donde practicar sin miedo a romper nada en nuestro ordenador personal (ya sea Windows o macOS). Para ello utilizaremos **Docker**.

### ¿Qué es Docker?
Tradicionalmente, si querías usar Linux dentro de Windows o Mac, tenías que instalar una **Máquina Virtual** pesada (usando programas como VirtualBox o VMware), reservando varios gigabytes de memoria RAM y disco duro, y esperando varios minutos a que el sistema operativo arrancase.

**Docker** es una tecnología de **contenedores**. Un contenedor es como una "máquina virtual ultraligera" que arranca en apenas un segundo. Nos permite descargar un sistema operativo **Ubuntu Linux** limpio, meternos dentro de su consola para trabajar, instalar programas y, al terminar, destruirlo sin que deje basura ni archivos residuales en nuestro ordenador.

### ¿Qué es el *Docker Daemon* (El motor en segundo plano)?
Si intentas ejecutar un comando de Docker en tu terminal sin haber abierto antes la aplicación **Docker Desktop**, verás un error que dice: *"Cannot connect to the Docker daemon"*. ¿Qué significa esto?

* **La analogía del software base:** Imagina que quieres abrir un documento `.docx` pero no tienes Microsoft Word instalado o en ejecución, o que quieres jugar a un videojuego pero la consola está apagada.
* El **Docker Daemon** (`dockerd`) es el **"motor" o programa servidor** que se ejecuta de forma invisible en segundo plano en tu ordenador. Es el software encargado de hacer el trabajo pesado: hablar con el procesador y la memoria de tu equipo, descargar los sistemas operativos de Internet, crear la red virtual y mantener encendidos los contenedores.
* Cuando escribes `docker ...` en tu ventana de terminal, tú solo estás usando el **mando a distancia (el cliente)** para enviarle órdenes al **Docker Daemon**. Por eso, **el requisito número uno antes de empezar es abrir la aplicación visual Docker Desktop** y esperar unos segundos hasta que su icono inferior indique que el motor está en verde (*Engine running*).

---

## 2. Práctica Paso a Paso: Levantar Linux e Inspeccionar Archivos (UTF-8, UTF-16 y UTF-32)

### Paso 1: Levantar nuestra máquina Ubuntu Linux y entrar en ella
Con **Docker Desktop abierto**, abre la aplicación **Terminal** de tu ordenador (o PowerShell en Windows) y ejecuta el siguiente comando:

```bash
docker run -it --rm ubuntu bash
```

#### ¿Qué ocurre exactamente al ejecutar este comando?
1. **`docker run`**: Le pide al *Docker Daemon* que cree y encienda un contenedor nuevo.
2. **`ubuntu`**: Es la plantilla (imagen) que queremos usar. Si es la primera vez que lo ejecutas, verás cómo el *Docker Daemon* la descarga automáticamente de Internet (*Pulling from library/ubuntu*). En pocos segundos tendrás un sistema **Ubuntu Linux** oficial en tu equipo.
3. **`-it`** (*Interactive + TTY*): Conecta tu teclado y tu pantalla directamente con el interior del contenedor para que puedas interactuar con él en tiempo real.
4. **`--rm`** (*Remove*): Le ordena a Docker que, en el momento en que salgamos del contenedor al final de la clase, lo borre automáticamente para no ocupar espacio en tu disco duro.
5. **`bash`**: Es el programa que queremos abrir nada más entrar; en este caso, el intérprete de comandos de Linux (*Bourne Again SHell*).

> **¿Cómo sé que ha funcionado?**  
> El cursor de tu terminal habrá cambiado y ahora mostrará algo similar a `root@4a8b9c1d2e3f:/#`. Eso significa que **ya estás dentro de Linux** como superusuario (`root`), el administrador total de esa máquina.

---

### Paso 2: Instalar herramientas en nuestro Linux recién creado
Por defecto, la imagen de Ubuntu que descarga Docker viene reducida al mínimo indispensable (apenas ocupa 30 MB) para descargarse rápido, por lo que no trae editores de texto ni herramientas adicionales. Vamos a descargarlas usando el gestor de paquetes de Ubuntu (`apt-get`):

```bash
apt-get update && apt-get install -y nano file xxd bsdextrautils
```

#### ¿Qué hace cada parte de esta orden?
* **`apt-get update`**: Conecta con los servidores oficiales de Ubuntu en Internet para descargar el catálogo actualizado de programas disponibles.
* **`&&`**: Es un operador lógico que significa *"y, solo si el comando anterior ha terminado sin errores, ejecuta el siguiente"*.
* **`apt-get install -y ...`**: Descarga e instala los programas que le indicamos. La opción **`-y`** (*yes*) responde automáticamente "Sí" cuando el sistema pregunta si deseamos confirmar la descarga.
* **Programas que instalamos**:
  * `nano`: Un editor de textos sencillo en terminal.
  * `file`: Una utilidad que analiza un archivo y nos dice de qué tipo es y en qué formato está codificado.
  * `xxd` y `bsdextrautils`: Utilidades avanzadas para inspeccionar el interior de los archivos en hexadecimal y binario.

---

### Paso 3: Crear nuestra carpeta de trabajo y el archivo original en UTF-8
En los ordenadores todo se almacena como números (bytes). Para representar letras existen las **tablas de codificación de caracteres**:
* **UTF-8:** Es el estándar actual en Linux y la Web. Es de **longitud variable**: las letras inglesas normales (ASCII) ocupan solo **1 byte** (8 bits), mientras que caracteres especiales como la `ñ` o las vocales con tilde ocupan 2 bytes.
* **UTF-16:** Utiliza un mínimo de **2 bytes** (16 bits) por cada carácter.
* **UTF-32:** Utiliza siempre una longitud fija de **4 bytes** (32 bits) por cada carácter, rellenando con **ceros** el espacio sobrante.

Vamos a crear una carpeta llamada `/practica`, entrar en ella y crear un archivo con las 4 letras de la palabra `"Hola"`:

```bash
mkdir /practica
cd /practica
printf "Hola" > hola_utf8.txt
```

#### ¿Qué ocurre con estos comandos?
* **`mkdir /practica`**: Crea un directorio nuevo llamado `practica` en la raíz del sistema.
* **`cd /practica`**: Nos mete dentro de esa carpeta (*Change Directory*).
* **`printf "Hola" > hola_utf8.txt`**: Imprime las cuatro letras de `"Hola"` (usamos `printf` en lugar de `echo` porque `echo` añade un salto de línea invisible al final y queremos exactamente 4 caracteres) y, mediante el símbolo de redirección **`>`**, en vez de mostrarlo en pantalla lo guarda dentro del archivo `hola_utf8.txt`.

---

### Paso 4: Convertir el archivo a UTF-16 y UTF-32
Ahora utilizaremos la herramienta **`iconv`** (*Internationalization Conversion*), que sirve para traducir archivos de texto de una codificación a otra:

```bash
iconv -f UTF-8 -t UTF-16BE hola_utf8.txt > hola_utf16.txt
iconv -f UTF-8 -t UTF-32BE hola_utf8.txt > hola_utf32.txt
```

#### ¿Qué significan los parámetros de `iconv`?
* **`-f UTF-8`** (*from*): Indica el formato de origen (venimos de UTF-8).
* **`-t UTF-16BE` / `-t UTF-32BE`** (*to*): Indica el formato de destino. Añadimos la terminación **BE** (*Big Endian*) para que ordene los bytes de izquierda a derecha (orden natural de lectura humana) y no inserte bytes de cabecera adicionales.
* **`> hola_utf16.txt`**: Guarda el resultado traducido en un archivo nuevo.

Comprobemos ahora cuánto ocupa físicamente cada archivo en el disco duro ejecutando:

```bash
ls -l
```

Verás este resultado en pantalla:
```text
-rw-r--r-- 1 root root 16 Oct 19 05:00 hola_utf32.txt
-rw-r--r-- 1 root root  8 Oct 19 05:00 hola_utf16.txt
-rw-r--r-- 1 root root  4 Oct 19 05:00 hola_utf8.txt
```
Observa la quinta columna (el tamaño en bytes): ¡el mismo texto `"Hola"` de 4 letras ocupa **4 bytes** en UTF-8, **8 bytes** en UTF-16 y **16 bytes** en UTF-32!

---

### Paso 5: Ver los bytes y los ceros por dentro con el comando `od`
Si abrieras los archivos con `cat`, la terminal intentaría mostrar solo las letras visibles. Para hacer una "radiografía" del archivo y ver exactamente qué bytes reales hay guardados en el disco duro, usamos el comando **`od`** (*Octal Dump*).

Le pasaremos dos opciones:
* **`-t x1`**: Muestra el contenido byte a byte en código **hexadecimal** (números del `00` al `ff`).
* **`-t c`**: Muestra justo debajo la letra equivalente o el símbolo **`\0`** cuando se encuentra un byte lleno de ceros (byte nulo).

#### 1. Radiografía del archivo en UTF-8 (1 byte por letra, sin ceros):
```bash
od -t x1 -t c hola_utf8.txt
```
**Resultado:**
```text
0000000  48  6f  6c  61
          H   o   l   a
0000004
```
* **Explicación:** En la tabla ASCII/UTF-8, la `H` es el número hexadecimal `48`, la `o` es el `6f`, la `l` es el `6c` y la `a` es el `61`. Ocupa exactamente 4 bytes, sin ningún cero de relleno.

#### 2. Radiografía del archivo en UTF-16 (2 bytes por letra, 1 cero de relleno por letra):
```bash
od -t x1 -t c hola_utf16.txt
```
**Resultado:**
```text
0000000  00  48  00  6f  00  6c  00  61
         \0   H  \0   o  \0   l  \0   a
0000010
```
* **Explicación:** Como UTF-16 obliga a usar bloques de 16 bits (2 bytes) por letra, introduce **un byte de ceros (`00` / `\0`)** delante de cada carácter.

#### 3. Radiografía del archivo en UTF-32 (4 bytes por letra, 3 ceros de relleno por letra):
```bash
od -t x1 -t c hola_utf32.txt
```
**Resultado:**
```text
0000000  00  00  00  48  00  00  00  6f  00  00  00  6c  00  00  00  61
         \0  \0  \0   H  \0  \0  \0   o  \0  \0  \0   l  \0  \0  \0   a
0000020
```
* **Explicación:** Como UTF-32 utiliza bloques fijos de 32 bits (4 bytes) para cada carácter, **introduce tres bytes completos llenos de ceros (`00 00 00` / `\0 \0 \0`)** delante de cada letra normal. Tres cuartas partes del archivo (12 de los 16 bytes) son simplemente ceros vacíos de relleno.

#### Extra: Ver los 24 bits de ceros en binario puro (0s y 1s)
Si quieres ver los bits individuales (ocho ceros por cada byte `00`), ejecuta `xxd` en modo binario agrupando de 4 en 4 bytes (una letra por línea):

```bash
xxd -b -c 4 hola_utf32.txt
```
**Resultado:**
```text
00000000: 00000000 00000000 00000000 01001000  ...H
00000004: 00000000 00000000 00000000 01101111  ...o
00000008: 00000000 00000000 00000000 01101100  ...l
0000000c: 00000000 00000000 00000000 01100001  ...a
```

---

## 3. Guía de Referencia: 30 Comandos Básicos de Linux para Principiantes

Aprovechando que estás dentro del contenedor Ubuntu, puedes probar cualquiera de estos **30 comandos esenciales** divididos por categorías:

### A. Orientación y Navegación por Carpetas
1. **`pwd`** (*Print Working Directory*): Muestra la ruta exacta de la carpeta en la que te encuentras ahora mismo.
   * *Ejemplo:* `pwd`
2. **`ls`** (*List*): Lista los archivos y carpetas que hay en el directorio actual.
   * *Variantes útiles:* `ls -l` (en lista detallada con tamaños y permisos), `ls -la` (muestra también los archivos ocultos que empiezan por punto `.`).
3. **`cd`** (*Change Directory*): Cambia de carpeta.
   * *Ejemplos:* `cd /etc` (ir a `/etc`), `cd ..` (subir un nivel a la carpeta padre), `cd ~` (volver a tu carpeta personal).
4. **`tree`**: Dibuja en pantalla un árbol visual con todas las carpetas y subcarpetas (si no está instalado, se instala con `apt-get install -y tree`).

### B. Creación, Copia, Movimiento y Borrado de Archivos
5. **`mkdir`** (*Make Directory*): Crea una carpeta nueva.
   * *Ejemplo:* `mkdir mis_apuntes`
6. **`touch`**: Crea un archivo vacío nuevo (o actualiza su fecha de modificación si ya existía).
   * *Ejemplo:* `touch notas.txt`
7. **`cp`** (*Copy*): Copia archivos o carpetas de un lugar a otro.
   * *Ejemplo:* `cp hola_utf8.txt copia_hola.txt` (usa `cp -r carpeta1 carpeta2` para copiar carpetas enteras).
8. **`mv`** (*Move*): Sirve tanto para **mover** un archivo de carpeta como para **cambiarle el nombre**.
   * *Ejemplo:* `mv copia_hola.txt nuevo_nombre.txt`
9. **`rm`** (*Remove*): Borra un archivo de forma permanente (en la terminal de Linux no hay "Papelera de reciclaje").
   * *Ejemplo:* `rm nuevo_nombre.txt` (usa `rm -r carpeta` para borrar una carpeta y todo su interior).

### C. Lectura, Edición y Creación de Texto
10. **`cat`** (*Concatenate*): Muestra de golpe todo el contenido de un archivo de texto en la pantalla.
    * *Ejemplo:* `cat hola_utf8.txt`
11. **`less`**: Abre un archivo de texto largo página a página permitiendo desplazarse con las flechas del teclado (se sale pulsando la tecla **`q`**).
    * *Ejemplo:* `less /etc/services`
12. **`head`**: Muestra únicamente las primeras 10 líneas de un archivo (o las que le indiques con `-n`).
    * *Ejemplo:* `head -n 5 /etc/passwd`
13. **`tail`**: Muestra las últimas 10 líneas de un archivo. Muy usado para ver el final de archivos de registro (*logs*).
    * *Ejemplo:* `tail -n 5 /etc/passwd`
14. **`nano`**: Abre un editor de textos interactivo muy fácil de usar dentro de la terminal. Abajo muestra los atajos: `Ctrl+O` para guardar y `Ctrl+X` para salir.
    * *Ejemplo:* `nano notas.txt`
15. **`echo`** y **`printf`**: Imprimen un texto en pantalla (o dentro de un archivo si usamos `>` para sobrescribir o `>>` para añadir al final).
    * *Ejemplo:* `echo "Primera línea" > notas.txt`

### D. Inspección, Búsqueda y Filtros
16. **`file`**: Analiza el contenido interno de un archivo y te dice qué es realmente (independientemente de su extensión) y su codificación.
    * *Ejemplo:* `file hola_utf8.txt hola_utf16.txt hola_utf32.txt`
17. **`wc`** (*Word Count*): Cuenta cuántas líneas (`-l`), palabras (`-w`) o bytes (`-c`) tiene un archivo.
    * *Ejemplo:* `wc -c hola_utf32.txt`
18. **`grep`**: Busca una palabra o patrón de texto dentro de un archivo y muestra solo las líneas donde aparece.
    * *Ejemplo:* `grep "root" /etc/passwd`
19. **`find`**: Busca archivos o carpetas por su nombre dentro del disco.
    * *Ejemplo:* `find /practica -name "*.txt"`
20. **`od`** (*Octal Dump*) y **`xxd`**: Vuelcan el contenido interno de cualquier archivo en formato hexadecimal, octal o binario byte a byte.
    * *Ejemplo:* `od -t x1 -t c hola_utf32.txt`
21. **`iconv`**: Convierte archivos de texto entre distintas codificaciones de caracteres (UTF-8, UTF-16, UTF-32, ISO-8859-1).

### E. Información del Sistema, Procesos y Permisos
22. **`whoami`**: Te dice qué nombre de usuario estás utilizando en este momento (por ejemplo, `root`).
23. **`uname -a`**: Muestra información del núcleo (*kernel*) de Linux y la arquitectura del procesador.
24. **`df -h`** (*Disk Free*): Muestra el espacio libre y ocupado en los discos duros en formato legible (*Human-readable*: MB, GB).
25. **`free -h`**: Muestra cuánta memoria RAM tiene el sistema, cuánta está en uso y cuánta queda libre.
26. **`ps aux`** (o **`top`**): Muestra la lista de todos los programas y procesos que se están ejecutando en este instante en la máquina.
27. **`chmod`** (*Change Mode*): Cambia los permisos de lectura (`r`), escritura (`w`) y ejecución (`x`) de un archivo.
    * *Ejemplo:* `chmod +x mi_script.sh` (le da permiso para ejecutarse como un programa).

### F. Ayuda, Limpieza y Salida
28. **`history`**: Muestra la lista numerada de todos los comandos que has escrito durante la sesión. (Truco: puedes pulsar la **flecha hacia arriba `↑`** del teclado para recuperar comandos anteriores).
29. **`clear`** (o el atajo **`Ctrl + L`**): Limpia toda la pantalla de la terminal dejando el cursor arriba del todo.
30. **`exit`**: Cierra la sesión de Linux. Al haber lanzado nuestro contenedor de Docker con la opción `--rm`, escribir `exit` apagará y eliminará limpiamente nuestra máquina de pruebas devolviéndonos a la terminal de nuestro ordenador.

---

## 4. Práctica Avanzada: Conexión Multiventana y Secuencia Guiada de Comandos

En el mundo real de los servidores y el desarrollo profesional nunca se trabaja con una única ventana de terminal. Es muy habitual tener **un proceso ejecutándose en una ventana** (por ejemplo, una base de datos o un servidor web) y abrir **una segunda ventana** para conectarnos a la misma máquina, inspeccionar archivos, vigilar recursos o depurar problemas.

Vamos a experimentar esta dinámica paso a paso.

---

### Paso A: Dejar nuestro contenedor en marcha (Ventana 1)

Si aún tienes la terminal del **Paso 1** abierta con tu contenedor corriendo, ¡perfecto! Si no la tienes o la cerraste, arranca un contenedor asignándole un nombre reconocible para facilitarnos la vida:

```bash
docker run -it --name mi_linux ubuntu bash
```

> **Nota:** La opción `--name mi_linux` le da una etiqueta clara a nuestro contenedor para no tener que memorizar un identificador numérico aleatorio.

Deja esta **Ventana 1** abierta con su consola `root@...:/#` visible.

---

### Paso B: Conectarse al mismo contenedor desde otra ventana (Ventana 2)

1. Abre una **nueva ventana o pestaña** de tu aplicación Terminal (o PowerShell).
2. Preguntémosle a Docker qué contenedores están encendidos en este momento:
   ```bash
   docker ps
   ```
   Verás una fila donde aparece la imagen `ubuntu` y al final su nombre (`mi_linux`).
3. Ahora nos conectaremos al interior de **ese mismo contenedor que ya está vivo** utilizando el comando `docker exec`:
   ```bash
   docker exec -it mi_linux bash
   ```

> **¿Qué acaba de ocurrir?**  
> `docker exec` ejecuta un nuevo programa dentro de un contenedor en marcha. Al pedirle `-it ... bash`, hemos abierto **una segunda puerta de acceso simultánea**. Ambas ventanas están compartiendo exactamente el mismo procesador, la misma memoria y el mismo sistema de archivos. Lo que hagas o crees en la Ventana 2 existirá de inmediato en la Ventana 1.

---

### Paso C: Una secuencia bonita y pedagógica de comandos en la Ventana 2

Desde esta nueva ventana, sigue esta secuencia lógica de trabajo diseñada para asentar los 30 comandos que vimos anteriormente como si fueras un auténtico administrador de sistemas:

#### 1. Reconocimiento e identidad: ¿Quién soy y dónde estoy?
```bash
whoami
pwd
uname -a
```
* Compruebas que eres el usuario `root` (superadministrador), que estás situado en el directorio raíz `/` y ves los detalles del kernel Linux.

#### 2. Auditoría rápida de recursos: ¿Cómo está de salud la máquina?
```bash
df -h
free -h
```
* Ves el espacio disponible en disco (`df -h`) y el consumo de memoria RAM (`free -h`). En contenedores ligeros verás consumos mínimos de apenas unos megabytes.

#### 3. Exploración del terreno y creación del espacio de trabajo
```bash
ls -la /
mkdir /workspace
cd /workspace
pwd
```
* Listas el sistema raíz viendo permisos y archivos ocultos (`ls -la`), creas una carpeta de proyecto (`mkdir /workspace`), entras en ella (`cd`) y confirmas tu nueva ubicación (`pwd`).

#### 4. Generación y edición de contenido
```bash
touch app.log
echo "Servicio iniciado correctamente" > app.log
echo "Conexión entrante desde 192.168.1.50" >> app.log
echo "ADVERTENCIA: Memoria al 85%" >> app.log
echo "ERROR: Fallo de autenticación para usuario anonimo" >> app.log
echo "Servicio detenido por mantenimiento" >> app.log
```
* Creas un archivo con `touch` y utilizas `>` para escribir la primera línea y `>>` para añadir más líneas sin borrar lo anterior.

#### 5. Lectura y conteo rápido
```bash
cat app.log
wc -l app.log
head -n 2 app.log
tail -n 2 app.log
```
* `cat` te muestra todo el fichero; `wc -l` cuenta sus 5 líneas; `head` te enseña las dos primeras y `tail` las dos últimas.

#### 6. Búsqueda y filtrado forense con `grep`
```bash
grep "ERROR" app.log
grep -n "ADVERTENCIA" app.log
```
* Encuentras al instante las líneas críticas de tu registro de eventos.

#### 7. Seguridad y permisos de ejecución
Vamos a crear un pequeño script de mantenimiento:
```bash
printf '#!/bin/bash\necho "Auditoría en curso..."\ndate\n' > informe.sh
ls -l informe.sh
chmod +x informe.sh
ls -l informe.sh
./informe.sh
```
* Observa cómo antes de `chmod +x` el archivo no tenía permisos de ejecución (`-rw-r--r--`). Tras `chmod +x`, los permisos cambian a `-rwxr-xr-x` (a menudo coloreado en verde) y Linux te permite ejecutarlo directamente con `./informe.sh`.

#### 8. Monitorización de procesos activos
```bash
ps aux
```
* Verás la lista de procesos: verás los dos intérpretes de comandos `bash` correspondientes a la **Ventana 1** y a la **Ventana 2**.

#### 9. Historial y limpieza
```bash
history | tail -n 15
clear
```
* Repasas los últimos comandos que has escrito para recordar los pasos dados y dejas tu terminal impecable con `clear`.

---

## 5. Discusión Clave: El Modo Desacoplado (*Detach* `-d`), Procesos en Segundo Plano y ¿Dónde va la Salida Estándar (*stdout*)?

Uno de los conceptos más importantes y que más confunden a quienes empiezan en Linux y Docker es la diferencia entre ejecutar un programa en **primer plano (*foreground*)** y en **segundo plano o modo desacoplado (*detached / background*)**.

---

### 1. ¿Qué es el modo interactivo vs el modo Detach?

Hasta ahora hemos lanzado contenedores con:
```bash
docker run -it ...
```
* Aquí, **tu teclado está físicamente atado a la entrada del contenedor** y **tu pantalla está atada a su salida**. Si el contenedor imprime algo, lo ves en directo; si pulsas `Ctrl + C` o escribes `exit`, el proceso principal finaliza y el contenedor se apaga.

En cambio, en servidores de producción (bases de datos, APIs web, bots) no queremos una terminal ocupada. Para ello usamos la opción **`-d`** (*detached* o desacoplado):
```bash
docker run -d --name mi_servidor nginx
```
* Docker descarga y arranca el contenedor, pero **te devuelve el control de tu terminal inmediatamente**. En la pantalla solo ves un código largo (el identificador único del contenedor).

---

### 2. El misterio: Si está desacoplado, ¿dónde va la Salida Estándar (*stdout*)?

En los sistemas operativos tipo Unix/Linux, todo proceso que arranca dispone de tres canales de comunicación automáticos llamados **flujos estándar (*Standard Streams*)**:

```
                  +-----------------------------------+
[ Teclado ] ----->| 0: stdin  (Entrada Estándar)      |
                  |                                   |
                  |          PROCESO LINUX            |
                  |                                   |
                  | 1: stdout (Salida Estándar: info) |---> [ Pantalla ]
                  | 2: stderr (Salida de Error)       |---> [ Pantalla ]
                  +-----------------------------------+
```

1. **`stdin` (0 - Entrada estándar):** Por donde el proceso recibe datos (habitualmente tu teclado).
2. **`stdout` (1 - Salida estándar):** Por donde el proceso emite sus mensajes normales y resultados.
3. **`stderr` (2 - Salida de errores):** Canal independiente reservado para mensajes de error y advertencias.

Cuando un proceso se ejecuta con **detach (`-d`)**, se **desconectan la pantalla y el teclado** de ese proceso. El programa sigue ejecutándose y sigue emitiendo datos por `stdout`, pero **no hay ningún cristal de terminal acoplado para renderizar esos caracteres**.

¿Significa eso que la información se ha perdido para siempre? **Rotundamente no.** Y aquí es donde entran las dos grandes soluciones del mundo Linux y Docker.

---

### 3. Solución A: A nivel de Docker con `docker logs`

Docker actúa como una "caja negra inteligente". Cada vez que un contenedor en modo `-d` emite algo por `stdout` o `stderr`, el *Docker Daemon* lo intercepta silenciosamente y lo almacena en un archivo de registro interno (*json-file logging driver*).

Para inspeccionar esa salida desde el exterior tenemos dos opciones:

#### Ver los mensajes acumulados hasta el momento:
```bash
docker logs mi_servidor
```
Muestra todo el historial de texto que el proceso ha generado desde que arrancó.

#### "Cazar" la salida en vivo (como si estuviéramos mirando la pantalla):
```bash
docker logs -f mi_servidor
```
> La opción **`-f`** (*follow*) mantiene abierta la conexión con los logs: a medida que el proceso en segundo plano escriba nuevas líneas, irán apareciendo en tu terminal en tiempo real. Para salir basta pulsar **`Ctrl + C`** (esto solo desconecta tu visor de logs, el contenedor continúa funcionando plácidamente de fondo).

---

### 4. Solución B: A nivel de Linux nativo (Redirecciones y segundo plano)

Dentro del propio Linux ocurre exactamente lo mismo cuando ejecutamos un script o comando y no queremos que bloquee nuestra sesión. Si ejecutas:

```bash
python3 servicio.py &
```
El símbolo **`&`** al final envía el proceso a segundo plano (*background*). Sin embargo, si ese programa sigue imprimiendo mensajes por `stdout`, estos seguirán apareciendo en mitad de tu pantalla mientras intentas escribir otros comandos, lo cual es muy molesto. Y peor aún: si cierras la ventana de terminal, el proceso podría morir.

La práctica profesional en Linux consiste en **redirigir explícitamente los flujos a un archivo físico de registro (*log file*)**:

```bash
./mi_proceso.sh > salida.log 2>&1 &
```

Desglosemos esta "fórmula mágica" que todo desarrollador debe dominar:
* **`> salida.log`**: Desvía el canal 1 (`stdout`) hacia el archivo `salida.log`.
* **`2>&1`**: Conecta el canal 2 (`stderr`, errores) al mismo destino que el canal 1 (`stdout`), de modo que tanto los mensajes normales como los errores queden registrados juntos en el mismo fichero.
* **`&`**: Libera tu terminal ejecutando todo en segundo plano.

#### ¿Cómo revisamos la salida en otra ventana?
Ahora que la salida está a buen recaudo en `salida.log`, abrimos nuestra segunda ventana de terminal y usamos el comando **`tail -f`**:
```bash
tail -f salida.log
```
* `tail -f` monitoriza el archivo y te muestra en vivo cada nueva línea que el programa en segundo plano va escribiendo.

---

### 5. Experimento de Laboratorio: Ponlo a prueba ahora mismo

Comprobemos todo esto empíricamente con dos ventanas:

#### En la Ventana 1 (Máquina anfitriona):
Lanza un contenedor desacoplado (`-d`) que actúe como un "reloj emisor" imprimiendo la hora cada 2 segundos:
```bash
docker run -d --name emisor_hora ubuntu bash -c "while true; do echo \"[TIC-TAC] Son las \$(date +%T)\"; sleep 2; done"
```
* Fíjate que tu terminal te devuelve el control de inmediato. No ves ningún texto de "TIC-TAC".

#### En la Ventana 2:
1. Comprueba que el contenedor está vivo:
   ```bash
   docker ps
   ```
2. Caza la salida estándar en directo:
   ```bash
   docker logs -f emisor_hora
   ```
   * ¡Ahí están! Cada 2 segundos verás brotar una nueva línea con la hora exacta.
3. Pulsa `Ctrl + C` para dejar de ver los logs (el contenedor sigue funcionando).
4. Ahora entra dentro del contenedor para ver su proceso activo:
   ```bash
   docker exec -it emisor_hora ps aux
   ```
   * Verás el bucle `bash` y el comando `sleep` activos.

#### Limpieza final al terminar la práctica:
Una vez terminadas tus pruebas, apaga y elimina el contenedor de prueba con:
```bash
docker rm -f emisor_hora
```