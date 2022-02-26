# Heroku-Flask-Docker

Flask webapp sample with Heroku - Docker

## Local development

### Install libraries

```bash
$ pip3 install -r requirements.txt

Collecting flask
  Downloading flask....tar.gz (1000 kB)
```

### Run webapp

```bash
$ gunicorn --bind 0.0.0.0:8080 wsgi

[2022-02-26 19:37:54 +0000] [2119] [INFO] Starting gunicorn 20.1.0
[2022-02-26 19:37:54 +0000] [2119] [INFO] Listening at: http://0.0.0.0:8080 (2119)
[2022-02-26 19:37:54 +0000] [2119] [INFO] Using worker: sync
[2022-02-26 19:37:54 +0000] [2121] [INFO] Booting worker with pid: 2121
[2022-02-26 19:38:01 +0000] [2119] [INFO] Handling signal: int
[2022-02-26 19:38:02 +0000] [2121] [INFO] Worker exiting (pid: 2121)
[2022-02-26 19:38:02 +0000] [2119] [INFO] Shutting down: Master
```

### Run webapp with gunicorn

```bash
$ python3 app.py

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.0.2.100:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 292-118-220
```

## Deploy to Heroku - Docker container

### Install heroku cli

```bash
$ curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

### Heroku login (Password -> Heroku Token)

```bash
$ heroku login -i
```

### Create container

```bash
$ heroku create webapp
```

### Push remote

```bash
$ heroku container:push web
```

### Release container

```bash
$ heroku container:release web
```

### Open webapp

```bash
$ heroku open
```

### Logs webapp

```bash
$ heroku logs --tail
```
