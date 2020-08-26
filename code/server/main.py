# 標準
import pprint, csv
# 自作クラス
from libs import scrap, parse


def getKeywordList(word_list: list):

    result_list: list = []

    for word in word_list:
        keyword: dict = {
            'word': word,
            'count': 0
        }
        result_list.append(keyword)
    return result_list


# テキスト内に含まれているキーワードのリストを返す
def extractWord(target_text: str, keyword_list:list) -> list:
    extracted_list: list = []
    for keyword in keyword_list:
        if keyword['word'] in target_text:
            keyword['count'] += 1
            extracted_list.append(keyword)
    return extracted_list


# 要素毎にマッチしたワードリストを返す
def getMatchWords(tag_name: str, el_list: list, keyword_list: list) -> dict:

    match_list: list = []

    for el in el_list:
        text: str = el.getText()
        # キーワードリストと照合して一致するワードを抽出
        word_list: list = extractWord(text, keyword_list)
        # 重複しないようにmatch_listに追加
        for w in word_list:
            if not w['word'] in match_list:
                match_list.append(w['word'])
    return {
        tag_name: match_list
    }


def parsePage(html) -> dict:
        article: dict = {
            'url': url
        }
        # h1
        h1_list = html.select('h1')
        article['h1'] = h1_list[0].getText()

        # h2 -> h3
        target_tag_list: list = ['h2', 'h3']
        for tag_name in target_tag_list:
            el_list: list = html.select(tag_name)

            get_words: dict = getMatchWords(tag_name, el_list, keyword_list)
            article.update(get_words)

        return article



if __name__ == "__main__":
    # [input]
    url_list: list = [
        'https://madalis.jp/article/seo-description',
        # 'https://madalis.jp/article/seo-algorithm/',
        # 'https://madalis.jp/article/seo-title/',
        # 'https://madalis.jp/article/google-seo/',
        # 'https://madalis.jp/article/seo-basic/'
    ]
    file = parse.File()
    word_list: list = file.csvToList('file/keyword_list.csv', 2)
    keyword_list: list = getKeywordList(word_list)

    # [output]
    article_list: list = []

    # ページ毎に処理
    for url in url_list:
        page = scrap.Page(url)
        html = page.html
        # 必要なデータ抽出
        article: dict = parsePage(html)
        article_list.append(article)
        # 単なる表示
        pprint.pprint(article, indent=2)
        pprint.pprint(keyword_list, indent=2)
        print('=' * 50)
