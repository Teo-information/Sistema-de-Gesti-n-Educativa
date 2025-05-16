FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    python3-dev \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Crear directorio para archivos estáticos
RUN mkdir -p staticfiles

# Recolectar archivos estáticos
RUN python manage.py collectstatic --noinput

# Configurar variables de entorno para producción
ENV DJANGO_SETTINGS_MODULE=sistema_educativo.settings
ENV PORT=8000

# Exponer el puerto
EXPOSE $PORT

# Comando para ejecutar la aplicación
CMD gunicorn sistema_educativo.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 60