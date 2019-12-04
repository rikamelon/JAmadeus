import requests.auth
import requests

# TODO: Add error handling


class RedditBot:

    base_url = "https://oauth.reddit.com/"

    def __init__(self, username, password, app_client_id, app_secret_id, user_agent):
        self.username = username
        self.password = password
        self.app_client_id = app_client_id
        self.app_secret_id = app_secret_id
        self.headers = {"User-Agent": user_agent}

        self.authorized = False

    def authorize(self):
        client_auth = requests.auth.HTTPBasicAuth(self.app_client_id, self.app_secret_id)
        post_data = {"grant_type": "password", "username": self.username, "password": self.password}
        response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                                 headers=self.headers)
        self.headers["Authorization"] = "bearer " + response.json()['access_token']

        self.authorized = True

    def get_posts(self, subreddit, sort, amount):
        if not self.authorized:
            raise RuntimeError("Bot has not been authorized yet!")

        after = None

        url = self.base_url + "r/" + subreddit + "/" + sort

        posts = []

        while True:
            params = {'limit': 100}
            if amount < 100:
                params['limit'] = amount
            if after is not None:
                params['after'] = after

            req = requests.get(url, params=params, headers=self.headers)
            data = req.json()

            posts.extend(data['data']['children'])

            if amount <= 100:
                break
            amount -= 100

            after = data['data']['after']

        return posts

