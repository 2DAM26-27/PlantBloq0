# Resumen Técnico: Nivelación Python 3, Docker y AWS Academy Learner Lab
## Bloque 0 | Operación Springfield: Modernización de la Fábrica Duff y el Badulaque
**Módulo**: Sistemas de Gestión Empresarial (SGE - 2º DAM) | Curso 2026-2027

---

## 1. Fundamentos de Python 3 para el Ecosistema Odoo
Odoo está íntegramente construido sobre Python. Para programar módulos personalizados y comprender el ORM se requiere dominar:

1. **Tipado Dinámico y Estructuras de Datos Nativas**:
   - Diccionarios (`dict`) para definición de contextos, valores por defecto y manifiestos.
   - Listas de tuplas (`list[tuple]`) para definición de dominios de filtrado en el ORM: `[('state', '=', 'done'), ('user_id', '=', uid)]`.
2. **Programación Orientada a Objetos (POO)**:
   - Clases y herencia múltiple (`class DuffBatch(models.Model)`).
   - Métodos mágicos (`__init__`, `super()`).
3. **Decoradores de Python**:
   - Funciones que envuelven a otras funciones para dotarlas de comportamiento reactivo en Odoo: `@api.depends`, `@api.constrains`, `@api.model`.
4. **Manejo Robusto de Excepciones**:
   - `UserError` y `ValidationError` para detener transacciones de base de datos cuando se violan reglas de negocio (ej. graduación de alcohol excesiva).

---

## 2. Docker & Docker Compose: El Motor de Contenedores de Springfield

### Conceptos Clave:
- **Imágenes vs. Contenedores**: La imagen oficial de Odoo (`odoo:16.0` u `odoo:19.0`) y de PostgreSQL (`postgres:15-alpine`) son plantillas inmutables. El contenedor es la instancia en ejecución.
- **Volúmenes Persistentes**:
  - Volúmenes con nombre de Docker para custodiar `/var/lib/postgresql/data` y `/var/lib/odoo` (filestore de adjuntos).
  - Bind mounts locales (`./custom_addons:/mnt/extra-addons`) para que cualquier cambio de código en Visual Studio Code se refleje inmediatamente en Odoo sin reconstruir la imagen.
- **Redes Docker**: Comunicación interna mediante resolución de nombres DNS. Odoo se conecta a Postgres usando `db` como hostname sin exponer contraseñas en la red pública.

---

## 3. Conexión y FinOps con AWS Academy ($50 USD Sandbox)

Para alumnos de 2º DAM (conectando SGE con OPT-CLOUD):
- **Instancia EC2 Ubuntu**: Servidor en la nube en la región `us-east-1` con IP pública elástica o asignada.
- **Acceso SSH mediante `vockey.pem`**:
  ```bash
  chmod 400 vockey.pem
  ssh -i "vockey.pem" ubuntu@<IP_EC2_AWS>
  ```
- **Control de Saldo FinOps**:
  - Cada hora de ejecución cuesta céntimos de dólar de los 50 dólares asignados.
  - Al terminar la práctica es **preceptivo** ejecutar:
    ```bash
    sudo docker compose stop
    sudo shutdown -h now  # O desde la consola AWS: Stop Instance
    ```
