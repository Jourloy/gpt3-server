# ruGPT3 server

## Getting start

### Install packages

soon

### Start

In example below **0.0.0.0** is a IP. If you don't want share access and use local only, just remove this IP. **10000** is a port for app.

#### MacOS / Linux

```bash
$ python manage.py runserver 0.0.0.0:10000
```

#### Windows

```bash
$ py manage.py runserver 0.0.0.0:10000
```

## Endpoints

### ruGPT3

**Endpoint**: /gpt3/text?text=&maxLength=

-   text: _string_. Text for start.
-   maxLength: _number_. Recomend max length for text.
