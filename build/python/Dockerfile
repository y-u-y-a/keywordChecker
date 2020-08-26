FROM python:3.7-slim-buster

# /__pycache__を生成させない
ENV PYTHONDONTWRITEBYTECODE=1
# ディレクトリ作成も実行
RUN mkdir code

WORKDIR /code

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
