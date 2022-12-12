FROM python:3.10

WORKDIR /nutriapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]