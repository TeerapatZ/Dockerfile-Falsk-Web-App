FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install Flask requests

EXPOSE 5005

ENV NAME=World

CMD ["python","app.py"]