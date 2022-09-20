FROM python:3.9.9

ARG HOST_IP
ARG HOST_PORT

ENV HOST_IP=${HOST_IP}
ENV HOST_PORT=${HOST_PORT}

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python /app/prestart.py

EXPOSE ${HOST_PORT}

CMD ["python", "src/manage.py", "runserver", "${HOST_IP}:${HOST_PORT}"];