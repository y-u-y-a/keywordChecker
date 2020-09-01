FROM python:3.7-slim-buster

# Install into Debian
RUN apt-get update \
    && apt-get install -y sudo wget gnupg2 vim \
    # set Japanese
    && apt-get install fonts-ipafont-gothic fonts-ipafont-mincho


# Install Chrome (Chromeのリポジトリを追加, 公開鍵の登録)
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && apt-get update \
    && apt-get install -y google-chrome-stable


# Don't create "/__pycache__"
ENV PYTHONDONTWRITEBYTECODE=1
#  Pass through the path
ENV PATH=$PATH:usr/bin/google-chrome


# Install Python Libraries
WORKDIR /code
RUN pip3 install \
    python-dotenv \
    requests \
    beautifulsoup4 \
    selenium \
    pyquery \
    scrapy \
    Flask \
    # https://chromedriver.chromium.org/downloads
    chromedriver-binary==85.0.4183.87
