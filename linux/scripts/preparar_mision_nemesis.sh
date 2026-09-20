#!/usr/bin/env bash
# ==============================================================================
# SCRIPT DE PREPARACIÓN: Misión Servidor Némesis (Laboratorio de Prácticas Linux)
# ==============================================================================
# Este script crea un entorno aislado y seguro en ./laboratorio_nemesis/
# para que el alumno pueda experimentar sin alterar archivos críticos de su SO.
# ==============================================================================

set -e

LAB_DIR="laboratorio_nemesis"
echo "🚀 [INIT] Preparando el escenario de la misión en: ./${LAB_DIR}..."

# 1. Limpieza si ya existía
rm -rf "${LAB_DIR}"
mkdir -p "${LAB_DIR}"
cd "${LAB_DIR}"

# 2. Recrear estructura de sistema simulada
mkdir -p etc var/log home/agente tmp dev srv/backup bin

# 3. Archivos simulados del sistema
cat << 'EOF' > etc/passwd_simulado
root:x:0:0:root:/root:/bin/bash
operador:x:1001:1001:Operador del Sistema:/home/operador:/bin/bash
agente:x:1002:1002:Agente Encubierto:/home/agente:/bin/bash
intruso:x:1003:1003:Desconocido:/tmp:/bin/sh
EOF

cat << 'EOF' > etc/servidor.conf
# Configuración del Núcleo Némesis
PUERTO_ESCUCHA=8080
NIVEL_LOG=DEBUG
TIMEOUT=300
ACCESO_ROOT=DESHABILITADO
EOF

# 4. Logs con anomalías para rastrear con grep/cat/tail
cat << 'EOF' > var/log/sistema.log
2026-09-20 04:00:01 [INFO] Kernel iniciado correctamente. Versión 6.8.0-generic.
2026-09-20 04:02:15 [INFO] Servicio SSH en puerto 2222 iniciado.
2026-09-20 04:10:30 [WARNING] Consumo anómalo de memoria detectado en PID 4096.
2026-09-20 04:15:42 [SECURITY] Intento de acceso fallido desde 192.168.1.105 usuario 'admin'.
2026-09-20 04:15:44 [SECURITY] Intento de acceso fallido desde 192.168.1.105 usuario 'root'.
2026-09-20 04:16:01 [ALERT] Conexión establecida no autorizada en socket TCP:8080.
2026-09-20 04:20:10 [INFO] Tarea programada backup finalizada con código 0.
2026-09-20 04:22:00 [CRITICAL] Modificación no autorizada de permisos en /srv/backup/clave_secreta.txt.
EOF

# 5. Archivos con trampas de permisos e inodos
echo "COORDINADAS_ESCAPE: 40.4168° N, 3.7038° W" > srv/backup/clave_secreta.txt
chmod 600 srv/backup/clave_secreta.txt

echo "DATOS_TRANSMISION_CONFIDENCIAL_BLOQUE_1" > home/agente/transmision.dat
# Crear un hard link para la misión de inodos
ln home/agente/transmision.dat home/agente/transmision_respaldo.dat
# Crear un enlace simbólico
ln -s home/agente/transmision.dat home/agente/acceso_directo_transmision.lnk

# 6. Archivo oculto con datos de la trama
echo "FLAG{LINUX_KERNEL_MASTER_2026}" > home/agente/.archivo_oculto_mision.key

# 7. Script misterioso dejado por el antiguo sysadmin
cat << 'EOF' > bin/proceso_fantasma.sh
#!/usr/bin/env bash
# Proceso fantasma que simula una tarea en segundo plano
echo "[FANTASMA $$] Iniciando proceso fantasma en segundo plano..."
while true; do
    sleep 2
done
EOF
chmod +x bin/proceso_fantasma.sh

echo "✅ [LISTO] Escenario desplegado con éxito en '$(pwd)'."
echo "👉 Ahora puedes seguir la guía paso a paso en: PRACTICA_LINUX_STORYTELLING.md"
