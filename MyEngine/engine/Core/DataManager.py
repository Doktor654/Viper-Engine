import json

class DataManager:
    def save(self, path, data):
        with open(path, 'w') as f:
            json.dump(data, f)

    def load(self, path):
        with open(path) as f:
            return json.load(f)