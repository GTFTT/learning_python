import json

# Creates file if it doesn't exist
with open('test_json.json', 'w', encoding='utf-8') as f:
    some_value = [1, 2, 3, 4, 5]
    print(json.dumps(some_value))
    json.dump(some_value, f)
