FROM python:3.9-slim-buster

ENV TZ=Asia/Tokyo
ENV LANG=ja_JP.UTF-8
ENV LANGUAGE=ja_JP.UTF-8

COPY . /app
WORKDIR /app

RUN pip install -r packages.txt

CMD ["/app/bootstrap.sh"]
