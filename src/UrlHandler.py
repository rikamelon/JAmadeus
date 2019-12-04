import re
from src import imgur_url
import urllib.request


def handle(link):

    link = link.split("?")[0]

    if "i.reddit.com" in link:
        return link

    elif "i.redd.it" in link:
        return link

    elif link.endswith(".jpg") or link.endswith(".png"):
        return link

    elif "imgur.com" in link:
        new_link, code = imgur_url.get_imgur_urls(link)

        if code == -1:
            return None

        return new_link

    elif "gfycat.com" in link:
        response = urllib.request.urlopen(link)
        html = str(response.read().decode("utf8"))
        new_link = re.search(r"srcSet=\"([^\"]*)\"", html).group(1)
        if new_link.split(".")[-1] != "gif":
            return None
        return new_link


if __name__ == '__main__':
    print(handle("https://gfycat.com/zealousunfinishedeyra"))
