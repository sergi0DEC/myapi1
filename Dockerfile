# 1. Imagen base oficial de Python
FROM python:3.12-slim

# 2. Establecer directorio de trabajo
WORKDIR /app

# 3. Copiar archivos de dependencias (si tienes requirements.txt)
COPY requirements.txt .

# 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el proyecto
COPY . .

# 6. Comando para correr FastAPI con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
