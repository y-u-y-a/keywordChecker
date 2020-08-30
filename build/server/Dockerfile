FROM python:3.7-slim-buster

RUN apt-get update && \
    apt-get install -y sudo
RUN sudo apt-get update && \
    sudo apt-get install -y wget gnupg2 vim

# [Chromeをインストール]
# Chromeのリポジトリを追加, 公開鍵の登録
RUN sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - && \
    sudo apt-get update && \
    sudo apt-get install -y google-chrome-stable

# /__pycache__を生成させない
ENV PYTHONDONTWRITEBYTECODE=1
# chromedriver-binaryのパスを通す
ENV PATH=$PATH:usr/bin/google-chrome


# ディレクトリ作成も実行
RUN mkdir code

WORKDIR /code

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
