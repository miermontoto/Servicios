FROM python:3.7
RUN pip install flask && pip install gunicorn
RUN pip install flask-sqlalchemy pymysql flask-migrate pyfcm

RUN mkdir /amigos
COPY . /amigos
WORKDIR /amigos

ENV DEPLOYMENT_MODE 'development'
ENV FLASK_APP 'lanzar.py'
ENV DATABASE_URI 'mysql+pymysql://amigosuser:amigospass@basedatos/amigosdb'

EXPOSE 5000
CMD ["/usr/local/bin/gunicorn", "-b",  "0.0.0.0:5000", "-w", "4", "lanzar:app"]
