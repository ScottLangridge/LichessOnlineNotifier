import json


class UserBank:
    def __init__(self, data_file_name):
        self.file = data_file_name
        self.data = None
        self._read()

    def _read(self):
        with open(self.file, 'r') as f:
            self.data = json.loads(f.read())

    def _write(self):
        with open(self.file, 'w') as f:
            f.write(json.dumps(self.data))

    def list_users(self):
        return self.data.keys()

    def get_nickname(self, username):
        if 'nickname' in self.data[username].keys():
            return self.data[username]['nickname']
        else:
            return username

    def online(self, username):
        return self.data[username]['online']

    def update_online(self, username, online):
        self.data[username]['online'] = online
        self._write()