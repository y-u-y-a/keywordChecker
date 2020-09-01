
# dictのリスト形式で返す
def get_keyword_list(word_list: list):

    result_list: list = []

    for index, word in enumerate(word_list):
        keyword: dict = {
            'priority': index + 1,
            'word': word,
            'count': 0
        }
        result_list.append(keyword)
    return result_list
