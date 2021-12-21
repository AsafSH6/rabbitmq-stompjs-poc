FROM python:3.10.1-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV PYTHONUNBUFFERED=1

COPY . .

CMD [ "python3", "main.py"]