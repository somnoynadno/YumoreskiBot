FROM python:3.7-alpine3.12
LABEL maintainer="Alexander Zorkin"

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD [ "gunicorn", "--bind", "0.0.0.0:6789", "--timeout", "120", "main:app" ]
