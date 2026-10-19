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