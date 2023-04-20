FROM alpine:latest
LABEL maintainer="d.m.abheethaishan@gmail.com"
RUN apk add --no-cache python3 py3-pip
WORKDIR /app
COPY requirements.txt requirements.txt
COPY *.py .
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD  ["app.py"]