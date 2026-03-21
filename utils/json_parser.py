import json

def get_json_data(file_path):
    with open(file_path) as file:
        json_data = json.load(file)
    return json_data


