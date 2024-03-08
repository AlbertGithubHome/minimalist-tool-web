# minimalist-tool-web
Develop a minimalist tool webpage to facilitate daily work and life.

```
.
├── main.py
├── static
│   └── style.css
├── templates
│   ├── base64.html
│   ├── bytes.html
│   ├── holidays.html
│   ├── index.html
│   └── xor.html
└── tools
│   ├── datetimes.py
    └── encoding.py
```

# examle web

[minimalist tool web](http://008ct.space:9205/)

# install requirements

```bash
[python3 -m] pip install -r requirements.txt
```

# run

```
python3 main.py
```

# some pip source address

- https://pypi.douban.com/simple/
- https://mirrors.aliyun.com/pypi/simple/

# docker

## make

```bash
sudo docker build -t minimalist-web-tool .
```

## images

```bash
$ sudo docker images
REPOSITORY            TAG       IMAGE ID       CREATED          SIZE
minimalist-web-tool   latest    f11497961379   5 minutes ago    65.6MB
hello-world           latest    d2c94e258dcb   10 months ago    13.3kB
```

## run

```bash
sudo docker run -d -p 9206:9205 minimalist-web-tool
```

## ps

```bash
$ sudo docker ps -a
CONTAINER ID   IMAGE                 COMMAND             CREATED              STATUS                      PORTS                                                 NAMES
af98cf2f93bf   minimalist-web-tool   "python3 main.py"   About a minute ago   Up About a minute           9206/tcp, 0.0.0.0:9206->9205/tcp, :::9206->9205/tcp   eager_panini
df6e26375539   122741b7c691          "python3 main.py"   18 minutes ago       Exited (0) 4 minutes ago    5000/tcp, 0.0.0.0:5000->9205/tcp, :::5000->9205/tcp   suspicious_goldwasser
933dbeba9722   hello-world           "/hello"            33 minutes ago       Exited (0) 33 minutes ago                                                         magical_antonelli
8aa681d9bd42   hello-world           "/hello"            33 minutes ago       Exited (0) 33 minutes ago                                                         eager_jemison
```

## stop

```bash
$ sudo docker stop af98cf2f93bf
af98cf2f93bf
```

## remove

```bash
$ sudo docker rm df6e26375539
df6e26375539

$ sudo docker rmi f11497961379
df6e26375539
```

## tag login and push

```bash
$ sudo docker tag f11497961379 ghcr.io/albertgithubhome/minimalist-tool-web:1.0.0

$ cat ~/TOKEN.txt | docker login ghcr.io -u USERNAME --password-stdin xxxx
(用这种方式登录在push时报错，可能没加sudo的原因)
(unauthorized: unauthenticated: User cannot be authenticated with the token provided.)

$ sudo docker login ghcr.io -u USERNAME -p ghp_xxxx

$ sudo docker push ghcr.io/albertgithubhome/minimalist-tool-web:1.0.0
```