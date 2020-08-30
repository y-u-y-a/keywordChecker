FROM python:3.7-slim-buster

# /__pycache__を生成させない
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
    apt-get install -y sudo
RUN sudo apt-get update && \
    sudo apt-get install -y wget gnupg2

# # Chromeのリポジトリを追加
# RUN sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
# # 公開鍵の登録
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
# # Chromeをインストール
# RUN sudo apt-get update && \
#     sudo apt-get install -y google-chrome-stable


# ディレクトリ作成も実行
RUN mkdir code

WORKDIR /code

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
