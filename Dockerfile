FROM python:3.10-alpine
LABEL maintainer="Alexander Zorkin"

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "python3", "bot.py" ]
