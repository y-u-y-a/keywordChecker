
# dictのリスト形式で返す
def getKeywordList(word_list: list):

    result_list: list = []

    for w in word_list:
        keyword: dict = {
            'word': w,
            'count': 0
        }
        result_list.append(keyword)
    return result_list


def parsePage(html, url, keyword_list) -> dict:
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
