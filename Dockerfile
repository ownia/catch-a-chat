FROM python:3.6-alpine

RUN adduser -D catchachat

WORKDIR /home/catchachat

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY catchachat.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP catchachat.py

RUN chown -R catchachat:catchachat ./
USER catchachat

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]