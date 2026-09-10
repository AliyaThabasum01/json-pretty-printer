import json


def format_json(data):
    parsed = json.loads(data)
    return json.dumps(parsed, indent=4, ensure_ascii=False)
