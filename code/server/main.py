# 標準
import os, pprint, csv
# PyPI
from flask import Flask, jsonify, render_template,request, redirect, abort, url_for
# 自作モジュール
from libs import scrap, file
from libs import keyword as kw


# Flaskの標準テンプレートエンジンJinja2(/templates内を自動的に読み込む)
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 文字化け対処


# GET =====================================
@app.route('/')
def top():
    return render_template('pages/form.html')


# POST ====================================
@app.route('/form', methods=['POST'])
def form():
    # [input]
    url_list: list = []
    if request.form['url_1']:
        url_list.append(request.form['url_1'])
    if request.form['url_2']:
        url_list.append(request.form['url_2'])
    if request.form['url_3']:
        url_list.append(request.form['url_3'])
    if request.form['url_4']:
        url_list.append(request.form['url_4'])
    if request.form['url_5']:
        url_list.append(request.form['url_5'])

    get_keyword: str = 'SEO_対策'
    if get_keyword == 'SEO_対策':
        file_name: str = 'libs/keyword_list.csv'

    word_list: list = file.csv_to_list(file_name, 2)
    keyword_list: list = kw.get_keyword_list(word_list)

    # [output]
    article_list: list = []

    # [ページ毎に処理]
    for url in url_list:
        html = scrap.get_html(url)
        # 必要なデータ抽出
        article: dict = scrap.parse_page(html, url, keyword_list)
        article_list.append(article)

    result = {
        'keyword_list': keyword_list,
        'article_list': article_list
    }
    return render_template('pages/result.html', data=result)


# エラーハンドリング
@app.route('/error')
def intentionalError():
    # return redirect(url_for('top'))
    return abort(500, 'エラー発生')

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def systemError(e):
    err_message = e.description
    return render_template('errors/system_error.html', err_message=err_message), 500


# '__name__'はこのファイルが呼ばれたファイルの名前が入る(このファイルでは'main')
if __name__ == '__main__':
    # webサーバーの立ち上げ
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
