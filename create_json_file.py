import json


def write_json(json_data):
    a_dict = json_data

    with open('words.json', 'r') as f:
        data = json.load(f)

    data.update(a_dict)

    with open('words.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)
