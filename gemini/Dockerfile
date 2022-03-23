FROM python:3.7
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
ADD . /code
