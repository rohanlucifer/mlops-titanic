FROM python:3.9

WORKDIR /app
COPY src/ /app/
COPY data/titanic.csv /app/data/titanic.csv

RUN pip install -r requirements.txt
RUN python train.py

EXPOSE 5000
CMD ["python", "predict.py"]

