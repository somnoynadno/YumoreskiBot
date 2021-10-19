FROM python:3.8-alpine
LABEL maintainer="Alexander Zorkin"

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD [ "python3", "bot.py" ]
