# docker operation

## make docker image

```bash
sudo docker build -t minimalist-tool-web .
```

## show docker images

```bash
$ sudo docker images
REPOSITORY            TAG       IMAGE ID       CREATED          SIZE
minimalist-tool-web   latest    f11497961379   5 minutes ago    65.6MB
hello-world           latest    d2c94e258dcb   10 months ago    13.3kB
```

## docker run

```bash
sudo docker run -d -p 9206:9205 minimalist-tool-web
# Bind container ports(9205) to physical server port(9206)
# http://10.10.49.172:9206
```

## docker ps

```bash
$ sudo docker ps -a
CONTAINER ID   IMAGE                 COMMAND             CREATED              STATUS                      PORTS                                                 NAMES
af98cf2f93bf   minimalist-tool-web   "python3 main.py"   About a minute ago   Up About a minute           9206/tcp, 0.0.0.0:9206->9205/tcp, :::9206->9205/tcp   eager_panini
df6e26375539   122741b7c691          "python3 main.py"   18 minutes ago       Exited (0) 4 minutes ago    5000/tcp, 0.0.0.0:5000->9205/tcp, :::5000->9205/tcp   suspicious_goldwasser
933dbeba9722   hello-world           "/hello"            33 minutes ago       Exited (0) 33 minutes ago                                                         magical_antonelli
8aa681d9bd42   hello-world           "/hello"            33 minutes ago       Exited (0) 33 minutes ago                                                         eager_jemison
```

## docker stop

```bash
$ sudo docker stop af98cf2f93bf
af98cf2f93bf
```

## docker rm

```bash
# delete container ID
$ sudo docker rm df6e26375539
df6e26375539

# delete image ID
$ sudo docker rmi f11497961379
df6e26375539
```

## doctor tag

```bash
$ sudo docker tag f11497961379 ghcr.io/albertgithubhome/minimalist-tool-web:1.0.0
```

## doctor login

```bash
$ cat ~/TOKEN.txt | docker login ghcr.io -u USERNAME --password-stdin
$ sudo docker login ghcr.io -u USERNAME -p ghp_xxxx
$ sudo docker login --username=xxx@abc.com registry.cn-hangzhou.aliyuncs.com
```

## docker push

```
$ sudo docker push ghcr.io/albertgithubhome/minimalist-tool-web:1.0.0
```

## docker pull

```bash
$ sudo docker pull ghcr.io/albertgithubhome/minimalist-tool-web:1.0.0
```