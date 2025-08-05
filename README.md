# ✅ TodoApp

Una aplicación minimalista de gestión de tareas (ToDo) construida con **FastAPI** como backend. Incluye autenticación básica, operaciones CRUD y almacenamiento en base de datos con SQLite.

---

## 🚀 Tecnologías utilizadas

- 🔧 **FastAPI** – Framework moderno y rápido para construir APIs con Python
- 🗃️ **SQLite** – Base de datos ligera y sencilla para desarrollo local
- 🔐 **JWT Authentication** – Seguridad mediante tokens
- 🔁 **CRUD completo** – Crear, Leer, Actualizar y Eliminar tareas
- 🧪 **Pytest** – Para testing básico (si lo usaste)
- 🌐 **Uvicorn** – Servidor ASGI para producción/desarrollo

---

## 📸 Capturas de pantalla *(opcional)*

_Añade aquí imágenes de tu app en uso si tiene interfaz gráfica (puedes hacerlo en el futuro si haces frontend)_

---

## ⚙️ Instalación y ejecución local

```bash
# 1. Clona el repositorio
git clone https://github.com/santicardona/todoapp.git
cd todoapp

# 2. Crea entorno virtual
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Corre el servidor
uvicorn main:app --reload
