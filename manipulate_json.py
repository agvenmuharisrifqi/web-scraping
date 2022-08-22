import json

def update_json_file(filename: str, key: str, data: dict):
    file_json = open(filename, 'r+')
    data_json = json.load(file_json)
    file_json.truncate(0)
    file_json.seek(0)
    data_json[key] = data
    json.dump(data_json, file_json, indent=4)
    file_json.close()

def get_keys_json(filename: str) -> str:
    file_json = open(filename, 'r')
    data_json = json.load(file_json)
    keys = list(data_json.keys())
    file_json.close()
    return keys