# 🐧 Módulo Linux - UFV Bootcamp 2026

Bienvenido al módulo de **Sistemas Operativos GNU/Linux**. Este espacio reúne infografías didácticas, ejercicios guiados con *storytelling*, scripts de automatización y una guía de referencia rápida para dominar la terminal desde cero hasta nivel profesional.

---

## 🚀 Práctica Destacada: Operación Némesis (Storytelling SysAdmin)

Sumérgete en una misión paso a paso donde encarnas a un administrador de sistemas recién llegado a un servidor en crisis:

👉 **[📖 Comenzar la Práctica: Operación Némesis (Paso a Paso)](./PRACTICA_LINUX_STORYTELLING.md)**

Para desplegar el entorno de prácticas aislado en tu terminal:
```bash
bash scripts/preparar_mision_nemesis.sh
cd laboratorio_nemesis
```

---

## 🎨 Serie Visual: Linux Desde Cero (6 Infografías)

La formación se apoya en una serie gráfica de 6 láminas infográficas de alta resolución:

| Parte | Título | Temas Clave |
| :--- | :--- | :--- |
| **[Parte 1](./linux-intro1.png)** | **¿Qué es un Sistema Operativo?** | Kernel vs GNU, Hardware, Software, Linus Torvalds & Richard Stallman, Shell. |
| **[Parte 2](./linux-intro2.png)** | **Terminal, Shell y Primeros Comandos** | GUI vs CLI, anatomía de comandos, `ls`, `cd`, `mkdir`, redirecciones (`>`, `>>`) y tuberías (`\|`). |
| **[Parte 3](./linux-intro3.png)** | **Sistema de Archivos Linux** | Jerarquía `/`, carpetas del sistema (`/etc`, `/var`, `/home`), rutas, hard links vs symlinks. |
| **[Parte 4](./linux-intro4.png)** | **¿Cómo se guarda un archivo por dentro?** | Inodos, bloques de 4 KB, metadatos, tamaño lógico (`ls`) vs ocupación real (`du`). |
| **[Parte 5](./linux-intro5.png)** | **Usuarios, Permisos y Procesos** | Tríada `rwx` (octal), `chmod`, `chown`, permisos especiales (`Sticky bit`, `Setuid`), señales `kill -15` vs `kill -9`. |
| **[Parte 6](./linux-intro6.png)** | **Red, Scripting y Visión Final** | Sockets TCP/UDP, estados `LISTENING`/`ESTABLISHED`, Netfilter/Firewall, scripts Bash con `trap`. |

---

## 🧰 Gestores de Paquetes según la Distribución

Para instalar herramientas adicionales (`tree`, `htop`, `netcat`, `curl`):

- **Ubuntu / Debian / Linux Mint**: `sudo apt update && sudo apt install -y tree htop netcat-openbsd curl`
- **Fedora / RHEL / Rocky Linux**: `sudo dnf install -y tree htop nc curl`
- **Arch Linux / Manjaro**: `sudo pacman -Sy tree htop gnu-netcat curl`
- **openSUSE**: `sudo zypper install -y tree htop netcat-openbsd curl`
- **macOS**: `brew install tree htop netcat curl`

---

## 📜 Scripts en este Módulo
- **[`scripts/preparar_mision_nemesis.sh`](./scripts/preparar_mision_nemesis.sh)**: Generador del escenario interactivo de la práctica.
- **[`scripts/resource_management_example.sh`](./scripts/resource_management_example.sh)**: Script de ejemplo de gestión de recursos cloud / shell.
