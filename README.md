La documentación interactiva estará disponible en: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📁 Estructura del Proyecto

*   `main.py`: Punto de entrada de la aplicación y definición de endpoints.
*   `models.py`: Definición de los modelos de datos y esquemas de Pydantic.
*   `database.py`: Configuración del motor de SQLModel y conexión a SQLite.
*   `security.py`: Lógica de hashing, validación y gestión del Pepper.

## 📝 Endpoints Principales

*   `POST /register`: Registra un nuevo usuario, aplica el Pepper y almacena el hash resultante.
*   `POST /login`: Autentica al usuario verificando su contraseña contra el hash almacenado en la base de datos.

---

### Tips adicionales para tu README:
*   **Capturas de pantalla:** Si quieres que destaque, puedes añadir una sección de "Evidencias" y enlazar la captura de tu base de datos donde se vea que usuarios con la misma contraseña tienen hashes distintos.
*   **Autor:** No olvides poner tu nombre al final (Matheus Solano de la SalaPara tu archivo `README.md`, lo ideal es que sea claro y profesional, permitiendo que cualquier persona (o tu profesor) entienda qué hace el proyecto y cómo ejecutarlo.

Aquí tienes una estructura recomendada que puedes copiar y pegar:

---

# API de Autenticación Segura con SQLModel

Este proyecto implementa un sistema de gestión de identidades robusto utilizando **FastAPI** y **SQLModel**. Se enfoca en la protección de credenciales mediante el uso de capas de seguridad avanzadas: **Hashing**, **Salting** y **Peppering**.

## 🛡️ Características de Seguridad

*   **Algoritmo de Hashing:** Se utiliza **Bcrypt**, un algoritmo de derivación de claves "lento" diseñado para resistir ataques de fuerza bruta.
*   **Salting:** Implementado automáticamente por Bcrypt para asegurar que cada usuario tenga un hash único, incluso si comparten la misma contraseña.
*   **Peppering:** Se añade una capa de seguridad global mediante una cadena secreta (Pepper) almacenada en variables de entorno, la cual se concatena antes del proceso de hashing.

## 🚀 Requisitos e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-de-la-carpeta
   ⚙️ Configuración e Instalación
Clonar el repositorio:

Bash
git clone <url-del-repositorio>
cd api_segura
Instalar dependencias:

Bash
pip install fastapi[all] sqlmodel bcrypt python-dotenv
Configurar variables de entorno:
Crea un archivo .env en la raíz con el siguiente contenido:

Fragmento de código
PEPPER=TuClaveSecretaGlobalAqui
