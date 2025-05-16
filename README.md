# Sistema de Gestión Educativa

Este es un sistema web desarrollado en Django para la gestión de estudiantes, cursos, matrículas y notas en una institución educativa.

## Características

- Gestión de estudiantes (alta, baja, modificación, listado)
- Gestión de cursos
- Matrícula de estudiantes en cursos
- Registro y consulta de notas
- Panel de administración para usuarios autenticados
- Interfaz moderna y responsiva con Bootstrap
- Formularios estilizados con Django Crispy Forms
- Autenticación de usuarios

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Teo-information/Sistema-de-Gesti-n-Educativa.git
   cd Sistema-de-Gesti-n-Educativa
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realiza las migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Crea un superusuario:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicia el servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Accede a la aplicación:**
   - Panel de administración: [http://localhost:8000/admin/](http://localhost:8000/admin/)
   - Sistema: [http://localhost:8000/](http://localhost:8000/)

## Estructura del Proyecto

- `estudiantes/` - Gestión de estudiantes
- `cursos/` - Gestión de cursos
- `matriculas/` - Matrículas de estudiantes en cursos
- `notas/` - Registro y consulta de notas
- `templates/` - Plantillas HTML
- `static/` - Archivos estáticos (CSS, JS, imágenes)

## Tecnologías utilizadas

- Python 3
- Django
- Bootstrap 5
- Django Crispy Forms

## Licencia

Este proyecto está bajo la licencia MIT.

---

> Desarrollado por Teo-information 