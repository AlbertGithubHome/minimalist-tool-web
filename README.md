# minimalist-tool-web
Develop a minimalist tool webpage to facilitate daily work and life.

```
.
├── Dockerfile
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── static
│   └── style.css
├── templates
│   ├── base64.html
│   ├── bytes.html
│   ├── holidays.html
│   ├── index.html
│   └── xor.html
└── tools
    ├── datetimes.py
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

# docker run

```bash
sudo docker run -d -p 9206:9205 minimalist-tool-web
# Bind container ports(9205) to physical server port(9206)
# visit by http://10.10.49.172:9206
```

[More docker operations](./DockerOps.md)