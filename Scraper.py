from bs4 import BeautifulSoup
import requests


class LichessScraper:
    def __init__(self):
        self.base_url = 'https://lichess.org/@/'

    def fetch_profile(self, username):
        r = requests.get(self.base_url + username)
        assert r.status_code == 200, 'Lichess response code was not 200'
        return BeautifulSoup(r.content, 'html.parser')

    def is_online(self, username):
        profile = self.fetch_profile(username)
        if profile.find('h1', {'class': 'user-link online'}):
            return True
        elif profile.find('h1', {'class': 'user-link offline'}):
            return False
        else:
            raise ValueError('Could not find h1 with class "user-link online" or "user-link offline".')

