# 標準
import csv

class File(object):

    def __init__(self):
        return

    # 列番目を指定してcsvからリストを返す
    def csvToList(self, csv_file: str, column_index: int) -> list:

        result_list: list = []

        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                result_list.append(row[column_index])
        return result_list
