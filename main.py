import time

import config
from Notifier import PushoverSender
from Scraper import LichessScraper
from UserBank import UserBank

scraper = LichessScraper()
notifier = PushoverSender(config.pushover_user_key, config.pushover_api_key)
users = UserBank(config.user_file_name)

print('Running Lichess Online Notifier for the following users:')
[print(f' - {user} ({users.get_nickname(user)})') for user in users.list_users()]

while True:
    for user in users.list_users():
        try:
            is_online = scraper.is_online(user)
            was_online = users.online(user)

            if is_online != was_online:
                if is_online:
                    nickname = users.get_nickname(user)
                    notifier.notify_user_online(nickname)
                users.update_online(user, is_online)
        except AssertionError:
            pass
        time.sleep(config.min_request_interval)

    time.sleep(config.refresh_interval)
