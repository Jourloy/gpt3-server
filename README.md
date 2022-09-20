# ruGPT3 server

## Getting start

### Change settings

Look into `src/gpt3/settings.py` and change `SECRET_KEY` and `ALLOWED_HOSTS`!

### About ENV

Project have two env variables, look into `.env.temlpate`. If you are want to use Docker-Compose way, so you should create `.env` file. `HOST_IP` is allowed IPs for you backend (`0.0.0.0` = Allow all). `HOST_PORT` is a port for your backend

If you are want to use Docker way, so you should pass this variables in command

### Starting

#### Docker-Compose

You can just start docker-compose

```bash
$ docker-compose up -d
```

Done, now you can use endpoints

##### Warning

You should have too many memory for start docker. If docker build was killed use **Install packages** way.

#### Docker

You can build a docker container

```bash
$ docker build --build-arg HOST_IP=0.0.0.0 --build-arg HOST_PORT=3000 -t rugpt3 .
```

And run it

```bash
$ docker run -d --name ruGP3-Apache rugpt3
```

##### Warning

You should have too many memory for start docker. If docker build was killed use **Python** way

#### Python

##### Install packages

```bash
$ pip install requirements.txt
```

##### Start

In example below **0.0.0.0** is a IP. If you don't want share access and use local only, just remove this IP. **10000** is a port for app

###### MacOS / Linux

```bash
$ python manage.py runserver 0.0.0.0:10000
```

###### Windows

```bash
$ py manage.py runserver 0.0.0.0:10000
```

## Endpoints

You can change it in `src/rpute/urls.py`

### ruGPT3

Generate text on Russian

**Endpoint**: /gpt3/text?text=&maxLength=

-   text: _string_. Text for start.
-   maxLength: _number_. Recomend max length for text.

### ruTitle

Generate title for text on Russian

**Endpoint**: /gpt3/title?text=

-   text: _string_. Title will be generated for this text.

### ruDolph

Generate image by a text on Russian

**Endpoint**: /gpt3/image?text=

-   text: _string_. Short description for image

## Links

[ru-promts](https://github.com/sberbank-ai/ru-prompts)

[ruGPT3](https://github.com/sberbank-ai/ru-gpts)

[ruDolph](https://github.com/sberbank-ai/ru-dolph)
