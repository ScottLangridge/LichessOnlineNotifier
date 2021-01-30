import requests


class PushoverSender:
    def __init__(self, user_key, api_key):
        self.user_key = user_key
        self.api_key = api_key

    def notify_user_online(self, user_online):
        url = 'https://api.pushover.net/1/messages.json'
        params = {
            'user': self.user_key,
            'token': self.api_key,
            'title': f'Lichess: Player Online',
            'message': f'{user_online} is active on Lichess',
            'sound': 'gamelan'
        }
        r = requests.post(url, params=params)
        assert r.status_code == 200
