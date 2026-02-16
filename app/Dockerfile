FROM python:3.11-slim

# Install git + curl + wget
RUN apt-get update && \
    apt-get install -y git curl wget && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]

