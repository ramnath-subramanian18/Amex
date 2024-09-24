# syntax=docker/dockerfile:1

FROM python:3.11.3-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
