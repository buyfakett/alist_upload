FROM python:3.12.1-alpine3.19
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple