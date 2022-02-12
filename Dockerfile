FROM python:3.9.9

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python /app/prestart.py