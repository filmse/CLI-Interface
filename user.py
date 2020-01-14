import requests
import json
from art_font import ArtFont
from list_of_menu import ListOfMenu


class User:
    def __init__(self, username=None, password=None, token=None):
        self.username = username
        self.password = password
        self.token = token

    def login(self):
        self.username = input("Enter Username: ")
        self.password = input("Enter Password: ")
        self.verify_user(self.username, self.password)

    def verify_user(self, username, password):
        # Login to get Token
        link = ""
        data = {"params": {"username": self.username, "password": self.password,
                           "remote_name": "Local"}}

        r = requests.post(url=link, json=data)
        r = r.json()
        self.token = r['token']

        if(r['token']):
            print(self.token)
            c = ArtFont()
            c.add_text()

            list_menu = ListOfMenu()
            result = list_menu.main_menu(self.token)

            # print(result)
            while result == 0:
                result = list_menu.main_menu(self.token)
        else:
            print('--Login Unsuccessfully--')
            cli.login()


if __name__ == '__main__':
    cli = User()
    cli.login()
