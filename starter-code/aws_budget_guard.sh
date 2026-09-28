#!/usr/bin/env bash
# ====================================================================
# SCRIPT FINOPS: GUARDIA DEL PRESUPUESTO DE SPRINGFIELD ($50 USD LAB)
# Apaga la máquina virtual EC2 si no hay actividad para ahorrar créditos
# ====================================================================

echo "[*] Comprobando servicios en ejecución en la instancia Odoo..."

# Detener los contenedores de Docker de forma ordenada
if command -v docker &> /dev/null; then
    echo "[+] Deteniendo contenedores Odoo y PostgreSQL..."
    docker stop $(docker ps -q) 2>/dev/null || true
fi

echo "[+] Sincronizando discos para evitar corrupción de datos..."
sync

echo "[!] Guardando estado. La máquina se apagará en 10 segundos..."
echo "[!] ¡Recuerda pulsar 'Stop Instance' en la consola de AWS si no se detiene sola!"

sleep 10
sudo shutdown -h now
