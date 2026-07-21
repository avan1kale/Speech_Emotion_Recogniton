FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY . .
CMD gunicorn --workers 1 --threads 2 --timeout 120 --bind 0.0.0.0:${PORT:-5000} app:app