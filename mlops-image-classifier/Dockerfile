FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app
WORKDIR /app

EXPOSE 5000
CMD ["python", "predict.py"]

