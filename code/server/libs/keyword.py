
# dictのリスト形式で返す
def getKeywordList(word_list: list):

    result_list: list = []

    for index, word in enumerate(word_list):
        keyword: dict = {
            'priority': index + 1,
            'word': word,
            'count': 0
        }
        result_list.append(keyword)
    return result_list
