# coding: utf-8
import json

def write(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        if isinstance(data, dict):
            _data = json.dumps(data)
            f.write(_data)
        else:
            raise TypeError("data is dict")
    return True

data = {'name': '汤姆1', 'top': 23, 'is_student': False, 'courses': ['Math', 'Science'], 'address': {'city': 'Wonderland', 'zip': '12345'}}

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        _data = f.read()
        return json.loads(_data)

if __name__ == "__main__":
  write("a.json", data)
  read_data = read("a.json")
  print(read_data)