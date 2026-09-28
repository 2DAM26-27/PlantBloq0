#!/usr/bin/env python3
"""
Script de Verificación del Entorno Springfield: SGE 2º DAM
Comprueba Python 3.10+, Docker CLI, Docker Compose y conexión con AWS CLI.
"""
import sys
import subprocess
import shutil

def check_step(name, check_fn):
    print(f"[*] Comprobando {name}...", end=" ")
    success, msg = check_fn()
    if success:
        print(f"[OK] -> {msg}")
        return True
    else:
        print(f"[FAIL] -> {msg}")
        return False

def check_python():
    v = sys.version_info
    if v.major == 3 and v.minor >= 10:
        return True, f"Python {v.major}.{v.minor}.{v.micro} detectado (Apto para Odoo 16 y 19)"
    return False, f"Se requiere Python 3.10 o superior (Actual: {v.major}.{v.minor})"

def check_docker():
    path = shutil.which("docker")
    if not path:
        return False, "Docker CLI no encontrado en el PATH del sistema."
    try:
        out = subprocess.check_output(["docker", "--version"], text=True).strip()
        return True, out
    except Exception as e:
        return False, str(e)

def check_compose():
    try:
        out = subprocess.check_output(["docker", "compose", "version"], text=True).strip()
        return True, out
    except Exception:
        try:
            out = subprocess.check_output(["docker-compose", "--version"], text=True).strip()
            return True, f"Legacy Compose: {out}"
        except Exception as e:
            return False, f"Docker Compose no disponible: {e}"

def check_aws_cli():
    path = shutil.which("aws")
    if not path:
        return True, "AWS CLI no instalado localmente (Opcional si se opera directamente en EC2)."
    try:
        out = subprocess.check_output(["aws", "--version"], text=True).strip()
        return True, f"AWS CLI detectado: {out}"
    except Exception as e:
        return True, f"AWS CLI disponible con advertencia: {e}"

def main():
    print("=" * 65)
    print("  VERIFICADOR DE ENTORNO: OPERACIÓN SPRINGFIELD 2.0 (SGE 2026-27)")
    print("  IES Poeta Paco Mollá - Profesora: Ana J. Martínez Montesinos")
    print("=" * 65)

    results = [
        check_step("Versión de Python", check_python),
        check_step("Instalación de Docker", check_docker),
        check_step("Docker Compose v2", check_compose),
        check_step("Herramienta AWS CLI", check_aws_cli),
    ]

    print("-" * 65)
    if all(results[:3]):
        print("[✓] ¡ENHORABUENA! Tu entorno cumple todos los requisitos técnicos.")
        print("[+] ¡Insignia desbloqueada: 'Operario del Sector 7-G' (Nivel 0)!")
        print("[+] Recuerda exportar tu Mini-Guía 0 en PDF y DOCX antes del 30/09/2026.")
        sys.exit(0)
    else:
        print("[✗] ATENCIÓN: Faltan componentes críticos en tu sistema.")
        print("[!] Revisa la guía técnica de instalación antes de continuar.")
        sys.exit(1)

if __name__ == "__main__":
    main()
