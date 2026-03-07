# Dockerfile
FROM python:3.11-slim

# Verhindert, dass Python die Ausgabe puffert (Logs erscheinen sofort)
ENV PYTHONUNBUFFERED=1

# Arbeitsverzeichnis festlegen
WORKDIR /app

# Abhängigkeiten kopieren und installieren (falls vorhanden)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Den Quellcode kopieren
COPY main.py .

# Befehl zum Ausführen der Anwendung
CMD ["python", "main.py"]
