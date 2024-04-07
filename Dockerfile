# 使用 Alpine Linux 作为基础镜像
FROM python:3.8-alpine

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录
COPY . .

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 清理不必要的缓存
RUN rm -rf /var/cache/apk/*

# 暴露应用端口
EXPOSE 9205

# 运行应用
CMD ["python3", "main.py"]
