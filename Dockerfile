FROM python:3.12-slim

WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
COPY README.md .
COPY hive_server.py .

RUN pip install --no-cache-dir -e .

ENV PYTHONUNBUFFERED=1

CMD ["python", "hive_server.py"]