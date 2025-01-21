FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar todo el contenido del proyecto al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Establecer PYTHONPATH para que Python reconozca el paquete `app`
ENV PYTHONPATH=/app

# Exponer el puerto que usa Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
