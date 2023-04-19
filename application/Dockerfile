# Dockerfile
FROM alpine:latest

RUN apk add --no-cache python3 py3-pip

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD  ["app.py"]