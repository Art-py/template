FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend ./backend

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]
