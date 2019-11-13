import json


def read_json():
    count = 0
    with open('words.json', 'r') as f:
        data = json.load(f)
    for i in data:
        word_count = 'word_' + str(count)
        json_data = {
            word_count: data[i]
        }
        count += 1
        return json_data


read_json()
