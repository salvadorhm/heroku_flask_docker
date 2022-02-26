# Heroku-Flask-Docker

Flask webapp sample with Heroku-Docker

***

## 1. GitHub repo

1. Create a new Github repo with any name and README.md file.

## 2. Gitpod for development

1. Create and account in https://gitpod.io - Use Github credentials.
2. Copy the Github URL.
3. Paste de Github URL in Gipod.

```bash
http://gitpod.io#github_url
```


***

## Local development

1. Copy and paste Dockerfile.
2. Copy and paste heroku.yml
3. Create webapp/ copy and paste all files [app.py, requirements.txt, wsgi.py, templates/, base.html, index.html]

### 1. Install libraries

Open webapp/ and run the next commands.


```bash
$ pip3 install -r requirements.txt

Collecting flask
  Downloading flask....tar.gz (1000 kB)
```

### 2. Run webapp

For debbug the webapp.

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
### 3. Run webapp  with gunicorn

For deploy the webapp.

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

***

## Deploy to Heroku - Docker container

### 1. Sign up Heroku

* Sign Up in [Heroku](https://dashboard.heroku.com/)

### 2. Install heroku cli

```bash
$ curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

### 3. Heroku login (Password -> Heroku Token)

```bash
$ heroku login -i
```

### 4. Create remote container in Heroku

```bash
$ heroku create webapp
```

### 5. Push to remote container

* This use the Dockerfile and heroku.yml for createa a remote contianer in Heroku.

```bash
$ heroku container:push web
```

### 6. Release container

* If the remote container was succefull created, then relese the webapp.

```bash
$ heroku container:release web
```

### 7. Open webapp

* Open in a Web Browser the Webapp deployed.

```bash
$ heroku open
```

### 8. Logs webapp

* Show the logs of the remote webapp.

```bash
$ heroku logs --tail
```
