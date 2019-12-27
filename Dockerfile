FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir beautifulsoup4 feedparser

COPY . .

CMD [ "python","./main.py","-r","$LOCATION"]
