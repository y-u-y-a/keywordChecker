# 標準
import os, pprint, csv
# PyPI
from flask import Flask, jsonify, render_template,request
# 自作クラス
from libs import scrap, parse
# 自作モジュール
from services import functions as func


# Flaskの標準テンプレートエンジンJinja2(/templates内を自動的に読み込む)
app = Flask(__name__)
# 文字化け対処
app.config['JSON_AS_ASCII'] = False

# GET =====================================
@app.route('/')
def main():
    return render_template('pages/form.html')


# POST ====================================
@app.route('/form', methods=['POST'])
def form():
    # [input]
    url_list: list = [
        request.form['url_1'],
        request.form['url_2'],
        # 'https://madalis.jp/article/seo-title/',
        # 'https://madalis.jp/article/google-seo/',
        # 'https://madalis.jp/article/seo-basic/'
    ]
    file = parse.File()
    word_list: list = file.csvToList('file/keyword_list.csv', 2)
    keyword_list: list = func.getKeywordList(word_list)

    # [output]
    article_list: list = []

    # ページ毎に処理
    for url in url_list:
        page = scrap.Page(url)
        html = page.html
        # 必要なデータ抽出
        article: dict = func.parsePage(html, url, keyword_list)
        article_list.append(article)

    result = {
        'keyword_list': keyword_list,
        'article_list': article_list
    }
    return render_template('pages/result.html', data=result)


# '__name__'はこのファイルが呼ばれたファイルの名前が入る(このファイルでは'main')
if __name__ == '__main__':
    # webサーバーの立ち上げ
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
