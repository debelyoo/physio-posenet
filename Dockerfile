FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY backend/physio-backend/requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY backend/physio-backend /usr/src/app

RUN mkdir -p /usr/src/app/static/

ADD frontend/arkathon-frontend/dist/arkathon-frontend /usr/src/app/static

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]