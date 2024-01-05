import requests


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self):
        url = "https://auth.x-kom.pl/xkom/token"
        payload = {
            'client_id': 'www-xkom',
            'grant_type': 'password',
            'username': self.username,
            'scope': 'api_v1 offline_access',
            'password': self.password
        }
        headers = {
            # ... include all necessary headers ...
        }
        response = self.session.post(url, headers=headers, data=payload)
        return response.text
