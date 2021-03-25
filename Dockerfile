FROM python3.7-alpine
LABEL maintainer="Alexander Zorkin"

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "120", "main:app" ]