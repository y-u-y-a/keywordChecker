import csv

# 列番目を指定してcsvからリストを返す
def csv_to_list(csv_file_name: str, column_index: int) -> list:

    result_list: list = []

    with open(csv_file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            result_list.append(row[column_index])
    return result_list
