import requests
from src import EmbedFactory
import urllib

api_url = "https://nhentai.net/api/gallery/"
base_url = "https://nhentai.net"


def random():
    return requests.get("https://nhentai.net/random").url.split("/")[-2]


def search(query):
    query = urllib.parse.quote_plus(query)

    results = requests.get("https://nhentai.net/api/galleries/search?query="+query).json()

    ids = [(str(x['id']), x['title']['english']) for x in results['result']]

    return ids


class Gallery:

    def __init__(self, numbers):

        self.numbers = numbers
        self.data = {}
        self.exists = True
        self.title = ""
        self.url = base_url + "/g/" + str(numbers)
        self.media_id = 0
        self.cover_url = ""

        self.tags = []
        self.languages = []
        self.artists = []
        self.categories = []
        self.parodies = []
        self.characters = []
        self.groups = []
        self.pages = 0

        self.get_data()

        if not self.exists:
            print(self.numbers)
            return

        self.process_data()
        self.get_cover()

    def get_data(self):
        request = requests.get(api_url + str(self.numbers))
        if request.status_code == 200:
            self.data = request.json()
        elif request.status_code == 404:
            self.exists = False

    def process_data(self):
        self.title = self.data['title']['english']
        self.pages = self.data['num_pages']
        self.media_id = self.data['media_id']

        for tags in self.data['tags']:
            if 'tag' in tags['type']:
                self.tags.append([tags['name'], tags['count'], tags['url']])
            elif 'language' in tags['type']:
                self.languages.append([tags['name'], tags['count'], tags['url']])
            elif 'artist' in tags['type']:
                self.artists.append([tags['name'], tags['count'], tags['url']])
            elif 'category' in tags['type']:
                self.categories.append([tags['name'], tags['count'], tags['url']])
            elif 'parody' in tags['type']:
                self.parodies.append([tags['name'], tags['count'], tags['url']])
            elif 'character' in tags['type']:
                self.characters.append([tags['name'], tags['count'], tags['url']])
            elif 'group' in tags['type']:
                self.groups.append([tags['name'], tags['count'], tags['url']])

    def create_embed(self):
        if not self.exists:
            return EmbedFactory.blank(str(self.numbers) + " does not exist")

        return EmbedFactory.nhentai_gallery(self.numbers, self.url, self.title, self.pages, self.tags, self.languages,
                                            self.artists, self.categories, self.parodies, self.characters, self.groups,
                                            self.cover_url)

    def get_cover(self):

        footers = ["/cover.jpg", "/cover.png"]

        for i in footers:
            url = "https://t.nhentai.net/galleries/" + str(self.media_id) + i

            request = requests.get(url)

            if request.status_code != 404:
                break

        self.cover_url = url


if __name__ == '__main__':
    print("A")
    print(Gallery(177013).cover_url)
    print(Gallery(116647).cover_url)
